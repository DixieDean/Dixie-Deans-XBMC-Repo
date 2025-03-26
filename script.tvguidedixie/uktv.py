# coding: UTF-8
import sys
l11ll111_opy_ = sys.version_info [0] == 2
l1lll1l1_opy_ = 2048
l11lllll_opy_ = 7
def l1l11_opy_ (l11ll1_opy_):
	global l1llll11_opy_
	l1ll1111_opy_ = ord (l11ll1_opy_ [-1])
	l11ll11l_opy_ = l11ll1_opy_ [:-1]
	l11l11l_opy_ = l1ll1111_opy_ % len (l11ll11l_opy_)
	l111l1_opy_ = l11ll11l_opy_ [:l11l11l_opy_] + l11ll11l_opy_ [l11l11l_opy_:]
	if l11ll111_opy_:
		l1lll1_opy_ = unicode () .join ([unichr (ord (char) - l1lll1l1_opy_ - (l1l1l_opy_ + l1ll1111_opy_) % l11lllll_opy_) for l1l1l_opy_, char in enumerate (l111l1_opy_)])
	else:
		l1lll1_opy_ = str () .join ([chr (ord (char) - l1lll1l1_opy_ - (l1l1l_opy_ + l1ll1111_opy_) % l11lllll_opy_) for l1l1l_opy_, char in enumerate (l111l1_opy_)])
	return eval (l1lll1_opy_)
import xbmc
import xbmcaddon
import json
import urllib
import os
import dixie
l1l1ll111_opy_   = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡺࡱࡴࡷࡨࡵࡥࡳࡩࡥࠨࢷ")
l1l1l1l1l_opy_ = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡸࡵࡺࡣ࡬ࡴࡹࡼࠧࢸ")
l1l1l111l_opy_    = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡱࡶ࡫ࡦ࡯࡮ࡶࡴࡷࠩࢹ")
l1l11llll_opy_   = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡧࡷࡷࡹࡷ࡫ࡳࡵࡴࡨࡥࡲࡹࠧࢺ")
l1l1l11l1_opy_    = l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡳ࡭ࡳࢀࠧࢻ")
l1l1l1lll_opy_  = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡶࡸࡪࡧ࡬ࡵࡪࡸࡲࡩ࡫ࡲࡨࡴࡲࡹࡳࡪࠧࢼ")
l1lllll11_opy_     = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡳࡹࡺࡡ࡭ࡲ࡫ࡥࠬࢽ")
l1l1lllll_opy_   =  [l1l1ll111_opy_, l1l1l111l_opy_, l1l11llll_opy_, l1l1l11l1_opy_, l1l1l1lll_opy_]
def checkAddons():
    for addon in l1l1lllll_opy_:
        if l1lll11l1_opy_(addon):
            createINI(addon)
def l1lll11l1_opy_(addon):
    if xbmc.getCondVisibility(l1l11_opy_ (u"࡙ࠬࡹࡴࡶࡨࡱ࠳ࡎࡡࡴࡃࡧࡨࡴࡴࠨࠦࡵࠬࠫࢾ") % addon) == 1:
        return True
    else:
        return False
def createINI(addon):
    HOME = dixie.PROFILE
    PATH = os.path.join(HOME, l1l11_opy_ (u"࠭ࡩ࡯࡫ࠪࢿ"))
    l1ll1ll11_opy_ = str(addon).split(l1l11_opy_ (u"ࠧ࠯ࠩࣀ"))[2] + l1l11_opy_ (u"ࠨ࠰࡬ࡲ࡮࠭ࣁ")
    l1ll11111_opy_  = os.path.join(PATH, l1ll1ll11_opy_)
    response = l111l111_opy_(addon)
    try:
        result = response[l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩࣂ")]
    except KeyError:
        dixie.log(l1l11_opy_ (u"ࠪ࠱࠲࠳࠭࠮ࠢࡎࡩࡾࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡊ࡮ࡲࡥࡴࠢ࠰࠱࠲࠳࠭ࠡࠩࣃ") + addon)
        result = {l1l11_opy_ (u"ࡹࠬ࡬ࡩ࡭ࡧࡶࠫࣄ"): [{l1l11_opy_ (u"ࡺ࠭ࡦࡪ࡮ࡨࡸࡾࡶࡥࠨࣅ"): l1l11_opy_ (u"ࡻࠧࡧ࡫࡯ࡩࠬࣆ"), l1l11_opy_ (u"ࡵࠨࡶࡼࡴࡪ࠭ࣇ"): l1l11_opy_ (u"ࡶࠩࡸࡲࡰࡴ࡯ࡸࡰࠪࣈ"), l1l11_opy_ (u"ࡷࠪࡪ࡮ࡲࡥࠨࣉ"): l1l11_opy_ (u"ࡸࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡾࡸࡹࠩ࣊"), l1l11_opy_ (u"ࡹࠬࡲࡡࡣࡧ࡯ࠫ࣋"): l1l11_opy_ (u"ࡺ࠭ࡎࡐࠢࡆࡌࡆࡔࡎࡆࡎࡖࠫ࣌")}], l1l11_opy_ (u"ࡻࠧ࡭࡫ࡰ࡭ࡹࡹࠧ࣍"): {l1l11_opy_ (u"ࡵࠨࡵࡷࡥࡷࡺࠧ࣎"): 0, l1l11_opy_ (u"ࡶࠩࡷࡳࡹࡧ࡬ࠨ࣏"): 1, l1l11_opy_ (u"ࡷࠪࡩࡳࡪ࣐ࠧ"): 1}}
    l1ll1l111_opy_ = result[l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡴ࣑ࠩ")]
    l1ll11lll_opy_  = file(l1ll11111_opy_, l1l11_opy_ (u"ࠫࡼ࣒࠭"))
    l1ll11lll_opy_.write(l1l11_opy_ (u"ࠬࡡ࣓ࠧ"))
    l1ll11lll_opy_.write(addon)
    l1ll11lll_opy_.write(l1l11_opy_ (u"࠭࡝ࠨࣔ"))
    l1ll11lll_opy_.write(l1l11_opy_ (u"ࠧ࡝ࡰࠪࣕ"))
    l1llll1ll_opy_ = []
    for channel in l1ll1l111_opy_:
        l1lll1ll1_opy_ = dixie.cleanLabel(channel[l1l11_opy_ (u"ࠨ࡮ࡤࡦࡪࡲࠧࣖ")])
        l11111ll_opy_ = dixie.mapChannelName(l1lll1ll1_opy_)
        stream   = channel[l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧࣗ")]
        l1lllll1l_opy_ = l11111ll_opy_ + l1l11_opy_ (u"ࠪࡁࠬࣘ") + stream
        l1llll1ll_opy_.append(l1lllll1l_opy_)
        l1llll1ll_opy_.sort()
    for item in l1llll1ll_opy_:
      l1ll11lll_opy_.write(l1l11_opy_ (u"ࠦࠪࡹ࡜࡯ࠤࣙ") % item)
    l1ll11lll_opy_.close()
def l111l111_opy_(addon):
    l1l1l1ll1_opy_ = (l1l11_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࣚ") % addon)
    if addon == l1l1l1lll_opy_:
        login = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡨࡥࡱࡺࡨࡶࡰࡧࡩࡷ࡭ࡲࡰࡷࡱࡨ࠴ࡅ࡭ࡰࡦࡨࡁ࡬࡫࡮ࡳࡧࡶࠪࡵࡵࡲࡵࡣ࡯ࡁࠪ࠽ࡢࠦ࠴࠵ࡲࡦࡳࡥࠦ࠴࠵ࠩ࠸ࡧࠥ࠳࠲ࠨ࠶࠷ࠫ࠵ࡣࡋࠨ࠹ࡩࠫ࠵ࡣࡅࡒࡐࡔࡘࠥ࠳࠲ࡺ࡬࡮ࡺࡥࠦ࠷ࡧࡇࡱ࡯ࡣ࡬ࠧ࠵࠴࡙ࡵࠥ࠳࠲࡙࡭ࡪࡽࠥ࠳࠲ࡗ࡬ࡪࠫ࠲࠱ࡎ࡬ࡷࡹࠫ࠲࠱ࡑࡩࠩ࠷࠶ࡃࡩࡣࡱࡲࡪࡲࡳࠦ࠷ࡥࠩ࠷࡬ࡃࡐࡎࡒࡖࠪ࠻ࡤࠦ࠷ࡥࠩ࠷࡬ࡉࠦ࠷ࡧࠩ࠷࠸ࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡲࡤࡶࡪࡴࡴࡢ࡮ࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲ࡧࡣ࡯ࡷࡪࠫ࠲࠳ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡹࡷࡲࠥ࠳࠴ࠨ࠷ࡦࠫ࠲࠱ࠧ࠵࠶࡭ࡺࡴࡱࠧ࠶ࡥࠪ࠸ࡦࠦ࠴ࡩࡱࡼ࠷࠮ࡪࡲࡷࡺ࠻࠼࠮ࡵࡸࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡱࡲࡤࡷࡸࡽ࡯ࡳࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲࠱࠲࠳࠴ࠪ࠸࠲ࠦ࠴ࡦࠩ࠷࠶ࠥ࠳࠴ࡰࡥࡨࠫ࠲࠳ࠧ࠶ࡥࠪ࠸࠰ࠦ࠴࠵࠴࠵ࠫ࠳ࡢ࠳ࡄࠩ࠸ࡧ࠷࠹ࠧ࠶ࡥ࠹࠹ࠥ࠴ࡣ࠴࠶ࠪ࠹ࡡ࠸࠶ࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡴࡧࡵ࡭ࡦࡲࠥ࠳࠴ࠨ࠷ࡦࠫ࠲࠱ࠧ࠺ࡦࠪ࠸࠲ࡴࡧࡱࡨࡤࡹࡥࡳ࡫ࡤࡰࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࡴࡳࡷࡨࠩ࠷ࡩࠥ࠳࠲ࠨ࠶࠷ࡩࡵࡴࡶࡲࡱࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࡴࡳࡷࡨࠩ࠷ࡩࠥ࠳࠲ࠨ࠶࠷ࡹ࡮ࠦ࠴࠵ࠩ࠸ࡧࠥ࠳࠲ࠨ࠶࠷ࠫ࠲࠳ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࠫ࠲࠳ࠧ࠶ࡥࠪ࠸࠰ࠦ࠴࠵ࠩ࠷࠸ࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡦࡨࡺ࡮ࡩࡥࡠ࡫ࡧ࠶ࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࠥ࠳࠴ࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡥࡧࡹ࡭ࡨ࡫࡟ࡪࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲ࠦ࠴࠵ࠩ࠼ࡪࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡲࡤࡷࡸࡽ࡯ࡳࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࡳࡻ࡬࡭ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡰࡴ࡭ࡩ࡯ࠧ࠵࠶ࠪ࠹ࡡࠦ࠴࠳ࡲࡺࡲ࡬ࠦ࠹ࡧࠫࣛ")
    else:
        login = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪࣜ") + addon + l1l11_opy_ (u"ࠨ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡷࡪࡩࡵࡳ࡫ࡷࡽࡤࡩࡨࡦࡥ࡮ࠪࡪࡾࡴࡳࡣࠩࡴࡦ࡭ࡥࠧࡲ࡯ࡳࡹࠬࡴࡩࡷࡰࡦࡳࡧࡩ࡭ࠨࡷ࡭ࡹࡲࡥ࠾ࡎ࡬ࡺࡪࠫ࠲࠱ࡖ࡙ࠪࡺࡸ࡬ࠨࣝ")
    try:
        query = l1l1lll11_opy_(addon)
    except: pass
    l1l1l11ll_opy_ = (l1l11_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࣞ") % login)
    l1l1l1l11_opy_ = (l1l11_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࠫࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࣟ") % query)
    try:
        xbmc.executeJSONRPC(l1l1l1ll1_opy_)
        if addon != l1l1l1l1l_opy_:
            xbmc.executeJSONRPC(l1l1l11ll_opy_)
        response = xbmc.executeJSONRPC(l1l1l1l11_opy_)
        content  = json.loads(response.decode(l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ࣠"), l1l11_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬ࣡")))
        return content
    except:
        dixie.log(l1l11_opy_ (u"࠭࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭ࠡࡒ࡯ࡹ࡬࡯࡮ࠡࡇࡵࡶࡴࡸࠠ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮ࠩ࣢"))
        return {l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࣣ࠭") : l1l11_opy_ (u"ࠨࡒ࡯ࡹ࡬࡯࡮ࠡࡇࡵࡶࡴࡸࠧࣤ")}
def l1l1lll11_opy_(addon):
    if addon == l1l1l1l1l_opy_:
        return l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡺࡿࡡࡪࡲࡷࡺ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃ࡬ࡪࡸࡨࡸࡻࡥࡡ࡭࡮ࠩࡩࡽࡺࡲࡢࠨࡳࡥ࡬࡫ࠦࡱ࡮ࡲࡸࠫࡺࡨࡶ࡯ࡥࡲࡦ࡯࡬࠾ࠧ࠵ࡪ࡚ࡹࡥࡳࡵࠨ࠶࡫ࡸࡩࡤࡪࡤࡶࡩࠫ࠲ࡧࡎ࡬ࡦࡷࡧࡲࡺࠧ࠵ࡪࡆࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯ࠧ࠵࠴ࡘࡻࡰࡱࡱࡵࡸࠪ࠸ࡦࡌࡱࡧ࡭ࠪ࠸ࡦࡢࡦࡧࡳࡳࡹࠥ࠳ࡨࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡸࡻࡹࡵࡣࡵ࠵࠲࠹ࠫ࠲ࡧࡴࡨࡷࡴࡻࡲࡤࡧࡶࠩ࠷࡬ࡩ࡮ࡩࠨ࠶࡫࡮࡯ࡵ࠰ࡳࡲ࡬ࠬࡴࡪࡶ࡯ࡩࡂࡇ࡬࡭ࠧ࠵࠴ࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬࡵࡳ࡮ࠪࣥ")
    if addon == l1l1l111l_opy_:
        return l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡶࡻࡩࡤ࡭࡬ࡴࡹࡼ࠯ࡀࡣࡦࡸ࡮ࡵ࡮࠾ࡵࡷࡶࡪࡧ࡭ࡠࡸ࡬ࡨࡪࡵࠦࡦࡺࡷࡶࡦࠬࡰࡢࡩࡨࠪࡵࡲ࡯ࡵࠨࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡂࠬࡴࡪࡶ࡯ࡩࡂࡇ࡬࡭ࠨࡸࡶࡱࡃ࠰ࠨࣦ")
    if addon == l1l11llll_opy_:
        return l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡬ࡵࡵࡷࡵࡩࡸࡺࡲࡦࡣࡰࡷ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃࡳࡵࡴࡨࡥࡲࡥࡶࡪࡦࡨࡳࠫ࡫ࡸࡵࡴࡤࠪࡵࡧࡧࡦࠨࡳࡰࡴࡺࠦࡵࡪࡸࡱࡧࡴࡡࡪ࡮ࡀࠪࡹ࡯ࡴ࡭ࡧࡀࡅࡱࡲࠦࡶࡴ࡯ࡁ࠵࠭ࣧ")
    if addon == l1l1l1lll_opy_:
        return l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡳࡵࡧࡤࡰࡹ࡮ࡵ࡯ࡦࡨࡶ࡬ࡸ࡯ࡶࡰࡧ࠳ࡄ࡭ࡥ࡯ࡴࡨࡣࡳࡧ࡭ࡦ࠿ࡄࡰࡱࠬࡰࡰࡴࡷࡥࡱࡃࠥ࠸ࡄࠨ࠶࠷ࡴࡡ࡮ࡧࠨ࠶࠷ࠫ࠳ࡂ࠭ࠨ࠶࠷ࠫ࠵ࡃࡋࠨ࠹ࡉࠫ࠵ࡃࡅࡒࡐࡔࡘࠫࡸࡪ࡬ࡸࡪࠫ࠵ࡅࡅ࡯࡭ࡨࡱࠫࡕࡱ࠮࡚࡮࡫ࡷࠬࡖ࡫ࡩ࠰ࡒࡩࡴࡶ࠮ࡓ࡫࠱ࡃࡩࡣࡱࡲࡪࡲࡳࠦ࠷ࡅࠩ࠷ࡌࡃࡐࡎࡒࡖࠪ࠻ࡄࠦ࠷ࡅࠩ࠷ࡌࡉࠦ࠷ࡇࠩ࠷࠸ࠥ࠳ࡅ࠮ࠩ࠷࠸ࡰࡢࡴࡨࡲࡹࡧ࡬ࠦ࠴࠵ࠩ࠸ࡇࠫࠦ࠴࠵ࡪࡦࡲࡳࡦࠧ࠵࠶ࠪ࠸ࡃࠬࠧ࠵࠶ࡺࡸ࡬ࠦ࠴࠵ࠩ࠸ࡇࠫࠦ࠴࠵࡬ࡹࡺࡰࠦ࠵ࡄࠩ࠷ࡌࠥ࠳ࡈࡰࡻ࠶࠴ࡩࡱࡶࡹ࠺࠻࠴ࡴࡷࠧ࠵࠶ࠪ࠸ࡃࠬࠧ࠵࠶ࡵࡶࡡࡴࡵࡺࡳࡷࡪࠥ࠳࠴ࠨ࠷ࡆ࠱ࠥ࠳࠴࠳࠴࠵࠶ࠥ࠳࠴ࠨ࠶ࡈ࠱ࠥ࠳࠴ࡰࡥࡨࠫ࠲࠳ࠧ࠶ࡅ࠰ࠫ࠲࠳࠲࠳ࠩ࠸ࡇ࠱ࡂࠧ࠶ࡅ࠼࠾ࠥ࠴ࡃ࠷࠷ࠪ࠹ࡁ࠲࠴ࠨ࠷ࡆ࠽࠴ࠦ࠴࠵ࠩ࠷ࡉࠫࠦ࠴࠵ࡷࡪࡸࡩࡢ࡮ࠨ࠶࠷ࠫ࠳ࡂ࠭ࠨ࠻ࡇࠫ࠲࠳ࡵࡨࡲࡩࡥࡳࡦࡴ࡬ࡥࡱࠫ࠲࠳ࠧ࠶ࡅ࠰ࡺࡲࡶࡧࠨ࠶ࡈ࠱ࠥ࠳࠴ࡦࡹࡸࡺ࡯࡮ࠧ࠵࠶ࠪ࠹ࡁࠬࡶࡵࡹࡪࠫ࠲ࡄ࠭ࠨ࠶࠷ࡹ࡮ࠦ࠴࠵ࠩ࠸ࡇࠫࠦ࠴࠵ࠩ࠷࠸ࠥ࠳ࡅ࠮ࠩ࠷࠸ࡳࡪࡩࡱࡥࡹࡻࡲࡦࠧ࠵࠶ࠪ࠹ࡁࠬࠧ࠵࠶ࠪ࠸࠲ࠦ࠴ࡆ࠯ࠪ࠸࠲ࡥࡧࡹ࡭ࡨ࡫࡟ࡪࡦ࠵ࠩ࠷࠸ࠥ࠴ࡃ࠮ࠩ࠷࠸ࠥ࠳࠴ࠨ࠶ࡈ࠱ࠥ࠳࠴ࡧࡩࡻ࡯ࡣࡦࡡ࡬ࡨࠪ࠸࠲ࠦ࠵ࡄ࠯ࠪ࠸࠲ࠦ࠴࠵ࠩ࠼ࡊࠥ࠳ࡅ࠮ࠩ࠷࠸ࡰࡢࡵࡶࡻࡴࡸࡤࠦ࠴࠵ࠩ࠸ࡇࠫ࡯ࡷ࡯ࡰࠪ࠸ࡃࠬࠧ࠵࠶ࡱࡵࡧࡪࡰࠨ࠶࠷ࠫ࠳ࡂ࠭ࡱࡹࡱࡲࠥ࠸ࡆࠩࡱࡴࡪࡥ࠾ࡥ࡫ࡥࡳࡴࡥ࡭ࡵࠩ࡫ࡪࡴࡲࡦࡡ࡬ࡨࡂࠫ࠲ࡂࠩࣨ")
    else:
        Addon = xbmcaddon.Addon(addon)
        if addon == l1lllll11_opy_:
            username =  Addon.getSetting(l1l11_opy_ (u"࠭ࡕࡴࡧࡵࡲࡦࡳࡥࠨࣩ"))
            password =  Addon.getSetting(l1l11_opy_ (u"ࠧࡑࡣࡶࡷࡼࡵࡲࡥࠩ࣪"))
        else:
            username =  Addon.getSetting(l1l11_opy_ (u"ࠨ࡭ࡤࡷࡺࡺࡡ࡫ࡣࡱ࡭ࡲ࡯ࠧ࣫"))
            password =  Addon.getSetting(l1l11_opy_ (u"ࠩࡶࡥࡱࡧࡳࡰࡰࡤࠫ࣬"))
        l1l11lll1_opy_     = l1l11_opy_ (u"ࠪ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡹࡴࡳࡧࡤࡱࡤࡼࡩࡥࡧࡲࠪࡪࡾࡴࡳࡣࠩࡴࡦ࡭ࡥࠧࡲ࡯ࡳࡹࠬࡴࡩࡷࡰࡦࡳࡧࡩ࡭࠿ࠩࡸ࡮ࡺ࡬ࡦ࠿ࡄࡰࡱࠬࡵࡳ࡮ࡀ࣭ࠫ")
        l1l1l1111_opy_  =  l1l1ll1ll_opy_(addon)
        l1ll11ll1_opy_   = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵࣮ࠧ") + addon
        l1l1ll11l_opy_  =  l1ll11ll1_opy_ + l1l11lll1_opy_ + l1l1l1111_opy_
        l1l1ll1l1_opy_ = l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡱࡥࡲ࡫࠽ࠨ࣯") + username + l1l11_opy_ (u"࠭ࠦࡱࡣࡶࡷࡼࡵࡲࡥ࠿ࣰࠪ") + password + l1l11_opy_ (u"ࠧࠧࡶࡼࡴࡪࡃࡧࡦࡶࡢࡰ࡮ࡼࡥࡠࡵࡷࡶࡪࡧ࡭ࡴࠨࡦࡥࡹࡥࡩࡥ࠿࠳ࣱࠫ")
        return l1l1ll11l_opy_ + urllib.quote_plus(l1l1ll1l1_opy_)
def l1l1ll1ll_opy_(addon):
    if (addon == l1l1ll111_opy_):
        return l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࠵࠺࠲࠶࠾࠷࠯࠳࠶࠽࠳࠷࠵࠶࠼࠻࠴࠵࠶࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄࣲ࠭")
    if addon == l1l1l11l1_opy_:
        return l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࡶࡴ࡮ࡴࡺࡵࡸࡳࡶࡴ࠴ࡴ࡬࠼࠻࠴࠵࠶࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄ࠭ࣳ")
    if addon == l1lllll11_opy_:
        return l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡳࡹࡺࡴࡷ࠰ࡪࡥ࠿࠸࠰࠺࠷࠲ࡩࡳ࡯ࡧ࡮ࡣ࠵࠲ࡵ࡮ࡰࡀࠩࣴ")
def l1ll1l11l_opy_(e):
    l1lll1lll_opy_ = l1l11_opy_ (u"ࠫࡘࡵࡲࡳࡻ࠯ࠤࡦࡴࠠࡦࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡪࡪ࠺ࠡࡌࡖࡓࡓࠦࡅࡳࡴࡲࡶ࠿ࠦࠥࡴࠩࣵ")  %e
    l1llll111_opy_ = l1l11_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥࡩ࡯࡯ࡶࡤࡧࡹࠦࡵࡴࠢࡲࡲࠥࡺࡨࡦࠢࡩࡳࡷࡻ࡭࠯ࣶࠩ")
    l1llll11l_opy_ = l1l11_opy_ (u"࠭ࡕࡱ࡮ࡲࡥࡩࠦࡡࠡ࡮ࡲ࡫ࠥࡼࡩࡢࠢࡷ࡬ࡪࠦࡡࡥࡦࡲࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠠࡢࡰࡧࠤࡵࡵࡳࡵࠢࡷ࡬ࡪࠦ࡬ࡪࡰ࡮࠲ࠬࣷ")
    dixie.log(e)
    dixie.DialogOK(l1lll1lll_opy_, l1llll111_opy_, l1llll11l_opy_)
    dixie.SetSetting(SETTING, l1l11_opy_ (u"ࠧࠨࣸ"))
if __name__ == l1l11_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࣹࠪ"):
    checkAddons()