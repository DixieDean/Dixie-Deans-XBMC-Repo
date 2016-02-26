#
#       Copyright (C) 2014
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

import urllib
import os
import sfile
import dixie

DSF = dixie.isDSF()


def tidy(text):
    if (not isinstance(text, unicode)) and (not isinstance(text, str)):
        text = str(text)
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    text = text.replace('\\', '/')
    return text


class Channel(object):
    def __init__(self, id, title='', logo='', streamUrl='', visible=1, weight=-1, categories='', userDef=0, desc='', isClone=0):
        if isinstance(id, list):
            self.setFromList(id)
        else:
            self.set(id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone)


    def set(self, id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone):
        if logo:
            logo = tidy(logo)

        self.id         = tidy(id)
        self.title      = tidy(title)
        self.categories = tidy(categories)
        self.logo       = logo
        self.streamUrl  = tidy(streamUrl)

        self.visible = int(tidy(visible))
        self.weight  = int(tidy(weight))
        self.userDef = int(tidy(userDef))
        self.isClone = int(tidy(isClone))

        self.desc = tidy(desc)

        if DSF:
            self.title = urllib.unquote_plus(self.title)

    def isProtected(self):
        return dixie.ADULT in self.categories


    def setFromList(self, list):
        userDef = False
        isClone = False
        desc    = ''

        if len(list) > 7:
            userDef = list[7]

        if len(list) > 8:
            desc = list[8]

        if len(list) > 9:
            isClone = list[9]
        
        self.set(list[0], list[1], list[2], list[3], list[4], list[5], list[6], userDef, desc, isClone)


    def safeWriteToFile(self, file, text):
        if text:
            try:    file.write(text.encode('utf8'))
            except: file.write(text)

        file.write('\n')


    def writeToFile(self, filename):
        cloneID = -1
        localID = self.id

        if self.isClone:
            filename, cloneID = self.cloneFilename(filename)
            localID += cloneID
            
        try:    f = sfile.file(filename, 'w')
        except: return False

        self.safeWriteToFile(f, localID)
        self.safeWriteToFile(f, self.title)
        self.safeWriteToFile(f, self.logo)
        self.safeWriteToFile(f, self.streamUrl)

        if self.visible:
            f.write('1\n')
        else:
            f.write('0\n')

        f.write(str(self.weight) + '\n')

        self.safeWriteToFile(f, self.categories)

        if self.userDef:
            f.write('1\n')
        else:
            f.write('0\n')

        self.safeWriteToFile(f, self.desc)

        if self.isClone:
            f.write('1\n')
        else:
            f.write('0\n')

        f.close()
        return True


    def cloneFilename(self, filename):
        if '_clone_' in filename:
            return filename, ''

        index    = 1
        root     = filename
        filename = root + '_clone_%d' % index

        while sfile.exists(filename):
            index += 1
            filename = root + '_clone_%d' % index

        return filename, '_clone_%d' % index


    def clone(self):
        c = Channel(self.id, self.title, self.logo, self.streamUrl, self.visible, self.weight, self.categories, self.userDef, self.desc, self.isClone)
        return c
    
   
    def compare(self, channel):
        if self.visible != channel.visible:
            return False
    
        if self.weight != channel.weight:
            return False
    
        if self.title != channel.title:
            return False
    
        if self.logo != channel.logo:
            return False
    
        if self.categories != channel.categories:
           return False

        return True


    def __eq__(self, other):
        if not hasattr(self, 'id'):
            return False

        if not hasattr(other, 'id'):
            return False

        return self.id == other.id


    def __repr__(self):
        try:
            return 'Channel(id=%s, title=%s, categories=%s, logo=%s, streamUrl=%s, weight=%s, visible=%s userDef=%s desc=%s isClone=%s)' \
               % (self.id, self.title, self.categories, self.logo, self.streamUrl, str(self.weight), str(self.visible), str(self.userDef), self.desc, str(self.isClone))
        except:
            return 'Can\'t display channel'


    def getWeight(self):
        return self.weight