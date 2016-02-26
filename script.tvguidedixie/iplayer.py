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

    l1l1l1l1 = l1l1llll1(url)

    stream   = url.split(l1lll1 (u"ࠩ࠽ࠫࢴ"), 1)[-1].lower()



    try:

        result = l1l1l1l1[l1lll1 (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪࢵ")]

        l11l11l1  = result[l1lll1 (u"ࠫ࡫࡯࡬ࡦࡵࠪࢶ")]

    except Exception as e:

        l1l1lllll(e)

        return None



    for file in l11l11l1:

        l1ll111ll = file[l1lll1 (u"ࠬࡲࡡࡣࡧ࡯ࠫࢷ")]



        if stream == l1ll111ll.lower():

            return file[l1lll1 (u"࠭ࡦࡪ࡮ࡨࠫࢸ")]



    return None





def l1l1llll1(url):

    if url.startswith(l1lll1 (u"ࠧࡊࡒࡏࡅ࡞ࡀࠧࢹ")):

        l1ll11l1l = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡧࡨࡣࡪࡲ࡯ࡥࡾ࡫ࡲ࠰ࡁࡸࡶࡱࡃࡵࡳ࡮ࠩࡱࡴࡪࡥ࠾࠴ࠩࡲࡦࡳࡥ࠾ࡎ࡬ࡺࡪࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࠩࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠾ࠨࡌࡔࡎࡊ࠽ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢺ"))



    if url.startswith(l1lll1 (u"ࠩࡌࡔࡑࡇ࡙࠳࠼ࠪࢻ")):

        l1ll11l1l = (l1lll1 (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡩࡱ࡮ࡤࡽࡪࡸࡷࡸࡹ࠲ࡃࡺࡸ࡬࠾ࡷࡵࡰࠫࡳ࡯ࡥࡧࡀ࠵࠵࠷ࠦ࡯ࡣࡰࡩࡂ࡝ࡡࡵࡥ࡫࠯ࡑ࡯ࡶࡦࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡹࡵࡣࡶ࡬ࡸࡱ࡫ࡳࡠࡷࡵࡰࡂࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢼ"))



    if url.startswith(l1lll1 (u"ࠫࡎࡖࡌࡂ࡛ࡕ࠾ࠬࢽ")):

        l1ll11l1l = (l1lll1 (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡰࡦࡿࡥࡳࡹࡺࡻ࠴ࡅࡵࡳ࡮ࡀࡹࡷࡲࠦ࡮ࡱࡧࡩࡂ࠷࠱࠹ࠨࡱࡥࡲ࡫࠽ࠧ࡫ࡦࡳࡳ࡯࡭ࡢࡩࡨࡁࠫࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡀࠪࡸࡻࡢࡵ࡫ࡷࡰࡪࡹ࡟ࡶࡴ࡯ࡁࠫࡲ࡯ࡨࡩࡨࡨࡤ࡯࡮࠾ࡈࡤࡰࡸ࡫ࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࢾ"))

        



    try:

        dixie.ShowBusy()

        l1l1l1l1 = xbmc.executeJSONRPC(l1ll11l1l)

        dixie.CloseBusy()



        content = json.loads(l1l1l1l1)



        return content



    except Exception as e:

        l1l1lllll(e)

        return {l1lll1 (u"࠭ࡅࡳࡴࡲࡶࠬࢿ") : l1lll1 (u"ࠧࡑ࡮ࡸ࡫࡮ࡴࠠࡆࡴࡵࡳࡷ࠭ࣀ")}





def l1l1lllll(e):

    l11111l1 = l1lll1 (u"ࠨࡕࡲࡶࡷࡿࠬࠡࡣࡱࠤࡪࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡧࡧ࠾ࠥࡐࡓࡐࡐࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠩࡸ࠭ࣁ")  %e

    l11111ll = l1lll1 (u"ࠩࡓࡰࡪࡧࡳࡦࠢࡵࡩ࠲ࡲࡩ࡯࡭ࠣࡸ࡭࡯ࡳࠡࡥ࡫ࡥࡳࡴࡥ࡭ࠢࡤࡲࡩࠦࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯࠰ࠪࣂ")

    l1111l11 = l1lll1 (u"࡙ࠪࡸ࡫࠺ࠡࡅࡲࡲࡹ࡫ࡸࡵࠢࡐࡩࡳࡻࠠ࠾ࡀࠣࡖࡪࡳ࡯ࡷࡧࠣࡗࡹࡸࡥࡢ࡯ࠪࣃ")

    

    dixie.log(e)

    dixie.DialogOK(l11111l1, l11111ll, l1111l11)

