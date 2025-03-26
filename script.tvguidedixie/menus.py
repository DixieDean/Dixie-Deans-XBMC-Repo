
#       Copyright (C) 2017
#       OTT Networks Ltd
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

import xbmcgui

def selectMenu(menu, title=''):
    options = []
    for option in menu:
        options.append(option[0])

    option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]


def showMenu(menu, title='', forceSelect=False):
    if forceSelect or not hasattr(xbmcgui.Dialog(), 'contextmenu'):
        return selectMenu(menu, title)

    list = []
    for item in menu:
        list.append(item[0])

    param = xbmcgui.Dialog().contextmenu(list)

    if param > -1:
        param = menu[param][1]

    return param