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




import xbmc
import json
import dixie

def getURL(url):
    url      = url.split(l1ll11 (u"ࠩ࠽ࠫ࢑"), 1)[-1].lower()
    l1l111ll = l1l1ll11l()
    result   = l1l111ll[l1ll11 (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ࢒")]
    l111l11l    = result[l1ll11 (u"ࠫ࡫࡯࡬ࡦࡵࠪ࢓")]

    for file in l111l11l:
        l1l1l1lll   = file[l1ll11 (u"ࠬࡲࡡࡣࡧ࡯ࠫ࢔")]
        l1l1l1ll1 = l1l1l1lll.rsplit(l1ll11 (u"࡛࠭࠰ࡅࡒࡐࡔࡘ࡝ࠨ࢕"), 1)[0].split(l1ll11 (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࠧ࢖"), 1)[-1]
        
        if url == l1l1l1ll1.lower():

            return file[l1ll11 (u"ࠨࡨ࡬ࡰࡪ࠭ࢗ")]


def l1l1ll11l():
    l1l1ll1l1 = l1ll11 (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡪࡧࡸࡻ࠭࢘")
    l1l1ll111  =  xbmc.getCondVisibility(l1ll11 (u"ࠪࡗࡾࡹࡴࡦ࡯࠱ࡌࡦࡹࡁࡥࡦࡲࡲ࠭ࠫࡳ࢙ࠪࠩ") % l1l1ll1l1) == True

    if l1l1ll111:
        l1ll1l11    = (l1ll11 (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡩࡦࡷࡺ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃ࡭ࡢ࡫ࡱࡣࡱ࡯ࡳࡵࠨࡷ࡭ࡹࡲࡥ࠾ࠨࡸࡶࡱࡃࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁ࢚ࠬ"))
        l1l1ll1ll  = (l1ll11 (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡪࡧࡸࡻ࠵࠿ࡢࡥࡷ࡭ࡴࡴ࠽࡭࡫ࡹࡩࡹࡼ࡟ࡢ࡮࡯ࠪࡹ࡯ࡴ࡭ࡧࡀࡅࡱࡲࠫࡤࡪࡤࡲࡳ࡫࡬ࡴࠨࡸࡶࡱࡃࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁ࢛ࠬ"))
    else:
        l1ll1l11    = (l1ll11 (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡹࡾࡧࡩࡱࡶࡹ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡳࡡࡪࡰࡢࡰ࡮ࡹࡴࠧࡶ࡬ࡸࡱ࡫࠽ࠧࡷࡵࡰࡂࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫ࢜"))
        l1l1ll1ll  = (l1ll11 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡺࡿࡡࡪࡲࡷࡺ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃ࡬ࡪࡸࡨࡸࡻࡥࡡ࡭࡮ࠩࡸ࡮ࡺ࡬ࡦ࠿ࡄࡰࡱ࠱ࡣࡩࡣࡱࡲࡪࡲࡳࠧࡷࡵࡰࡂࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫ࢝"))

    try:
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1ll1l11)
        l1l111ll = xbmc.executeJSONRPC(l1l1ll1ll)

        dixie.CloseBusy()
        return json.loads(l1ll11 (u"ࡶࠤࠥ࢞") + (l1l111ll.decode(l1ll11 (u"ࠩ࡯ࡥࡹ࡯࡮࠮࠳ࠪ࢟"), l1ll11 (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪࢠ"))))
    
    except Exception:
        dixie.CloseBusy()
        return {l1ll11 (u"ࠫࡊࡸࡲࡰࡴࠪࢡ") : l1ll11 (u"ࠬࡖ࡬ࡶࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠫࢢ")}
