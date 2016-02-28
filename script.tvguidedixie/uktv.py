# coding: UTF-8

import sys

l1lllll11 = sys.version_info [0] == 2
l1l111l1 = 2048
l111l11l = 7

def l1lll1 (l1ll111):
	global l1l111ll
	
	l11l1ll1 = ord (l1ll111 [-1])
	l1111111 = l1ll111 [:-1]
	
	l1ll11ll = l11l1ll1 % len (l1111111)
	l1l11ll = l1111111 [:l1ll11ll] + l1111111 [l1ll11ll:]
		
	if l1lllll11:
		l11lll = unicode () .join ([unichr (ord (char) - l1l111l1 - (l1111 + l11l1ll1) % l111l11l) for l1111, char in enumerate (l1l11ll)])
	else:
		l11lll = str () .join ([chr (ord (char) - l1l111l1 - (l1111 + l11l1ll1) % l111l11l) for l1111, char in enumerate (l1l11ll)])
		
	return eval (l11lll)




import xbmc
import xbmcaddon
import json
import urllib
import time
import datetime
import os

import dixie

PATH    = os.path.join(dixie.PROFILE, l1lll1 (u"ࠧࡶ࡭ࡷࡺࡤࡩࡨࡢࡰࡱࡩࡱࡹࠧष"))
SETTING = l1lll1 (u"ࠨࡎࡒࡋࡎࡔ࡟ࡖࡍࡗ࡚ࠬस")


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 24): 
        l1l1l1l1 = json.load(open(PATH))
        message = l1lll1 (u"ࠩࡏࡳ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳࡺ࡯ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠢࡒࡲࡪࠦ࡭ࡰ࡯ࡨࡲࡹࠦࡰ࡭ࡧࡤࡷࡪ࠴ࠧह")
        dixie.notify(message)
    else:
        l1l1l1l1 = l1lll1llll(url)
        l1ll11111(SETTING)

    stream = url.split(l1lll1 (u"ࠪ࠾ࠬऺ"), 1)[-1].lower()
    
    try:
        result = l1l1l1l1[l1lll1 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫऻ")]
        l11l11l1  = result[l1lll1 (u"ࠬ࡬ࡩ࡭ࡧࡶ़ࠫ")]
    except Exception as e:
        l1l1lllll(e)
        return None

    for file in l11l11l1:
        l1ll111ll   = file[l1lll1 (u"࠭࡬ࡢࡤࡨࡰࠬऽ")]
        l1ll111ll   = l1ll111ll.replace(l1lll1 (u"ࠧࠡࠢࠪा"), l1lll1 (u"ࠨࠢࠪि")).replace(l1lll1 (u"ࠩࠣ࡟࠴ࡉࡏࡍࡑࡕࡡࠬी"), l1lll1 (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬु"))
        l1ll1111l = l1ll111ll.rsplit(l1lll1 (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ू"), 1)[0].split(l1lll1 (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࠬृ"), 1)[-1]

        if stream == l1ll1111l.lower():
            return file[l1lll1 (u"࠭ࡦࡪ࡮ࡨࠫॄ")]

    return None


def l1lll1llll(url):
    l1l1ll1ll = l1lll1ll11(url)
    Addon   = xbmcaddon.Addon(l1l1ll1ll)

    username =  Addon.l1l1l11l(l1lll1 (u"ࠧ࡬ࡣࡶࡹࡹࡧࡪࡢࡰ࡬ࡱ࡮࠭ॅ"))
    password =  Addon.l1l1l11l(l1lll1 (u"ࠨࡵࡤࡰࡦࡹ࡯࡯ࡣࠪॆ"))

    l1lll1ll1l   = l1lll1 (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠬे") + l1l1ll1ll
    l1lll1l111     = l1lll1 (u"ࠪ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡹࡴࡳࡧࡤࡱࡤࡼࡩࡥࡧࡲࠪࡪࡾࡴࡳࡣࠩࡴࡦ࡭ࡥࠧࡲ࡯ࡳࡹࠬࡴࡩࡷࡰࡦࡳࡧࡩ࡭࠿ࠩࡸ࡮ࡺ࡬ࡦ࠿ࡄࡰࡱࠬࡵࡳ࡮ࡀࠫै")
    l1lll1l1ll  =  l1llll1111()

    l1l11111  =  l1lll1ll1l + l1lll1l111 + l1lll1l1ll

    l1lll1lll1 = l1lll1 (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪࡃࠧॉ") + username + l1lll1 (u"ࠬࠬࡰࡢࡵࡶࡻࡴࡸࡤ࠾ࠩॊ") + password + l1lll1 (u"࠭ࠦࡵࡻࡳࡩࡂ࡭ࡥࡵࡡ࡯࡭ࡻ࡫࡟ࡴࡶࡵࡩࡦࡳࡳࠧࡥࡤࡸࡤ࡯ࡤ࠾࠲ࠪो")

    l1lll1l1 = l1lll1ll1l  + l1lll1 (u"ࠧ࠰ࡁࡤࡧࡹ࡯࡯࡯࠿ࡶࡩࡨࡻࡲࡪࡶࡼࡣࡨ࡮ࡥࡤ࡭ࠩࡩࡽࡺࡲࡢࠨࡳࡥ࡬࡫ࠦࡱ࡮ࡲࡸࠫࡺࡨࡶ࡯ࡥࡲࡦ࡯࡬ࠧࡶ࡬ࡸࡱ࡫࠽ࡍ࡫ࡹࡩࠪ࠸࠰ࡕࡘࠩࡹࡷࡲࠧौ")
    query = l1l11111 +  urllib.quote_plus(l1lll1lll1)

    l1lll1l11l = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࠩࡸࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀ्ࠫ") % l1lll1l1)
    l1lll1l1l1 = (l1lll1 (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬॎ") % query)


    try:
        message = l1lll1 (u"ࠪࡐࡴ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡴࡰࠢࡶࡩࡷࡼࡥࡳ࠰ࠣࡓࡳ࡫ࠠ࡮ࡱࡰࡩࡳࡺࠠࡱ࡮ࡨࡥࡸ࡫࠮ࠨॏ")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll1l11l)
        l1l1l1l1 = xbmc.executeJSONRPC(l1lll1l1l1)

        dixie.CloseBusy()

        content = json.loads(l1l1l1l1)

        json.dump(content, open(PATH,l1lll1 (u"ࠫࡼ࠭ॐ")))

        return content

    except Exception as e:
        l1l1lllll(e)
        return {l1lll1 (u"ࠬࡋࡲࡳࡱࡵࠫ॑") : l1lll1 (u"࠭ࡐ࡭ࡷࡪ࡭ࡳࠦࡅࡳࡴࡲࡶ॒ࠬ")}


def l1lll1ll11(url):
    if url.startswith(l1lll1 (u"ࠧࡖࡍࡗ࡚࠿࠭॓")):
        return l1lll1 (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡲࡷࡺࡸࡻࡢࡴࠩ॔")

    if url.startswith(l1lll1 (u"ࠩࡘࡏ࡙࡜࠲࠻ࠩॕ")):
        return l1lll1 (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡻࡸࡷ࡫ࡡ࡮࠯ࡦࡳࡩ࡫ࡳࠨॖ")


def l1llll1111(url):
    if (url.startswith(l1lll1 (u"࡚ࠫࡑࡔࡗ࠼ࠪॗ"))) or (url.startswith(l1lll1 (u"࡛ࠬࡋࡕࡘ࠵࠾ࠬक़"))):
        return l1lll1 (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࠳࠸࠰࠴࠼࠼࠴࠱࠴࠻࠱࠵࠺࠻࠺࠹࠲࠳࠴࠴࡫࡮ࡪࡩࡰࡥ࠷࠴ࡰࡩࡲࡂࠫख़")
    
    if url.startswith(l1lll1 (u"ࠧࡖࡍࡗ࡚࠸ࡀࠧग़")):
        return l1lll1 (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡱ࡮࠵࠳ࡹࡥ࠻࠺࠳࠴࠵࠵ࡥ࡯࡫ࡪࡱࡦ࠸࠮ࡱࡪࡳࡃࠬज़")


def l1ll11111(l1ll111l1):
    now = datetime.datetime.today()
    dixie.SetSetting(l1ll111l1, str(now))


def l1l1lllll(e):
    l11111l1 = l1lll1 (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡨࡨ࠿ࠦࡊࡔࡑࡑࠤࡊࡸࡲࡰࡴ࠽ࠤࠪࡹࠧड़")  %e
    l11111ll = l1lll1 (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡶࡪ࠳࡬ࡪࡰ࡮ࠤࡹ࡮ࡩࡴࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࠣࡥࡳࡪࠠࡵࡴࡼࠤࡦ࡭ࡡࡪࡰ࠱ࠫढ़")
    l1111l11 = l1lll1 (u"࡚ࠫࡹࡥ࠻ࠢࡆࡳࡳࡺࡥࡹࡶࠣࡑࡪࡴࡵࠡ࠿ࡁࠤࡗ࡫࡭ࡰࡸࡨࠤࡘࡺࡲࡦࡣࡰࠫफ़")

    dixie.l1l1ll11(e)
    dixie.l111ll1(l11111l1, l11111ll, l1111l11)    
    dixie.SetSetting(SETTING, l1lll1 (u"ࠬ࠭य़"))
