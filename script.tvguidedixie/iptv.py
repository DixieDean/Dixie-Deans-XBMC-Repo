# coding: UTF-8

import sys

l1llll1ll = sys.version_info [0] == 2
l1l1111l = 2048
l111l111 = 7

def l1lll1 (l1l1lll):
	global l1l111l1
	
	l11l1l1l = ord (l1l1lll [-1])
	l1lllllll = l1l1lll [:-1]
	
	l1ll11l1 = l11l1l1l % len (l1lllllll)
	l1l11l1 = l1lllllll [:l1ll11l1] + l1lllllll [l1ll11l1:]
		
	if l1llll1ll:
		l11lll = unicode () .join ([unichr (ord (char) - l1l1111l - (l1111 + l11l1l1l) % l111l111) for l1111, char in enumerate (l1l11l1)])
	else:
		l11lll = str () .join ([chr (ord (char) - l1l1111l - (l1111 + l11l1l1l) % l111l111) for l1111, char in enumerate (l1l11l1)])
		
	return eval (l11lll)




import xbmc
import xbmcaddon
import json
import time
import datetime
import urllib
import os

import dixie

PATH    = os.path.join(dixie.PROFILE, l1lll1 (u"ࠩ࡬ࡴࡹࡼ࡟ࡤࡪࡤࡲࡳ࡫࡬ࡴࠩࢴ"))
SETTING = l1lll1 (u"ࠪࡐࡔࡍࡉࡏࡡࡌࡔ࡙࡜ࠧࢵ")

def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 24): 
        l1l1l11l = json.load(open(PATH))
    else:
        l1l1l11l = l1l1lll11()
        l1l1lllll(SETTING)
    
    stream = url.split(l1lll1 (u"ࠫ࠿࠭ࢶ"), 1)[-1].lower()
    
    try:
        result = l1l1l11l[l1lll1 (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࢷ")]
        l11l111l  = result[l1lll1 (u"࠭ࡦࡪ࡮ࡨࡷࠬࢸ")]
    
    except Exception as e:
        l1l1llll1(e)
        return None


    for file in l11l111l:
        l1ll111l1 = file[l1lll1 (u"ࠧ࡭ࡣࡥࡩࡱ࠭ࢹ")]

        if stream == l1ll111l1.lower():
            return file[l1lll1 (u"ࠨࡨ࡬ࡰࡪ࠭ࢺ")]

    return None


def l1l1lll11():
    l1l1ll1ll = l1lll1 (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡷࡥࡱࡱࡥࡳࠩࢻ")
    Addon   =  xbmcaddon.Addon(l1l1ll1ll)
    
    l1l1lll1l   =  Addon.getSetting('portal_mac_1')
    root  = l1lll1 (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡹࡴࡢ࡮࡮ࡩࡷ࠵࠿ࡨࡧࡱࡶࡪࡥ࡮ࡢ࡯ࡨࡁࡆࡲ࡬ࠧࡲࡲࡶࡹࡧ࡬࠾ࠩࢽ")
    query = (l1lll1 (u"ࠬࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠣࡐࡉࡔࡘࠨࠬࠡࠤࡳࡥࡷ࡫࡮ࡵࡣ࡯ࠦ࠿ࠦࠢࡧࡣ࡯ࡷࡪࠨࠬࠡࠤࡸࡶࡱࠨ࠺ࠡࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡳࡳࡷࡺࡡ࡭࠰࡬ࡴࡹࡼࡰࡳ࡫ࡹࡥࡹ࡫ࡳࡦࡴࡹࡩࡷ࠴ࡴࡷࠤ࠯ࠤࠧࡳࡡࡤࠤ࠽ࠤࠧࠫࡳࠣ࠮ࠣࠦࡸ࡫ࡲࡪࡣ࡯ࠦ࠿ࠦࡻࠣࡥࡸࡷࡹࡵ࡭ࠣ࠼ࠣࡪࡦࡲࡳࡦࡿ࠯ࠤࠧࡶࡡࡴࡵࡺࡳࡷࡪࠢ࠻ࠢࠥ࠴࠵࠶࠰ࠣࡿࠪࢾ") % l1l1lll1l)
    url   =  urllib.quote_plus(query)
    l11l1 =  root + url + l1lll1 (u"࠭ࠦ࡮ࡱࡧࡩࡂࡩࡨࡢࡰࡱࡩࡱࡹࠦࡨࡧࡱࡶࡪࡥࡩࡥ࠿࠭ࠫࢿ")
    l1lll11l    = (l1lll1 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡧ࡬࡬ࡧࡵࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࣀ"))
    l1ll11l11  = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࠩࡸࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫࣁ") % l11l1)
    

    try:
        message = l1lll1 (u"ࠩࡏࡳ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳࡺ࡯ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠢࡒࡲࡪࠦ࡭ࡰ࡯ࡨࡲࡹࠦࡰ࡭ࡧࡤࡷࡪ࠴ࠧࣂ")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll11l)
        l1l1l11l = xbmc.executeJSONRPC(l1ll11l11)
        
        dixie.CloseBusy()
    
        content = json.loads(l1l1l11l.decode(l1lll1 (u"ࠪࡹࡹ࡬࠭࠹ࠩࣃ"), l1lll1 (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫࣄ")))
    
        json.dump(content, open(PATH,l1lll1 (u"ࠬࡽࠧࣅ")))

        return content
    
    except Exception as e:
        l1l1llll1(e)
        return {l1lll1 (u"࠭ࡅࡳࡴࡲࡶࠬࣆ") : l1lll1 (u"ࠧࡑ࡮ࡸ࡫࡮ࡴࠠࡆࡴࡵࡳࡷ࠭ࣇ")}


def l1l1lllll(l1ll1111l):
    now = datetime.datetime.today()
    dixie.SetSetting(l1ll1111l, str(now))


def l1l1llll1(e):
    l111111l = l1lll1 (u"ࠨࡕࡲࡶࡷࡿࠬࠡࡣࡱࠤࡪࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡧࡧ࠾ࠥࡐࡓࡐࡐࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠩࡸ࠭ࣈ")  %e
    l11111l1 = l1lll1 (u"ࠩࡓࡰࡪࡧࡳࡦࠢࡵࡩ࠲ࡲࡩ࡯࡭ࠣࡸ࡭࡯ࡳࠡࡥ࡫ࡥࡳࡴࡥ࡭ࠢࡤࡲࡩࠦࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯࠰ࠪࣉ")
    l11111ll = l1lll1 (u"࡙ࠪࡸ࡫࠺ࠡࡅࡲࡲࡹ࡫ࡸࡵࠢࡐࡩࡳࡻࠠ࠾ࡀࠣࡖࡪࡳ࡯ࡷࡧࠣࡗࡹࡸࡥࡢ࡯ࠪ࣊")
    
    dixie.log(e)
    dixie.DialogOK(l111111l, l11111l1, l11111ll)    
    dixie.SetSetting(SETTING, l1lll1 (u"ࠫࠬ࣋"))
