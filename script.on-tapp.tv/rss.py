#
#       Copyright (C) 2016
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

import xbmcgui
import urllib2

SHOW_FADE_EFFECT = 'effect=fade start=0 end=100 time=1000 delay=0, condition=Control.IsVisible(%d)'


def getURL(url):
    req = urllib2.Request(url)
    
    response = urllib2.urlopen(req)
    html     = response.read()
    response.close()

    return html


class RSS(object):
    def __init__(self, winID, x,  y,  width, height, url, refresh=20, reload=3600):
        self.duplicates = False
        self.url        = url
        self.tick       = 0
        self.index      = -1
        self.images     = None
        self.control    = None 
        self.cache      = None 

        self.winID  = winID
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.refresh = refresh
        self.reload  = reload


    def close(self):
        if self.control:
            try:    xbmcgui.Window(self.winID).removeControl(self.self.control)
            except: pass


    def update(self):
        if (self.images == None) or (self.tick == 0):
            self.images = self.getImages()

        if self.tick % self.refresh == 0:
            self.cycleImage()

        self.tick += 1

        if self.tick > self.reload:
            self.tick = 0


    def getImages(self):
        import re

        imgList  = []
        response = getURL(self.url)
        images   = re.compile('url="(.+?)"').findall(response)

        for image in images:
            if (self.duplicates) or (image not in imgList):
                imgList.append(image)

        return imgList


    def cycleImage(self):
        self.index += 1

        if self.index == len(self.images):
            self.index = 0

        try:
            self.setImage(self.images[self.index])
            self.preFetch()
            
        except Exception, e:
            pass


    def preFetch(self):
        try:
            if self.cache == None:
                self.cache = xbmcgui.ControlImage(-10, -10, 10, 10, '')

            self.cache.setImage(self.images[self.index+1])

            xbmcgui.Window(self.winID).addControl(self.cache)

        except Exception, e:
            self.cache = None
            

    def setImage(self, image):
        #http://mirrors.xbmc.org/docs/python-docs/stable/xbmcgui.html#ControlImage
        wnd = xbmcgui.Window(self.winID)

        prevCtrl = self.control

        self.control = xbmcgui.ControlImage(self.x, self.y, self.width, self.height, filename=image, aspectRatio=0)

        self.control.setVisible(False)

        wnd.addControl(self.control)

        self.control.setAnimations([('Conditional', SHOW_FADE_EFFECT % self.control.getId())])

        self.control.setVisible(True)

        if self.prevCtrl:
            try:    wnd.removeControl(self.prevCtrl)
            except: pass