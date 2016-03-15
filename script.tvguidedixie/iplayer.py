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
import json

import dixie


def getURL(url):
    l1l1l1l1 = l1l1l11ll(url)
    stream   = url.split(l1lll1 (u"ࠪ࠾ࠬࢵ"), 1)[-1].lower()

    try:
        result = l1l1l1l1[l1lll1 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࢶ")]
        l11l11l1  = result[l1lll1 (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࢷ")]
    except Exception as e:
        l1l1ll111(e)
        return None

    for file in l11l11l1:
        l1l1lll1l = file[l1lll1 (u"࠭࡬ࡢࡤࡨࡰࠬࢸ")]

        if stream == l1l1lll1l.lower():
            return file[l1lll1 (u"ࠧࡧ࡫࡯ࡩࠬࢹ")]

    return None


def l1l1l11ll(url):
    if url.startswith(l1lll1 (u"ࠨࡋࡓࡐࡆ࡟࠺ࠨࢺ")):
        l1ll111ll = (l1lll1 (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡨࡢࡤ࡫ࡳࡰࡦࡿࡥࡳ࠱ࡂࡹࡷࡲ࠽ࡶࡴ࡯ࠪࡲࡵࡤࡦ࠿࠵ࠪࡳࡧ࡭ࡦ࠿ࡏ࡭ࡻ࡫ࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠪࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯࠿ࠩࡍࡕࡏࡄ࠾ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢻ"))

    if url.startswith(l1lll1 (u"ࠪࡍࡕࡒࡁ࡚࠴࠽ࠫࢼ")):
        l1ll111ll = (l1lll1 (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡲ࡯ࡥࡾ࡫ࡲࡸࡹࡺ࠳ࡄࡻࡲ࡭࠿ࡸࡶࡱࠬ࡭ࡰࡦࡨࡁ࠶࠶࠱ࠧࡰࡤࡱࡪࡃࡗࡢࡶࡦ࡬࠰ࡒࡩࡷࡧࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠦࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡂࠬࡳࡶࡤࡷ࡭ࡹࡲࡥࡴࡡࡸࡶࡱࡃࠦ࡭ࡱࡪ࡫ࡪࡪ࡟ࡪࡰࡀࡊࡦࡲࡳࡦࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢽ"))

    if url.startswith(l1lll1 (u"ࠬࡏࡐࡍࡃ࡜ࡖ࠿࠭ࢾ")):
        l1ll111ll = (l1lll1 (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡬ࡴࡱࡧࡹࡦࡴࡺࡻࡼ࠵࠿ࡶࡴ࡯ࡁࡺࡸ࡬ࠧ࡯ࡲࡨࡪࡃ࠱࠲࠺ࠩࡲࡦࡳࡥ࠾ࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡹࡵࡣࡶ࡬ࡸࡱ࡫ࡳࡠࡷࡵࡰࡂࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢿ"))

    if url.startswith(l1lll1 (u"ࠧࡊࡒࡏࡅ࡞ࡏࡔࡗ࠼ࠪࣀ")):
        l1ll111ll = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡮ࡺࡶࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࣁ"))

    try:
        dixie.ShowBusy()
        l1l1l1l1 = xbmc.executeJSONRPC(l1ll111ll)
        dixie.CloseBusy()

        content = json.loads(l1l1l1l1)

        return content

    except Exception as e:
        l1l1ll111(e)
        return {l1lll1 (u"ࠫࡊࡸࡲࡰࡴࠪࣄ") : l1lll1 (u"ࠬࡖ࡬ࡶࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠫࣅ")}


def l1l1ll111(e):
    l11111l1 = l1lll1 (u"࠭ࡓࡰࡴࡵࡽ࠱ࠦࡡ࡯ࠢࡨࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡥࡥ࠼ࠣࡎࡘࡕࡎࠡࡇࡵࡶࡴࡸ࠺ࠡࠧࡶࠫࣆ")  %e
    l11111ll = l1lll1 (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧ࠰ࡰ࡮ࡴ࡫ࠡࡶ࡫࡭ࡸࠦࡣࡩࡣࡱࡲࡪࡲࠠࡢࡰࡧࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴ࠮ࠨࣇ")
    l1111l11 = l1lll1 (u"ࠨࡗࡶࡩ࠿ࠦࡃࡰࡰࡷࡩࡽࡺࠠࡎࡧࡱࡹࠥࡃ࠾ࠡࡔࡨࡱࡴࡼࡥࠡࡕࡷࡶࡪࡧ࡭ࠨࣈ")
    
    dixie.log(e)
    dixie.DialogOK(l11111l1, l11111ll, l1111l11)
