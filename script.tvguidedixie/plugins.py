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

l1llll1ll     = l1l1l (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡮ࡵࡸࠪࡉ")
l111l1l1     = l1l1l (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡹࡷࡱࠧࡊ")
l1lllll11 = l1l1l (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡘ࡬ࡨ࡙࡯࡭ࡦࠩࡋ")
l11111l1  = l1l1l (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡷࡺࡹ࡯࡭ࡦ࠰ࡷࡺࡦ࠭ࡌ")

l1ll1llll = [l1llll1ll, l111l1l1, l1lllll11, l11111l1]

l111ll1l = dixie.PROFILE
PATH = os.path.join(l111ll1l, l1l1l (u"ࠫ࡮ࡴࡩࠨࡍ"))


def checkAddons():
    for l1lll1lll in l1ll1llll:
        if l1lll1111(l1lll1lll):
            try: l1lll1l1l(l1lll1lll)
            except: pass


def l1lll1111(l1lll1lll):
    if xbmc.getCondVisibility(l1l1l (u"࡙ࠬࡹࡴࡶࡨࡱ࠳ࡎࡡࡴࡃࡧࡨࡴࡴࠨࠦࡵࠬࠫࡎ") % l1lll1lll) == 1:
        return True
    return False


def l1lll1l1l(l1lll1lll):
    l111lll1 = l11111ll(l1lll1lll) + l1l1l (u"࠭࠮ࡪࡰ࡬ࠫࡏ")
    l1111111  = os.path.join(PATH, l111lll1)

    l1lll1ll1 = l11l11l1(l1lll1lll)

    l11l1111  = file(l1111111, l1l1l (u"ࠧࡸࠩࡐ"))

    l11l1111.write(l1l1l (u"ࠨ࡝ࠪࡑ"))
    l11l1111.write(l1lll1lll)
    l11l1111.write(l1l1l (u"ࠩࡠࠫࡒ"))
    l11l1111.write(l1l1l (u"ࠪࡠࡳ࠭ࡓ"))

    for l111111l in l1lll1ll1:
        l1111ll1   = l111111l[l1l1l (u"ࠫࡱࡧࡢࡦ࡮ࠪࡔ")]
        l1111ll1   = l1111ll1.replace(l1l1l (u"࡛ࠬࠦࠨࡕ"), l1l1l (u"࡛࠭ࠨࡖ")).replace(l1l1l (u"ࠧ࡞ࠢࠪࡗ"), l1l1l (u"ࠨ࡟ࠪࡘ")).replace(l1l1l (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡤࡵࡺࡧ࡝ࠨ࡙"), l1l1l (u"࡚ࠪࠫ")).replace(l1l1l (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡱ࡯࡭ࡦࡩࡵࡩࡪࡴ࡝ࠨ࡛"), l1l1l (u"ࠬ࠭࡜")).replace(l1l1l (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡹࡦ࡮࡯ࡳࡼࡣࠧ࡝"), l1l1l (u"ࠧࠨ࡞")).replace(l1l1l (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡤ࡯ࡹࡪࡣࠧ࡟"), l1l1l (u"ࠩࠪࡠ")).replace(l1l1l (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡳࡷࡧ࡮ࡨࡧࡠࠫࡡ"), l1l1l (u"ࠫࠬࡢ")).replace(l1l1l (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟ࠪࡣ"), l1l1l (u"࠭ࠧࡤ")).replace(l1l1l (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࠧࡥ"), l1l1l (u"ࠨࠩࡦ")).replace(l1l1l (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡧ"), l1l1l (u"ࠪࠫࡨ"))
        
        if l1lll1lll == l11111l1:
            l1111ll1 = l1111ll1.split(l1l1l (u"ࠫࠥ࠳ࠠࠨࡩ"))[0]

        stream  = l111111l[l1l1l (u"ࠬ࡬ࡩ࡭ࡧࠪࡪ")]

        l11l1111.write(l1l1l (u"࠭ࠥࡴࠩ࡫") % l1111ll1)
        l11l1111.write(l1l1l (u"ࠧ࠾ࠩ࡬"))
        l11l1111.write(l1l1l (u"ࠨࠧࡶࠫ࡭") % stream)
        l11l1111.write(l1l1l (u"ࠩ࡟ࡲࠬ࡮"))

    l11l1111.write(l1l1l (u"ࠪࡠࡳ࠭࡯"))
    l11l1111.close()


def l11111ll(l1lll1lll):
    if l1lll1lll == l1llll1ll:
        return l1l1l (u"ࠫࡳࡺࡶࠨࡰ")

    if l1lll1lll == l111l1l1:
        return l1l1l (u"ࠬࡻ࡫ࡵࠩࡱ")

    if l1lll1lll == l1lllll11:
        return l1l1l (u"࠭ࡶࡪࡦࡷ࡭ࡲ࡫ࠧࡲ")

    if l1lll1lll == l11111l1:
        return l1l1l (u"ࠧࡵࡸࡷ࡭ࡲ࡫ࠧࡳ")


def l11l11l1(l1lll1lll):
    if l1lll1lll == l111l1l1:
        return l1llll1l1(l1lll1lll)

    if l1lll1lll == l1llll1ll:
        xbmcaddon.Addon(l1llll1ll).setSetting(l1l1l (u"ࠨࡩࡨࡲࡷ࡫ࠧࡴ"), l1l1l (u"ࠩࡩࡥࡱࡹࡥࠨࡵ"))
        xbmcaddon.Addon(l1llll1ll).setSetting(l1l1l (u"ࠪࡸࡻ࡭ࡵࡪࡦࡨࠫࡶ"), l1l1l (u"ࠫ࡫ࡧ࡬ࡴࡧࠪࡷ"))

    l1lll11ll  = l1l1l (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠨࡸ") + l1lll1lll
    l1111l11 =  l11l111l(l1lll1lll)
    query   =  l1lll11ll + l1111l11

    return sendJSON(query, l1lll1lll)


def l1llll1l1(l1lll1lll):
    l1lll11ll = l1l1l (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠩࡹ") + l1lll1lll

    l1ll1ll1l = l1l1l (u"ࠧ࠰ࡁࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠪࡲࡵࡤࡦ࠿࠴ࠪࡳࡧ࡭ࡦ࠿ࡏ࡭ࡻ࡫ࠥ࠳࠲ࡗ࡚ࠫࡻࡲ࡭࠿࡫ࡸࡹࡶࠥ࠴ࡣࠨ࠶࡫ࠫ࠲ࡧ࡯ࡨࡸࡦࡲ࡫ࡦࡶࡷࡰࡪ࠴ࡣࡰࠧ࠵ࡪ࡚ࡑࡔࡶࡴ࡮࠵࠽࠶࠲࠳࠲࠴࠺ࠪ࠸ࡦࡍ࡫ࡹࡩࠪ࠸࠵࠳࠲ࡗ࡚࠳ࡺࡸࡵࠩࡺ")
    l1ll1lll1 = l1l1l (u"ࠨ࠱ࡂࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠧ࡫ࡦࡳࡳ࡯࡭ࡢࡩࡨࡁࠫࡳ࡯ࡥࡧࡀ࠵ࠫࡴࡡ࡮ࡧࡀࡗࡵࡵࡲࡵࡵࠩࡹࡷࡲ࠽ࡩࡶࡷࡴࠪ࠹ࡡࠦ࠴ࡩࠩ࠷࡬࡭ࡦࡶࡤࡰࡰ࡫ࡴࡵ࡮ࡨ࠲ࡨࡵࠥ࠳ࡨࡘࡏ࡙ࡻࡲ࡬࠳࠻࠴࠷࠸࠰࠲࠸ࠨ࠶࡫࡙ࡰࡰࡴࡷࡷࡑ࡯ࡳࡵ࠰ࡷࡼࡹ࠭ࡻ")

    l1lllllll  = []
    l1lllllll += sendJSON(l1lll11ll + l1ll1ll1l, l1lll1lll)
    l1lllllll += sendJSON(l1lll11ll + l1ll1lll1, l1lll1lll)

    return l1lllllll


def l11l111l(l1lll1lll):
    if l1lll1lll == l1llll1ll:
        return l1l1l (u"ࠩ࠲ࡃࡨࡧࡴ࠾࠯࠵ࠪࡲࡵࡤࡦ࠿࠵ࠪࡳࡧ࡭ࡦ࠿ࡐࡽࠪ࠸࠰ࡄࡪࡤࡲࡳ࡫࡬ࡴࠨࡸࡶࡱࡃࡵࡳ࡮ࠪࡼ")

    if l1lll1lll == l1lllll11:
        return l1l1l (u"ࠪ࠳ࡄࡳ࡯ࡥࡧࡀࡔࡊࡘࡃࡉࠧ࠵࠴ࡕࡏࡃࡌࡕࠨ࠶࠵࠳ࠥ࠳࠲ࡄࡗࡘࡕࡒࡕࡇࡇࠩ࠷࠶ࡓࡑࡑࡕࡘࡘ࠭ࡽ")

    if l1lll1lll == l11111l1:
        return l1l1l (u"ࠫࠬࡾ")


def sendJSON(query, l1lll1lll):
    try:
        l1111l1l     = l1l1l (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࡿ") % query
        l1lllll1l  = xbmc.executeJSONRPC(l1111l1l)
        l1llll11l = json.loads(l1lllll1l)
        result   = l1llll11l[l1l1l (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ࢀ")]

        return result[l1l1l (u"ࠧࡧ࡫࡯ࡩࡸ࠭ࢁ")]

    except Exception as e:
        l1llll111(e, l1lll1lll)
        return {l1l1l (u"ࠨࡇࡵࡶࡴࡸࠧࢂ") : l1l1l (u"ࠩࡓࡰࡺ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠨࢃ")}


def l1llll111(e, l1lll1lll):
    l1111lll = l1l1l (u"ࠪࡗࡴࡸࡲࡺ࠮ࠣࡥࡳࠦࡥࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡩࡩࡀࠠࡋࡕࡒࡒࠥࡋࡲࡳࡱࡵ࠾ࠥࠫࡳ࠭ࠢࠨࡷࠬࢄ")  % (e, l1lll1lll) 
    l111l111 = l1l1l (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡨࡵ࡮ࡵࡣࡦࡸࠥࡻࡳࠡࡱࡱࠤࡹ࡮ࡥࠡࡨࡲࡶࡺࡳ࠮ࠨࢅ")
    l111l11l = l1l1l (u"࡛ࠬࡰ࡭ࡱࡤࡨࠥࡧࠠ࡭ࡱࡪࠤࡻ࡯ࡡࠡࡶ࡫ࡩࠥࡧࡤࡥࡱࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸࠦࡡ࡯ࡦࠣࡴࡴࡹࡴࠡࡶ࡫ࡩࠥࡲࡩ࡯࡭࠱ࠫࢆ")

    dixie.log(l1lll1lll)
    dixie.log(e)


def getPlaylist():
    import requests

    l1llllll1 = [l1l1l (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡸ࠯ࡥࡲ࠳ࡩࡨࡣࡩ࠲࠴ࠫࢇ"), l1l1l (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࡬ࡱࡧ࡭࠳ࡩࡣ࡭ࡦ࠱࡭ࡴ࠭࢈"), l1l1l (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡣ࡬ࡳ࠳ࡩࡣ࡭ࡱࡸࡨࡹࡼ࠮ࡰࡴࡪ࠳ࡰࡵࡤࡪࠩࢉ"), l1l1l (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࡪࡳ࠷ࡲ࠮ࡪࡰ࡮࠳ࡰࡵࡤࡪࠩࢊ")]
    l1lll11l1 =  l1l1l (u"ࠪࠧࡊ࡞ࡔࡎ࠵ࡘࠫࢋ")

    for url in l1llllll1:
        dixie.log(url)
        try:
            l1lll111l  = requests.get(url)
            l111ll11 = l1lll111l.text
        except: pass

        if l1lll11l1 in l111ll11:
            path = os.path.join(dixie.PROFILE, l1l1l (u"ࠫࡵࡲࡡࡺ࡮࡬ࡷࡹ࠴࡭࠴ࡷࠪࢌ"))
            with open(path, l1l1l (u"ࠬࡽࠧࢍ")) as f:
                f.write(l111ll11)


    import urllib

    l111l1ll = os.path.join(PATH, l1l1l (u"࠭ࡴࡦ࡯ࡳࠫࢎ"))
    l1111111  = os.path.join(PATH, l1l1l (u"ࠧࡪࡰ࡬࠶࠳࡯࡮ࡪࠩ࢏"))
    l1llllll1  = l1l1l (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡵࡥࡼ࠴ࡧࡪࡶ࡫ࡹࡧࡻࡳࡦࡴࡦࡳࡳࡺࡥ࡯ࡶ࠱ࡧࡴࡳ࠯ࡓࡧࡱࡩ࡬ࡧࡤࡦࡵࡗ࡚࠴ࡸࡥࡱࡱࡶ࡭ࡹࡵࡲࡺ࠰ࡵࡩࡳ࡫ࡧࡢࡦࡨࡷࡹࡼ࠯࡮ࡣࡶࡸࡪࡸ࠯ࡢࡦࡧࡳࡳࡹ࠲࠯࡫ࡱ࡭ࠬ࢐")

    urllib.urlretrieve(l1llllll1, l111l1ll)

    l1lll1l11 = open(l111l1ll)
    l111llll  = open(l1111111, l1l1l (u"ࠩࡺࡸࠬ࢑"))

    for line in l1lll1l11:
        l111llll.write(line.replace(
                               l1l1l (u"ࠪ࡟ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡨࡪࡾ࡝ࠨ࢒"), l1l1l (u"ࠫࡠࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡽࡾࡸ࡞ࠩ࢓"))
                               .replace(l1l1l (u"ࠬࡡࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡜ࡩࡥࡖ࡬ࡱࡪࡣ࠮ࠨ࢔"), l1l1l (u"࡛࠭ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸࡹࡺࡠࠫ࢕"))
                               .replace(l1l1l (u"ࠧ࡜ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡇ࠰ࡗ࠲࡛ࡣࠧ࢖"), l1l1l (u"ࠨ࡝ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡺࡻࡼࡢ࠭ࢗ"))
                               .replace(l1l1l (u"ࠩ࡞ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡬ࡴࡱࡧࡹࡦࡴࡺࡻࡼࡣࠧ࢘"), l1l1l (u"ࠪ࡟ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡼࡽࡾ࡝ࠨ࢙"))
                               .replace(l1l1l (u"ࠫࡠࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡮ࡺࡶ࡞࢚ࠩ"), l1l1l (u"ࠬࡡࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡾࡸࡹ࡟࢛ࠪ"))
                               .replace(l1l1l (u"࡛࠭ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡢࡣࡥ࡬ࡴࡱࡧࡹࡦࡴࡠࠫ࢜"), l1l1l (u"ࠧ࡜ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡺࡻࡡࠬ࢝"))
                               )

    l1lll1l11.close()
    l111llll.close()

    os.remove(l111l1ll)
