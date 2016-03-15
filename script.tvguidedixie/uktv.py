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
import urllib
import os

import dixie

l1111l1l   = l1l1l (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡵ࡬ࡶࡹࡪࡷࡧ࡮ࡤࡧࠪࡉ")
l1lllll11   = l1l1l (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡶࡵࡩࡦࡳ࠭ࡤࡱࡧࡩࡸ࠭ࡊ")
l11111ll = l1l1l (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡸࡻࡹࡵࡣࡵࠪࡋ")
l111l11l   = l1l1l (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡧࡩࡽ࠭ࡌ")

l1lll1111   =  [l1111l1l, l1lllll11, l11111ll, l111l11l]


def checkAddons():
    for l1lll1ll1 in l1lll1111:
        if l1llllll1(l1lll1ll1):
            l1111111(l1lll1ll1)


def l1llllll1(l1lll1ll1):
    if xbmc.getCondVisibility(l1l1l (u"ࠫࡘࡿࡳࡵࡧࡰ࠲ࡍࡧࡳࡂࡦࡧࡳࡳ࠮ࠥࡴࠫࠪࡍ") % l1lll1ll1) == 1:
        return True
    return False


def l1111111(l1lll1ll1):
    l111ll11 = dixie.PROFILE
    PATH = os.path.join(l111ll11, l1l1l (u"ࠬ࡯࡮ࡪࠩࡎ"))
    l111ll1l = l11111l1(l1lll1ll1) + l1l1l (u"࠭࠮ࡪࡰ࡬ࠫࡏ")
    l1lll11l1  = os.path.join(PATH, l111ll1l)

    l1llll111 = l11l11l1(l1lll1ll1)
    result   = l1llll111[l1l1l (u"ࠧࡳࡧࡶࡹࡱࡺࠧࡐ")]
    l1lll1l1l = result[l1l1l (u"ࠨࡨ࡬ࡰࡪࡹࠧࡑ")]
    
    l111llll  = file(l1lll11l1, l1l1l (u"ࠩࡺࠫࡒ"))

    l111llll.write(l1l1l (u"ࠪ࡟ࠬࡓ"))
    l111llll.write(l1lll1ll1)
    l111llll.write(l1l1l (u"ࠫࡢ࠭ࡔ"))
    l111llll.write(l1l1l (u"ࠬࡢ࡮ࠨࡕ"))

    for l1lllllll in l1lll1l1l:
        l111l1ll   = l1lllllll[l1l1l (u"࠭࡬ࡢࡤࡨࡰࠬࡖ")]
        stream  = l1lllllll[l1l1l (u"ࠧࡧ࡫࡯ࡩࠬࡗ")]

        l1llll1ll  = l111111l(l1lll1ll1, l111l1ll)
        l1lllllll = l1llll11l(l1lll1ll1, l1llll1ll)

        l111llll.write(l1l1l (u"ࠨࠧࡶࠫࡘ") % l1lllllll)
        l111llll.write(l1l1l (u"ࠩࡀ࡙ࠫ"))
        l111llll.write(l1l1l (u"ࠪࠩࡸ࡚࠭") % stream)
        l111llll.write(l1l1l (u"ࠫࡡࡴ࡛ࠧ"))

    l111llll.write(l1l1l (u"ࠬࡢ࡮ࠨ࡜"))
    l111llll.close()


def l11111l1(l1lll1ll1):
    if l1lll1ll1 == l1111l1l:
        return l1l1l (u"࠭ࡵ࡬ࡶࡹࡪࡷࡧ࡮ࡤࡧࠪ࡝")

    if l1lll1ll1 == l1lllll11:
        return l1l1l (u"ࠧࡹࡶࡵࡩࡦࡳ࠭ࡤࡱࡧࡩࡸ࠭࡞")

    if l1lll1ll1 == l11111ll:
        return l1l1l (u"ࠨ࡫ࡳࡸࡻࡹࡵࡣࡵࠪ࡟")

    if l1lll1ll1 == l111l11l:
        return l1l1l (u"ࠩࡧࡩࡽ࠭ࡠ")


def l11l11l1(l1lll1ll1):
    Addon    =  xbmcaddon.Addon(l1lll1ll1)
    l1lllll1l =  Addon.getSetting(l1l1l (u"ࠪ࡯ࡦࡹࡵࡵࡣ࡭ࡥࡳ࡯࡭ࡪࠩࡡ"))
    password =  Addon.getSetting(l1l1l (u"ࠫࡸࡧ࡬ࡢࡵࡲࡲࡦ࠭ࡢ"))

    l1lll11ll   = l1l1l (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠨࡣ") + l1lll1ll1
    l1lll1l11     = l1l1l (u"࠭࠯ࡀࡣࡦࡸ࡮ࡵ࡮࠾ࡵࡷࡶࡪࡧ࡭ࡠࡸ࡬ࡨࡪࡵࠦࡦࡺࡷࡶࡦࠬࡰࡢࡩࡨࠪࡵࡲ࡯ࡵࠨࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡂࠬࡴࡪࡶ࡯ࡩࡂࡇ࡬࡭ࠨࡸࡶࡱࡃࠧࡤ")
    l1111l11  =  l11l111l(l1lll1ll1)

    l1llll1l1  =  l1lll11ll + l1lll1l11 + l1111l11

    l11l1111 = l1l1l (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦ࠿ࠪࡥ") + l1lllll1l + l1l1l (u"ࠨࠨࡳࡥࡸࡹࡷࡰࡴࡧࡁࠬࡦ") + password + l1l1l (u"ࠩࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡲࡩࡷࡧࡢࡷࡹࡸࡥࡢ࡯ࡶࠪࡨࡧࡴࡠ࡫ࡧࡁ࠵࠭ࡧ")

    l1lll111l = l1lll11ll  + l1l1l (u"ࠪ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡹࡥࡤࡷࡵ࡭ࡹࡿ࡟ࡤࡪࡨࡧࡰࠬࡥࡹࡶࡵࡥࠫࡶࡡࡨࡧࠩࡴࡱࡵࡴࠧࡶ࡫ࡹࡲࡨ࡮ࡢ࡫࡯ࠪࡹ࡯ࡴ࡭ࡧࡀࡐ࡮ࡼࡥࠦ࠴࠳ࡘ࡛ࠬࡵࡳ࡮ࠪࡨ")
    query = l1llll1l1 +  urllib.quote_plus(l11l1111)

    l111l1l1 = (l1l1l (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࠥࡴࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࡩ") % l1lll111l)
    l111lll1 = (l1l1l (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࡪ") % query)


    try:
        xbmc.executeJSONRPC(l111l1l1)
        l1llll111 = xbmc.executeJSONRPC(l111lll1)
        content = json.loads(l1llll111.decode(l1l1l (u"࠭ࡵࡵࡨ࠰࠼ࠬ࡫"), l1l1l (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧ࡬")))

        return content

    except Exception as e:
        l1lll1lll(e)
        return {l1l1l (u"ࠨࡇࡵࡶࡴࡸࠧ࡭") : l1l1l (u"ࠩࡓࡰࡺ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠨ࡮")}


def l111111l(l1lll1ll1, l111l1ll):
    if (l1lll1ll1 == l1111l1l) or (l1lll1ll1 == l1lllll11) or (l1lll1ll1 == l11111ll):
        l111l1ll = l111l1ll.replace(l1l1l (u"ࠪࠤࠥ࠭࡯"), l1l1l (u"ࠫࠥ࠭ࡰ")).replace(l1l1l (u"࡛ࠬࠦ࠰ࡅࡒࡐࡔࡘ࡝ࠨࡱ"), l1l1l (u"࡛࠭࠰ࡅࡒࡐࡔࡘ࡝ࠨࡲ"))
        return l111l1ll

    if l1lll1ll1 == l111l11l:
        l111l1ll = l111l1ll.replace(l1l1l (u"ࠧࠡࠢࠪࡳ"), l1l1l (u"ࠨࠢࠪࡴ")).replace(l1l1l (u"ࠩࠣ࡟࠴ࡈ࡝ࠨࡵ"), l1l1l (u"ࠪ࡟࠴ࡈ࡝ࠨࡶ"))
        return l111l1ll


def l1llll11l(l1lll1ll1, l1llll1ll):
    if (l1lll1ll1 == l1111l1l) or (l1lll1ll1 == l1lllll11) or (l1lll1ll1 == l11111ll):
        l1lllllll = l1llll1ll.rsplit(l1l1l (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࡷ"), 1)[0].split(l1l1l (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࠬࡸ"), 1)[-1]
        return l1lllllll

    if l1lll1ll1 == l111l11l:
        l1lllllll = l1llll1ll.rsplit(l1l1l (u"࡛࠭࠰ࡄࡠࠫࡹ"), 1)[0].split(l1l1l (u"ࠧ࡜ࡄࡠࠫࡺ"), 1)[-1]
        return l1lllllll


def l11l111l(l1lll1ll1):
    if (l1lll1ll1 == l1111l1l) or (l1lll1ll1 == l1lllll11):
        return l1l1l (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࠵࠺࠲࠶࠾࠷࠯࠳࠶࠽࠳࠷࠵࠶࠼࠻࠴࠵࠶࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄ࠭ࡻ")

    if l1lll1ll1 == l11111ll:
        return l1l1l (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࠵࠲ࡼ࡫࡬ࡤ࡯࠱ࡸࡻࡀ࠸࠱࠲࠳࠳ࡪࡴࡩࡨ࡯ࡤ࠶࠳ࡶࡨࡱࡁࠪࡼ")

    if l1lll1ll1 == l111l11l:
        return l1l1l (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࠵࠽࠻࠮࠲࠳࠸࠲࠸࠸࠮࠲࠴࠽࠼࠵࠶࠰࠰ࡧࡱ࡭࡬ࡳࡡ࠳࠰ࡳ࡬ࡵࡅࠧࡽ")


def l1lll1lll(e):
    l1111ll1 = l1l1l (u"ࠫࡘࡵࡲࡳࡻ࠯ࠤࡦࡴࠠࡦࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡪࡪ࠺ࠡࡌࡖࡓࡓࠦࡅࡳࡴࡲࡶ࠿ࠦࠥࡴࠩࡾ")  %e
    l1111lll = l1l1l (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥࡩ࡯࡯ࡶࡤࡧࡹࠦࡵࡴࠢࡲࡲࠥࡺࡨࡦࠢࡩࡳࡷࡻ࡭࠯ࠩࡿ")
    l111l111 = l1l1l (u"࠭ࡕࡱ࡮ࡲࡥࡩࠦࡡࠡ࡮ࡲ࡫ࠥࡼࡩࡢࠢࡷ࡬ࡪࠦࡡࡥࡦࡲࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠠࡢࡰࡧࠤࡵࡵࡳࡵࠢࡷ࡬ࡪࠦ࡬ࡪࡰ࡮࠲ࠬࢀ")

    dixie.log(e)
    dixie.DialogOK(l1111ll1, l1111lll, l111l111)    
    dixie.SetSetting(SETTING, l1l1l (u"ࠧࠨࢁ"))
