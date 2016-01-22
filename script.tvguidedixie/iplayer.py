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
import json

import dixie


def getURL(url):
    l1l1l11l = l1l1lll1l(url)
    stream   = url.split(l1lll1 (u"ࠩ࠽ࠫࢴ"), 1)[-1].lower()

    try:
        result = l1l1l11l[l1lll1 (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪࢵ")]
        l11l111l  = result[l1lll1 (u"ࠫ࡫࡯࡬ࡦࡵࠪࢶ")]
    except Exception as e:
        l1l1llll1(e)
        return None

    for file in l11l111l:
        l1ll111l1 = file[l1lll1 (u"ࠬࡲࡡࡣࡧ࡯ࠫࢷ")]

        if stream == l1ll111l1.lower():
            return file[l1lll1 (u"࠭ࡦࡪ࡮ࡨࠫࢸ")]

    return None


def l1l1lll1l(url):
    if url.startswith(l1lll1 (u"ࠧࡊࡒࡏࡅ࡞ࡀࠧࢹ")):
        l1ll11l11  = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡧࡨࡣࡪࡲ࡯ࡥࡾ࡫ࡲ࠰ࡁࡸࡶࡱࡃࡵࡳ࡮ࠩࡱࡴࡪࡥ࠾࠴ࠩࡲࡦࡳࡥ࠾ࡎ࡬ࡺࡪࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࠩࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠾ࠨࡌࡔࡎࡊ࠽ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢺ"))

    if url.startswith(l1lll1 (u"ࠩࡌࡔࡑࡇ࡙࠳࠼ࠪࢻ")):
        l1ll11l11  = (l1lll1 (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡩࡱ࡮ࡤࡽࡪࡸࡷࡸࡹ࠲ࡃࡺࡸ࡬࠾ࡷࡵࡰࠫࡳ࡯ࡥࡧࡀ࠵࠵࠷ࠦ࡯ࡣࡰࡩࡂ࡝ࡡࡵࡥ࡫࠯ࡑ࡯ࡶࡦࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡹࡵࡣࡶ࡬ࡸࡱ࡫ࡳࡠࡷࡵࡰࡂࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢼ"))

    try:
        dixie.ShowBusy()
        l1l1l11l = xbmc.executeJSONRPC(l1ll11l11)
        dixie.CloseBusy()

        content = json.loads(l1l1l11l)

        return content

    except Exception as e:
        l1l1llll1(e)
        return {l1lll1 (u"ࠫࡊࡸࡲࡰࡴࠪࢽ") : l1lll1 (u"ࠬࡖ࡬ࡶࡩ࡬ࡲࠥࡋࡲࡳࡱࡵࠫࢾ")}


def l1l1llll1(e):
    l111111l = l1lll1 (u"࠭ࡓࡰࡴࡵࡽ࠱ࠦࡡ࡯ࠢࡨࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡥࡥ࠼ࠣࡎࡘࡕࡎࠡࡇࡵࡶࡴࡸ࠺ࠡࠧࡶࠫࢿ")  %e
    l11111l1 = l1lll1 (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧ࠰ࡰ࡮ࡴ࡫ࠡࡶ࡫࡭ࡸࠦࡣࡩࡣࡱࡲࡪࡲࠠࡢࡰࡧࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴ࠮ࠨࣀ")
    l11111ll = l1lll1 (u"ࠨࡗࡶࡩ࠿ࠦࡃࡰࡰࡷࡩࡽࡺࠠࡎࡧࡱࡹࠥࡃ࠾ࠡࡔࡨࡱࡴࡼࡥࠡࡕࡷࡶࡪࡧ࡭ࠨࣁ")
    
    dixie.log(e)
    dixie.DialogOK(l111111l, l11111l1, l11111ll)
