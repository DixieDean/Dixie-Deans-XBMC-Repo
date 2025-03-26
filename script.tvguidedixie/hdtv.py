# coding: UTF-8
import sys
l1llll_opy_ = sys.version_info [0] == 2
l1ll1_opy_ = 2048
l11l_opy_ = 7
def l11l1_opy_ (ll_opy_):
	global l1lll1_opy_
	l11ll1_opy_ = ord (ll_opy_ [-1])
	l1111_opy_ = ll_opy_ [:-1]
	l1_opy_ = l11ll1_opy_ % len (l1111_opy_)
	l1l1l1_opy_ = l1111_opy_ [:l1_opy_] + l1111_opy_ [l1_opy_:]
	if l1llll_opy_:
		l1ll11_opy_ = unicode () .join ([unichr (ord (char) - l1ll1_opy_ - (l11ll_opy_ + l11ll1_opy_) % l11l_opy_) for l11ll_opy_, char in enumerate (l1l1l1_opy_)])
	else:
		l1ll11_opy_ = str () .join ([chr (ord (char) - l1ll1_opy_ - (l11ll_opy_ + l11ll1_opy_) % l11l_opy_) for l11ll_opy_, char in enumerate (l1l1l1_opy_)])
	return eval (l1ll11_opy_)
import xbmc
import xbmcgui
import time
import datetime
import os
import sys
import json
import dixie
l1l1lll_opy_   = l11l1_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸ࡭ࠩ࠘")
l1l111l_opy_   = [l1l1lll_opy_]
def checkAddons():
    for addon in l1l111l_opy_:
        if l1ll1l1_opy_(addon):
            createINI(addon)
def l1ll1l1_opy_(addon):
    if xbmc.getCondVisibility(l11l1_opy_ (u"ࠨࡕࡼࡷࡹ࡫࡭࠯ࡊࡤࡷࡆࡪࡤࡰࡰࠫࠩࡸ࠯ࠧ࠙") % addon) == 1:
        return True
    else:
        return False
def createINI(addon):
    HOME  = dixie.PROFILE
    l1lll11_opy_ = os.path.join(HOME, l11l1_opy_ (u"ࠩ࡬ࡲ࡮࠭ࠚ"))
    l11l11_opy_  = str(addon).split(l11l1_opy_ (u"ࠪ࠲ࠬࠛ"))[2] + l11l1_opy_ (u"ࠫ࠳࡯࡮ࡪࠩࠜ")
    l1l11l1_opy_   = os.path.join(l1lll11_opy_, l11l11_opy_)
    response = l111ll_opy_(addon)
    l1l_opy_ = response[l11l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࠝ")][l11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡷࠬࠞ")]
    l1ll1ll_opy_  = l11l1_opy_ (u"ࠧ࡜ࠩࠟ") + addon + l11l1_opy_ (u"ࠨ࡟࡟ࡲࠬࠠ")
    l1l11l_opy_  =  file(l1l11l1_opy_, l11l1_opy_ (u"ࠩࡺࠫࠡ"))
    l1l11l_opy_.write(l1ll1ll_opy_)
    l1ll11l_opy_ = []
    for channel in l1l_opy_:
        if l11l1_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡦࡱࡻࡥ࡞ࠩࠢ") in channel[l11l1_opy_ (u"ࠫࡱࡧࡢࡦ࡮ࠪࠣ")]:
            category =  channel[l11l1_opy_ (u"ࠬࡲࡡࡣࡧ࡯ࠫࠤ")]
            category =  l11l1l_opy_(category)
            l1l1111_opy_  = l11l1_opy_ (u"࠭࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥ࠭ࠥ") + category + l11l1_opy_ (u"ࠧࠡ࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠽ࠨࠦ")
            if l1l1111_opy_ not in l1ll11l_opy_:
                l1ll11l_opy_.append(l1l1111_opy_)
        if l11l1_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝ࠨࠧ") in channel[l11l1_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࠨ")]:
            l1l1l11_opy_ = channel[l11l1_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩࠩ")]
            l1l11ll_opy_ = l11111_opy_(l1l1l11_opy_)
            l1ll111_opy_ = l1l11ll_opy_
            l1111l_opy_ = l1l1l1l_opy_(l1l11ll_opy_, category)
            l1llll1_opy_ = l1lll1l_opy_(addon)
            stream    = l1llll1_opy_ + l1ll111_opy_
            l1lllll_opy_   = l1111l_opy_ + l11l1_opy_ (u"ࠫࡂ࠭ࠪ") + stream
            if l1lllll_opy_ not in l1ll11l_opy_:
                l1ll11l_opy_.append(l1lllll_opy_)
    for item in l1ll11l_opy_:
        l1l11l_opy_.write(l11l1_opy_ (u"ࠧࠫࡳ࡝ࡰࠥࠫ") % item)
    l1l11l_opy_.close()
def l1lll1l_opy_(addon):
    if addon == l1l1lll_opy_:
        return l11l1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹ࡮࠲ࡃࡦࡩࡴࡪࡱࡱࡁࡕࡲࡡࡺࡡࡈࡔࡌࠬࡣࡩࡣࡱࡲࡪࡲ࠽ࠨࠬ")
def l11111_opy_(l1l11_opy_):
    l111l1_opy_ = l1l11_opy_.split(l11l1_opy_ (u"ࠧࠡࠪࠪ࠭"), 1)
    l1l11_opy_  = l111l1_opy_[0]
    return l11l1l_opy_(l1l11_opy_)
def l11l1l_opy_(name):
    import re
    name  = re.sub(l11l1_opy_ (u"ࠨ࡞ࠫ࡟࠵࠳࠹ࠪ࡟࠭ࡠ࠮࠭࠮"), l11l1_opy_ (u"ࠩࠪ࠯"), name)
    items = name.split(l11l1_opy_ (u"ࠪࡡࠬ࠰"))
    name  = l11l1_opy_ (u"ࠫࠬ࠱")
    for item in items:
        if len(item) == 0:
            continue
        item += l11l1_opy_ (u"ࠬࡣࠧ࠲")
        item  = re.sub(l11l1_opy_ (u"࠭࡜࡜࡝ࡡ࠭ࡢ࠰࡜࡞ࠩ࠳"), l11l1_opy_ (u"ࠧࠨ࠴"), item)
        if len(item) > 0:
            name += item
    name  = name.replace(l11l1_opy_ (u"ࠨ࡝ࠪ࠵"), l11l1_opy_ (u"ࠩࠪ࠶"))
    name  = name.replace(l11l1_opy_ (u"ࠪࡡࠬ࠷"), l11l1_opy_ (u"ࠫࠬ࠸"))
    name  = name.strip()
    while True:
        length = len(name)
        name = name.replace(l11l1_opy_ (u"ࠬࠦࠠࠨ࠹"), l11l1_opy_ (u"࠭ࠠࠨ࠺"))
        if length == len(name):
            break
    return name.strip()
def l1l1l1l_opy_(l1l11_opy_, category):
    if (l1l11_opy_ == l11l1_opy_ (u"ࠧࡕࡘ࠶ࠫ࠻")) and (category == l11l1_opy_ (u"ࠨࡕࡺࡩࡩ࡯ࡳࡩࠢࡊࡩࡳ࡫ࡲࡢ࡮ࠪ࠼")):
        return l11l1_opy_ (u"ࠩࡗ࡚ࠥ࠹ࠠࡔࡇࠪ࠽")
    if (l1l11_opy_ == l11l1_opy_ (u"ࠪࡘ࡛࠺ࠧ࠾")) and (category == l11l1_opy_ (u"ࠫࡘࡽࡥࡥ࡫ࡶ࡬ࠥࡍࡥ࡯ࡧࡵࡥࡱ࠭࠿")):
        return l11l1_opy_ (u"࡚ࠬࡖࠡ࠶ࠣࡗࡊ࠭ࡀ")
    if (l1l11_opy_ == l11l1_opy_ (u"࠭ࡔࡗ࠵ࠪࡁ")) and (category == l11l1_opy_ (u"ࠧࡅࡧࡱࡱࡦࡸ࡫ࠡࡉࡨࡲࡪࡸࡡ࡭ࠩࡂ")):
        return l11l1_opy_ (u"ࠨࡖ࡙ࠤ࠸ࠦࡄࡌࠩࡃ")
    if (l1l11_opy_ == l11l1_opy_ (u"ࠩࡗ࡚࠹࠭ࡄ")) and (category == l11l1_opy_ (u"ࠪࡈࡪࡴ࡭ࡢࡴ࡮ࠤࡌ࡫࡮ࡦࡴࡤࡰࠬࡅ")):
        return l11l1_opy_ (u"࡙ࠫ࡜ࠠ࠵ࠢࡇࡏࠬࡆ")
    return dixie.mapChannelName(l1l11_opy_)
def l111ll_opy_(addon):
    if addon == l1l1lll_opy_:
        query = l11l1_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸ࡭࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡰ࡮ࡼࡥࡵࡸࡢࡥࡱࡲࠦࡵ࡫ࡷࡰࡪࡃࡁ࡭࡮࠮ࡧ࡭ࡧ࡮࡯ࡧ࡯ࡷࠬࡇ")
        return doJSON(query)
def doJSON(query):
    l1l1ll1_opy_  = (l11l1_opy_ (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࡈ") % query)
    response = xbmc.executeJSONRPC(l1l1ll1_opy_)
    content  = json.loads(response.decode(l11l1_opy_ (u"ࠧ࡭ࡣࡷ࡭ࡳ࠳࠱ࠨࡉ"), l11l1_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨࡊ")))
    return content
if __name__ == l11l1_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫࡋ"):
    checkAddons()