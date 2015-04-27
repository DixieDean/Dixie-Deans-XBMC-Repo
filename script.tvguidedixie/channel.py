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

import os

class Channel(object):
    def __init__(self, id, title='', logo='', streamUrl='', visible=1, weight=-1, categories='', userDef=0, desc='', isClone=0):
        if isinstance(id, list):
            self.setFromList(id)
        else:
            self.set(id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone)


    def set(self, id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone):
        if logo:
            logo = logo.replace('\\', '/').replace('\n', '').replace('\r', '')
        self.id         = id.replace('\n', '').replace('\r', '')
        self.title      = title.replace('\n', '').replace('\r', '')
        self.categories = categories.replace('\n', '').replace('\r', '')
        self.logo       = logo
        self.streamUrl  = streamUrl.replace('\n', '').replace('\r', '')

        try:    self.visible = int(visible.replace('\n', '').replace('\r', ''))
        except: self.visible = int(visible)

        try:    self.weight = int(weight.replace('\n', '').replace('\r', ''))
        except: self.weight = int(weight)

        try:    self.userDef = int(userDef.replace('\n', '').replace('\r', ''))
        except: self.userDef = int(userDef)

        try:    self.isClone = int(isClone.replace('\n', '').replace('\r', ''))
        except: self.isClone = int(isClone)

        self.desc = desc.replace('\n', '').replace('\r', '')


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


    def writeToFile(self, filename):
        cloneID = -1
        localID = self.id


        if self.isClone:
            filename, cloneID = self.cloneFilename(filename)
            localID += cloneID
            
        try:    f = open(filename, mode='w')
        except: return False        

        try:    f.write(localID.encode('utf8') + '\n')
        except: f.write(localID + '\n')

        f.write(self.title.encode('utf8') + '\n')

        if self.logo:
            f.write(self.logo.encode('utf8') + '\n')
        else:
            f.write('\n')

        if self.streamUrl:
            f.write(self.streamUrl.encode('utf8') + '\n')
        else:
            f.write('\n')

        if self.visible:
            f.write('1\n')
        else:
            f.write('0\n')

        f.write(str(self.weight) + '\n')
        f.write(self.categories.encode('utf8') + '\n')

        if self.userDef:
            f.write('1\n')
        else:
            f.write('0\n')

        if self.desc:
            f.write(self.desc.encode('utf8') + '\n')
        else:
            f.write('\n')

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

        while os.path.exists(filename):
            index += 1
            filename = root + '_clone_%d' % index

        return filename, '_clone_%d' % index


    def clone(self):
        c = Channel(self.id, self.title, self.logo, self.streamUrl, self.visible, self.weight, self.categories, self.userDef, self.desc, self.isClone)
        return c
    
    
    def compare(self, channel):
        if self.id != channel.id:
            return False
        return True


    # def compare(self, channel):
    #     if self.visible != channel.visible:
    #         return False
    #
    #     if self.weight != channel.weight:
    #         return False
    #
    #     if self.title != channel.title:
    #         return False
    #
    #     if self.logo != channel.logo:
    #         return False
    #
        #if self.categories != channel.categories:
        #    return False

        # return True


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