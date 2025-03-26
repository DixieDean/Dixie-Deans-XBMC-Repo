#
#      Copyright (C) 2017 On-Tapp-Networks Limited
#

import xbmc
import xbmcaddon
import os
import re

import dixie

ADDONID = 'script.tvguidedixie'
ADDON   =  xbmcaddon.Addon(ADDONID)
HOME    =  ADDON.getAddonInfo('path')
PROFILE =  xbmc.translatePath(ADDON.getAddonInfo('profile'))


def mapLabel(labelmap, text):
    name = text.strip()
    for item in labelmap:
        if name.upper() == item[0].upper():
            return item[1].upper()
    return name


def cleanLabel(name):
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

    return name.strip()


def cleanStreamLabel(text):
    name     = text.strip()
    tmplabel = name.replace(' | ', ' ').replace('|', '').replace(' l ', ' ').replace(' : ', ' ')

    return tmplabel


def cleanPrefix(text):
    name     = text.strip()
    tmplabel = stripName(name)

    if 'HD.' in tmplabel:
        tmplabel = tmplabel.replace('HD.', 'HD')

    prefixes  = ['UK:', 'INT: ', 'LIVE ', 'UK l ', 'IN l ', 'IN | ', 'DE l ', 'RAD l ', 'VIP l ', ' Local', 'USA/CA : ', 'USA/CA: ', 'CA: ','CA : ','CA ','UK VIP : ', 'UK : ', 'UK: ', 'UK | ', 'USA : LIVE ', 'USA | LIVE ', 'USA : ', 'USA :', 'USA: ', 'USA | ', 'USA ', 'US | ','US: ', ' -','NORDIC ']
    viplabels = ['VIP: ', 'VIP : ', 'VIp : ', 'V.I.P : ']
    replacers = ['=', '>', '<' '@', ' | ', '|', '.', ' : ', ':', '     ', '    ', '   ', '  ']

    for prefix in prefixes:
        if prefix in tmplabel:
            tmplabel = tmplabel.replace(prefix, '')

    for item in viplabels:
        if item in tmplabel:
            tmplabel = tmplabel.replace(item, '')

    for item in replacers:
        if item in tmplabel:
            tmplabel = tmplabel.replace(item, ' ')

    return tmplabel.strip()


def editPrefix(prefixes, tmplabel):
    tmplabel = tmplabel.upper()

    for prefix in prefixes:
        oldprefix = prefix[0]
        newprefix = prefix[1]

        if oldprefix in tmplabel:
            tmplabel = tmplabel.replace(oldprefix, newprefix)

    tmplabel = tmplabel.replace('SKY CINEMA', 'SKY').replace('SKY MOVIES', 'SKY')

    return tmplabel


def mapEPGLabel(prefixes, maps, tmplabel):
    tmplabel = tmplabel.upper()

    for item in maps:
        oldmap = item[0]
        newmap = item[1]

        if (oldmap in tmplabel) or (tmplabel in oldmap):
            epglabel = tmplabel.replace(oldmap, newmap)
            return epglabel

    return tmplabel


def mapChannelName(maps, text):
    name = text.strip().upper()
    for item in maps:
        if name == item[0]:
            return item[1]

    return name


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

