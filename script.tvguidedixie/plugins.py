# coding: UTF-8
import sys
l1l11ll1_opy_ = sys.version_info [0] == 2
l11111l_opy_ = 2048
l1ll111l_opy_ = 7
def l1l1l_opy_ (l11ll1_opy_):
	global l1111ll_opy_
	l1lll1ll_opy_ = ord (l11ll1_opy_ [-1])
	l1l1l11l_opy_ = l11ll1_opy_ [:-1]
	l11ll11_opy_ = l1lll1ll_opy_ % len (l1l1l11l_opy_)
	l111l1_opy_ = l1l1l11l_opy_ [:l11ll11_opy_] + l1l1l11l_opy_ [l11ll11_opy_:]
	if l1l11ll1_opy_:
		l1llll_opy_ = unicode () .join ([unichr (ord (char) - l11111l_opy_ - (l1lll_opy_ + l1lll1ll_opy_) % l1ll111l_opy_) for l1lll_opy_, char in enumerate (l111l1_opy_)])
	else:
		l1llll_opy_ = str () .join ([chr (ord (char) - l11111l_opy_ - (l1lll_opy_ + l1lll1ll_opy_) % l1ll111l_opy_) for l1lll_opy_, char in enumerate (l111l1_opy_)])
	return eval (l1llll_opy_)
import xbmc
import xbmcaddon
import xbmcgui
import json
import os
import shutil
import dixie
l11l11111_opy_     = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡴࡴࡷࠩਏ")
l111ll1ll_opy_  = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡷ࡭࡫ࡳࡸࡻ࠭ਐ")
l11l1l11l_opy_     = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡹࡷࡱࠧ਑")
locked  = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡮ࡲࡧࡰ࡫ࡤࡵࡸࠪ਒")
l111l1ll1_opy_      = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡸࡰࡹ࡯࡭ࡢࡶࡨࡱࡦࡴࡩࡢࠩਓ")
l111ll11l_opy_    = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡰ࡮ࡻࡸ࠯ࡶࡹࠫਔ")
l111lll1l_opy_     = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡉࡉࡓࡱࡱࡵࡸࡸ࠭ਕ")
l11l1l111_opy_  = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡸࡥࡣࡱࡲࡸࠬਖ")
l111llll1_opy_     = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡣ࡭ࡷ࡬ࡴࡹࡼࠧਗ")
l11l11lll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡺ࠹࡫ࡸࡱࡣࡷࡷ࠳ࡩ࡯࡮ࠩਘ")
l1lll111_opy_ = [l11l11111_opy_, locked, l111ll11l_opy_, l111ll1ll_opy_, l11l11lll_opy_]
HOME = dixie.PROFILE
PATH = os.path.join(HOME, l1l1l_opy_ (u"ࠩ࡬ࡲ࡮࠭ਙ"))
OPEN_OTT  = dixie.OPEN_OTT
CLOSE_OTT = dixie.CLOSE_OTT
l1l11ll_opy_ = l1l1l_opy_ (u"ࠪࠫਚ")
def l11lll_opy_(i, t1, l1l11l_opy_=[]):
 t = l1l11ll_opy_
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 for c in l1l11l_opy_:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t
l11_opy_ = l11lll_opy_(0,[79,98,84,141,84,68,95,248,82],[189,85,0,78,245,78,83,73,147,78,11,71])
l11l1l_opy_ = l11lll_opy_(191,[106,79,109,84,70,84,112,95,252,79,57,83,3,68,163,95,50,82,125,85,51,78,28,78],[215,73,180,78,40,71])
def checkAddons():
    for addon in l1lll111_opy_:
        if l1l11lll_opy_(addon):
            try:
                createINI(addon)
            except: pass
def l1l11lll_opy_(addon):
    if xbmc.getCondVisibility(l1l1l_opy_ (u"ࠫࡘࡿࡳࡵࡧࡰ࠲ࡍࡧࡳࡂࡦࡧࡳࡳ࠮ࠥࡴࠫࠪਛ") % addon) == 1:
        return True
    return False
def createINI(addon):
    l11ll1l1_opy_ = str(addon).split(l1l1l_opy_ (u"ࠬ࠴ࠧਜ"))[2] + l1l1l_opy_ (u"࠭࠮ࡪࡰ࡬ࠫਝ")
    l11llll_opy_  = os.path.join(PATH, l11ll1l1_opy_)
    try:
        l11l1ll_opy_ = l1ll1lll_opy_(addon)
    except KeyError:
        dixie.log(l1l1l_opy_ (u"ࠧ࠮࠯࠰࠱࠲ࠦࡋࡦࡻࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡇ࡫࡯ࡩࡸࠦ࠭࠮࠯࠰࠱ࠥ࠭ਞ") + addon)
        result = {l1l1l_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫ࡳࠨਟ"): [{l1l1l_opy_ (u"ࡷࠪࡪ࡮ࡲࡥࡵࡻࡳࡩࠬਠ"): l1l1l_opy_ (u"ࡸࠫ࡫࡯࡬ࡦࠩਡ"), l1l1l_opy_ (u"ࡹࠬࡺࡹࡱࡧࠪਢ"): l1l1l_opy_ (u"ࡺ࠭ࡵ࡯࡭ࡱࡳࡼࡴࠧਣ"), l1l1l_opy_ (u"ࡻࠧࡧ࡫࡯ࡩࠬਤ"): l1l1l_opy_ (u"ࡵࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡻࡼࡽ࠭ਥ"), l1l1l_opy_ (u"ࡶࠩ࡯ࡥࡧ࡫࡬ࠨਦ"): l1l1l_opy_ (u"ࡷࠪࡒࡔࠦࡃࡉࡃࡑࡒࡊࡒࡓࠨਧ")}], l1l1l_opy_ (u"ࡸࠫࡱ࡯࡭ࡪࡶࡶࠫਨ"):{l1l1l_opy_ (u"ࡹࠬࡹࡴࡢࡴࡷࠫ਩"): 0, l1l1l_opy_ (u"ࡺ࠭ࡴࡰࡶࡤࡰࠬਪ"): 1, l1l1l_opy_ (u"ࡻࠧࡦࡰࡧࠫਫ"): 1}}
    l1l1l1_opy_  = l1l1l_opy_ (u"ࠧ࡜ࠩਬ") + addon + l1l1l_opy_ (u"ࠨ࡟࡟ࡲࠬਭ")
    l1ll11ll_opy_  =  file(l11llll_opy_, l1l1l_opy_ (u"ࠩࡺࠫਮ"))
    l1ll11ll_opy_.write(l1l1l1_opy_)
    l1l11l11_opy_ = []
    for channel in l11l1ll_opy_:
        l1l1_opy_ = dixie.cleanLabel(channel[l1l1l_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩਯ")])
        l1l1111_opy_   = dixie.cleanPrefix(l1l1_opy_)
        l111ll_opy_ = dixie.mapChannelName(l1l1111_opy_)
        stream   = channel[l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࠩਰ")]
        l11111_opy_ = l111ll_opy_ + l1l1l_opy_ (u"ࠬࡃࠧ਱") + stream
        l1l11l11_opy_.append(l11111_opy_)
        l1l11l11_opy_.sort()
    for item in l1l11l11_opy_:
        l1ll11ll_opy_.write(l1l1l_opy_ (u"ࠨࠥࡴ࡞ࡱࠦਲ") % item)
    l1ll11ll_opy_.close()
def l1ll1lll_opy_(addon):
    if (addon == l11l11111_opy_) or (addon == l111ll1ll_opy_):
        if xbmcaddon.Addon(addon).getSetting(l1l1l_opy_ (u"ࠧࡨࡧࡱࡶࡪ࠭ਲ਼")) == l1l1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭਴"):
            xbmcaddon.Addon(addon).setSetting(l1l1l_opy_ (u"ࠩࡪࡩࡳࡸࡥࠨਵ"), l1l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩਸ਼"))
            xbmcgui.Window(10000).setProperty(l1l1l_opy_ (u"ࠫࡕࡒࡕࡈࡋࡑࡣࡌࡋࡎࡓࡇࠪ਷"), l1l1l_opy_ (u"࡚ࠬࡲࡶࡧࠪਸ"))
        if xbmcaddon.Addon(addon).getSetting(l1l1l_opy_ (u"࠭ࡴࡷࡩࡸ࡭ࡩ࡫ࠧਹ")) == l1l1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ਺"):
            xbmcaddon.Addon(addon).setSetting(l1l1l_opy_ (u"ࠨࡶࡹ࡫ࡺ࡯ࡤࡦࠩ਻"), l1l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ਼"))
            xbmcgui.Window(10000).setProperty(l1l1l_opy_ (u"ࠪࡔࡑ࡛ࡇࡊࡐࡢࡘ࡛ࡍࡕࡊࡆࡈࠫ਽"), l1l1l_opy_ (u"࡙ࠫࡸࡵࡦࠩਾ"))
        l111ll1l1_opy_  = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠨਿ") + addon
        l11l11ll1_opy_ =  l11l1l1ll_opy_(addon)
        query   =  l111ll1l1_opy_ + l11l11ll1_opy_
        return sendJSON(query, addon)
    return l11l111l1_opy_(addon)
def l11l111l1_opy_(addon):
    if addon == l11l11lll_opy_:
        l11l111ll_opy_ = [l1l1l_opy_ (u"࠭࠱࠷࠳ࠪੀ"), l1l1l_opy_ (u"ࠧ࠲࠸࠳ࠫੁ"), l1l1l_opy_ (u"ࠨ࠴࠶࠺ࠬੂ"), l1l1l_opy_ (u"ࠩ࠵࠸࠷࠭੃"), l1l1l_opy_ (u"ࠪ࠵࠺࠾ࠧ੄"), l1l1l_opy_ (u"ࠫ࠶࠻࠹ࠨ੅")]
    if addon == l111ll11l_opy_:
        l11l111ll_opy_ = [l1l1l_opy_ (u"ࠬ࠻ࠧ੆"), l1l1l_opy_ (u"࠭࠱࠱࠸ࠪੇ"), l1l1l_opy_ (u"ࠧ࠵ࠩੈ"), l1l1l_opy_ (u"ࠨ࠴࠹࠷ࠬ੉"), l1l1l_opy_ (u"ࠩ࠴࠷࠷࠭੊")]
    if addon == locked:
        l11l111ll_opy_ = [l1l1l_opy_ (u"ࠪ࠷࠵࠭ੋ"), l1l1l_opy_ (u"ࠫ࠸࠷ࠧੌ"), l1l1l_opy_ (u"ࠬ࠹࠲ࠨ੍"), l1l1l_opy_ (u"࠭࠳࠴ࠩ੎"), l1l1l_opy_ (u"ࠧ࠴࠶ࠪ੏"), l1l1l_opy_ (u"ࠨ࠵࠸ࠫ੐"), l1l1l_opy_ (u"ࠩ࠶࠼ࠬੑ"), l1l1l_opy_ (u"ࠪ࠸࠵࠭੒"), l1l1l_opy_ (u"ࠫ࠹࠷ࠧ੓"), l1l1l_opy_ (u"ࠬ࠺࠵ࠨ੔"), l1l1l_opy_ (u"࠭࠴࠸ࠩ੕"), l1l1l_opy_ (u"ࠧ࠵࠻ࠪ੖"), l1l1l_opy_ (u"ࠨ࠷࠵ࠫ੗")]
    if addon == l111l1ll1_opy_:
        l11l111ll_opy_ = [l1l1l_opy_ (u"ࠩ࠵࠹ࠬ੘"), l1l1l_opy_ (u"ࠪ࠶࠻࠭ਖ਼"), l1l1l_opy_ (u"ࠫ࠷࠽ࠧਗ਼"), l1l1l_opy_ (u"ࠬ࠸࠹ࠨਜ਼"), l1l1l_opy_ (u"࠭࠳࠱ࠩੜ"), l1l1l_opy_ (u"ࠧ࠴࠳ࠪ੝"), l1l1l_opy_ (u"ࠨ࠵࠵ࠫਫ਼"), l1l1l_opy_ (u"ࠩ࠶࠹ࠬ੟"), l1l1l_opy_ (u"ࠪ࠷࠻࠭੠"), l1l1l_opy_ (u"ࠫ࠸࠽ࠧ੡"), l1l1l_opy_ (u"ࠬ࠹࠸ࠨ੢"), l1l1l_opy_ (u"࠭࠳࠺ࠩ੣"), l1l1l_opy_ (u"ࠧ࠵࠲ࠪ੤"), l1l1l_opy_ (u"ࠨ࠶࠴ࠫ੥"), l1l1l_opy_ (u"ࠩ࠷࠼ࠬ੦"), l1l1l_opy_ (u"ࠪ࠸࠾࠭੧"), l1l1l_opy_ (u"ࠫ࠺࠶ࠧ੨"), l1l1l_opy_ (u"ࠬ࠻࠲ࠨ੩"), l1l1l_opy_ (u"࠭࠵࠵ࠩ੪"), l1l1l_opy_ (u"ࠧ࠶࠸ࠪ੫"), l1l1l_opy_ (u"ࠨ࠷࠺ࠫ੬"), l1l1l_opy_ (u"ࠩ࠸࠼ࠬ੭"), l1l1l_opy_ (u"ࠪ࠹࠾࠭੮"), l1l1l_opy_ (u"ࠫ࠻࠶ࠧ੯"), l1l1l_opy_ (u"ࠬ࠼࠱ࠨੰ"), l1l1l_opy_ (u"࠭࠶࠳ࠩੱ"), l1l1l_opy_ (u"ࠧ࠷࠵ࠪੲ"), l1l1l_opy_ (u"ࠨ࠸࠸ࠫੳ"), l1l1l_opy_ (u"ࠩ࠹࠺ࠬੴ"), l1l1l_opy_ (u"ࠪ࠺࠼࠭ੵ"), l1l1l_opy_ (u"ࠫ࠻࠿ࠧ੶"), l1l1l_opy_ (u"ࠬ࠽࠰ࠨ੷"), l1l1l_opy_ (u"࠭࠷࠵ࠩ੸"), l1l1l_opy_ (u"ࠧ࠸࠹ࠪ੹"), l1l1l_opy_ (u"ࠨ࠹࠻ࠫ੺"), l1l1l_opy_ (u"ࠩ࠻࠴ࠬ੻"), l1l1l_opy_ (u"ࠪ࠼࠶࠭੼")]
    login = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࠥࡴ࠱ࠪ੽") % addon
    sendJSON(login, addon)
    l111l11_opy_ = []
    for l11l1l1l1_opy_ in l11l111ll_opy_:
        if (addon == l11l11lll_opy_) or (addon == l111ll11l_opy_):
            query = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠦࡵ࠲ࡃࡲࡵࡤࡦࡡ࡬ࡨࡂࡩࡨࡢࡰࡱࡩࡱࡹࠦ࡮ࡱࡧࡩࡂࡩࡨࡢࡰࡱࡩࡱࡹࠦࡴࡧࡦࡸ࡮ࡵ࡮ࡠ࡫ࡧࡁࠪࡹࠧ੾") % (addon, l11l1l1l1_opy_)
        if (addon == locked) or (addon == l111l1ll1_opy_):
            query = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠧࡶ࠳ࡄࡻࡲ࡭࠿ࠨࡷࠫࡳ࡯ࡥࡧࡀ࠸ࠫࡴࡡ࡮ࡧࡀࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠧࡲ࡯ࡥࡾࡃࠦࡥࡣࡷࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡶࡡࡨࡧࡀࠫ੿") % (addon, l11l1l1l1_opy_)
        response = sendJSON(query, addon)
        l111l11_opy_.extend(response)
    return l111l11_opy_
def sendJSON(query, addon):
    l111lll_opy_     = l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࠨࡷࠧࢃࠬࠡࠤ࡬ࡨࠧࡀࠠ࠲ࡿࠪ઀") % query
    l111l_opy_  = xbmc.executeJSONRPC(l111lll_opy_)
    response = json.loads(l111l_opy_)
    result   = response[l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨઁ")]
    if xbmcgui.Window(10000).getProperty(l1l1l_opy_ (u"ࠩࡓࡐ࡚ࡍࡉࡏࡡࡊࡉࡓࡘࡅࠨં")) == l1l1l_opy_ (u"ࠪࡘࡷࡻࡥࠨઃ"):
        xbmcaddon.Addon(addon).setSetting(l1l1l_opy_ (u"ࠫ࡬࡫࡮ࡳࡧࠪ઄"), l1l1l_opy_ (u"ࠬࡺࡲࡶࡧࠪઅ"))
    if xbmcgui.Window(10000).getProperty(l1l1l_opy_ (u"࠭ࡐࡍࡗࡊࡍࡓࡥࡔࡗࡉࡘࡍࡉࡋࠧઆ")) == l1l1l_opy_ (u"ࠧࡕࡴࡸࡩࠬઇ"):
        xbmcaddon.Addon(addon).setSetting(l1l1l_opy_ (u"ࠨࡶࡹ࡫ࡺ࡯ࡤࡦࠩઈ"), l1l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧઉ"))
    return result[l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡴࠩઊ")]
def l11l1l1ll_opy_(addon):
    if (addon == l11l11111_opy_) or (addon == l111ll1ll_opy_):
        return l1l1l_opy_ (u"ࠫ࠴ࡅࡣࡢࡶࡀ࠱࠷ࠬࡤࡢࡶࡨࠪࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠨࡨࡲࡩࡊࡡࡵࡧࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠦ࡮ࡱࡧࡩࡂ࠸ࠦ࡯ࡣࡰࡩࡂࡓࡹࠦ࠴࠳ࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷࠫࡸࡥࡤࡱࡵࡨࡳࡧ࡭ࡦࠨࡶࡸࡦࡸࡴࡅࡣࡷࡩࠫࡻࡲ࡭࠿ࡸࡶࡱ࠭ઋ")
    return l1l1l_opy_ (u"ࠬ࠭ઌ")
def l1l1l1ll_opy_():
    modules = map(__import__, [l11lll_opy_(0,[120,164,98],[147,109,68,99,113,103,201,117,2,105])])
    if len(modules[-1].Window(10**4).getProperty(l11_opy_)):
        return l1l1l_opy_ (u"࠭ࡔࡳࡷࡨࠫઍ")
    if len(modules[-1].Window(10**4).getProperty(l11l1l_opy_)):
        return l1l1l_opy_ (u"ࠧࡕࡴࡸࡩࠬ઎")
    return l1l1l_opy_ (u"ࠨࡈࡤࡰࡸ࡫ࠧએ")
def l11lll1l_opy_(e, addon):
    l1l1ll11_opy_ = l1l1l_opy_ (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡨࡨ࠿ࠦࡊࡔࡑࡑࠤࡊࡸࡲࡰࡴ࠽ࠤࠪࡹࠬࠡࠧࡶࠫઐ")  % (e, addon)
    l11l11l_opy_ = l1l1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡧࡴࡴࡴࡢࡥࡷࠤࡺࡹࠠࡰࡰࠣࡸ࡭࡫ࠠࡧࡱࡵࡹࡲ࠴ࠧઑ")
    l1l1lll1_opy_ = l1l1l_opy_ (u"࡚ࠫࡶ࡬ࡰࡣࡧࠤࡦࠦ࡬ࡰࡩࠣࡺ࡮ࡧࠠࡵࡪࡨࠤࡦࡪࡤࡰࡰࠣࡷࡪࡺࡴࡪࡰࡪࡷࠥࡧ࡮ࡥࠢࡳࡳࡸࡺࠠࡵࡪࡨࠤࡱ࡯࡮࡬࠰ࠪ઒")
    dixie.log(addon)
    dixie.log(e)
def getPluginInfo(streamurl, kodiID=False):
    try:
        if streamurl.split(dixie.CLOSE_OTT)[1].isdigit():
            l111l1l1l_opy_   = l1l1l_opy_ (u"ࠬࡑ࡯ࡥ࡫ࠣࡔ࡛ࡘࠧઓ")
            l111ll111_opy_ = os.path.join(dixie.RESOURCES, l1l1l_opy_ (u"࠭࡫ࡰࡦ࡬࠱ࡵࡼࡲ࠯ࡲࡱ࡫ࠬઔ"))
            return l111l1l1l_opy_, l111ll111_opy_
    except:
        pass
    try:
        url = streamurl.split(dixie.CLOSE_OTT)[1]
        if url.startswith(l1l1l_opy_ (u"ࠧࡳࡶࡰࡴࠬક")) or url.startswith(l1l1l_opy_ (u"ࠨࡴࡷࡱࡵ࡫ࠧખ")) or url.startswith(l1l1l_opy_ (u"ࠩࡵࡸࡸࡶࠧગ")) or url.startswith(l1l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࠨઘ")):
            l111l1l1l_opy_   = l1l1l_opy_ (u"ࠫࡲ࠹ࡵࠡࡒ࡯ࡥࡾࡲࡩࡴࡶࠪઙ")
            l111ll111_opy_ = os.path.join(dixie.RESOURCES, l1l1l_opy_ (u"ࠬ࡯ࡰࡵࡸ࠰ࡴࡱࡧࡹ࡭࡫ࡶࡸ࠳ࡶ࡮ࡨࠩચ"))
            return l111l1l1l_opy_, l111ll111_opy_
    except:
        pass
    if streamurl.startswith(l1l1l_opy_ (u"࠭ࡰࡷࡴ࠽࠳࠴࠭છ")):
        l111l1l1l_opy_   = l1l1l_opy_ (u"ࠧࡌࡱࡧ࡭ࠥࡖࡖࡓࠩજ")
        l111ll111_opy_ = os.path.join(dixie.RESOURCES, l1l1l_opy_ (u"ࠨ࡭ࡲࡨ࡮࠳ࡰࡷࡴ࠱ࡴࡳ࡭ࠧઝ"))
        return l111l1l1l_opy_, l111ll111_opy_
    if streamurl.startswith(dixie.OPEN_OTT):
        l111lllll_opy_ = streamurl.split(l1l1l_opy_ (u"ࠩࡠࡓ࡙࡚࡟ࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪઞ"), 1)[-1].split(l1l1l_opy_ (u"ࠪ࠳ࠬટ"), 1)[0]
    if l1l1l_opy_ (u"ࠫࡢࡕࡔࡕࡡࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠬઠ") in streamurl:
        l111lllll_opy_ = streamurl.split(l1l1l_opy_ (u"ࠬࡣࡏࡕࡖࡢࡴࡱࡻࡧࡪࡰ࠽࠳࠴࠭ડ"), 1)[-1].split(l1l1l_opy_ (u"࠭࠯ࠨઢ"), 1)[0]
    if streamurl.startswith(l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪણ")):
        l111lllll_opy_ = streamurl.split(l1l1l_opy_ (u"ࠨ࠱࠲ࠫત"), 1)[-1].split(l1l1l_opy_ (u"ࠩ࠲ࠫથ"), 1)[0]
    if l1l1l_opy_ (u"ࠪࡋࡘࡖࡒࡕࡕ࠽ࠫદ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡫࡮ࢀ࡭ࡰࡵࡳࡳࡷࡺࡳࠨધ")
    if l1l1l_opy_ (u"ࠬࡥ࡟ࡔࡈࡢࡣࠬન") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡰࡳࡱࡪࡶࡦࡳ࠮ࡴࡷࡳࡩࡷ࠴ࡦࡢࡸࡲࡹࡷ࡯ࡴࡦࡵࠪ઩")
    if l1l1l_opy_ (u"ࠧࡂࡐࡒ࡚ࡆࡀࠧપ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡯ࡣࡷ࡬ࡴࡧ࡮ࡰࡸࡤࠫફ")
    if l1l1l_opy_ (u"࡙ࠩࡍࡕ࡙ࡓ࠻ࠩબ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡙ࡍࡕ࡙ࡵࡱࡧࡵࡗࡹࡸࡥࡢ࡯ࡶࡘ࡛࠭ભ")
    if l1l1l_opy_ (u"ࠫࡑࡏࡍ࠳࠼ࠪમ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡑ࡯࡭ࡪࡶ࡯ࡩࡸࡹࡖ࠴ࠩય")
    if l1l1l_opy_ (u"࠭ࡎࡂࡖࡋ࠾ࠬર") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡎࡢࡶ࡫ࡳ࠳ࡏࡐࡕࡘࠪ઱")
    if l1l1l_opy_ (u"ࠨࡐࡌࡇࡊࡀࠧલ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡰࡤࡸ࡭ࡵࡳࡶࡤࡶ࡭ࡨ࡫ࠧળ")
    if l1l1l_opy_ (u"ࠪࡔࡗࡋࡍ࠻ࠩ઴") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡴࡷ࡫࡭ࡪࡷࡰ࡭ࡵࡺࡶࠨવ")
    if l1l1l_opy_ (u"ࠬࡍࡉ࡛࠼ࠪશ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡭ࡩࡻ࡯ࡲࡸࡻ࠭ષ")
    if l1l1l_opy_ (u"ࠧࡈࡇࡋ࠾ࠬસ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡨࡧ࡫ࡳࡸࡺࡩ࡯ࡩࠪહ")
    if l1l1l_opy_ (u"ࠩࡐࡘ࡝ࡏࡅ࠻ࠩ઺") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡰࡥࡹࡸࡩࡹ࡫ࡵࡩࡱࡧ࡮ࡥࠩ઻")
    if l1l1l_opy_ (u"࡙ࠫ࡜ࡋ࠻઼ࠩ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡹࡼ࡫ࡪࡰࡪࡷࠬઽ")
    if l1l1l_opy_ (u"࠭ࡘࡕࡅ࠽ࠫા") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸࡵࡴࡨࡥࡲ࠳ࡣࡰࡦࡨࡷࠬિ")
    if l1l1l_opy_ (u"ࠨࡕࡆࡘ࡛ࡀࠧી") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡦࡸࡻ࠭ુ")
    if l1l1l_opy_ (u"ࠪࡗ࡚ࡖ࠺ࠨૂ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡸࡥࡢ࡯ࡶࡹࡵࡸࡥ࡮ࡧ࠵ࠫૃ")
    if l1l1l_opy_ (u"࡛ࠬࡋࡕ࠼ࠪૄ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡻ࡫ࡵࡷࡵ࡯ࠬૅ")
    if l1l1l_opy_ (u"ࠧࡍࡋࡐࡍ࡙ࡀࠧ૆") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡍ࡫ࡰ࡭ࡹࡲࡥࡴࡵࡌࡔ࡙࡜ࠧે")
    if l1l1l_opy_ (u"ࠩࡉࡅࡇࡀࠧૈ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡩࡥࡧ࡮࡯ࡴࡶ࡬ࡲ࡬࠭ૉ")
    if l1l1l_opy_ (u"ࠫࡆࡉࡅ࠻ࠩ૊") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡦࡩࡥࡵࡸࠪો")
    if l1l1l_opy_ (u"࠭ࡈࡐࡔࡌ࡞࠿࠭ૌ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡨࡰࡴ࡬ࡾࡴࡴࡩࡱࡶࡹ્ࠫ")
    if l1l1l_opy_ (u"ࠨࡔࡒࡓ࡙࠸࠺ࠨ૎") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡴࡲࡳࡹࡏࡐࡕࡘࠪ૏")
    if l1l1l_opy_ (u"ࠪࡑࡊࡍࡁ࠻ࠩૐ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡱࡪ࡭ࡡࡪࡲࡷࡺࠬ૑")
    if l1l1l_opy_ (u"ࠬ࡜ࡄࡓࡖ࡙࠾ࠬ૒") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡜ࡁࡅࡇࡕࠫ૓")
    if l1l1l_opy_ (u"ࠧࡉࡆࡗ࡚࠿࠭૔") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴ࡯ࡤࡶࡹ࡮ࡵࡣࠩ૕")
    if l1l1l_opy_ (u"ࠩࡋࡈ࡙࡜࠲࠻ࠩ૖") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡹࡾࡧ࠲ࠨ૗")
    if l1l1l_opy_ (u"ࠫࡍࡊࡔࡗ࠵࠽ࠫ૘") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡷࡻࡹࡢ࠴ࠪ૙")
    if l1l1l_opy_ (u"࠭ࡈࡅࡖ࡙࠸࠿࠭૚") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸ࡭ࠩ૛")
    if l1l1l_opy_ (u"ࠨࡋࡓࡐࡆ࡟࠺ࠨ૜") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡤࡥࡧ࡮ࡶ࡬ࡢࡻࡨࡶࠬ૝")
    if l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚࠴࠽ࠫ૞") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡭ࡵࡲࡡࡺࡧࡵࡻࡼࡽࠧ૟")
    if l1l1l_opy_ (u"ࠬࡏࡐࡍࡃ࡜ࡖ࠿࠭ૠ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡯ࡰ࡭ࡣࡼࡩࡷࡽࡷࡸࠩૡ")
    if l1l1l_opy_ (u"ࠧࡊࡒࡏࡅ࡞ࡏࡔࡗ࠼ࠪૢ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡶࡹࠫૣ")
    if l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙ࡅ࠼ࠪ૤") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡧࡩࡽ࠭૥")
    if l1l1l_opy_ (u"ࠫࡏࡏࡎ࡙࠴࠽ࠫ૦") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡯࡯࡮ࡹࡶࡹ࠶ࠬ૧")
    if l1l1l_opy_ (u"࠭ࡍࡂࡖࡖ࠾ࠬ૨") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡍࡢࡶࡶࡆࡺ࡯࡬ࡥࡵࡌࡔ࡙࡜ࠧ૩")
    if l1l1l_opy_ (u"ࠨࡔࡒࡓ࡙ࡀࠧ૪") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡴࡲࡳࡹ࡯ࡰࡵࡸࠪ૫")
    if l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡔࡅ࠾ࠬ૬") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡪࡨ࡯ࡰࡶࠪ૭")
    if l1l1l_opy_ (u"ࠬࡏࡐࡍࡃ࡜ࡇࡑ࡛࠺ࠨ૮") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡩ࡬ࡶ࡫ࡳࡸࡻ࠭૯")
    if l1l1l_opy_ (u"ࠧࡊࡒࡗࡗࠬ૰") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡲࡷࡺࡸࡻࡢࡴࠩ૱")
    if l1l1l_opy_ (u"ࠩࡏࡍ࡛ࡋࡔࡗ࠼ࠪ૲") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡯࡭ࡻ࡫࡭ࡪࡺࠪ૳")
    if l1l1l_opy_ (u"ࠫࡊࡔࡄ࠻ࠩ૴") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡊࡴࡤ࡭ࡧࡶࡷࠬ૵")
    if l1l1l_opy_ (u"࠭ࡆࡍࡃ࠽ࠫ૶") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡆ࡭ࡣࡺࡰࡪࡹࡳࡕࡸࠪ૷")
    if l1l1l_opy_ (u"ࠨࡏࡄ࡜ࡎࡀࠧ૸") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡯ࡤࡼ࡮ࡽࡥࡣࡶࡹࠫૹ")
    if l1l1l_opy_ (u"ࠪࡊࡑࡇࡓ࠻ࠩૺ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡊࡱࡧࡷ࡭ࡧࡶࡷ࡙ࡼࠧૻ")
    if l1l1l_opy_ (u"࡙ࠬࡐࡓࡏ࠽ࠫૼ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡙ࡵࡱࡴࡨࡱࡦࡩࡹࡕࡘࠪ૽")
    if l1l1l_opy_ (u"ࠧࡎࡅࡎࡘ࡛ࡀࠧ૾") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡮ࡥ࡮ࡸࡻ࠳ࡰ࡭ࡷࡶࠫ૿")
    if l1l1l_opy_ (u"ࠩࡗ࡛ࡎ࡙ࡔ࠻ࠩ଀") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡷࡻ࡮ࡹࡴࡦࡦࡷࡺࠬଁ")
    if l1l1l_opy_ (u"ࠫࡕࡘࡅࡔࡖ࠽ࠫଂ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡵࡹࡡࡥࡦࡲࡲࠬଃ")
    if l1l1l_opy_ (u"࠭ࡂࡍࡍࡌ࠾ࠬ଄") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡂ࡭ࡣࡦ࡯ࡎࡩࡥࡕࡘࠪଅ")
    if l1l1l_opy_ (u"ࠨࡈࡕࡉࡊࡀࠧଆ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡨࡵࡩࡪࡼࡩࡦࡹࠪଇ")
    if l1l1l_opy_ (u"ࠪࡹࡵࡴࡰ࠻ࠩଈ") in streamurl:
        l111lllll_opy_ = l1l1l_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷ࠲࡭ࡪࡨࡰ࡯ࡨࡶࡺࡴ࠮ࡷ࡫ࡨࡻࠬଉ")
    return l11l11l1l_opy_(l111lllll_opy_, kodiID)
def l11l11l1l_opy_(l111lllll_opy_, kodiID):
    l111l1l1l_opy_     = l1l1l_opy_ (u"ࠬ࠭ଊ")
    l111ll111_opy_   = l1l1l_opy_ (u"࠭ࠧଋ")
    try:
        l11l1ll11_opy_ = xbmcaddon.Addon(l111lllll_opy_).getAddonInfo(l1l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬଌ"))
        l111l1l1l_opy_    = dixie.cleanLabel(l11l1ll11_opy_)
        l111ll111_opy_  = xbmcaddon.Addon(l111lllll_opy_).getAddonInfo(l1l1l_opy_ (u"ࠨ࡫ࡦࡳࡳ࠭଍"))
        if kodiID:
            l111l1lll_opy_ = xbmcaddon.Addon(l111lllll_opy_).getAddonInfo(l1l1l_opy_ (u"ࠩ࡬ࡨࠬ଎"))
            return l111l1l1l_opy_, l111l1lll_opy_
        return l111l1l1l_opy_, l111ll111_opy_
    except:
        l111l1l1l_opy_   = l1l1l_opy_ (u"࡙ࠪࡳࡱ࡮ࡰࡹࡱࠤࡘࡵࡵࡳࡥࡨࠫଏ")
        l111ll111_opy_ =  dixie.ICON
        return l111l1l1l_opy_, l111ll111_opy_
    return l111l1l1l_opy_, l111ll111_opy_
def selectStream(url, channel):
    l111l1l11_opy_ = url.split(l1l1l_opy_ (u"ࠫࢁ࠭ଐ"))
    if len(l111l1l11_opy_) == 0:
        return None
    options, l1l11l1l_opy_ = getOptions(l111l1l11_opy_, channel)
    if not dixie.IGNORESTRM:
        if len(l111l1l11_opy_) == 1:
            return l1l11l1l_opy_[0]
    import selectDialog
    l11l1111l_opy_ = selectDialog.select(l1l1l_opy_ (u"࡙ࠬࡥ࡭ࡧࡦࡸࠥࡧࠠࡴࡶࡵࡩࡦࡳࠧ଑"), options)
    if l11l1111l_opy_ < 0:
        raise Exception(l1l1l_opy_ (u"࠭ࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡆࡥࡳࡩࡥ࡭ࠩ଒"))
    return l1l11l1l_opy_[l11l1111l_opy_]
def getOptions(l111l1l11_opy_, channel, addmore=True):
    options = []
    l1l11l1l_opy_    = []
    for index, stream in enumerate(l111l1l11_opy_):
        l111l1l1l_opy_ = getPluginInfo(stream)
        l1ll1ll_opy_ = l1l1l_opy_ (u"ࠧࠨଓ")
        l111lll11_opy_  = l111l1l1l_opy_[1]
        if stream.startswith(OPEN_OTT):
            l11l11l11_opy_ = stream.split(CLOSE_OTT)[0].replace(OPEN_OTT, l1l1l_opy_ (u"ࠨࠩଔ"))
            l1ll1ll_opy_  = l1ll1ll_opy_ + l11l11l11_opy_
            stream = stream.split(CLOSE_OTT)[1].replace(OPEN_OTT, l1l1l_opy_ (u"ࠩࠪକ"))
        else:
            l1ll1ll_opy_  = l1ll1ll_opy_ + channel
        options.append([l1ll1ll_opy_, index, l111lll11_opy_])
        l1l11l1l_opy_.append(stream)
    if addmore:
        options.append([l1l1l_opy_ (u"ࠪࡅࡩࡪࠠ࡮ࡱࡵࡩ࠳࠴࠮ࠨଖ"), index + 1, dixie.ICON])
        l1l11l1l_opy_.append(l1l1l_opy_ (u"ࠫࡦࡪࡤࡎࡱࡵࡩࠬଗ"))
    return options, l1l11l1l_opy_
if __name__ == l1l1l_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧଘ"):
    checkAddons()