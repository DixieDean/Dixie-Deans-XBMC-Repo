# coding: UTF-8

import sys

l1 = sys.version_info [0] == 2
l1l1l1 = 2048
l1ll1 = 7

def l1ll1l (ll):
	global l1l1ll
	
	l111l1 = ord (ll [-1])
	l111l = ll [:-1]
	
	l1ll = l111l1 % len (l111l)
	l11ll1 = l111l [:l1ll] + l111l [l1ll:]
		
	if l1:
		l1l11l = unicode () .join ([unichr (ord (char) - l1l1l1 - (l11ll + l111l1) % l1ll1) for l11ll, char in enumerate (l11ll1)])
	else:
		l1l11l = str () .join ([chr (ord (char) - l1l1l1 - (l11ll + l111l1) % l1ll1) for l11ll, char in enumerate (l11ll1)])
		
	return eval (l1l11l)




import xbmc
import json
import os

import dixie


def createPVRINI():
    if not dixie.PVRACTIVE:
        return

    l1lll1lll = dixie.PROFILE
    path = os.path.join(l1lll1lll, l1ll1l (u"ࠧࡪࡰ࡬ࠫࡺ"))
    l1llll11l  = os.path.join(path, l1ll1l (u"ࠨࡲࡹࡶ࠳࡯࡮ࡪࠩࡻ"))

    try:
        l1lll1ll1  = _getPVRChannels(l1ll1l (u"ࠩࠥࡸࡻࠨࠧࡼ"))
        l1lll1l11 = l1lll1ll1[l1ll1l (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪࡽ")]
    except: pass

    try:
        l1llll1l1  = _getPVRChannels(l1ll1l (u"ࠫࠧࡸࡡࡥ࡫ࡲࠦࠬࡾ"))
        l1lll1l1l = l1llll1l1[l1ll1l (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࡿ")]
    except: pass

    try:
        l1llll1ll  = l1lll1l11[l1ll1l (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡳࠨࢀ")]
        l1lllll1l  = l1lll1l1l[l1ll1l (u"ࠧࡤࡪࡤࡲࡳ࡫࡬ࡴࠩࢁ")]
    except: pass

    l11l1l  = file(l1llll11l, l1ll1l (u"ࠨࡹࠪࢂ"))
    
    l11l1l.write(l1ll1l (u"ࠩ࡞ࡷࡨࡸࡩࡱࡶ࠱ࡳࡳ࠳ࡴࡢࡲࡳ࠲ࡹࡼ࡝࡝ࡰࠪࢃ"))

    try:
        for l1lll1 in l1llll1ll:
            l1l11  = l1lll1[l1ll1l (u"ࠪࡰࡦࡨࡥ࡭ࠩࢄ")]
            stream = l1ll1l (u"ࠫࠪࡹࠧࢅ") % l1lll1[l1ll1l (u"ࠬࡩࡨࡢࡰࡱࡩࡱ࡯ࡤࠨࢆ")]

            l11l1l.write(l1ll1l (u"࠭ࠥࡴࠩࢇ") % l1l11)
            l11l1l.write(l1ll1l (u"ࠧ࠾ࠩ࢈"))
            l11l1l.write(l1ll1l (u"ࠨࠧࡶࠫࢉ") % stream)
            l11l1l.write(l1ll1l (u"ࠩ࡟ࡲࠬࢊ"))
    except: pass

    try:
        for l1lll1 in l1lllll1l:
            l1l11  = l1lll1[l1ll1l (u"ࠪࡰࡦࡨࡥ࡭ࠩࢋ")]
            stream = l1ll1l (u"ࠫࠪࡹࠧࢌ") % l1lll1[l1ll1l (u"ࠬࡩࡨࡢࡰࡱࡩࡱ࡯ࡤࠨࢍ")]

            l11l1l.write(l1ll1l (u"࠭ࠥࡴࠩࢎ") % l1l11)
            l11l1l.write(l1ll1l (u"ࠧ࠾ࠩ࢏"))
            l11l1l.write(l1ll1l (u"ࠨࠧࡶࠫ࢐") % stream)
            l11l1l.write(l1ll1l (u"ࠩ࡟ࡲࠬ࢑"))
    except: pass

    l11l1l.write(l1ll1l (u"ࠪࡠࡳ࠭࢒"))
    l11l1l.close()


def _getPVRChannels(group):
    method   = l1ll1l (u"ࠫࡕ࡜ࡒ࠯ࡉࡨࡸࡈ࡮ࡡ࡯ࡰࡨࡰࡸ࠭࢓")
    params   = l1ll1l (u"ࠬࡩࡨࡢࡰࡱࡩࡱ࡭ࡲࡰࡷࡳ࡭ࡩ࠭࢔")
    l1lllll11  =  getGroupID(group)
    l1llll111 =  sendJSON(method, params, l1lllll11)
    
    return l1llll111


def getGroupID(group):
    method   = l1ll1l (u"࠭ࡐࡗࡔ࠱ࡋࡪࡺࡃࡩࡣࡱࡲࡪࡲࡇࡳࡱࡸࡴࡸ࠭࢕")
    params   = l1ll1l (u"ࠧࡤࡪࡤࡲࡳ࡫࡬ࡵࡻࡳࡩࠬ࢖")
    l1llll111 =  sendJSON(method, params, group)
    result   =  l1llll111[l1ll1l (u"ࠨࡴࡨࡷࡺࡲࡴࠨࢗ")]
    groups   =  result[l1ll1l (u"ࠩࡦ࡬ࡦࡴ࡮ࡦ࡮ࡪࡶࡴࡻࡰࡴࠩ࢘")]

    for group in groups:
        l1l11 = group[l1ll1l (u"ࠪࡰࡦࡨࡥ࡭࢙ࠩ")]

        if l1l11 == l1ll1l (u"ࠫࡆࡲ࡬ࠡࡥ࡫ࡥࡳࡴࡥ࡭ࡵ࢚ࠪ"):
            return group[l1ll1l (u"ࠬࡩࡨࡢࡰࡱࡩࡱ࡭ࡲࡰࡷࡳ࡭ࡩ࢛࠭")]


def sendJSON(method, params, value):
    l1llllll1  = (l1ll1l (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࠫࡳࠣ࠮ࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࠥࡴࠤ࠽ࠩࡸࢃࠬࠡࠤ࡬ࡨࠧࡀ࠱ࡾࠩ࢜") % (method, params, value))
    l1llll111 = xbmc.executeJSONRPC(l1llllll1)

    return json.loads(l1llll111.decode(l1ll1l (u"ࠧࡶࡶࡩ࠱࠽࠭࢝"), l1ll1l (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨ࢞")))
