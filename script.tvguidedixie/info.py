#
#       Copyright (C) 2015-
#       Sean Poyser (seanpoyser@gmail.com)
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

import datetime
import time
import sqlite3
import os

import dixie
from channel import Channel
from source import Program

PROGRAM_DB = 'program.db'
DB_KEY     = 'dixie.' + dixie.GetKey()


class InfoService(object):
    def __init__(self):
        #initialise database connection
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime)
        sqlite3.register_converter('timestamp',     self.convert_datetime)

        path = os.path.join(dixie.PROFILE, PROGRAM_DB)
        self.conn = sqlite3.connect(path, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row


    def adapt_datetime(self, ts):
        # http://docs.python.org/2/library/sqlite3.html#registering-an-adapter-callable
        return time.mktime(ts.timetuple())


    def convert_datetime(self, ts):
        try:   return datetime.datetime.fromtimestamp(float(ts))
        #except ValueError: return None
        except: return None
    
    def getCurrentProgram(self, channel):   
        try:    
            channelMap = {}
            if channel.id:
                id = channel.id.split('_clone_')[0]
                channelMap[id] = channel

            channelMap[channel.id] = channel

            strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

            program = None

            now = datetime.datetime.now()
            c = self.conn.cursor()
            c.execute('SELECT * FROM programs WHERE channel IN ' + strCh  + ' AND source=? AND start_date <= ? AND end_date >= ?', [DB_KEY, now, now])
            row = c.fetchone()
            if row:
                program = Program(channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
            c.close()

            return program

        except:
            return None


    def getNextProgram(self, program):
        try:
            channel = ''
            channelMap = {}
            if program.channel.id:
                id = program.channel.id.split('_clone_')[0]
                channelMap[id] = channel

            channelMap[program.channel.id] = channel

            strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'
  
            nextProgram = None
            c = self.conn.cursor()
            c.execute('SELECT * FROM programs WHERE channel IN ' + strCh + ' AND source=? AND start_date >= ? ORDER BY start_date ASC LIMIT 1', [DB_KEY, program.endDate])
            row = c.fetchone()
            if row:
                nextProgram = Program(program.channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
            c.close()

            return nextProgram

        except:
            return None


    def getPreviousProgram(self, program):
        try:
            channel = ''
            channelMap = {}
            if program.channel.id:
                id = program.channel.id.split('_clone_')[0]
                channelMap[id] = channel

            channelMap[program.channel.id] = channel

            strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

            previousProgram = None
            c = self.conn.cursor()
            c.execute('SELECT * FROM programs WHERE channel IN ' + strCh + ' AND source=? AND end_date <= ? ORDER BY start_date DESC LIMIT 1', [DB_KEY, program.startDate])
            row = c.fetchone()
            if row:
                previousProgram = Program(program.channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
            c.close()

            return previousProgram

        except:
            return None
