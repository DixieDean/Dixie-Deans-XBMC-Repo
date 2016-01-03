# coding: UTF-8

import sys

l1llll1l1 = sys.version_info [0] == 2
l1l11111 = 2048
l1111lll = 7

def l1lll1 (l1l1lll):
	global l1l1111l
	
	l11l1l11 = ord (l1l1lll [-1])
	l1llllll1 = l1l1lll [:-1]
	
	l1ll11l1 = l11l1l11 % len (l1llllll1)
	l1l11l1 = l1llllll1 [:l1ll11l1] + l1llllll1 [l1ll11l1:]
		
	if l1llll1l1:
		l11lll = unicode () .join ([unichr (ord (char) - l1l11111 - (l1111 + l11l1l11) % l1111lll) for l1111, char in enumerate (l1l11l1)])
	else:
		l11lll = str () .join ([chr (ord (char) - l1l11111 - (l1111 + l11l1l11) % l1111lll) for l1111, char in enumerate (l1l11l1)])
		
	return eval (l11lll)




import json
import urllib

import xbmc
import xbmcaddon

import dixie

def getURL(url):
    url      = url.split(l1lll1 (u"ࠪ࠾ࠬࢮ"), 1)[-1].lower()
    l1l1l111 = l1l1ll1l1()
    result   = l1l1l111[l1lll1 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࢯ")]
    l11l1111    = result[l1lll1 (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࢰ")]

    for file in l11l1111:
        l1ll11111   = file[l1lll1 (u"࠭࡬ࡢࡤࡨࡰࠬࢱ")]
        
        if url == l1ll11111.lower():

            return file[l1lll1 (u"ࠧࡧ࡫࡯ࡩࠬࢲ")]


def l1l1ll1l1():
    l1l1ll11l = l1lll1 (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡤࡰࡰ࡫ࡲࠨࢳ")
    Addon   =  xbmcaddon.Addon(l1l1ll11l)
    
    l1l1ll1ll   = Addon.getSetting('portal_mac_1')
    root  = l1lll1 (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡺࡡ࡭࡭ࡨࡶ࠴ࡅࡧࡦࡰࡵࡩࡤࡴࡡ࡮ࡧࡀࡅࡱࡲࠦࡱࡱࡵࡸࡦࡲ࠽ࠨࢵ")
    query = (l1lll1 (u"ࠫࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠢࡏࡈࡓࡗࠧ࠲ࠠࠣࡲࡤࡶࡪࡴࡴࡢ࡮ࠥ࠾ࠥࠨࡦࡢ࡮ࡶࡩࠧ࠲ࠠࠣࡷࡵࡰࠧࡀࠠࠣࡪࡷࡸࡵࡀ࠯࠰ࡲࡲࡶࡹࡧ࡬࠯࡫ࡳࡸࡻࡶࡲࡪࡸࡤࡸࡪࡹࡥࡳࡸࡨࡶ࠳ࡺࡶࠣ࠮ࠣࠦࡲࡧࡣࠣ࠼ࠣࠦࠪࡹࠢ࠭ࠢࠥࡷࡪࡸࡩࡢ࡮ࠥ࠾ࠥࢁࠢࡤࡷࡶࡸࡴࡳࠢ࠻ࠢࡩࡥࡱࡹࡥࡾ࠮ࠣࠦࡵࡧࡳࡴࡹࡲࡶࡩࠨ࠺ࠡࠤ࠳࠴࠵࠶ࠢࡾࠩࢶ") % l1l1ll1ll)
    url   =  urllib.quote_plus(query)
    l11l1 =  root + url + l1lll1 (u"ࠬࠬ࡭ࡰࡦࡨࡁࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬࡧࡦࡰࡵࡩࡤ࡯ࡤ࠾ࠬࠪࢷ")
    l1ll111ll  = (l1lll1 (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࢸ") % l11l1)
    l1lll11l    = (l1lll1 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡧ࡬࡬ࡧࡵࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࢹ"))
    

    try:
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll11l)
        l1l1l111 = xbmc.executeJSONRPC(l1ll111ll)

        dixie.CloseBusy()
        return json.loads(l1lll1 (u"ࡶࠤࠥࢺ") + (l1l1l111.decode(l1lll1 (u"ࠩࡸࡸ࡫࠳࠸ࠨࢻ"), l1lll1 (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪࢼ"))))
    
    except Exception:
        dixie.CloseBusy()
        return {l1lll1 (u"ࠫࡊࡸࡲࡰࡴࠪࢽ") : l1lll1 (u"ࠬࡖ࡬ࡶࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠫࢾ")}
