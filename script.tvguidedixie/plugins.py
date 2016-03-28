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

l1lllllll     = l1l1l (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡮ࡵࡸࠪࡉ")
l111ll1l     = l1l1l (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡹࡷࡱࠧࡊ")
l1111111 = l1l1l (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡘ࡬ࡨ࡙࡯࡭ࡦࠩࡋ")
l1111l1l  = l1l1l (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡷࡺࡹ࡯࡭ࡦ࠰ࡷࡺࡦ࠭ࡌ")

l1lll1ll1 = [l1lllllll, l111ll1l, l1111111, l1111l1l]


def checkAddons():
    for l1llll1ll in l1lll1ll1:
        if l11111ll(l1llll1ll):
            l1llll11l(l1llll1ll)


def l11111ll(l1llll1ll):
    if xbmc.getCondVisibility(l1l1l (u"ࠫࡘࡿࡳࡵࡧࡰ࠲ࡍࡧࡳࡂࡦࡧࡳࡳ࠮ࠥࡴࠫࠪࡍ") % l1llll1ll) == 1:
        return True
    return False


def l1llll11l(l1llll1ll):
    l111lll1 = dixie.PROFILE
    PATH = os.path.join(l111lll1, l1l1l (u"ࠬ࡯࡮ࡪࠩࡎ"))
    l111llll = l1111ll1(l1llll1ll) + l1l1l (u"࠭࠮ࡪࡰ࡬ࠫࡏ")
    l1lll1lll  = os.path.join(PATH, l111llll)

    l1llll1l1 = l11l11l1(l1llll1ll)

    l11l1111  = file(l1lll1lll, l1l1l (u"ࠧࡸࠩࡐ"))

    l11l1111.write(l1l1l (u"ࠨ࡝ࠪࡑ"))
    l11l1111.write(l1llll1ll)
    l11l1111.write(l1l1l (u"ࠩࡠࠫࡒ"))
    l11l1111.write(l1l1l (u"ࠪࡠࡳ࠭ࡓ"))

    for l1111l11 in l1llll1l1:
        l111l11l   = l1111l11[l1l1l (u"ࠫࡱࡧࡢࡦ࡮ࠪࡔ")]
        l111l11l   = l111l11l.replace(l1l1l (u"࡛ࠬࠦࠨࡕ"), l1l1l (u"࡛࠭ࠨࡖ")).replace(l1l1l (u"ࠧ࡞ࠢࠪࡗ"), l1l1l (u"ࠨ࡟ࠪࡘ")).replace(l1l1l (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡤࡵࡺࡧ࡝ࠨ࡙"), l1l1l (u"࡚ࠪࠫ")).replace(l1l1l (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡱ࡯࡭ࡦࡩࡵࡩࡪࡴ࡝ࠨ࡛"), l1l1l (u"ࠬ࠭࡜")).replace(l1l1l (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡹࡦ࡮࡯ࡳࡼࡣࠧ࡝"), l1l1l (u"ࠧࠨ࡞")).replace(l1l1l (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡤ࡯ࡹࡪࡣࠧ࡟"), l1l1l (u"ࠩࠪࡠ")).replace(l1l1l (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡳࡷࡧ࡮ࡨࡧࡠࠫࡡ"), l1l1l (u"ࠫࠬࡢ")).replace(l1l1l (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࠪࡣ"), l1l1l (u"࠭ࠧࡤ")).replace(l1l1l (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࠧࡥ"), l1l1l (u"ࠨࠩࡦ")).replace(l1l1l (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡧ"), l1l1l (u"ࠪࠫࡨ"))
        
        if l1llll1ll == l1111l1l:
            l111l11l = l111l11l.split(l1l1l (u"ࠫࠥ࠳ࠠࠨࡩ"))[0]

        stream  = l1111l11[l1l1l (u"ࠬ࡬ࡩ࡭ࡧࠪࡪ")]

        l11l1111.write(l1l1l (u"࠭ࠥࡴࠩ࡫") % l111l11l)
        l11l1111.write(l1l1l (u"ࠧ࠾ࠩ࡬"))
        l11l1111.write(l1l1l (u"ࠨࠧࡶࠫ࡭") % stream)
        l11l1111.write(l1l1l (u"ࠩ࡟ࡲࠬ࡮"))

    l11l1111.write(l1l1l (u"ࠪࡠࡳ࠭࡯"))
    l11l1111.close()


def l1111ll1(l1llll1ll):
    if l1llll1ll == l1lllllll:
        return l1l1l (u"ࠫࡳࡺࡶࠨࡰ")

    if l1llll1ll == l111ll1l:
        return l1l1l (u"ࠬࡻ࡫ࡵࠩࡱ")

    if l1llll1ll == l1111111:
        return l1l1l (u"࠭ࡶࡪࡦࡷ࡭ࡲ࡫ࠧࡲ")

    if l1llll1ll == l1111l1l:
        return l1l1l (u"ࠧࡵࡸࡷ࡭ࡲ࡫ࠧࡳ")


def l11l11l1(l1llll1ll):
    if l1llll1ll == l111ll1l:
        return l1llllll1(l1llll1ll)

    l1llll111  = l1l1l (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࠫࡴ") + l1llll1ll
    l1111lll =  l11l111l(l1llll1ll)
    query   =  l1llll111 + l1111lll

    return sendJSON(query)


def l1llllll1(l1llll1ll):
    l1llll111 = l1l1l (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠬࡵ") + l1llll1ll

    l1lll1l11 = l1l1l (u"ࠪ࠳ࡄࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠦ࡮ࡱࡧࡩࡂ࠷ࠦ࡯ࡣࡰࡩࡂࡒࡩࡷࡧࠨ࠶࠵࡚ࡖࠧࡷࡵࡰࡂ࡮ࡴࡵࡲࠨ࠷ࡦࠫ࠲ࡧࠧ࠵ࡪࡲ࡫ࡴࡢ࡮࡮ࡩࡹࡺ࡬ࡦ࠰ࡦࡳࠪ࠸ࡦࡖࡍࡗࡹࡷࡱ࠱࠹࠲࠵࠶࠵࠷࠶ࠦ࠴ࡩࡐ࡮ࡼࡥࠦ࠴࠸࠶࠵࡚ࡖ࠯ࡶࡻࡸࠬࡶ")
    l1lll1l1l = l1l1l (u"ࠫ࠴ࡅࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠧ࡯ࡲࡨࡪࡃ࠱ࠧࡰࡤࡱࡪࡃࡓࡱࡱࡵࡸࡸࠬࡵࡳ࡮ࡀ࡬ࡹࡺࡰࠦ࠵ࡤࠩ࠷࡬ࠥ࠳ࡨࡰࡩࡹࡧ࡬࡬ࡧࡷࡸࡱ࡫࠮ࡤࡱࠨ࠶࡫࡛ࡋࡕࡷࡵ࡯࠶࠾࠰࠳࠴࠳࠵࠻ࠫ࠲ࡧࡕࡳࡳࡷࡺࡳࡍ࡫ࡶࡸ࠳ࡺࡸࡵࠩࡷ")

    l11111l1  = []
    l11111l1 += sendJSON(l1llll111 + l1lll1l11)
    l11111l1 += sendJSON(l1llll111 + l1lll1l1l)

    return l11111l1


def l11l111l(l1llll1ll):
    if l1llll1ll == l1lllllll:
        return l1l1l (u"ࠬ࠵࠿ࡤࡣࡷࡁ࠲࠸ࠦ࡮ࡱࡧࡩࡂ࠸ࠦ࡯ࡣࡰࡩࡂࡓࡹࠦ࠴࠳ࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷࠫࡻࡲ࡭࠿ࡸࡶࡱ࠭ࡸ")

    if l1llll1ll == l1111111:
        return l1l1l (u"࠭࠯ࡀ࡯ࡲࡨࡪࡃࡐࡆࡔࡆࡌࠪ࠸࠰ࡑࡋࡆࡏࡘࠫ࠲࠱࠯ࠨ࠶࠵ࡇࡓࡔࡑࡕࡘࡊࡊࠥ࠳࠲ࡖࡔࡔࡘࡔࡔࠩࡹ")

    if l1llll1ll == l1111l1l:
        return l1l1l (u"ࠧࠨࡺ")


def sendJSON(query):
    try:
        l111l111     = l1l1l (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࠩࡸࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫࡻ") % query
        l111111l  = xbmc.executeJSONRPC(l111l111)
        l1lllll1l = json.loads(l111111l)
        result   = l1lllll1l[l1l1l (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩࡼ")]

        return result[l1l1l (u"ࠪࡪ࡮ࡲࡥࡴࠩࡽ")]

    except Exception as e:
        l1lllll11(e)
        return {l1l1l (u"ࠫࡊࡸࡲࡰࡴࠪࡾ") : l1l1l (u"ࠬࡖ࡬ࡶࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠫࡿ")}


def l1lllll11(e):
    l111l1l1 = l1l1l (u"࠭ࡓࡰࡴࡵࡽ࠱ࠦࡡ࡯ࠢࡨࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡥࡥ࠼ࠣࡎࡘࡕࡎࠡࡇࡵࡶࡴࡸ࠺ࠡࠧࡶࠫࢀ")  %e
    l111l1ll = l1l1l (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡤࡱࡱࡸࡦࡩࡴࠡࡷࡶࠤࡴࡴࠠࡵࡪࡨࠤ࡫ࡵࡲࡶ࡯࠱ࠫࢁ")
    l111ll11 = l1l1l (u"ࠨࡗࡳࡰࡴࡧࡤࠡࡣࠣࡰࡴ࡭ࠠࡷ࡫ࡤࠤࡹ࡮ࡥࠡࡣࡧࡨࡴࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࡴࠢࡤࡲࡩࠦࡰࡰࡵࡷࠤࡹ࡮ࡥࠡ࡮࡬ࡲࡰ࠴ࠧࢂ")

    dixie.log(e)
    dixie.DialogOK(l111l1l1, l111l1ll, l111ll11)
