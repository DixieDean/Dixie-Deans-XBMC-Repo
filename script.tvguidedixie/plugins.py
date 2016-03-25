# coding: UTF-8

import sys

l1l1111l = sys.version_info [0] == 2
l1llllll = 2048
l1l1l111 = 7

def l1l1l (l1l111):
	global l11111l
	
	l1ll1l1l = ord (l1l111 [-1])
	l1l111l1 = l1l111 [:-1]
	
	l11lll1 = l1ll1l1l % len (l1l111l1)
	l11l11 = l1l111l1 [:l11lll1] + l1l111l1 [l11lll1:]
		
	if l1l1111l:
		l1llll = unicode () .join ([unichr (ord (char) - l1llllll - (l1ll1 + l1ll1l1l) % l1l1l111) for l1ll1, char in enumerate (l11l11)])
	else:
		l1llll = str () .join ([chr (ord (char) - l1llllll - (l1ll1 + l1ll1l1l) % l1l1l111) for l1ll1, char in enumerate (l11l11)])
		
	return eval (l1llll)




import xbmc
import xbmcaddon
import json
import os

import dixie

l11111l1 = l1l1l (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡮ࡵࡸࠪࡉ")




l1llll1ll = [l11111l1]


def checkAddons():
    for l1lllllll in l1llll1ll:
        if l11111ll(l1lllllll):
            l1111l1l(l1lllllll)


def l11111ll(l1lllllll):
    if xbmc.getCondVisibility(l1l1l (u"ࠨࡕࡼࡷࡹ࡫࡭࠯ࡊࡤࡷࡆࡪࡤࡰࡰࠫࠩࡸ࠯ࠧࡊ") % l1lllllll) == 1:
        return True
    return False


def l1111l1l(l1lllllll):
    l111ll11 = dixie.PROFILE
    PATH = os.path.join(l111ll11, l1l1l (u"ࠩ࡬ࡲ࡮࠭ࡋ"))
    l11l1111 = l1111ll1(l1lllllll) + l1l1l (u"ࠪ࠲࡮ࡴࡩࠨࡌ")
    l1lllll11  = os.path.join(PATH, l11l1111)

    l111111l = l11l11l1(l1lllllll)
    result   = l111111l[l1l1l (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࡍ")]
    l1llllll1 = result[l1l1l (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࡎ")]
    print l1llllll1

    l111llll  = file(l1lllll11, l1l1l (u"࠭ࡷࠨࡏ"))

    l111llll.write(l1l1l (u"ࠧ࡜ࠩࡐ"))
    l111llll.write(l1lllllll)
    l111llll.write(l1l1l (u"ࠨ࡟ࠪࡑ"))
    l111llll.write(l1l1l (u"ࠩ࡟ࡲࠬࡒ"))

    for l1111l11 in l1llllll1:
        l111l111   = l1111l11[l1l1l (u"ࠪࡰࡦࡨࡥ࡭ࠩࡓ")]
        stream  = l1111l11[l1l1l (u"ࠫ࡫࡯࡬ࡦࠩࡔ")]

        l111llll.write(l1l1l (u"ࠬࠫࡳࠨࡕ") % l111l111)
        l111llll.write(l1l1l (u"࠭࠽ࠨࡖ"))
        l111llll.write(l1l1l (u"ࠧࠦࡵࠪࡗ") % stream)
        l111llll.write(l1l1l (u"ࠨ࡞ࡱࠫࡘ"))

    l111llll.write(l1l1l (u"ࠩ࡟ࡲ࡙ࠬ"))
    l111llll.close()


def l1111ll1(l1lllllll):
    if l1lllllll == l11111l1:
        return l1l1l (u"ࠪࡲࡹࡼ࡚ࠧ")


def l11l11l1(l1lllllll):
    Addon   =  xbmcaddon.Addon(l1lllllll)
    l1lllll1l  = l1l1l (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵࡛ࠧ") + l1lllllll

    l1111lll =  l11l111l(l1lllllll)
    query   =  l1lllll1l + l1111lll

    l111ll1l = (l1l1l (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨ࡜") % l1lllll1l)
    l111lll1 = (l1l1l (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩ࡝") % query)


    try:
        xbmc.executeJSONRPC(l111ll1l)
        l111111l = xbmc.executeJSONRPC(l111lll1)
        content = json.loads(l111111l.decode(l1l1l (u"ࠧࡶࡶࡩ࠱࠽࠭࡞"), l1l1l (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨ࡟")))

        return content

    except Exception as e:
        l1111111(e)
        return {l1l1l (u"ࠩࡈࡶࡷࡵࡲࠨࡠ") : l1l1l (u"ࠪࡔࡱࡻࡧࡪࡰࠣࡉࡷࡸ࡯ࡳࠩࡡ")}


def l11l111l(l1lllllll):
    if l11111l1:
        return l1l1l (u"ࠫ࠴ࡅࡣࡢࡶࡀ࠵࠻ࠬ࡭ࡰࡦࡨࡁ࠷ࠬ࡮ࡢ࡯ࡨࡁ࡚ࡲࡴࡪ࡯ࡤࡸࡪࠫ࠲࠱ࡐࡗ࡚ࠫࡻࡲ࡭࠿ࡸࡶࡱ࠭ࡢ")


def l1111111(e):
    l111l11l = l1l1l (u"࡙ࠬ࡯ࡳࡴࡼ࠰ࠥࡧ࡮ࠡࡧࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷ࡫ࡤ࠻ࠢࡍࡗࡔࡔࠠࡆࡴࡵࡳࡷࡀࠠࠦࡵࠪࡣ")  %e
    l111l1l1 = l1l1l (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡣࡰࡰࡷࡥࡨࡺࠠࡶࡵࠣࡳࡳࠦࡴࡩࡧࠣࡪࡴࡸࡵ࡮࠰ࠪࡤ")
    l111l1ll = l1l1l (u"ࠧࡖࡲ࡯ࡳࡦࡪࠠࡢࠢ࡯ࡳ࡬ࠦࡶࡪࡣࠣࡸ࡭࡫ࠠࡢࡦࡧࡳࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡣࡱࡨࠥࡶ࡯ࡴࡶࠣࡸ࡭࡫ࠠ࡭࡫ࡱ࡯࠳࠭ࡥ")

    dixie.log(e)
    dixie.DialogOK(l111l11l, l111l1l1, l111l1ll)
