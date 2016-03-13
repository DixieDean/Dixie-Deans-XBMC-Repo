# coding: UTF-8

import sys

l1lllll11 = sys.version_info [0] == 2
l1l11ll1l = 2048
l111l11l = 7

def l1l111lll (l1ll111):
	global l1l111ll
	
	l11l1ll1 = ord (l1ll111 [-1])
	l1111111 = l1ll111 [:-1]
	
	l1ll11ll = l11l1ll1 % len (l1111111)
	l1l11ll = l1111111 [:l1ll11ll] + l1111111 [l1ll11ll:]
		
	if l1lllll11:
		l11ll1ll1 = unicode () .join ([unichr (ord (char) - l1l11ll1l - (l1l11111l + l11l1ll1) % l111l11l) for l1l11111l, char in enumerate (l1l11ll)])
	else:
		l11ll1ll1 = str () .join ([chr (ord (char) - l1l11ll1l - (l1l11111l + l11l1ll1) % l111l11l) for l1l11111l, char in enumerate (l1l11ll)])
		
	return eval (l11ll1ll1)




import xbmc
import xbmcaddon
import json
import urllib
import time
import datetime
import os

import dixie

PATH    = os.path.join(dixie.PROFILE, l1l111lll (u"ࠫࡺࡱࡴࡷࡡࡦ࡬ࡦࡴ࡮ࡦ࡮ࡶࠫू"))
SETTING = l1l111lll (u"ࠬࡒࡏࡈࡋࡑࡣ࡚ࡑࡔࡗࠩृ")


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 24): 
        l1l1l1l1 = json.load(open(PATH))
        message = l1l111lll (u"࠭ࡌࡰࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡷࡳࠥࡹࡥࡳࡸࡨࡶ࠳ࠦࡏ࡯ࡧࠣࡱࡴࡳࡥ࡯ࡶࠣࡴࡱ࡫ࡡࡴࡧ࠱ࠫॄ")
        dixie.notify(message)
    else:
        l1l1l1l1 = l1ll111lll(url)
        l1l1l1ll1(SETTING)

    stream = url.split(l1l111lll (u"ࠧ࠻ࠩॅ"), 1)[-1].lower()
    
    try:
        result = l1l1l1l1[l1l111lll (u"ࠨࡴࡨࡷࡺࡲࡴࠨॆ")]
        l11l11l1  = result[l1l111lll (u"ࠩࡩ࡭ࡱ࡫ࡳࠨे")]
    except Exception as e:
        l1l1ll111(e)
        return None

    for file in l11l11l1:
        l1l11llll   = file[l1l111lll (u"ࠪࡰࡦࡨࡥ࡭ࠩै")]
        l1l11llll   = l1l11llll.replace(l1l111lll (u"ࠫࠥࠦࠧॉ"), l1l111lll (u"ࠬࠦࠧॊ")).replace(l1l111lll (u"࠭ࠠ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩो"), l1l111lll (u"ࠧ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩौ"))
        l1l1l1l1l = l1l11llll.rsplit(l1l111lll (u"ࠨ࡝࠲ࡇࡔࡒࡏࡓ࡟्ࠪ"), 1)[0].split(l1l111lll (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞ࠩॎ"), 1)[-1]

        if stream == l1l1l1l1l.lower():
            return file[l1l111lll (u"ࠪࡪ࡮ࡲࡥࠨॏ")]

    return None


def l1ll111lll(url):
    l1l1ll11l = l1l1l1lll(url)
    Addon   = xbmcaddon.Addon(l1l1ll11l)

    username =  Addon.getSetting('kasutajanimi')
    password =  Addon.getSetting('salasona')

    l1ll111l1l   = l1l111lll (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰॒ࠩ") + l1l1ll11l
    l1ll11111l     = l1l111lll (u"ࠧ࠰ࡁࡤࡧࡹ࡯࡯࡯࠿ࡶࡸࡷ࡫ࡡ࡮ࡡࡹ࡭ࡩ࡫࡯ࠧࡧࡻࡸࡷࡧࠦࡱࡣࡪࡩࠫࡶ࡬ࡰࡶࠩࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࡃࠦࡵ࡫ࡷࡰࡪࡃࡁ࡭࡮ࠩࡹࡷࡲ࠽ࠨ॓")
    l1ll111l11  =  l1ll11l111(url)

    l1l11111  =  l1ll111l1l + l1ll11111l + l1ll111l11

    l1ll111ll1 = l1l111lll (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࡀࠫ॔") + username + l1l111lll (u"ࠩࠩࡴࡦࡹࡳࡸࡱࡵࡨࡂ࠭ॕ") + password + l1l111lll (u"ࠪࠪࡹࡿࡰࡦ࠿ࡪࡩࡹࡥ࡬ࡪࡸࡨࡣࡸࡺࡲࡦࡣࡰࡷࠫࡩࡡࡵࡡ࡬ࡨࡂ࠶ࠧॖ")

    l1lll1l1 = l1ll111l1l  + l1l111lll (u"ࠫ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃࡳࡦࡥࡸࡶ࡮ࡺࡹࡠࡥ࡫ࡩࡨࡱࠦࡦࡺࡷࡶࡦࠬࡰࡢࡩࡨࠪࡵࡲ࡯ࡵࠨࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࠫࡺࡩࡵ࡮ࡨࡁࡑ࡯ࡶࡦࠧ࠵࠴࡙࡜ࠦࡶࡴ࡯ࠫॗ")
    query = l1l11111 +  urllib.quote_plus(l1ll111ll1)

    l1ll1111l1 = (l1l111lll (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨक़") % l1lll1l1)
    l1ll1111ll = (l1l111lll (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩख़") % query)


    try:
        message = l1l111lll (u"ࠧࡍࡱࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡸࡴࠦࡳࡦࡴࡹࡩࡷ࠴ࠠࡐࡰࡨࠤࡲࡵ࡭ࡦࡰࡷࠤࡵࡲࡥࡢࡵࡨ࠲ࠬग़")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1ll1111l1)
        l1l1l1l1 = xbmc.executeJSONRPC(l1ll1111ll)

        dixie.CloseBusy()

        content = json.loads(l1l1l1l1)

        json.dump(content, open(PATH,l1l111lll (u"ࠨࡹࠪज़")))

        return content

    except Exception as e:
        l1l1ll111(e)
        return {l1l111lll (u"ࠩࡈࡶࡷࡵࡲࠨड़") : l1l111lll (u"ࠪࡔࡱࡻࡧࡪࡰࠣࡉࡷࡸ࡯ࡳࠩढ़")}


def l1l1l1lll(url):
    if url.startswith(l1l111lll (u"࡚ࠫࡑࡔࡗ࠼ࠪफ़")):
        return l1l111lll (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡺࡱࡴࡷࡨࡵࡥࡳࡩࡥࠨय़")

    if url.startswith(l1l111lll (u"࠭ࡕࡌࡖ࡙࠶࠿࠭ॠ")):
        return l1l111lll (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸࡵࡴࡨࡥࡲ࠳ࡣࡰࡦࡨࡷࠬॡ")

    if url.startswith(l1l111lll (u"ࠨࡗࡎࡘ࡛࠹࠺ࠨॢ")):
        return l1l111lll (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡸࡻࡹࡵࡣࡵࠪॣ")


def l1ll11l111(url):
    if (url.startswith(l1l111lll (u"࡙ࠪࡐ࡚ࡖ࠻ࠩ।"))) or (url.startswith(l1l111lll (u"࡚ࠫࡑࡔࡗ࠴࠽ࠫ॥"))):
        return l1l111lll (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠹࠷࠯࠳࠻࠻࠳࠷࠳࠺࠰࠴࠹࠺ࡀ࠸࠱࠲࠳࠳ࡪࡴࡩࡨ࡯ࡤ࠶࠳ࡶࡨࡱࡁࠪ०")
    
    if url.startswith(l1l111lll (u"࠭ࡕࡌࡖ࡙࠷࠿࠭१")):
        return 'http://2.welcm.tv:8000/enigma2.php?'


def l1l1l1ll1(l11lll11l):
    now = datetime.datetime.today()
    dixie.SetSetting(l11lll11l, str(now))


def l1l1ll111(e):
    l1l1l111l = l1l111lll (u"ࠨࡕࡲࡶࡷࡿࠬࠡࡣࡱࠤࡪࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡧࡧ࠾ࠥࡐࡓࡐࡐࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠩࡸ࠭३")  %e
    l11lll1ll = l1l111lll (u"ࠩࡓࡰࡪࡧࡳࡦࠢࡵࡩ࠲ࡲࡩ࡯࡭ࠣࡸ࡭࡯ࡳࠡࡥ࡫ࡥࡳࡴࡥ࡭ࠢࡤࡲࡩࠦࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯࠰ࠪ४")
    l1111l11 = l1l111lll (u"࡙ࠪࡸ࡫࠺ࠡࡅࡲࡲࡹ࡫ࡸࡵࠢࡐࡩࡳࡻࠠ࠾ࡀࠣࡖࡪࡳ࡯ࡷࡧࠣࡗࡹࡸࡥࡢ࡯ࠪ५")

    dixie.log(e)
    dixie.DialogOK(l1l1l111l, l11lll1ll, l1111l11)    
    dixie.SetSetting(SETTING, l1l111lll (u"ࠫࠬ६"))
