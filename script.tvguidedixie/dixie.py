
#       Copyright (C) 2018
#       On-Tapp-Networks Limited
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
import xbmcaddon
import xbmcgui
import os
import re
import time
import datetime

import sfile


ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
 t = ooOOOoo
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0  
 for c in t2:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t


ADDONID      = 'script.tvguidedixie'
ADDON        =  xbmcaddon.Addon(ADDONID)
HOME         =  ADDON.getAddonInfo('path')
ICON         =  xbmc.translatePath(os.path.join(HOME, 'icon.png'))
PROFILE      =  xbmc.translatePath(ADDON.getAddonInfo('profile'))
RESOURCES    =  os.path.join(HOME, 'resources')
PVRACTIVE    = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True
IGNORESTRM   =  ADDON.getSetting('ignore.stream') == 'true'
GETTEXT      =  ADDON.getLocalizedString
FAVE_POSTFIX = '~OTTFAVE'

try:
    OTT_ADDONID = 'script.on-tapp.tv'
    OTT_ADDON   =  xbmcaddon.Addon(OTT_ADDONID)
    OTT_HOME    =  xbmc.translatePath(OTT_ADDON.getAddonInfo('path'))
    OTT_PROFILE =  xbmc.translatePath(OTT_ADDON.getAddonInfo('profile'))
except:
    pass

resource    = 'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/'  # 'http://files.on-tapp.tv/'
baseurl     = 'https://www.on-tapp.tv/files/update/'
# resource    = 'http://files.on-tapp-networks.com/'
# baseurl     = 'http://www.on-tapp-networks.com/files/update/'
loginurl    =  ttTTtt(393,[72,104,176,116],[194,116,1,112,40,115,24,58,196,47,96,47,160,119,10,119,73,119,153,46,156,111,245,110,246,45,163,116,51,97,57,112,60,112,217,46,1,116,38,118,110,47,202,119,147,112,232,45,135,108,73,111,70,103,215,105,209,110,244,46,121,112,128,104,196,112])
verifyurl   =  ttTTtt(211,[136,104,34,116,82,116,10,112,216,115,105,58,30,47,240,47,201,111,178,110,160,45],[121,116,0,97,232,112,168,112,107,46,147,116,137,118,134,47,9,118,43,101,218,114,147,105,8,102,130,121,253,47,127,105,138,110,242,100,123,101,139,120,232,46,154,112,251,104,194,112])

try:
    DSFID   =  ttTTtt(0,[112,13,108,120,117],[115,103,45,105,212,110,32,46,233,118,53,105,75,100,34,101,38,111,148,46,218,103,216,118,30,97,110,120])
    DSF     =  xbmcaddon.Addon(DSFID)
    DSFVER  =  DSF.getAddonInfo('version')
except: pass

OPEN_OTT  = '_OTT['
CLOSE_OTT = ']OTT_'


def deleteCFG():
    path    = PROFILE
    cfgfile = os.path.join(path, 'settings.cfg')
    # catfile = os.path.join(path, 'catfile')

    if os.path.exists(cfgfile):
        sfile.remove(cfgfile)

    # if os.path.exists(catfile):
    #     sfile.remove(catfile)


def SetSetting(param, value):
    value = str(value)

    if GetSetting(param) == value:
        return

    xbmcaddon.Addon(ADDONID).setSetting(param, value)


def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


def GetFaveCategory():
    return GetSetting('FAVOURITE').strip() + FAVE_POSTFIX


def GetXBMCVersion():
    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor eg, 13.9.902


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)


DIXIELOGOS  =  GetSetting('dixie.logo.folder')
SKIN        =  GetSetting('dixie.skin')
FILMON      =  GetSetting('FILMON')
VERSION     =  ADDON.getAddonInfo('version')
TITLE       = 'On-Tapp.EPG'
LOGOPACK    = 'Colour Logo Pack'
DEBUG       =  GetSetting('DEBUG') == 'true'
KEYMAP_HOT  = 'ottv_hot.xml'

CATCHUP     =  GetSetting('CATCHUP') == 'true'
ADULT       = 'Adultos'
SWISS       = 'Swisscom+IPTV'

datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras      = os.path.join(datapath, 'extras')
logos       = os.path.join(extras,   'logos')
# cookiepath  = os.path.join(datapath, 'cookies')
# cookiefile  = os.path.join(cookiepath, 'cookie')


def getSkinPath(xmlFile):
    # folder = os.path.join(PROFILE, 'extras', 'skins', SKIN)
    # file   = os.path.join(folder, 'resources', 'skins', 'Default', '720p', xmlFile)
    #
    # if sfile.exists(file):
    #     return folder

    return os.path.join(RESOURCES, 'skins', 'Default Skin')


OTT_RECORD = 'plugin.video.ottplanner'


def IsRecordingEnabled():
    try:
        return str(xbmcaddon.Addon(OTT_RECORD).getSetting('ENABLED')).lower() == 'true'
    except:
        return False


def RecordingStartPad():
    try:    return int(xbmcaddon.Addon(OTT_RECORD).getSetting('START_PAD'))
    except: return 5


def RecordingEndPad():
    try:    return int(xbmcaddon.Addon(OTT_RECORD).getSetting('END_PAD'))
    except: return 10


def RecordingFolder():
    return xbmcaddon.Addon(OTT_RECORD).getSetting('FOLDER')



def GetChannelType():
    return GetSetting('chan.type')


def MigrateChannels(dst):
    chfolder = os.path.join(dst, 'channels')
    src = os.path.join(datapath, 'channels')

    if not sfile.exists(chfolder):
        try:    sfile.copytree(src, chfolder)
        except: pass

    return chfolder


def GetChannelFolder():
    CUSTOM = '1'

    channelType = GetChannelType()

    if channelType == CUSTOM:
        path = GetSetting('user.chan.folder')
        MigrateChannels(path)
        return path

    return datapath


OTT_CHANNELS  = os.path.join(GetChannelFolder(), 'channels')
TEMPCHANNELS  = os.path.join(GetChannelFolder(), 'tempchannels')
JSONCHANNELS  = os.path.join(datapath, 'channels.json')


def GetLogoType():
    return GetSetting('logo.type')


def GetLogoFolder():
    logoType = GetLogoType()

    if logoType == '1':
        logoFolder = GetSetting('user.logo.folder')
        return logoFolder

    logoFolder = GetSetting('dixie.logo.folder')
    return logoFolder


def log(text):
    if not DEBUG:
        return

    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)

        path   =  os.path.join(PROFILE, 'log.txt')
        now    =  str(datetime.datetime.now())
        output = '%s - %s\r\n' % (now, output)
        sfile.append(path, output)
    except:
        pass


def getDSFVersion():
    try:
        version = int(DSFVER.replace('.', ''))
        return version
    except:
        version = 999
        return version


def isProtected():
    try:    return DSF.getSetting('PROTECTED') == 'true'
    except: return False

def isSwiss():
    try:    return DSF.getSetting('SWISSCOM') == 'true'
    except: return False

def isLimited():
    return xbmcgui.Window(10000).getProperty('DSF_LIMITED').lower() == 'true'


def formatTime(when):
    format = xbmc.getRegion('time').replace(':%S', '').replace('%H%H', '%H')
    return when.strftime(format)


# def getCategories():
#     if isLimited():
#        return ['Ni%C3%B1os']

#     return GetSetting('categories').split('|')


def getCategoryList(path):
    import StringIO
    from xml.etree import ElementTree

    xml  = None
    cat  = dict()
    try:
        if sfile.exists(path):
            xml = sfile.read(path)
    except:
        pass

    if not xml:
        return {}

    xml = StringIO.StringIO(xml)
    xml = ElementTree.iterparse(xml, events=("start", "end"))

    for event, elem in xml:
        try:
            if event == 'end':
               if elem.tag == 'cats':
                   channel  = elem.findtext('channel')
                   category = elem.findtext('category')
                   if channel != '' and category != '':
                       cat[channel] = category
        except:
            pass

    return cat


def CloseBusy():
    try: xbmc.executebuiltin('Dialog.Close(busydialog)')
    except: pass

def ShowBusy():
    try: xbmc.executebuiltin('ActivateWindow(busydialog)')
    except: pass

    return None


def notify(message, length=5000):
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)


def loadKeymap():
    try:
        file = 'zOTT_Keymap.xml'
        src  = os.path.join(HOME, 'resources', file)
        dst  = os.path.join('special://profile/keymaps', file)

        if not sfile.exists(dst):
            sfile.copy(src, dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def removeKeymap():
    try:
        file = 'zOTT_Keymap.xml'
        dst  = os.path.join('special://profile/keymaps', file)

        if sfile.exists(dst):
            sfile.remove(dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def WriteKeymap(start, end, filename, cmd):
    filename = os.path.join('special://profile/keymaps', filename)
    theFile  = sfile.file(filename, 'w')
    cmd      = '\t\t\t<%s>%s</%s>\n'  % (start, cmd, end)

    theFile.write('<keymap>\n')
    theFile.write('\t<global>\n')
    theFile.write('\t\t<keyboard>\n')

    theFile.write(cmd)

    theFile.write('\t\t</keyboard>\n')
    theFile.write('\n')
    theFile.write('\t\t<remote>\n')

    theFile.write(cmd)

    theFile.write('\t\t</remote>\n')
    theFile.write('\t</global>\n')
    theFile.write('</keymap>\n')

    theFile.close()

    return True


def deleteLog():
    try:
        path = os.path.join(PROFILE, 'log.txt')
        if sfile.exists(path):
            sfile.remove(path)
    except: pass


def disableDebug():
    SetSetting('DEBUG', 'false')
    log('========== disableDebug =========')
    log(GetSetting('DEBUG'))
    SetSetting('LOGFIX', 'true')
    log(GetSetting('LOGFIX'))
    xbmcaddon.Addon(OTT_ADDONID).setSetting('DEBUG', 'false')


def GetDixieUrl():
    if isDSF():
        if getSubSystem() == '80906':
            return baseurl + 'swi/'

        if getSubSystem() == '348821':
            return baseurl + 'spa/'

        if getSubSystem() == '809010':
            return baseurl + 'ita/'

    # return baseurl + 'test/'
    return baseurl + 'all/'


def getSubSystem():
    return DSF.getSetting('GVAX-SUBSYS')


def GetKey():
    if isDSF():
        return 'OTHER'

    return 'ALL CHANNELS'


def isDSF():
    # if xbmc.getCondVisibility('System.HasAddon(%s)' % DSFID) == 1:
    #     log(DSFID)
    #     return True

    return False


def GetExtraUrl():
    return resource


def GetLoginUrl():
    return loginurl


def GetVerifyUrl():
    return verifyurl


def CheckForUpdate(silent=True):
    if xbmcgui.Window(10000).getProperty('OTT_UPDATING') != 'True':
        programDB = os.path.join(PROFILE, 'program.db')
        if not sfile.exists(programDB):
            import update
            update.checkForUpdate(silent=silent)

    while xbmcgui.Window(10000).getProperty('OTT_UPDATING') == 'True':
        xbmc.sleep(1000)

# def CheckForUpdate(silent=True):
#     if xbmcgui.Window(10000).getProperty('OTT_UPDATING') != 'True':
#         import update
#         update.checkForUpdate(silent=silent)

#     while xbmcgui.Window(10000).getProperty('OTT_UPDATING') == 'True':
#         xbmc.sleep(1000)


def CleanFilename(text):
    if isDSF():
        return text

    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text


def getChannelData():
    from channel import Channel
    channelList = loadChannelList()

    for channel in channelList:
        id       = channel[0]
        title    = channel[1]
        category = channel[2]

        result = Channel(id, title)

        if category:
            try:
                result.categories = category
            except:
                dixie.log('Couldnt find %s in the categories' % (title))

        if result:
            yield result


def loadChannelList():
    import json
    return json.load(open(JSONCHANNELS))


def getAllChannels():
    channels = []

    try:
        current, dirs, files = sfile.walk(OTT_CHANNELS)
    except Exception, e:
        return channels

    for file in files:
        channels.append(file)

    sorted = []

    for id in channels:
        try:
            channel = getChannelFromFile(id)
            sorter  = channel.weight
            sorted.append([sorter, id, channel])
        except Exception as e:
            log('Error loading channel %r %r' % (id, e))

    sorted.sort()

    return sorted


def getChannelFromFile(id):
    from channel import Channel
    path = os.path.join(OTT_CHANNELS, id)

    if not sfile.exists(path):
        return None

    cfg = sfile.readlines(path)

    return Channel(cfg)


def GetGMTOffset():
    offset = 0
    return datetime.timedelta(hours = offset)


def BackupCats():
    currcat = os.path.join(PROFILE, 'cats.xml')
    bakcat  = os.path.join(PROFILE, 'cats-bak.xml')

    try:    sfile.copy(currcat, bakcat)
    except: pass


def FirstRun():
    if GetUser() != '' and GetPass() != '':
        return True

    # if DialogYesNo('Would you like to choose from one of our Channel Line-ups?', 
    #                 'These are customised listings all set up to save you time.',
    #                 'You can change this later using On-Tapp.TV Tools'):

    #     import extras

    #     # URL      = 'http://files.on-tapp.tv/'
    #     # URL      = 'http://files.on-tapp-networks.com/'
    #     baseurl  =  resource + 'lineups/'
    #     jsonurl  =  baseurl  + 'lineups.json'
    #     response =  extras.getList(jsonurl, 'lineups', 'lineup')

    #     lineups  = []
    #     for result in response:
    #         label  = result['-name']
    #         url    = baseurl + result['-url']
    #         sfZip  = baseurl + result['-sfzip']
    #         isSF   = result['-sf']

    #         lineups.append((label, url, isSF, sfZip))

    #     menu = []
    #     for lineup in lineups:
    #         menu.append(lineup[0])

    #     title  = 'Please select a Channel Line-up'
    #     option =  xbmcgui.Dialog().select(title, menu)
    #     extras.installLineup(lineups[option])

    if DialogYesNo('On-Tapp.TV requires a subscription.', '', 'Would you like to enter your account details now?'):
        username = DialogKB('', 'Enter Your On-Tapp.TV Username')
        password = DialogKB('', 'Enter Your On-Tapp.TV Password')

        if isDSF():
            xbmcaddon.Addon(DSFID).setSetting('username', username)
            xbmcaddon.Addon(DSFID).setSetting('password', password)
        else:
            SetSetting('username', username)
            SetSetting('password', password)

    else:
        return False

    # if details still not correct inform user and return False
    if GetUser() == '' or GetPass() == '':
        DialogOK('On-Tapp.TV will not run until you enter valid account details')
        return False

    return True


def ShowSettings():
    ADDON.openSettings()


def getPreviousTime(setting):
    try:
        time_object  = GetSetting(setting)
        time_object  = time_object.split('.')[0]
        previousTime = parseTime(time_object)
        return previousTime

    except:
        time_object  = '2001-01-01 00:00:00'
        previousTime = parseTime(time_object)
        return previousTime


def parseTime(dateString, convertInt=False):
    if type(dateString) in [str, unicode]:
        dt = dateString.split(' ')
        d  = dt[0]
        t  = dt[1]
        ds = d.split('-')
        ts = t.split(':')
        return datetime.datetime(int(ds[0]), int(ds[1]) ,int(ds[2]), int(ts[0]), int(ts[1]), int(ts[2]))

    if convertInt and type(dateString) in [int]:
        return datetime.datetime.fromtimestamp(float(dateString))

    return dateString


def validTime(setting, maxAge):
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds

    return nSeconds <= maxAge


def validToRun(silent=False):
    now = datetime.datetime.today()

    if getSeconds(now):
        if not doLogin(silent):
            return False

        SetSetting('LOGIN_TIME', str(now))

    return True


def getSeconds(now):
    setting      = 'LOGIN_TIME'
    previousTime = getPreviousTime(setting)
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds

    # log('======== previousTime ========')
    # log(previousTime)
    # log('======== delta ========')
    # log(delta)
    # log('======== nSeconds ========')
    # log(nSeconds)

    if nSeconds > 1458 * 60: # 24.3 hours
         return True

    return False


def doLogin(silent=False, retry=False):
    import session

    if retry:
        log ('************ On-Tapp.EPG Login (Retry) ************')
    else:
        log ('************ On-Tapp.EPG Login ************')

    try:
        code, response = session.getSession(silent=False)
    except:
        return False, False

    if isCF(code):
        log('===== CF ACTIVE =====')
        return True

    if 'no-access-redirect' in response:
        error   = '301 - No Access.'
        message = 'It appears that your subscription has expired.'
        log(message + ' : ' + error)
        if not silent:
            DialogOK(message, error, 'Please check your account at www.on-tapp.tv')
        return False

    areLost    = 'Are you lost' in response
    loginError = 'login_error' in response
    okay       =  (not areLost) and (not loginError)

    incorrectPwd  = 'The password you entered for the username' in response
    incorrectUser = 'Invalid username' in response
    retryMsg      = None

    if incorrectPwd:
        retryMsg = 'Your password is incorrect'
        focus = 0.3

    if incorrectUser:
        retryMsg = 'Your username is incorrect'
        focus = 0.2

    if not silent and retryMsg:
        if DialogYesNo(retryMsg, 'Would you like to change it and retry?'):
            openSettings(focus=focus)
            return doLogin(silent=False, retry=True)
        else:
            return False

    if okay:
        message = 'Logged into On-Tapp.TV'
        log(message)
        # if not silent:
        #     notify(message)
        return True

    try:
        error = re.compile('<div id="login_error">(.+?)<br />').search(response).groups(1)[0]
        error = error.replace('<strong>',  '')
        error = error.replace('</strong>', '')
        error = error.replace('<a href="https://www.on-tapp.tv/wp-login.php?action=lostpassword">Lost your password?</a>', '')
        error = error.strip()
    except:
        error = ''

    message = 'There was a problem logging into On-Tapp.TV.'
    log(message + ' : ' + error)
    if not silent:
        DialogOK(message, error, 'Please check your account at www.on-tapp.tv')

    return False


def isCF(code):
    if code in [404, 500, 502, 522, 524]:
        log('=== WE FOUND A CODE ===')
        log(code)
        return code


def GetUser():
    if isDSF():
       username = xbmcaddon.Addon(DSFID).getSetting('username')
       return username

    username = GetSetting('username')
    return username


def GetPass():
    if isDSF():
       password = xbmcaddon.Addon(DSFID).getSetting('password')
       return password

    password = GetSetting('password')
    return password


def GetCats():
    path = os.path.join(PROFILE, 'cats.xml')


def GetChannels():
    path = os.path.join(PROFILE , 'chan.xml')

    return path


def selectMenu(title, menu):
    options = []
    for option in menu:
        options.append(option[0])

    option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, str(line1), str(line2) , str(line3))

    #log('======================================================')
    #if 'buffer' in line1:
    #    import traceback
    #    for line in traceback.format_stack():
    #        log(line.strip())
    #log('======================================================')


def DialogKB(value='', heading=''):
    kb = xbmc.Keyboard(value, heading)
    #kb.setHeading(heading)
    kb.doModal()
    if (kb.isConfirmed()):
        value = kb.getText()
    return value


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def Progress(line1 = '', line2 = '', line3 = '', hide = False):
    dp = xbmcgui.DialogProgress()
    dp.create(TITLE, line1, line2, line3)
    dp.update(0)

    if hide:
        try:
            xbmc.sleep(250)
            WINDOW_PROGRESS = xbmcgui.Window(10101)
            CANCEL_BUTTON   = WINDOW_PROGRESS.getControl(10)
            CANCEL_BUTTON.setVisible(False)
        except:
            pass

    return dp


def openSettings(focus=None):
    xbmc.executebuiltin('Addon.OpenSettings(%s)' % ADDONID)

    if focus: 
        try:
            value1, value2 = str(focus).split('.')
 
            if FRODO:
                xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 200))
                xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 100))
            else:
                xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 100))
                xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 200))
  
        except Exception, e:
            log(str(e))
            return

    xbmc.sleep(1000)
    while xbmc.getCondVisibility('Window.IsActive(addonsettings)') == 1:
        xbmc.sleep(10)



def getFilters():
    filters = ['###', 'VOD', 'XXX', 'Adult', 'group-title="Live Sports"', 'group-title="For Adults"', 'group-title="Family"', 'group-title="Action / Adventure"', 'group-title="Comedy"', 'group-title="Recently Added"', 'group-title="Horror"', 'group-title="Western And War"', 'group-title="Christmas Movies"', 'group-title="Kids"', 'group-title="3D"', 'group-title="Drama"', 'group-title="Crime / Thriller"', 'group-title="Sci Fi"', 'group-title="PPV"', 'group-title="ex-Yu"', 'group-title="The Grand Tour"', 'group-title="GAME OF THRONES"', 'group-title="3D Movies"', 'group-title="0Day BluRay"', 'group-title="0Day Scene"']
    return filters


def exactMatch(word1, word2):
    word1 = removeDixiePrefix(word1)
    word2 = removeDixiePrefix(word2)

    word1 = word1.lower()
    word2 = word2.lower()

    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')

    if word1 == word2:
        return True

    return False


def fuzzyMatch(word1, word2):
    try:
        word1 = word1.lower()
        word2 = word2.lower()

        word1 = word1.replace(' ', '')
        word2 = word2.replace(' ', '')

        word1 = word1.replace('hd', '').replace('sd', '')
        word2 = word2.replace('hd', '').replace('sd', '')

        if word1 in word2:
            return True

        if word2 in word1:
            return True

    except: pass

    return False



    # if ('+1' in word1) and not ('+1' in word2):
    #     return False

    # if ('+1' in word2) and not ('+1' in word1):
    #     return False

    # if ('extra' in word1) and not ('extra' in word2):
    #     return False

    # if ('extra' in word2) and not ('extra' in word1):
    #     return False

    # if ('javu' in word1) and not ('javu' in word2):
    #     return False

    # if ('javu' in word2) and not ('javu' in word1):
    #     return False

    # if word1 in word2:
    #     return True

    # if word2 in word1:
    #     return True

    # return False


def removeDixiePrefix(text):
    prefixes = ['IPTV1: ', 'IPTV2: ', 'IPTV3: ', 'URL1: ', 'URL2: ', 'URL3: ', 'FILE1: ', 'FILE2: ', 'FILE3: ']

    for prefix in prefixes:
        if text.startswith(prefix):
            return text.replace(prefix, '', 1)

    return text.strip()


def cleanLabel(name):
    import re
    name  = re.sub('\([0-9)]*\)', '', name)

    items = name.split(']')
    name  = ''

    for item in items:
        if len(item) == 0:
            continue

        item += ']'
        item  = re.sub('\[[^)]*\]', '', item)

        if len(item) > 0:
            name += item

    name = name.replace('[', '')
    name = name.replace(']', '')
    name = name.strip()

    while True:
        length = len(name)
        name = name.replace('  ', ' ')
        if length == len(name):
            break

    tmplabel = name.strip()

    return cleanPrefix(tmplabel)


def cleanPrefix(text):
    name     = text.strip()
    tmplabel = stripName(name)

    if 'HD.' in tmplabel:
        tmplabel = tmplabel.replace('HD.', 'HD')

    prefixes  = ['INT: ', 'LIVE ', 'UK l ', 'IN l ', 'DE l ', 'RAD l ', ' Local', 'USA/CA : ', 'USA/CA:', 'CA: ','CA : ','CA ', 'UK : ', 'UK: ', 'UK | ', 'USA : ', 'USA :', 'USA: ', 'USA | ', 'USA ', 'US | ','US: ', ' -']
    viplables = ['VIP', 'VIP: ', 'VIP : ', 'VIp : ', 'V.I.P : ']
    replacers = ['=', '>', '<' '@', ' | ', '|', '.', ' : ', ':', '     ', '    ', '   ', '  ']

    for prefix in prefixes:
        if prefix in tmplabel:
            tmplabel = tmplabel.replace(prefix, '')

    for item in viplables:
        if item in tmplabel:
            tmplabel = tmplabel.replace(item, '')
            # tmplabel = tmplabel.upper()

    for item in replacers:
        if item in tmplabel:
            tmplabel = tmplabel.replace(item, ' ')

    tmplabel = tmplabel.replace(' ---------', '')

    return tmplabel


def stripName(text):
    stripList = os.path.join(PROFILE, 'ini', 'strip.txt')

    if os.path.exists(stripList):
        with open(stripList) as f:
            names = f.read().splitlines()
            for name in names:
                if text == name:
                    fixed = text.replace('SKY ', '')
                    return fixed
    return text


def getDBPath():
    return os.path.join(PROFILE, 'program.db')


def validateDB():
    K = 1024

    size = sfile.size(getDBPath())

    if size < 100 * K:
        import deleteDB
        deleteDB.deleteDB(silent=False)


def mapChannelName(name):
    import channelMap
    return channelMap.mapChannelName(name)


def getDayAsString(_date):
    today  = datetime.datetime.today().date()
    dayone = datetime.timedelta(days=1)

    if today == _date:
       return 'Today'

    if today - dayone == _date:
       return 'Yesterday'

    if today + dayone == _date:
       return 'Tomorrow'

    return _date.strftime("%A")


def _isInternetConnected():
    try:
        urls = []
        urls.append('google.com')
        urls.append('youtube.com')
        urls.append('facebook.com')
        urls.append('baidu.com')
        urls.append('wikipedia.org')
        urls.append('reddit.com')
        urls.append('yahoo.com')
        urls.append('qq.com')
        urls.append('taobao.com')
        urls.append('google.co.in')
        urls.append('amazon.com')
        urls.append('tmall.com')
        urls.append('twitter.com')
        urls.append('sohu.com')
        urls.append('instagram.com')
        urls.append('vk.com')
        urls.append('live.com')
        urls.append('jd.com')
        urls.append('sina.com.cn')
        urls.append('weibo.com')
        urls.append('yandex.ru')
        urls.append('360.cn')
        urls.append('google.co.jp')
        urls.append('blogspot.com')
        urls.append('google.co.uk')
        urls.append('list.tmall.com')
        urls.append('google.ru')
        urls.append('google.com.br')
        urls.append('netflix.com')
        urls.append('google.de')
        urls.append('google.com.hk')
        urls.append('twitch.tv')
        urls.append('google.fr')
        urls.append('linkedin.com')
        urls.append('yahoo.co.jp')
        urls.append('t.co')
        urls.append('csdn.net')
        urls.append('microsoft.com')
        urls.append('bing.com')
        urls.append('office.com')
        urls.append('ebay.com')
        urls.append('alipay.com')
        urls.append('google.it')
        urls.append('google.ca')
        urls.append('mail.ru')
        urls.append('ok.ru')
        urls.append('google.es')
        urls.append('pages.tmall.com')
        urls.append('msn.com')
        urls.append('google.com.tr')
        urls.append('google.com.au')
        urls.append('whatsapp.com')
        urls.append('spotify.com')
        urls.append('google.pl')
        urls.append('google.co.id')
        urls.append('google.com.ar')
        urls.append('google.co.th')
        urls.append('Naver.com')
        urls.append('sogou.com')
        urls.append('samsung.com')
        urls.append('accuweather.com')
        urls.append('goo.gl')
        urls.append('sm.cn')
        urls.append('googleweblight.com')
        urls.append('stackoverflow.com')
        urls.append('github.com')

        import random
        url  = random.choice(urls)

        import httplib
        conn = httplib.HTTPConnection(url)
        conn.request('HEAD', '/')

        return True

    except:
        pass

    return False


def isInternetConnected(maxWait=30):
    internet = _isInternetConnected()
    while not internet and maxWait > 0:
        xbmc.sleep(1000)
        internet = _isInternetConnected()
        maxWait -= 1

    return internet


def callstack():
    import traceback
    for line in traceback.format_stack():
        log(line.strip())

