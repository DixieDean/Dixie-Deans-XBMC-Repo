
#       Copyright (C) 2013-
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
import xbmc
import re

def add(name, cmd, thumb = None):
    if thumb == None:
        thumb = ''  
  
    uName = name.upper()

    faves = getFavourites()
    found = False

    writeFile(faves, 'favourites.bak') 

    newEntry = 'name="%s" thumb="%s">%s' % (name, thumb, cmd)

    for i in range(len(faves)):
        try:
            name = re.compile('name="(.+?)"').findall(faves[i])[0]
        
            if name.upper() == uName:            
                found    = True            
                faves[i] = newEntry
                break
        except:
            pass

    if not found:
        faves.append(newEntry)

    writeFile(faves)

    
def getFavourites():
    xml  = '<favourites></favourites>'
    path = xbmc.translatePath('special://profile/favourites.xml')
    if os.path.exists(path):  
        fav = open(path , 'r')
        xml = fav.read()
        fav.close()

    return re.compile('<favourite(.+?)</favourite>').findall(xml)


def writeFile(faves, filename = 'favourites.xml'):
    path = xbmc.translatePath('special://profile/%s' % filename)
    f    = open(path, mode='w')

    f.write('<favourites>')
    for fave in faves:
        f.write('\n\t<favourite ')
        f.write(fave)
        f.write('</favourite>')
    f.write('\n</favourites>')            
    f.close()


if __name__ == "__main__":
    pass