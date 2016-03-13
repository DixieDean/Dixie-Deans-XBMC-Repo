# coding: UTF-8

import sys

l1ll11 = sys.version_info [0] == 2
l1l11 = 2048
l111 = 7

def l1111 (ll):
	global l1l1ll
	
	l11111 = ord (ll [-1])
	l1ll1l = ll [:-1]
	
	l1 = l11111 % len (l1ll1l)
	l1l1 = l1ll1l [:l1] + l1ll1l [l1:]
		
	if l1ll11:
		l1l111 = unicode () .join ([unichr (ord (char) - l1l11 - (l111l + l11111) % l111) for l111l, char in enumerate (l1l1)])
	else:
		l1l111 = str () .join ([chr (ord (char) - l1l11 - (l111l + l11111) % l111) for l111l, char in enumerate (l1l1)])
		
	return eval (l1l111)




import xbmc
import json
import os

import dixie


def createHDHRINI():
    l1ll = dixie.PROFILE
    path = os.path.join(l1ll, l1111 (u"ࠫ࡮ࡴࡩࠨࠀ"))
    l11  = os.path.join(path, l1111 (u"ࠬ࡮ࡤࡩࡴ࠱࡭ࡳ࡯ࠧࠁ"))
    
    l11ll1 = getHDHRChannels()
    result   = l11ll1[l1111 (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ࠂ")]
    l11l1l = result[l1111 (u"ࠧࡧ࡫࡯ࡩࡸ࠭ࠃ")]
    
    l1l  = file(l11, l1111 (u"ࠨࡹࠪࠄ"))
    
    l1l.write(l1111 (u"ࠩ࡞ࡷࡨࡸࡩࡱࡶ࠱࡬ࡩ࡮࡯࡮ࡧࡵࡹࡳ࠴ࡶࡪࡧࡺࡡࡡࡴࠧࠅ"))
    
    for l1lll1 in l11l1l:
        l11l1  = l1lll1[l1111 (u"ࠪࡰࡦࡨࡥ࡭ࠩࠆ")]
        stream = l1111 (u"ࠫࠪࡹࠧࠇ") % l1lll1[l1111 (u"ࠬ࡬ࡩ࡭ࡧࠪࠈ")]

        l1l.write(l1111 (u"࠭ࠥࡴࠩࠉ") % l11l1)
        l1l.write(l1111 (u"ࠧ࠾ࠩࠊ"))
        l1l.write(l1111 (u"ࠨࠧࡶࠫࠋ") % stream)
        l1l.write(l1111 (u"ࠩ࡟ࡲࠬࠌ"))

    l1l.write(l1111 (u"ࠪࡠࡳ࠭ࠍ"))
    l1l.close()


def getHDHRChannels():
    l1l1l1 = getHDHRDevices()
    l11l1l   = getChannels(l1l1l1)
    return l11l1l


def getHDHRDevices():
    l11l11 = getUPNP()
    l1llll  = l11l11[l1111 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࠎ")]
    l1111l     = l1llll[l1111 (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࠏ")]

    for l11lll in l1111l:
        l11l1   = l11lll[l1111 (u"࠭࡬ࡢࡤࡨࡰࠬࠐ")]
        l1l1l = l1111 (u"ࠧࠦࡵࠪࠑ") % l11lll[l1111 (u"ࠨࡨ࡬ࡰࡪ࠭ࠒ")]
        if l1111 (u"ࠩࡋࡈࡍࡵ࡭ࡦࡔࡸࡲࠬࠓ") in l11l1:
            return l1l1l


def getUPNP():
    l11l   = (l1111 (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡹࡵࡴࡰ࠻࠱࠲ࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿࠷ࡽࠨࠔ"))
    result = sendJSON(l11l)
    return result


def getChannels(l1l1l1):
    l1lll = (l1111 (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࡃࡩࡣࡱࡲࡪࡲࡳ࠰ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽࠵ࢂ࠭ࠕ") % l1l1l1)
    l11l1l  = sendJSON(l1lll)
    return l11l1l


def sendJSON(l11ll):
    l11ll1 = xbmc.executeJSONRPC(l11ll)
    return json.loads(l11ll1.decode(l1111 (u"ࠬࡻࡴࡧ࠯࠻ࠫࠖ"), l1111 (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ࠗ")))


def getPlaylist():
    import requests
    l1l11l = [l1111 (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡹ࠰ࡦࡳ࠴ࡪࡢࡤࡪ࠳࠵ࠬ࠘"), l1111 (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡭ࡲࡨ࡮࠴ࡣࡤ࡮ࡧ࠲࡮ࡵࠧ࠙"), l1111 (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࡤ࡭ࡴ࠴ࡣࡤ࡮ࡲࡹࡩࡺࡶ࠯ࡱࡵ࡫࠴ࡱ࡯ࡥ࡫ࠪࠚ"), l1111 (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࡫ࡴ࠸࡬࠯࡫ࡱ࡯࠴ࡱ࡯ࡥ࡫ࠪࠛ")]
    l111ll =  l1111 (u"ࠫࠨࡋࡘࡕࡏ࠶࡙ࠬࠜ")

    for url in l1l11l:
        dixie.log(url)
        try:
            l111l1  = requests.get(url)
            l1ll1 = l111l1.text
        except: pass

        if l111ll in l1ll1:
            path = os.path.join(dixie.PROFILE, l1111 (u"ࠬࡶ࡬ࡢࡻ࡯࡭ࡸࡺ࠮࡮࠵ࡸࠫࠝ"))
            with open(path, l1111 (u"࠭ࡷࠨࠞ")) as f:
                f.write(l1ll1)
