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



class Channel(object):
    def __init__(self, id, title, logo = None, streamUrl = None, visible = 1, weight = -1, categories = ''):
        self.id         = id
        self.title      = title
        self.categories = categories
        self.logo       = logo
        self.streamUrl  = streamUrl
        self.visible    = int(visible)
        self.weight     = int(weight)


    def clone(self):
        c = Channel(self.id, self.title, self.logo, self.streamUrl, self.visible, self.weight, self.categories)
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

        return True


    def __eq__(self, other):
        if not hasattr(self, 'id'):
            return False

        if not hasattr(other, 'id'):
            return False

        return self.id == other.id


    def __repr__(self):
        try:
            return 'Channel(id=%s, title=%s, categories=%s, logo=%s, streamUrl=%s, weight=%s, visible=%s)' \
               % (self.id, self.title, self.categories, self.logo, self.streamUrl, str(self.weight), str(self.visible))
        except:
            return 'Can\'t display channel'


    def getWeight(self):
        return self.weight