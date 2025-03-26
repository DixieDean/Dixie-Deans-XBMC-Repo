# coding: UTF-8
import sys
l1l111l_opy_ = sys.version_info [0] == 2
l11111_opy_ = 2048
l1111_opy_ = 7
def l11ll1_opy_ (ll_opy_):
	global l11l_opy_
	l1l11l1_opy_ = ord (ll_opy_ [-1])
	l111ll_opy_ = ll_opy_ [:-1]
	l1ll1ll_opy_ = l1l11l1_opy_ % len (l111ll_opy_)
	l1ll1_opy_ = l111ll_opy_ [:l1ll1ll_opy_] + l111ll_opy_ [l1ll1ll_opy_:]
	if l1l111l_opy_:
		l1llll1_opy_ = unicode () .join ([unichr (ord (char) - l11111_opy_ - (l11lll_opy_ + l1l11l1_opy_) % l1111_opy_) for l11lll_opy_, char in enumerate (l1ll1_opy_)])
	else:
		l1llll1_opy_ = str () .join ([chr (ord (char) - l11111_opy_ - (l11lll_opy_ + l1l11l1_opy_) % l1111_opy_) for l11lll_opy_, char in enumerate (l1ll1_opy_)])
	return eval (l1llll1_opy_)
import xbmc
import xbmcaddon
import dixie
import os
import sys
import json
l1l1ll11l_opy_ = l11ll1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡰࡥࡷࡺࡨࡶࡤࠪࢭ")
l1l1ll111_opy_ = l11ll1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡹࡾࡧ࠲ࠨࢮ")
l11ll11_opy_ = [l1l1ll11l_opy_, l1l1ll111_opy_]
def checkAddons():
    for addon in l11ll11_opy_:
        if l11lll1_opy_(addon):
            createINI(addon)
def l11lll1_opy_(addon):
    if xbmc.getCondVisibility(l11ll1_opy_ (u"ࠫࡘࡿࡳࡵࡧࡰ࠲ࡍࡧࡳࡂࡦࡧࡳࡳ࠮ࠥࡴࠫࠪࢯ") % addon) == 1:
        return True
    else:
        return False
def l1l1ll1ll_opy_(addon):
    Addon  = xbmcaddon.Addon(id=addon)
    prefix = l1l1111_opy_(Addon)
    if prefix == l11ll1_opy_ (u"ࠬࡎࡄࡕࡘ࠽ࠫࢰ"):
        return os.path.join(dixie.PROFILE, l11ll1_opy_ (u"࠭ࡳࡩࡶࡨࡱࡵ࠭ࢱ"))
    if prefix == l11ll1_opy_ (u"ࠧࡉࡆࡗ࡚࠷ࡀࠧࢲ"):
        return os.path.join(dixie.PROFILE, l11ll1_opy_ (u"ࠨࡴࡸࡸࡪࡳࡰࠨࢳ"))
def createINI(addon):
    l1l1l1lll_opy_ = [l11ll1_opy_ (u"ࠩࡶ࡬ࡹ࡫࡭ࡱࠩࢴ"), l11ll1_opy_ (u"ࠪࡶࡺࡺࡥ࡮ࡲࠪࢵ")]
    for l1l1lll11_opy_ in l1l1l1lll_opy_:
        path = os.path.join(dixie.PROFILE, l1l1lll11_opy_)
        if os.path.exists(path):
            os.remove(path)
    Addon  = xbmcaddon.Addon(id=addon)
    path   = Addon.getAddonInfo(l11ll1_opy_ (u"ࠫࡵࡧࡴࡩࠩࢶ"))
    prefix = l1l1111_opy_(Addon)
    sys.path.insert(0, path)
    import api
    api.login()
    doJSON(addon)
    HOME  = dixie.PROFILE
    l1ll11_opy_ = os.path.join(HOME, l11ll1_opy_ (u"ࠬ࡯࡮ࡪࠩࢷ"))
    l1lllll_opy_  = str(addon).split(l11ll1_opy_ (u"࠭࠮ࠨࢸ"))[2] + l11ll1_opy_ (u"ࠧ࠯࡫ࡱ࡭ࠬࢹ")
    l1l_opy_   = os.path.join(l1ll11_opy_, l1lllll_opy_)
    response = doJSON(addon)
    l1l1lll_opy_ = response[l11ll1_opy_ (u"ࠨࡤࡲࡨࡾ࠭ࢺ")]
    l11l11_opy_  = l11ll1_opy_ (u"ࠩ࡞ࠫࢻ") + addon + l11ll1_opy_ (u"ࠪࡡࡡࡴࠧࢼ")
    l1l1ll1_opy_  =  file(l1l_opy_, l11ll1_opy_ (u"ࠫࡼ࠭ࢽ"))
    l1l1ll1_opy_.write(l11l11_opy_)
    l1ll1l_opy_ = []
    for channel in l1l1lll_opy_:
        category =  channel[l11ll1_opy_ (u"ࠬࡩࡡࡵࡧࡪࡳࡷࡿࠧࢾ")]
        l1l1l1ll1_opy_  = l11ll1_opy_ (u"࠭࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥ࠭ࢿ") + category + l11ll1_opy_ (u"ࠧࠡ࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠽ࠨࣀ")
        l1l111_opy_    =  channel[l11ll1_opy_ (u"ࠨࡶ࡬ࡸࡱ࡫ࠧࣁ")]
        l1lll_opy_ =  l1l1lllll_opy_(l1l111_opy_, category)
        if (l1lll_opy_ == l11ll1_opy_ (u"ࠩࡗ࡚ࠥ࠹ࠠࡔࡇࠪࣂ")) or (l1lll_opy_ == l11ll1_opy_ (u"ࠪࡘ࡛ࠦ࠴ࠡࡕࡈࠫࣃ")) or (l1lll_opy_ == l11ll1_opy_ (u"࡙ࠫ࡜ࠠ࠴ࠢࡇࡏࠬࣄ")) or (l1lll_opy_ == l11ll1_opy_ (u"࡚ࠬࡖࠡ࠶ࠣࡈࡐ࠭ࣅ")):
            stream   =  prefix + l1lll_opy_
        else:
            stream   =  prefix + l1l111_opy_
        l11ll_opy_  =  l1lll_opy_ + l11ll1_opy_ (u"࠭࠽ࠨࣆ") + stream
        if l1l1l1ll1_opy_ not in l1ll1l_opy_:
            l1ll1l_opy_.append(l1l1l1ll1_opy_)
        if l11ll_opy_ not in l1ll1l_opy_:
            l1ll1l_opy_.append(l11ll_opy_)
    for item in l1ll1l_opy_:
        l1l1ll1_opy_.write(l11ll1_opy_ (u"ࠢࠦࡵ࡟ࡲࠧࣇ") % item)
    l1l1ll1_opy_.close()
def l1l1111_opy_(Addon):
    l1l1ll1l1_opy_ = Addon.getAddonInfo(l11ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ࣈ"))
    l1l1ll1l1_opy_ = l1l1ll1l1_opy_.replace(l11ll1_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞ࠩࣉ"), l11ll1_opy_ (u"ࠪࠫ࣊")).replace(l11ll1_opy_ (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭࣋"), l11ll1_opy_ (u"ࠬ࠭࣌"))
    if l1l1ll1l1_opy_ == l11ll1_opy_ (u"࠭ࡓࡎࡃࡕࡘࡍ࡛ࡂࠨ࣍"):
        return l11ll1_opy_ (u"ࠧࡉࡆࡗ࡚࠿࠭࣎")
    if l1l1ll1l1_opy_ == l11ll1_opy_ (u"ࠨࡔࡸࡽࡦࠦࡉࡑࡖ࡙࣏ࠫ"):
        return l11ll1_opy_ (u"ࠩࡋࡈ࡙࡜࠲࠻࣐ࠩ")
def l1l1lllll_opy_(l1l111_opy_, category):
    if (l1l111_opy_ == l11ll1_opy_ (u"ࠪࡘ࡛࠹࣑ࠧ")) and (category == l11ll1_opy_ (u"ࠫࡘࡽࡥࡥ࡫ࡶ࡬ࠥࡍࡥ࡯ࡧࡵࡥࡱ࣒࠭")):
        return l11ll1_opy_ (u"࡚ࠬࡖࠡ࠵ࠣࡗࡊ࣓࠭")
    if (l1l111_opy_ == l11ll1_opy_ (u"࠭ࡔࡗ࠶ࠪࣔ")) and (category == l11ll1_opy_ (u"ࠧࡔࡹࡨࡨ࡮ࡹࡨࠡࡉࡨࡲࡪࡸࡡ࡭ࠩࣕ")):
        return l11ll1_opy_ (u"ࠨࡖ࡙ࠤ࠹ࠦࡓࡆࠩࣖ")
    if (l1l111_opy_ == l11ll1_opy_ (u"ࠩࡗ࡚࠸࠭ࣗ")) and (category == l11ll1_opy_ (u"ࠪࡈࡪࡴ࡭ࡢࡴ࡮ࠤࡌ࡫࡮ࡦࡴࡤࡰࠬࣘ")):
        return l11ll1_opy_ (u"࡙ࠫ࡜ࠠ࠴ࠢࡇࡏࠬࣙ")
    if (l1l111_opy_ == l11ll1_opy_ (u"࡚ࠬࡖ࠵ࠩࣚ")) and (category == l11ll1_opy_ (u"࠭ࡄࡦࡰࡰࡥࡷࡱࠠࡈࡧࡱࡩࡷࡧ࡬ࠨࣛ")):
        return l11ll1_opy_ (u"ࠧࡕࡘࠣ࠸ࠥࡊࡋࠨࣜ")
    return dixie.mapChannelName(l1l111_opy_)
def getURL(url):
    if url.startswith(l11ll1_opy_ (u"ࠨࡊࡇࡘ࡛ࡀࠧࣝ")):
        addon = l1l1ll11l_opy_
    else:
        addon = l1l1ll111_opy_
    Addon = xbmcaddon.Addon(id=addon)
    path  = Addon.getAddonInfo(l11ll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧࣞ"))
    sys.path.insert(0, path)
    import api
    api.login()
    channel   = url.split(l11ll1_opy_ (u"ࠪ࠾ࠬࣟ"), 1)[-1]
    l1l1lll1l_opy_ = l1l1llll1_opy_(channel, addon)
    response  = api.remote_call( l11ll1_opy_ (u"ࠦࡸࡺࡲࡦࡣࡰ࠳࡬࡫ࡴ࠯ࡲ࡫ࡴࠧ࣠") , { l11ll1_opy_ (u"ࠧࡺࠢ࣡") : l11ll1_opy_ (u"ࠨࡣࡩࡣࡱࡲࡪࡲࠢ࣢") , l11ll1_opy_ (u"ࠢࡪࡦࣣࠥ") : l1l1lll1l_opy_ } )
    return response[l11ll1_opy_ (u"ࠣࡤࡲࡨࡾࠨࣤ")][l11ll1_opy_ (u"ࠤࡸࡶࡱࠨࣥ")]
def l1l1llll1_opy_(channel, addon):
    PATH = l1l1ll1ll_opy_(addon)
    if os.path.exists(PATH):
        response = json.load(open(PATH))
    else:
        response = doJSON(addon)
    items = response[l11ll1_opy_ (u"ࠥࡦࡴࡪࡹࣦࠣ")]
    for item in items:
        if channel == l11ll1_opy_ (u"࡙ࠫ࡜ࠠ࠴ࠢࡖࡉࠬࣧ"):
            if (item[l11ll1_opy_ (u"ࠧࡩࡡࡵࡧࡪࡳࡷࡿࠢࣨ")] == l11ll1_opy_ (u"࠭ࡓࡸࡧࡧ࡭ࡸ࡮ࠠࡈࡧࡱࡩࡷࡧ࡬ࠨࣩ")) and (item[l11ll1_opy_ (u"ࠢࡵ࡫ࡷࡰࡪࠨ࣪")] == l11ll1_opy_ (u"ࠨࡖ࡙࠷ࠬ࣫")):
                return item[l11ll1_opy_ (u"ࠤ࡬ࡨࠧ࣬")]
        if channel == l11ll1_opy_ (u"ࠪࡘ࡛ࠦ࠳ࠡࡆࡎ࣭ࠫ"):
            if (item[l11ll1_opy_ (u"ࠦࡨࡧࡴࡦࡩࡲࡶࡾࠨ࣮")] == l11ll1_opy_ (u"ࠬࡊࡥ࡯࡯ࡤࡶࡰࠦࡇࡦࡰࡨࡶࡦࡲ࣯ࠧ")) and (item[l11ll1_opy_ (u"ࠨࡴࡪࡶ࡯ࡩࣰࠧ")] == l11ll1_opy_ (u"ࠧࡕࡘ࠶ࣱࠫ")):
                return item[l11ll1_opy_ (u"ࠣ࡫ࡧࣲࠦ")]
        if channel == l11ll1_opy_ (u"ࠩࡗ࡚ࠥ࠺ࠠࡔࡇࠪࣳ"):
            if (item[l11ll1_opy_ (u"ࠥࡧࡦࡺࡥࡨࡱࡵࡽࠧࣴ")] == l11ll1_opy_ (u"ࠫࡘࡽࡥࡥ࡫ࡶ࡬ࠥࡍࡥ࡯ࡧࡵࡥࡱ࠭ࣵ")) and (item[l11ll1_opy_ (u"ࠧࡺࡩࡵ࡮ࡨࣶࠦ")] == l11ll1_opy_ (u"࠭ࡔࡗ࠶ࠪࣷ")):
                return item[l11ll1_opy_ (u"ࠢࡪࡦࠥࣸ")]
        if channel == l11ll1_opy_ (u"ࠨࡖ࡙ࠤ࠹ࠦࡄࡌࣹࠩ"):
            if (item[l11ll1_opy_ (u"ࠤࡦࡥࡹ࡫ࡧࡰࡴࡼࣺࠦ")] == l11ll1_opy_ (u"ࠪࡈࡪࡴ࡭ࡢࡴ࡮ࠤࡌ࡫࡮ࡦࡴࡤࡰࠬࣻ")) and (item[l11ll1_opy_ (u"ࠦࡹ࡯ࡴ࡭ࡧࠥࣼ")] == l11ll1_opy_ (u"࡚ࠬࡖ࠵ࠩࣽ")):
                return item[l11ll1_opy_ (u"ࠨࡩࡥࠤࣾ")]
        if channel == item[l11ll1_opy_ (u"ࠢࡵ࡫ࡷࡰࡪࠨࣿ")]:
            return item[l11ll1_opy_ (u"ࠣ࡫ࡧࠦऀ")]
def doJSON(addon):
    try:
        Addon = xbmcaddon.Addon(id=addon)
        path  = Addon.getAddonInfo(l11ll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧँ"))
        sys.path.insert(0, path)
        import api
        PATH    = l1l1ll1ll_opy_(addon)
        content = api.remote_call( l11ll1_opy_ (u"ࠥࡧ࡭ࡧ࡮࡯ࡧ࡯ࡷ࠴ࡲࡩࡴࡶ࠱ࡴ࡭ࡶࠢं") , {l11ll1_opy_ (u"ࠫࡦ࠭ः"): l11ll1_opy_ (u"ࠬ࠶ࠧऄ"), l11ll1_opy_ (u"࠭ࡱࡶࡣ࡯࡭ࡹࡿࠧअ"): l11ll1_opy_ (u"ࠧࡢ࡮࡯ࠫआ")} )
        json.dump(content, open(PATH,l11ll1_opy_ (u"ࠨࡹࠪइ")), indent=3)
        return json.load(open(PATH))
    except:
        return l11ll1_opy_ (u"ࠩࡾࠦࡧࡵࡤࡺࠤ࠽ࠤࡠࢁࠢࡤࡣࡷࡩ࡬ࡵࡲࡺࠤ࠽ࠤࠧࠨࠬࠡࠤࡦࡹࡷࡸࡥ࡯ࡶࡢࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࠧ࠲ࠠࠣࡥࡸࡶࡷ࡫࡮ࡵࡡࡷ࡭ࡹࡲࡥࠣ࠼ࠣࠦࠧ࠲ࠠࠣࡰࡨࡼࡹࡥ࡬ࡰࡥࡤࡰࡤࡹࡴࡢࡴࡷࠦ࠿ࠦ࡮ࡶ࡮࡯࠰ࠥࠨࡴࡪࡶ࡯ࡩࠧࡀࠠࠣࠤ࠯ࠤࠧ࡬ࡡࡷࡱࡵ࡭ࡹ࡫ࠢ࠻ࠢࠥ࠴ࠧ࠲ࠠࠣࡥࡸࡶࡷ࡫࡮ࡵࡡ࡯ࡳࡨࡧ࡬ࡠࡵࡷࡥࡷࡺࠢ࠻ࠢࡱࡹࡱࡲࠬࠡࠤ࡬ࡨࠧࡀࠠࠣࠤ࠯ࠤࠧࡴࡥࡹࡶࡢࡸ࡮ࡺ࡬ࡦࠤ࠽ࠤࠧࠨࡽ࡞࠮ࠣࠦࡪࡸࡲࡰࡴࡢࡱࡪࡹࡳࡢࡩࡨࠦ࠿ࠦࠢࠣ࠮ࠣࠦࡪࡸࡲࡰࡴࡢࡧࡴࡪࡥࠣ࠼ࠣࠦ࠷࠶࠰ࠣ࠮ࠣࠦࡪࡸࡲࡰࡴࠥ࠾ࠥ࡬ࡡ࡭ࡵࡨࢁࠬई")
if __name__ == l11ll1_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬउ"):
    checkAddons()