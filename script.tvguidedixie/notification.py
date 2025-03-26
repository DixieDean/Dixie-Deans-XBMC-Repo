#
#      Copyright (C) OTT-Networks 2017-
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc
import xbmcgui

import datetime
import time
import os

from strings import *
from sqlite3 import dbapi2 as sqlite3

import dixie


DSF     = dixie.isDSF()
ADDON   = dixie.ADDON
HOME    = dixie.HOME
PROFILE = dixie.PROFILE
TITLE   = dixie.TITLE
ICON    = dixie.ICON
DB      = 'notification.db'


from channel import Filename 
def CleanChannelFilename(channel_id):
    if DSF:
        return channel_id

    return Filename(channel_id)
 

def CleanTitle(title):
    title = title.replace(','  ,  '')
    title = title.replace('"'  ,  '')
    title = title.replace('\'' ,  '')
    title = title.replace('('  ,  '[')
    title = title.replace(')'  ,  ']')
    return title



def adapt_datetime(ts):
    #http://docs.python.org/2/library/sqlite3.html#registering-an-adapter-callable
    return time.mktime(ts.timetuple())


class Notification(object):

    def __init__(self, database):

        self.database = database 

        self.c = None

        self.conn = sqlite3.connect(os.path.join(PROFILE, DB), timeout=10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self._createTables()
        
        self.channels     = None #dict of channels where key is the channel.id
        self.programCache = None #used for efficiency during scheduleNotifications
        self.scheduleNotifications()


    def __del__(self):
        self.conn.close()


    def getChannel(self, channelID):
        if not self.channels:
            self.channels = {}

            for channel in self.database.getChannelList(onlyVisible=True):
                self.channels[channel.id] = channel

        try:    return self.channels[channelID]
        except: return None
            

    def getProgramList(self, channel, start, end): 
        if channel is None:
            return []

        if self.programCache is None:
            return self.database.getProgramList([channel], start, end)

        key = '%s-%s-%s' % (channel.id, str(start), str(end))
        if key in self.programCache:
            return self.programCache[key]
        
        programList = self.database.getProgramList([channel], start, end)
        self.programCache[key] = programList
        return programList


    def createAlarmClockName(self, program):
        name = '%s-%s-%s' % (TITLE, program.channel.id, program.startDate)
        return name.encode('utf-8', 'replace')


    def removeOld(self):
        now  = datetime.datetime.now()
        when = now - datetime.timedelta(hours=8)
        when = adapt_datetime(when)

        c = self.conn.cursor()
        c.execute('DELETE FROM notification WHERE start < ?', [when])
        self.conn.commit()
        c.close()


    def cancelAlarms(self):
        alarms = xbmcgui.Window(10000).getProperty('OTT_ALARMS').split('-OTT-')
        for alarm in alarms:
            xbmc.executebuiltin('CancelAlarm(%s,True)' % alarm)
          

    def scheduleNotifications(self):
       self.cancelAlarms()
       start = datetime.datetime.now()

       try:
           self.removeOld()
           self.programCache = {}

           programs = self.getPrograms()

           now = datetime.datetime.now()

           for program in programs: 
               channelId    = program[0]
               programTitle = program[1]
               startDate    = program[2] + (60 * self.getChannel(channelId).offset) 
               emailed      = program[3]
               if emailed == None:
                   emailed = 0
               self._processSingleNotification(channelId, programTitle, now, startDate, emailed==1, self._scheduleNotification)

           dayCheck = 1

           series = self.getSeries()

           self.c = self.conn.cursor()

           for channelId, programTitle in series:
               end = now + datetime.timedelta(hours=24*dayCheck)
               channel = self.getChannel(channelId)
               for p in self.getProgramList(channel, now, end): 
                   if p.title == programTitle:
                       self.addProgram(p, now)

           self.conn.commit()
           self.c.close()
           self.c = None

           self.programLists = None

           delta = datetime.datetime.now() - start
           dixie.log('Scheduling program notifications...Done')
           dixie.log('ScheduleNotifications... Time Taken = %s' % str(delta))
           #dixie.DialogOK('ScheduleNotifications...', 'Time Taken = %s' % str(delta))

       except:
           dixie.log('Error during scheduling program notifications')
       

    def _processSingleNotification(self, channelId, programTitle, now, startDate, emailed, action):
        dayCheck = 1
        theRange = range(-1, dayCheck+1)

        startDate = dixie.parseTime(startDate, True)
        end       = now + datetime.timedelta(hours=24*dayCheck)

        channel  = self.getChannel(channelId)
        programs = self.getProgramList(channel, now, end)

        for program in programs: 
            if programTitle == program.title:
                if startDate == program.startDate:
                    if self._timeToNotification(program).days in theRange:#[-1, 0, 1]:
                        action(program, channel, emailed)
                        break


    def _unscheduleRecording(self, program, channel):
        startDate = program.startDate

        name = '%s-%s-record' % (self.createAlarmClockName(program), str(startDate))
        xbmc.executebuiltin('CancelAlarm(%s,True)' % name)  #True - silent



    def _scheduleRecording(self, program, channel):
        dixie.log('======= _scheduleRecording =======')
        dixie.log(program)
        dixie.log(channel)
        if DSF:
            dixie.log('=== isDSF ===')
            return

        startPad = dixie.RecordingStartPad()
        dixie.log('=== startPad ===')
        dixie.log(startPad)

        t = self._timeToNotification(program)
        timeToNotification = ((t.days * 86400) + t.seconds) / 60

        when = timeToNotification - startPad
        if when < 0:
            when = 0

        startDate = program.startDate

        name = '%s-%s-record' % (self.createAlarmClockName(program), str(startDate))
 
        duration  = program.endDate - startDate

        xbmc.executebuiltin('CancelAlarm(%s,True)' % name)  #True - silent
        self._addAlarm(name)

        script =  os.path.join(HOME, 'record.py')
        args   = ''
        args  += CleanChannelFilename(channel.id) + ','
        args  += CleanTitle(program.title)        + ','
        args  += str(startDate)                   + ','
        args  += str(duration.seconds)            + ','
        args  += program.imageSmall               + ','
        cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, when)
        # cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0) #debug, records immediately

        self._addAlarm(name)

        dixie.log('======= cmd =======')
        dixie.log(cmd)
        xbmc.executebuiltin(cmd)

        dixie.log('Record notification created for %s at %s on %s' % (program.title, str(program.startDate), channel.title))
            

    def _scheduleNotification(self, program, channel, emailed):
        dixie.log('======= _scheduleNotification =======')
        dixie.log(program)
        t = self._timeToNotification(program)
        timeToNotification = ((t.days * 86400) + t.seconds) / 60

        self._scheduleRecording(program, channel)

        preNotify = 5

        when = timeToNotification - preNotify
        if when < 0:
            when = 0

        name = self.createAlarmClockName(program)

        xbmc.executebuiltin('CancelAlarm(%s-5mins,True)'  % name) #True - silent
        xbmc.executebuiltin('CancelAlarm(%s-now,True)'    % name) #True - silent 

        startsIn = self._timeToNotification(program).seconds
        if startsIn / 60 > preNotify:
            startsIn = preNotify * 60

        if timeToNotification <= 0:
            text = 'is on now...'
 
        elif startsIn <= 60:
            text = 'is on in ' + str(startsIn) + ' seconds...'
        else:
            text = 'is on in ' + str((startsIn) /60) + ' minutes...'

        description = 'on [B]%s[/B] %s' % (channel.title, text)

        self._setAlarm('%s-5mins' % name, program.title.encode('utf-8', 'replace'), description.encode('utf-8', 'replace'), when)
        
        if ADDON.getSetting('watch_prompt') == 'true':
            self._scheduleWatchPrompt(program, timeToNotification)
        else:
            if timeToNotification > 0:
                description = 'on [B]%s[/B] is now starting...' % channel.title
                self._setAlarm('%s-now' % name, program.title.encode('utf-8', 'replace'), description.encode('utf-8', 'replace'), timeToNotification)

        dixie.log('Alarm notifications created for %s at %s on %s' % (program.title, str(program.startDate), channel.title))


    def _setAlarm(self, name, title, desc, when):
        xbmc.executebuiltin('AlarmClock(%s,Notification(%s,%s,10000,%s),%d,True)' % (name, title, desc, ICON, when))
        self._addAlarm(name)


    def _addAlarm(self, name):
        alarms = xbmcgui.Window(10000).getProperty('OTT_ALARMS')
        alarms += '-OTT-'
        alarms += name
        xbmcgui.Window(10000).setProperty('OTT_ALARMS', alarms)


    def _unscheduleNotification(self, program, channel, emailed):
        self._unscheduleRecording(program, channel)

        self._unscheduleWatchPrompt(program)

        name = self.createAlarmClockName(program)
        xbmc.executebuiltin('CancelAlarm(%s-5mins,True)' % name)
        xbmc.executebuiltin('CancelAlarm(%s-now,True)' % name)

        dixie.log('Alarm notifications cancelled for %s at %s on %s' % (program.title, str(program.startDate), channel.title))


    def _timeToNotification(self, program):
        return program.startDate - datetime.datetime.now()


    def addProgram(self, program, now):
        #is it alrerady in the database?
        if self._isNotificationRequiredForProgram(program):
            return

        startDate = program.startDate - datetime.timedelta(minutes=program.channel.offset)

        if self.c == None:
            c = self.conn.cursor()
            c.execute('INSERT INTO notification(channel, program, start, emailed) VALUES(?, ?, ?, ?)', [program.channel.id, program.title, adapt_datetime(startDate), False])
            self.conn.commit()
            c.close()
        else:
            self.c.execute('INSERT INTO notification(channel, program, start, emailed) VALUES(?, ?, ?, ?)', [program.channel.id, program.title, adapt_datetime(startDate), False])

        self._processSingleNotification(program.channel.id, program.title, now, program.startDate, False, self._scheduleNotification)


    def removeProgram(self, program, now):
        startDate = program.startDate - datetime.timedelta(minutes=program.channel.offset)

        if self.c == None:
            c = self.conn.cursor()
            c.execute('DELETE FROM notification WHERE channel=? AND program=? AND start=?', [program.channel.id, program.title, startDate])
            self.conn.commit()
            c.close()         
        else:
            self.c.execute('DELETE FROM notification WHERE channel=? AND program=? AND start=?', [program.channel.id, program.title, startDate])  

        self._processSingleNotification(program.channel.id, program.title, now, program.startDate, False, self._unscheduleNotification)
        

    def addSeries(self, program):
        start = datetime.datetime.now() 

        c = self.conn.cursor()
        c.execute('INSERT INTO series(channel, program) VALUES(?, ?)', [program.channel.id, program.title])
        self.conn.commit()
        c.close()

        dayCheck = 1
                
        now = datetime.datetime.now()
        end = now + datetime.timedelta(hours=24*dayCheck)

        channel = self.getChannel(program.channel.id)

        self.programCache = {}

        self.c = self.conn.cursor()
        for p in self.getProgramList(channel, now, end):
            if p.title == program.title:
                self.addProgram(p, now)
        
        self.conn.commit()
        self.c.close()
        self.c = None

        self.programCache = None
        delta = datetime.datetime.now() - start
        dixie.log('AddSeries...Done : Time Taken = %s' % str(delta))
        #dixie.DialogOK('AddSeries...', 'Time Taken = %s' % str(delta))
        

    def removeSeries(self, program):
        start = datetime.datetime.now() 
        
        c = self.conn.cursor()
        c.execute('DELETE FROM series WHERE channel=? AND program=?', [program.channel.id, program.title])
        self.conn.commit()
        c.close()
                
        now = datetime.datetime.now()
        end = now + datetime.timedelta(hours = 36)

        self.programCache = {}

        self.c = self.conn.cursor()
        
        channel = self.getChannel(program.channel.id)
        for p in self.getProgramList(channel, now, end):
            if p.title == program.title:
                self.removeProgram(p, now)

        self.conn.commit()
        self.c.close()
        self.c = None

        self.programCache = None
        delta = datetime.datetime.now() - start
        dixie.log('RemoveSeries...Done : Time Taken = %s' % str(delta))
        #dixie.DialogOK('RemoveSeries...', 'Time Taken = %s' % str(delta))



    def getPrograms(self):
        # this returns notification database times, i.e channel offset has NOT been applied
        c = self.conn.cursor()
        c.execute('SELECT DISTINCT channel, program, start, emailed FROM notification')
        programs = c.fetchall()
        c.close()
        return programs


    def getSeries(self):
        c = self.conn.cursor()
        c.execute('SELECT DISTINCT channel, program FROM series')
        series = c.fetchall()
        c.close()
        return series


    def isNotificationRequiredForProgram(self, program):
        if self.isNotificationRequiredForSeries(program):
            return True

        return self._isNotificationRequiredForProgram(program)


    def _isNotificationRequiredForProgram(self, program):
        startDate = program.startDate - datetime.timedelta(minutes=program.channel.offset)
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM notification WHERE channel=? AND program=? AND start=?', [program.channel.id, program.title, adapt_datetime(startDate)])
        result = c.fetchone()
        c.close()
        return result is not None


    def isNotificationRequiredForSeries(self, program):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM series WHERE channel=? AND program=?', [program.channel.id, program.title])
        result = c.fetchone()
        c.close()
        return result is not None



    def clearAllNotifications(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM notification')
        c.execute('DELETE FROM series')
        self.conn.commit()
        c.close()


    def _scheduleWatchPrompt(self, program, timeToNotification):
        channelID = dixie.CleanFilename(program.channel.id)

        #in case it is already set
        self._unscheduleWatchPrompt(program)

        label = 'is about to start.'

        if timeToNotification <= 0:
            #check if program is actually on now
            if (program.endDate - now).days < 0:
                return
            else:
                label              = 'has started.'
                timeToNotification = 0

        name   = self.createAlarmClockName(program)+'-WatchPrompt'
        name   = name.encode('utf-8', 'replace')
        script = os.path.join(HOME, 'watch_prompt.py')

        args  =       program.title 
        args += ',' + str(channelID)
        args += ',' + label

        cmd = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script.encode('utf-8', 'replace'), args.encode('utf-8', 'replace'), timeToNotification)
        xbmc.executebuiltin(cmd)
        self._addAlarm(name)


    def _unscheduleWatchPrompt(self, program):
        name = self.createAlarmClockName(program)+'-WatchPrompt'
        xbmc.executebuiltin('CancelAlarm(%s,True)' % name)


    def _createTables(self):
        c = self.conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS notification (channel TEXT, program TEXT, start INT)')
        c.execute('CREATE TABLE IF NOT EXISTS series       (channel TEXT, program TEXT)')
        try:
            c.execute("ALTER TABLE notification add column 'emailed' 'BOOLEAN'")
        except:
            pass

        c.close()


    def seriesOrProgram(self, program): #returns True is 'series' selected, raises exception if cancelled
        isNotificationRequiredForProgram = self._isNotificationRequiredForProgram(program)
        isNotificationRequiredForSeries  = self.isNotificationRequiredForSeries(program)
        isRemovingNotification           = isNotificationRequiredForProgram or isNotificationRequiredForSeries

        PROGRAM = '[COLOR orange][B]' + program.title + '[/B][/COLOR]'

        if isRemovingNotification:
            #no need to ask, just remove program notification
            if not isNotificationRequiredForSeries:
                return False

            text     = 'This will clear the reminders for the whole series, are you sure?'
            noLabel  = 'No'
            yesLabel = 'Yes'

            if dixie.DialogYesNo(PROGRAM, text, noLabel=noLabel, yesLabel=yesLabel):
                return True
            else:
                dixie.log('Remove reminder cancelled')
                raise Exception('Remove reminder cancelled')
 
        else:
            #if program in past then can only add "Series notification"
            if program.startDate < datetime.datetime.now():
                text     = 'It is too late to set a program reminder, do you want to set a reminder for the whole series instead?'
                noLabel  = 'No'
                yesLabel = 'Yes'
                if dixie.DialogYesNo(PROGRAM, text, noLabel=noLabel, yesLabel=yesLabel):
                    return True
                else:
                    dixie.log('Add reminder cancelled')
                    raise Exception('Add notification cancelled')

            text     = 'Do you want to set a reminder for the single program or the whole series?'
            noLabel  = 'Program'
            yesLabel = 'Series'

        if dixie.DialogYesNo(PROGRAM, text, noLabel=noLabel, yesLabel=yesLabel):
            return True
    
        return False


def reset():
    import sfile

    filepath = os.path.join(PROFILE, DB)

    sfile.remove(filepath)

    if sfile.exists(filepath):
        dixie.DialogOK(strings(CLEAR_NOTIFICATIONS), 'Failed, please restart Kodi and try again.')
        return
    
    dixie.DialogOK(strings(CLEAR_NOTIFICATIONS), strings(DONE))


def main():
    if len(sys.argv) < 2:
        return

    mode = sys.argv[1].lower()

    if mode == 'reset':
        return reset()

        
if __name__ == '__main__':
    main()
