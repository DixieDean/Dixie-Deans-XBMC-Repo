# coding: UTF-8

import sys

l1l1ll1 = sys.version_info [0] == 2
l1ll1 = 2048
l11l = 7

def l11111 (ll):
	global l1ll1l
	
	l111ll = ord (ll [-1])
	l1llll = ll [:-1]
	
	l1 = l111ll % len (l1llll)
	l1111ll = l1llll [:l1] + l1llll [l1:]
		
	if l1l1ll1:
		l1l1ll = unicode () .join ([unichr (ord (char) - l1ll1 - (l11ll + l111ll) % l11l) for l11ll, char in enumerate (l1111ll)])
	else:
		l1l1ll = str () .join ([chr (ord (char) - l1ll1 - (l11ll + l111ll) % l11l) for l11ll, char in enumerate (l1111ll)])
		
	return eval (l1l1ll)




import xbmc
import json
import os

import dixie


def createPVRINI():
    if not dixie.PVRACTIVE:
        return

    l1ll = dixie.PROFILE
    path = os.path.join(l1ll, l11111 (u"࠭ࡩ࡯࡫ࠪࢀ"))
    l11  = os.path.join(path, l11111 (u"ࠧࡱࡸࡵ࠲࡮ࡴࡩࠨࢁ"))

    l1l1l1ll1  = _getPVRChannels(l11111 (u"ࠨࠤࡷࡺࠧ࠭ࢂ"))
    l1l1ll111 = l1l1l1ll1[l11111 (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩࢃ")]

    l1l1ll11l  = _getPVRChannels(l11111 (u"ࠪࠦࡷࡧࡤࡪࡱࠥࠫࢄ"))
    l1l1l1l1l = l1l1ll11l[l11111 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࢅ")]

    l1l1ll1l1  = l1l1ll111[l11111 (u"ࠬࡩࡨࡢࡰࡱࡩࡱࡹࠧࢆ")]
    l1l1lll11  = l1l1l1l1l[l11111 (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡳࠨࢇ")]

    l11ll1  = file(l11, l11111 (u"ࠧࡸࠩ࢈"))
    
    l11ll1.write(l11111 (u"ࠨ࡝ࡶࡧࡷ࡯ࡰࡵ࠰ࡲࡲ࠲ࡺࡡࡱࡲ࠱ࡸࡻࡣ࡜࡯ࠩࢉ"))

    for l11llll in l1l1ll1l1:
        l1l11  = l11llll[l11111 (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࢊ")]
        stream = l11111 (u"ࠪࠩࡸ࠭ࢋ") % l11llll[l11111 (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡮ࡪࠧࢌ")]

        l11ll1.write(l11111 (u"ࠬࠫࡳࠨࢍ") % l1l11)
        l11ll1.write(l11111 (u"࠭࠽ࠨࢎ"))
        l11ll1.write(l11111 (u"ࠧࠦࡵࠪ࢏") % stream)
        l11ll1.write(l11111 (u"ࠨ࡞ࡱࠫ࢐"))

    for l11llll in l1l1lll11:
        l1l11  = l11llll[l11111 (u"ࠩ࡯ࡥࡧ࡫࡬ࠨ࢑")]
        stream = l11111 (u"ࠪࠩࡸ࠭࢒") % l11llll[l11111 (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡮ࡪࠧ࢓")]

        l11ll1.write(l11111 (u"ࠬࠫࡳࠨ࢔") % l1l11)
        l11ll1.write(l11111 (u"࠭࠽ࠨ࢕"))
        l11ll1.write(l11111 (u"ࠧࠦࡵࠪ࢖") % stream)
        l11ll1.write(l11111 (u"ࠨ࡞ࡱࠫࢗ"))

    l11ll1.write(l11111 (u"ࠩ࡟ࡲࠬ࢘"))
    l11ll1.close()


def _getPVRChannels(group):
    method   = l11111 (u"ࠪࡔ࡛ࡘ࠮ࡈࡧࡷࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷ࢙ࠬ")
    params   = l11111 (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡬ࡸ࡯ࡶࡲ࡬ࡨ࢚ࠬ")
    l1l1ll1ll  =  getGroupID(group)
    l1l11l =  sendJSON(method, params, l1l1ll1ll)
    
    return l1l11l


def getGroupID(group):
    method   = l11111 (u"ࠬࡖࡖࡓ࠰ࡊࡩࡹࡉࡨࡢࡰࡱࡩࡱࡍࡲࡰࡷࡳࡷ࢛ࠬ")
    params   = l11111 (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡴࡺࡲࡨࠫ࢜")
    l1l11l =  sendJSON(method, params, group)
    result   =  l1l11l[l11111 (u"ࠧࡳࡧࡶࡹࡱࡺࠧ࢝")]
    groups   =  result[l11111 (u"ࠨࡥ࡫ࡥࡳࡴࡥ࡭ࡩࡵࡳࡺࡶࡳࠨ࢞")]

    for group in groups:
        l1l11 = group[l11111 (u"ࠩ࡯ࡥࡧ࡫࡬ࠨ࢟")]

        if l1l11 == l11111 (u"ࠪࡅࡱࡲࠠࡤࡪࡤࡲࡳ࡫࡬ࡴࠩࢠ"):
            return group[l11111 (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡬ࡸ࡯ࡶࡲ࡬ࡨࠬࢡ")]


def sendJSON(method, params, value):
    l1l1lll1l  = (l11111 (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࠪࡹࠢ࠭ࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࠫࡳࠣ࠼ࠨࡷࢂ࠲ࠠࠣ࡫ࡧࠦ࠿࠷ࡽࠨࢢ") % (method, params, value))
    l1l11l = xbmc.executeJSONRPC(l1l1lll1l)

    return json.loads(l1l11l.decode(l11111 (u"࠭ࡵࡵࡨ࠰࠼ࠬࢣ"), l11111 (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧࢤ")))
