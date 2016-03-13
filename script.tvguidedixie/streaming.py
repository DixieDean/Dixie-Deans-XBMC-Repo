# -*- coding: utf-8 -*-
#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com) - With acknowledgement to some original code by twinther (Tommy Winther)
#



import xbmc
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError
import ConfigParser
import os
import re
import xbmcaddon
import urllib
import requests
import json

import dixie

ADDON    = dixie.ADDON
LOCAL    = dixie.GetSetting('local.ini') == 'true'
FTVINI   = dixie.GetSetting('ftv.ini')
datapath = dixie.PROFILE


class StreamsService(object):
    def __init__(self):

        self.addonsParser = ConfigParser.ConfigParser(dict_type=OrderedDict)
        self.addonsParser.optionxform = lambda option: option

        iniFiles = self.getIniFiles()

        for file in iniFiles:
            try:    self.addonsParser.read(file)
            except: pass
        

    def getIniFiles(self):
        files = []

        import glob
        ini   = os.path.join(datapath, 'ini', '*.*')
        files = glob.glob(ini)
        
        for i in range(10):
            file = dixie.GetSetting('INI_%d' % i)
            if len(file) > 0:
                if file not in files:
                    files.append(file)

        files.append(os.path.join(datapath, 'addons.ini'))
        
        if LOCAL:
            files.append(os.path.join(datapath, 'local.ini'))

        if FTVINI == 'UK Links':
            files.append(os.path.join(datapath, 'uk.ini'))
        else:
            files.append(os.path.join(datapath, 'nongeo.ini'))

        return files
        

    def loadFavourites(self):
        entries = list()
        path = xbmc.translatePath('special://profile/favourites.xml')
        if os.path.exists(path):
            f = open(path)
            xml = f.read()
            f.close()

            try:
                doc = ElementTree.fromstring(xml)
                for node in doc.findall('favourite'):
                    value = node.text
                    value = node.text.replace(',return','')

                    if value[0:11] == 'PlayMedia("':
                        value = value[11:-2]
                    elif value[0:10] == 'PlayMedia(':
                        value = value[10:-1]
                    elif value[0:22] == 'ActivateWindow(10025,"':
                        value = value[22:-2]
                    elif value[0:21] == 'ActivateWindow(10025,':
                        value = value[22:-1]
                    elif value[0:22] == 'ActivateWindow(10001,"':
                        value = value[22:-2]
                    elif value[0:21] == 'ActivateWindow(10001,':
                        value = value[22:-1]
                    else:
                        continue
                    entries.append((node.get('name'), value))
            except ExpatError:
                pass

        return entries


    def loadPlaylist(self):
        iptv_type = dixie.GetSetting('playlist.type')
        IPTV_URL  = '0'
        IPTV_FILE = '1'

        entries   = list()
        label     = ''
        value     = ''
                
        if iptv_type == IPTV_FILE:
            path = os.path.join(dixie.GetSetting('playlist.file'))
        else:
            url  = dixie.GetSetting('playlist.url')
            path = os.path.join(datapath, 'playlist.m3u')

            try:
                if url == '':
                    path = os.path.join(datapath, 'playlist.m3u')
                else:
                    request  = requests.get(url)
                    playlist = request.content

                    with open(path, 'wb') as f:
                        f.write(playlist)
            except: pass

        if os.path.exists(path):
            f = open(path)
            playlist = f.readlines()
            f.close()
            
            for line in playlist:
                if line.startswith('#EXTINF:'):
                    label = line.split(',')[-1].strip()
        
                elif line.startswith('rtmp') or line.startswith('rtmpe') or line.startswith('rtsp') or line.startswith('http'):
                    value = line.replace('rtmp://$OPT:rtmp-raw=', '').replace('\n', '')

                    entries.append((label, value))

            entries.sort()
            return entries


    def locateSuperFavourites(self, title):
        SUPERFAVES   = 'plugin.program.super.favourites'
        SF_INSTALLED = xbmc.getCondVisibility('System.HasAddon(%s)' % SUPERFAVES) == 1

        if not SF_INSTALLED:
            return None

        sfAddon = xbmcaddon.Addon(id = SUPERFAVES)

        ROOT = sfAddon.getSetting('FOLDER')
        if not ROOT:
            ROOT = 'special://profile/addon_data/plugin.program.super.favourites/'

        folder = os.path.join(ROOT, 'Super Favourites')

        items = []

        self._locateSuperFavourites(title.lower(), folder, items)

        return items


    def _locateSuperFavourites(self, title, folder, items):    
        import sfile  
        import settings
        import urllib
        current, dirs, files = sfile.walk(folder)

        for dir in dirs:    
            folder = os.path.join(current, dir)
            if dir.lower() == title:
                cfg      = os.path.join(folder, 'folder.cfg')
                autoplay = settings.get('AUTOPLAY', cfg)

                if autoplay:
                    uTitle  = urllib.quote_plus(title)
                    mode    = 5400
                    uFolder = urllib.quote_plus(folder)
                    toAdd   = 'plugin://plugin.program.super.favourites/?label=%s&mode=%d&path=%s' % (uTitle, mode, uFolder)
                else:               
                    uTitle  = urllib.quote_plus(title)
                    mode    = 400
                    uFolder = urllib.quote_plus(folder)
                    toAdd   = 'plugin://plugin.program.super.favourites/?label=%s&mode=%d&path=%s' % (uTitle, mode, uFolder)
                    toAdd   = '__SF__ActivateWindow(10025,"%s",return)' % toAdd
                    
                items.append(['SF_'+folder, toAdd])

            self._locateSuperFavourites(title, folder, items)
        

    def getAddons(self):
        return self.addonsParser.sections()

    def getAddonStreams(self, id):
        return self.addonsParser.items(id)

    def detectStream(self, channel):
        """
        @param channel:
        @type channel: source.Channel
        """

        matches = list()

        # Get any Super Favourites with channel name
        superFaves = self.locateSuperFavourites(channel.title)
        
        if superFaves:
            if len(superFaves) == 1:
                matches.append((superFaves[0][0], 'Super Folder', superFaves[0][1]))
            else:
                index = 0
                for superFave in superFaves:
                    index += 1
                    label = 'Super Folder (%d)' % index
                    matches.append((superFave[0], label, superFave[1]))        

        # Get any Add-ons with channel name
        for id in self.getAddons():
            try:
                xbmcaddon.Addon(id)
            except Exception:
                continue # ignore addons that are not installed

            for (label, stream) in self.getAddonStreams(id):
                label = label.upper()
                channel.title = channel.title.upper()
                
                if (channel.title in label) or (label in channel.title):
                    matches.append((id, label, stream))

        
        # Get any Kodi Favourites with channel name
        kodiFaves = self.loadFavourites()
        
        if kodiFaves:
            id = 'kodi-favourite'
            
            for (label, stream) in kodiFaves:
                label = label.upper()
                channel.title = channel.title.upper()

                if (channel.title in label) or (label in channel.title):
                    matches.append((id, label, stream))
                

        # Get any Playlist entries with channel name
        iptvPlaylist = self.loadPlaylist()
        
        if iptvPlaylist:
            id = 'iptv-playlist'
        
            for (label, stream) in iptvPlaylist:
                label = label.upper()
                channel.title = channel.title.upper()

                if (channel.title in label) or (label in channel.title):
                    matches.append((id, label, stream))


        if len(matches) == 1:
            return matches[0][2]
        else:
            return matches


class OrderedDict(dict):
    # From: http://code.activestate.com/recipes/576693/
    'Dictionary that remembers insertion order'
    # An inherited dict maps keys to values.
    # The inherited dict provides __getitem__, __len__, __contains__, and get.
    # The remaining methods are order-aware.
    # Big-O running times for all methods are the same as for regular dictionaries.

    # The internal self.__map dictionary maps keys to links in a doubly linked list.
    # The circular doubly linked list starts and ends with a sentinel element.
    # The sentinel element never gets deleted (this simplifies the algorithm).
    # Each link is stored as a list of length three:  [PREV, NEXT, KEY].

    def __init__(self, *args, **kwds):
        '''Initialize an ordered dictionary.  Signature is the same as for
        regular dictionaries, but keyword arguments are not recommended
        because their insertion order is arbitrary.

        '''
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = []                     # sentinel node
            root[:] = [root, root, None]
            self.__map = {}
        self.__update(*args, **kwds)

    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        'od.__setitem__(i, y) <==> od[i]=y'
        # Setting a new item creates a new link which goes at the end of the linked
        # list, and the inherited dictionary is updated with the new key/value pair.
        if key not in self:
            root = self.__root
            last = root[0]
            last[1] = root[0] = self.__map[key] = [last, root, key]
        dict_setitem(self, key, value)

    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        'od.__delitem__(y) <==> del od[y]'
        # Deleting an existing item uses self.__map to find the link which is
        # then removed by updating the links in the predecessor and successor nodes.
        dict_delitem(self, key)
        link_prev, link_next, key = self.__map.pop(key)
        link_prev[1] = link_next
        link_next[0] = link_prev

    def __iter__(self):
        'od.__iter__() <==> iter(od)'
        root = self.__root
        curr = root[1]
        while curr is not root:
            yield curr[2]
            curr = curr[1]

    def __reversed__(self):
        'od.__reversed__() <==> reversed(od)'
        root = self.__root
        curr = root[0]
        while curr is not root:
            yield curr[2]
            curr = curr[0]

    def clear(self):
        'od.clear() -> None.  Remove all items from od.'
        try:
            for node in self.__map.itervalues():
                del node[:]
            root = self.__root
            root[:] = [root, root, None]
            self.__map.clear()
        except AttributeError:
            pass
        dict.clear(self)

    def popitem(self, last=True):
        '''od.popitem() -> (k, v), return and remove a (key, value) pair.
        Pairs are returned in LIFO order if last is true or FIFO order if false.

        '''
        if not self:
            raise KeyError('dictionary is empty')
        root = self.__root
        if last:
            link = root[0]
            link_prev = link[0]
            link_prev[1] = root
            root[0] = link_prev
        else:
            link = root[1]
            link_next = link[1]
            root[1] = link_next
            link_next[0] = root
        key = link[2]
        del self.__map[key]
        value = dict.pop(self, key)
        return key, value

    # -- the following methods do not depend on the internal structure --

    def keys(self):
        'od.keys() -> list of keys in od'
        return list(self)

    def values(self):
        'od.values() -> list of values in od'
        return [self[key] for key in self]

    def items(self):
        'od.items() -> list of (key, value) pairs in od'
        return [(key, self[key]) for key in self]

    def iterkeys(self):
        'od.iterkeys() -> an iterator over the keys in od'
        return iter(self)

    def itervalues(self):
        'od.itervalues -> an iterator over the values in od'
        for k in self:
            yield self[k]

    def iteritems(self):
        'od.iteritems -> an iterator over the (key, value) items in od'
        for k in self:
            yield (k, self[k])

    def update(*args, **kwds):
        '''od.update(E, **F) -> None.  Update od from dict/iterable E and F.

        If E is a dict instance, does:           for k in E: od[k] = E[k]
        If E has a .keys() method, does:         for k in E.keys(): od[k] = E[k]
        Or if E is an iterable of items, does:   for k, v in E: od[k] = v
        In either case, this is followed by:     for k, v in F.items(): od[k] = v

        '''
        if len(args) > 2:
            raise TypeError('update() takes at most 2 positional '
                            'arguments (%d given)' % (len(args),))
        elif not args:
            raise TypeError('update() takes at least 1 argument (0 given)')
        self = args[0]
        # Make progressively weaker assumptions about "other"
        other = ()
        if len(args) == 2:
            other = args[1]
        if isinstance(other, dict):
            for key in other:
                self[key] = other[key]
        elif hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value
        for key, value in kwds.items():
            self[key] = value

    __update = update  # let subclasses override update without breaking __init__

    __marker = object()

    def pop(self, key, default=__marker):
        '''od.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.

        '''
        if key in self:
            result = self[key]
            del self[key]
            return result
        if default is self.__marker:
            raise KeyError(key)
        return default

    def setdefault(self, key, default=None):
        'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
        if key in self:
            return self[key]
        self[key] = default
        return default

    def __repr__(self, _repr_running={}):
        'od.__repr__() <==> repr(od)'
        call_key = id(self), _get_ident()
        if call_key in _repr_running:
            return '...'
        _repr_running[call_key] = 1
        try:
            if not self:
                return '%s()' % (self.__class__.__name__,)
            return '%s(%r)' % (self.__class__.__name__, self.items())
        finally:
            del _repr_running[call_key]

    def __reduce__(self):
        'Return state information for pickling'
        items = [[k, self[k]] for k in self]
        inst_dict = vars(self).copy()
        for k in vars(OrderedDict()):
            inst_dict.pop(k, None)
        if inst_dict:
            return (self.__class__, (items,), inst_dict)
        return self.__class__, (items,)

    def copy(self):
        'od.copy() -> a shallow copy of od'
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S
        and values equal to v (which defaults to None).

        '''
        d = cls()
        for key in iterable:
            d[key] = value
        return d

    def __eq__(self, other):
        '''od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
        while comparison to a regular mapping is order-insensitive.

        '''
        if isinstance(other, OrderedDict):
            return len(self)==len(other) and self.items() == other.items()
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self == other
