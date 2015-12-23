# coding: UTF-8

import sys

l1lll11ll = sys.version_info [0] == 2
l11ll1l1 = 2048
l1111111 = 7

def l1ll11 (l1l1l1l):
	global l11ll1ll
	
	l111lll1 = ord (l1l1l1l [-1])
	l1lll1lll = l1l1l1l [:-1]
	
	l1l1ll1l = l111lll1 % len (l1lll1lll)
	l1l1111 = l1lll1lll [:l1l1ll1l] + l1lll1lll [l1l1ll1l:]
		
	if l1lll11ll:
		l11l1l = unicode () .join ([unichr (ord (char) - l11ll1l1 - (l1lll1 + l111lll1) % l1111111) for l1lll1, char in enumerate (l1l1111)])
	else:
		l11l1l = str () .join ([chr (ord (char) - l11ll1l1 - (l1lll1 + l111lll1) % l1111111) for l1lll1, char in enumerate (l1l1111)])
		
	return eval (l11l1l)




import json
import urllib

import xbmc
import xbmcaddon

import dixie

def getURL(url):
    url      = url.split(l1ll11 (u"࠭࠺ࠨࢣ"), 1)[-1].lower()
    l1l111ll = l1l1l1l11()
    result   = l1l111ll[l1ll11 (u"ࠧࡳࡧࡶࡹࡱࡺࠧࢤ")]
    l111l11l    = result[l1ll11 (u"ࠨࡨ࡬ࡰࡪࡹࠧࢥ")]

    for file in l111l11l:
        l1l1l1lll   = file[l1ll11 (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࢦ")]
        
        if url == l1l1l1lll.lower():

            return file[l1ll11 (u"ࠪࡪ࡮ࡲࡥࠨࢧ")]


def l1l1l1l11():
    l1l1l11ll = l1ll11 (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡧ࡬࡬ࡧࡵࠫࢨ")
    Addon   =  xbmcaddon.Addon(l1l1l11ll)
    
    l1l1l1l1l   =  Addon.getSetting('portal_mac_1')
    root  = l1ll11 (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡤࡰࡰ࡫ࡲ࠰ࡁࡪࡩࡳࡸࡥࡠࡰࡤࡱࡪࡃࡁ࡭࡮ࠩࡴࡴࡸࡴࡢ࡮ࡀࠫࢪ")
    query = (l1ll11 (u"ࠧࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠥࡒࡋࡖࡓࠣ࠮ࠣࠦࡵࡧࡲࡦࡰࡷࡥࡱࠨ࠺ࠡࠤࡩࡥࡱࡹࡥࠣ࠮ࠣࠦࡺࡸ࡬ࠣ࠼ࠣࠦ࡭ࡺࡴࡱ࠼࠲࠳ࡵࡵࡲࡵࡣ࡯࠲࡮ࡶࡴࡷࡲࡵ࡭ࡻࡧࡴࡦࡵࡨࡶࡻ࡫ࡲ࠯ࡶࡹࠦ࠱ࠦࠢ࡮ࡣࡦࠦ࠿ࠦࠢࠦࡵࠥ࠰ࠥࠨࡳࡦࡴ࡬ࡥࡱࠨ࠺ࠡࡽࠥࡧࡺࡹࡴࡰ࡯ࠥ࠾ࠥ࡬ࡡ࡭ࡵࡨࢁ࠱ࠦࠢࡱࡣࡶࡷࡼࡵࡲࡥࠤ࠽ࠤࠧ࠶࠰࠱࠲ࠥࢁࠬࢫ") % l1l1l1l1l)
    url   =  urllib.quote_plus(query)
    l1111 =  root + url + l1ll11 (u"ࠨࠨࡰࡳࡩ࡫࠽ࡤࡪࡤࡲࡳ࡫࡬ࡴࠨࡪࡩࡳࡸࡥࡠ࡫ࡧࡁ࠯࠭ࢬ")
    l1l1ll1ll  = (l1ll11 (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࢭ") % l1111)
    

    try:
        dixie.ShowBusy()
        
        l1l111ll = xbmc.executeJSONRPC(l1l1ll1ll)

        dixie.CloseBusy()
        return json.loads(l1ll11 (u"ࡸࠦࠧࢮ") + (l1l111ll.decode(l1ll11 (u"ࠫࡺࡺࡦ࠮࠺ࠪࢯ"), l1ll11 (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬࢰ"))))
    
    except Exception:
        dixie.CloseBusy()
        return {l1ll11 (u"࠭ࡅࡳࡴࡲࡶࠬࢱ") : l1ll11 (u"ࠧࡑ࡮ࡸ࡫࡮ࡴࠠࡆࡴࡵࡳࡷ࠭ࢲ")}
