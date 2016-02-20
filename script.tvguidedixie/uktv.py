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

PATH    = os.path.join(dixie.PROFILE, l1lll1 (u"ࠬࡻ࡫ࡵࡸࡢࡧ࡭ࡧ࡮࡯ࡧ࡯ࡷࠬव"))
SETTING = l1lll1 (u"࠭ࡌࡐࡉࡌࡒࡤ࡛ࡋࡕࡘࠪश")


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 24): 
        l1l1l1l1 = json.load(open(PATH))
        message = l1lll1 (u"ࠧࡍࡱࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡸࡴࠦࡳࡦࡴࡹࡩࡷ࠴ࠠࡐࡰࡨࠤࡲࡵ࡭ࡦࡰࡷࠤࡵࡲࡥࡢࡵࡨ࠲ࠬष")
        dixie.notify(message)
    else:
        l1l1l1l1 = l1llll1111(url)
        l1ll11111(SETTING)

    stream = url.split(l1lll1 (u"ࠨ࠼ࠪस"), 1)[-1].lower()
    
    try:
        result = l1l1l1l1[l1lll1 (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩह")]
        l11l11l1  = result[l1lll1 (u"ࠪࡪ࡮ࡲࡥࡴࠩऺ")]
    except Exception as e:
        l1l1lllll(e)
        return None

    for file in l11l11l1:
        l1ll111ll   = file[l1lll1 (u"ࠫࡱࡧࡢࡦ࡮ࠪऻ")]
        l1ll111ll   = l1ll111ll.replace(l1lll1 (u"ࠬࠦࠠࠨ़"), l1lll1 (u"࠭ࠠࠨऽ")).replace(l1lll1 (u"ࠧࠡ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪा"), l1lll1 (u"ࠨ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪि"))
        l1ll1111l = l1ll111ll.rsplit(l1lll1 (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫी"), 1)[0].split(l1lll1 (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟ࠪु"), 1)[-1]

        if stream == l1ll1111l.lower():
            return file[l1lll1 (u"ࠫ࡫࡯࡬ࡦࠩू")]

    return None


def l1llll1111(url):
    l1l1ll1ll = l1lll1ll1l(url)
    Addon   = xbmcaddon.Addon(l1l1ll1ll)

    username =  Addon.getSetting('kasutajanimi')
    password =  Addon.getSetting('salasona')

    l1lll1lll1   = l1lll1 (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪॅ") + l1l1ll1ll
    l1l11111  =  l1lll1lll1 + l1lll1 (u"ࠨ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡷࡹࡸࡥࡢ࡯ࡢࡺ࡮ࡪࡥࡰࠨࡨࡼࡹࡸࡡࠧࡲࡤ࡫ࡪࠬࡰ࡭ࡱࡷࠪࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲ࠽ࠧࡶ࡬ࡸࡱ࡫࠽ࡂ࡮࡯ࠪࡺࡸ࡬࠾ࡪࡷࡸࡵࡀ࠯࠰࠵࠺࠲࠶࠾࠷࠯࠳࠶࠽࠳࠷࠵࠶࠼࠻࠴࠵࠶࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄ࠭ॆ")
    l1lll1llll = l1lll1 (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࡁࠬे") + username + l1lll1 (u"ࠪࠪࡵࡧࡳࡴࡹࡲࡶࡩࡃࠧै") + password + l1lll1 (u"ࠫࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟࡭࡫ࡹࡩࡤࡹࡴࡳࡧࡤࡱࡸࠬࡣࡢࡶࡢ࡭ࡩࡃ࠰ࠨॉ")

    l1lll1l1 = l1lll1lll1 + l1lll1 (u"ࠬ࠵࠿ࡢࡥࡷ࡭ࡴࡴ࠽ࡴࡧࡦࡹࡷ࡯ࡴࡺࡡࡦ࡬ࡪࡩ࡫ࠧࡧࡻࡸࡷࡧࠦࡱࡣࡪࡩࠫࡶ࡬ࡰࡶࠩࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࠬࡴࡪࡶ࡯ࡩࡂࡒࡩࡷࡧࠨ࠶࠵࡚ࡖࠧࡷࡵࡰࠬॊ")
    query = l1l11111 + urllib.quote_plus(l1lll1llll)

    l1lll1l1ll = (l1lll1 (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩो") % l1lll1l1)
    l1lll1ll11 = (l1lll1 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࠨࡷࠧࢃࠬࠡࠤ࡬ࡨࠧࡀࠠ࠲ࡿࠪौ") % query)


    try:
        message = l1lll1 (u"ࠨࡎࡲ࡫࡬࡯࡮ࡨࠢ࡬ࡲࡹࡵࠠࡴࡧࡵࡺࡪࡸ࠮ࠡࡑࡱࡩࠥࡳ࡯࡮ࡧࡱࡸࠥࡶ࡬ࡦࡣࡶࡩ࠳्࠭")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll1l1ll)
        l1l1l1l1 = xbmc.executeJSONRPC(l1lll1ll11)

        dixie.CloseBusy()

        content = json.loads(l1l1l1l1)

        json.dump(content, open(PATH,l1lll1 (u"ࠩࡺࠫॎ")))

        return content

    except Exception as e:
        l1l1lllll(e)
        return {l1lll1 (u"ࠪࡉࡷࡸ࡯ࡳࠩॏ") : l1lll1 (u"ࠫࡕࡲࡵࡨ࡫ࡱࠤࡊࡸࡲࡰࡴࠪॐ")}


def l1lll1ll1l(url):
    if url.startswith(l1lll1 (u"࡛ࠬࡋࡕࡘ࠽ࠫ॑")):
        return l1lll1 (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡻ࡫ࡵࡸࡩࡶࡦࡴࡣࡦ॒ࠩ")

    if url.startswith(l1lll1 (u"ࠧࡖࡍࡗ࡚࠷ࡀࠧ॓")):
        return l1lll1 (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡶࡵࡩࡦࡳ࠭ࡤࡱࡧࡩࡸ࠭॔")


def l1ll11111(l1ll111l1):
    now = datetime.datetime.today()
    dixie.SetSetting(l1ll111l1, str(now))


def l1l1lllll(e):
    l11111l1 = l1lll1 (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡨࡨ࠿ࠦࡊࡔࡑࡑࠤࡊࡸࡲࡰࡴ࠽ࠤࠪࡹࠧॕ")  %e
    l11111ll = l1lll1 (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡶࡪ࠳࡬ࡪࡰ࡮ࠤࡹ࡮ࡩࡴࠢࡦ࡬ࡦࡴ࡮ࡦ࡮ࠣࡥࡳࡪࠠࡵࡴࡼࠤࡦ࡭ࡡࡪࡰ࠱ࠫॖ")
    l1111l11 = l1lll1 (u"࡚ࠫࡹࡥ࠻ࠢࡆࡳࡳࡺࡥࡹࡶࠣࡑࡪࡴࡵࠡ࠿ࡁࠤࡗ࡫࡭ࡰࡸࡨࠤࡘࡺࡲࡦࡣࡰࠫॗ")

    dixie.l1l1ll11(e)
    dixie.l111ll1(l11111l1, l11111ll, l1111l11)    
    dixie.SetSetting(SETTING, l1lll1 (u"ࠬ࠭क़"))
