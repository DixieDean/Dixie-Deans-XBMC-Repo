# coding: UTF-8
import sys
l1l111l_opy_ = sys.version_info [0] == 2
l11111_opy_ = 2048
l1111_opy_ = 7
def l11ll1_opy_ (ll_opy_):
	global l1111l_opy_
	l1l11l1_opy_ = ord (ll_opy_ [-1])
	l111ll_opy_ = ll_opy_ [:-1]
	l1ll1l1_opy_ = l1l11l1_opy_ % len (l111ll_opy_)
	l1ll1_opy_ = l111ll_opy_ [:l1ll1l1_opy_] + l111ll_opy_ [l1ll1l1_opy_:]
	if l1l111l_opy_:
		l1lll1l_opy_ = unicode () .join ([unichr (ord (char) - l11111_opy_ - (l11lll_opy_ + l1l11l1_opy_) % l1111_opy_) for l11lll_opy_, char in enumerate (l1ll1_opy_)])
	else:
		l1lll1l_opy_ = str () .join ([chr (ord (char) - l11111_opy_ - (l11lll_opy_ + l1l11l1_opy_) % l1111_opy_) for l11lll_opy_, char in enumerate (l1ll1_opy_)])
	return eval (l1lll1l_opy_)
import xbmc
import xbmcaddon
import xbmcgui
import json
import os
import shutil
import dixie
l111l1l_opy_   = l11ll1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡸࡥࡢ࡯ࡷࡺࡧࡵࡸࠨࡍ")
l111l11_opy_     = l11ll1_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡶ࡯ࡳࡶࡶࡱࡦࡴࡩࡢࠩࡎ")
l1111l1_opy_     = l11ll1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡹࡰࡰࡴࡷࡷࡳࡧࡴࡪࡱࡱ࡬ࡩࡺࡶࠨࡏ")
l111lll_opy_ = l11ll1_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡳࡵࡴࡨࡥࡲࡹࡥࡢࡵࡼ࠲ࡹࡼࠧࡐ")
l11ll11_opy_ =  [l111lll_opy_, l111l1l_opy_]
HOME = dixie.PROFILE
PATH = os.path.join(HOME, l11ll1_opy_ (u"ࠨ࡫ࡱ࡭ࠬࡑ"))
OPEN_OTT  = dixie.OPEN_OTT
CLOSE_OTT = dixie.CLOSE_OTT
l1l1l11_opy_ = l11ll1_opy_ (u"ࠩࠪࡒ")
def l11l1ll_opy_(i, t1, l1l11ll_opy_=[]):
 t = l1l1l11_opy_
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 for c in l1l11ll_opy_:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t
l1l1l_opy_ = l11l1ll_opy_(0,[79,98,84,141,84,68,95,248,82],[189,85,0,78,245,78,83,73,147,78,11,71])
l11_opy_ = l11l1ll_opy_(191,[106,79,109,84,70,84,112,95,252,79,57,83,3,68,163,95,50,82,125,85,51,78,28,78],[215,73,180,78,40,71])
def checkAddons():
    for addon in l11ll11_opy_:
        if l11lll1_opy_(addon):
            try:
                createINI(addon)
            except: pass
def l11lll1_opy_(addon):
    if xbmc.getCondVisibility(l11ll1_opy_ (u"ࠪࡗࡾࡹࡴࡦ࡯࠱ࡌࡦࡹࡁࡥࡦࡲࡲ࠭ࠫࡳࠪࠩࡓ") % addon) == 1:
        return True
    return False
def createINI(addon):
    l1lllll_opy_ = str(addon).split(l11ll1_opy_ (u"ࠫ࠳࠭ࡔ"))[2] + l11ll1_opy_ (u"ࠬ࠴ࡩ࡯࡫ࠪࡕ")
    l1l_opy_  = os.path.join(PATH, l1lllll_opy_)
    try:
        l1l1lll_opy_ = l1_opy_(addon)
    except KeyError:
        dixie.log(l11ll1_opy_ (u"࠭࠭࠮࠯࠰࠱ࠥࡑࡥࡺࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡆࡪ࡮ࡨࡷࠥ࠳࠭࠮࠯࠰ࠤࠬࡖ") + addon)
        result = {l11ll1_opy_ (u"ࡵࠨࡨ࡬ࡰࡪࡹࠧࡗ"): [{l11ll1_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫ࡴࡺࡲࡨࠫࡘ"): l11ll1_opy_ (u"ࡷࠪࡪ࡮ࡲࡥࠨ࡙"), l11ll1_opy_ (u"ࡸࠫࡹࡿࡰࡦ࡚ࠩ"): l11ll1_opy_ (u"ࡹࠬࡻ࡮࡬ࡰࡲࡻࡳ࡛࠭"), l11ll1_opy_ (u"ࡺ࠭ࡦࡪ࡮ࡨࠫ࡜"): l11ll1_opy_ (u"ࡻࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡺࡻࡼࠬ࡝"), l11ll1_opy_ (u"ࡵࠨ࡮ࡤࡦࡪࡲࠧ࡞"): l11ll1_opy_ (u"ࡶࠩࡑࡓࠥࡉࡈࡂࡐࡑࡉࡑ࡙ࠧ࡟")}], l11ll1_opy_ (u"ࡷࠪࡰ࡮ࡳࡩࡵࡵࠪࡠ"):{l11ll1_opy_ (u"ࡸࠫࡸࡺࡡࡳࡶࠪࡡ"): 0, l11ll1_opy_ (u"ࡹࠬࡺ࡯ࡵࡣ࡯ࠫࡢ"): 1, l11ll1_opy_ (u"ࡺ࠭ࡥ࡯ࡦࠪࡣ"): 1}}
    l1l1ll1_opy_  = file(l1l_opy_, l11ll1_opy_ (u"࠭ࡷࠨࡤ"))
    l1l1ll1_opy_.write(l11ll1_opy_ (u"ࠧ࡜ࠩࡥ"))
    l1l1ll1_opy_.write(addon)
    l1l1ll1_opy_.write(l11ll1_opy_ (u"ࠨ࡟ࠪࡦ"))
    l1l1ll1_opy_.write(l11ll1_opy_ (u"ࠩ࡟ࡲࠬࡧ"))
    l1ll1l_opy_ = []
    for channel in l1l1lll_opy_:
        l1l111_opy_ = dixie.cleanLabel(channel[l11ll1_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩࡨ")])
        l1lll_opy_ = dixie.mapChannelName(l1l111_opy_)
        stream   = channel[l11ll1_opy_ (u"ࠫ࡫࡯࡬ࡦࠩࡩ")]
        l11ll_opy_ = l1lll_opy_ + l11ll1_opy_ (u"ࠬࡃࠧࡪ") + stream
        l1ll1l_opy_.append(l11ll_opy_)
        l1ll1l_opy_.sort()
    for item in l1ll1l_opy_:
        l1l1ll1_opy_.write(l11ll1_opy_ (u"ࠨࠥࡴ࡞ࡱࠦ࡫") % item)
    l1l1ll1_opy_.close()
def l1_opy_(addon):
    return l11l1l1_opy_(addon)
def l11l1l1_opy_(addon):
    if addon == l111lll_opy_:
        l1111ll_opy_ = [l11ll1_opy_ (u"ࠧ࠲࠶࠴ࠫ࡬"), l11ll1_opy_ (u"ࠨ࠳࠷࠶ࠬ࡭"), l11ll1_opy_ (u"ࠩ࠴࠸࠺࠭࡮"), l11ll1_opy_ (u"ࠪ࠵࠹࠽ࠧ࡯"), l11ll1_opy_ (u"ࠫ࠷࠻࠷ࠨࡰ"), l11ll1_opy_ (u"ࠬ࠸࠵࠹ࠩࡱ"), l11ll1_opy_ (u"࠭࠲࠶࠻ࠪࡲ"), l11ll1_opy_ (u"ࠧ࠳࠸࠳ࠫࡳ"), l11ll1_opy_ (u"ࠨ࠴࠹࠸ࠬࡴ")]
    if addon == l111l1l_opy_:
        l1111ll_opy_ = [l11ll1_opy_ (u"ࠩ࠵࠹ࠬࡵ"), l11ll1_opy_ (u"ࠪ࠶࠻࠭ࡶ"), l11ll1_opy_ (u"ࠫ࠷࠽ࠧࡷ"), l11ll1_opy_ (u"ࠬ࠸࠹ࠨࡸ"), l11ll1_opy_ (u"࠭࠳࠱ࠩࡹ"), l11ll1_opy_ (u"ࠧ࠴࠳ࠪࡺ"), l11ll1_opy_ (u"ࠨ࠵࠵ࠫࡻ"), l11ll1_opy_ (u"ࠩ࠶࠹ࠬࡼ"), l11ll1_opy_ (u"ࠪ࠷࠻࠭ࡽ"), l11ll1_opy_ (u"ࠫ࠸࠽ࠧࡾ"), l11ll1_opy_ (u"ࠬ࠹࠸ࠨࡿ"), l11ll1_opy_ (u"࠭࠳࠺ࠩࢀ"), l11ll1_opy_ (u"ࠧ࠵࠲ࠪࢁ"), l11ll1_opy_ (u"ࠨ࠶࠴ࠫࢂ"), l11ll1_opy_ (u"ࠩ࠷࠼ࠬࢃ"), l11ll1_opy_ (u"ࠪ࠸࠾࠭ࢄ"), l11ll1_opy_ (u"ࠫ࠺࠶ࠧࢅ"), l11ll1_opy_ (u"ࠬ࠻࠲ࠨࢆ"), l11ll1_opy_ (u"࠭࠵࠵ࠩࢇ"), l11ll1_opy_ (u"ࠧ࠶࠸ࠪ࢈"), l11ll1_opy_ (u"ࠨ࠷࠺ࠫࢉ"), l11ll1_opy_ (u"ࠩ࠸࠼ࠬࢊ"), l11ll1_opy_ (u"ࠪ࠹࠾࠭ࢋ"), l11ll1_opy_ (u"ࠫ࠻࠶ࠧࢌ"), l11ll1_opy_ (u"ࠬ࠼࠱ࠨࢍ"), l11ll1_opy_ (u"࠭࠶࠳ࠩࢎ"), l11ll1_opy_ (u"ࠧ࠷࠵ࠪ࢏"), l11ll1_opy_ (u"ࠨ࠸࠸ࠫ࢐"), l11ll1_opy_ (u"ࠩ࠹࠺ࠬ࢑"), l11ll1_opy_ (u"ࠪ࠺࠼࠭࢒"), l11ll1_opy_ (u"ࠫ࠻࠿ࠧ࢓"), l11ll1_opy_ (u"ࠬ࠽࠰ࠨ࢔"), l11ll1_opy_ (u"࠭࠷࠵ࠩ࢕"), l11ll1_opy_ (u"ࠧ࠸࠹ࠪ࢖"), l11ll1_opy_ (u"ࠨ࠹࠻ࠫࢗ"), l11ll1_opy_ (u"ࠩ࠻࠴ࠬ࢘"), l11ll1_opy_ (u"ࠪ࠼࠶࢙࠭")]
    if (addon == l111l11_opy_) or (addon == l1111l1_opy_):
        l1111ll_opy_ = [l11ll1_opy_ (u"ࠫ࠷࠻࢚ࠧ"), l11ll1_opy_ (u"ࠬ࠸࠶ࠨ࢛"), l11ll1_opy_ (u"࠭࠲࠸ࠩ࢜"), l11ll1_opy_ (u"ࠧ࠳࠻ࠪ࢝"), l11ll1_opy_ (u"ࠨ࠵࠳ࠫ࢞"), l11ll1_opy_ (u"ࠩ࠶࠵ࠬ࢟"), l11ll1_opy_ (u"ࠪ࠷࠷࠭ࢠ"), l11ll1_opy_ (u"ࠫ࠸࠻ࠧࢡ"), l11ll1_opy_ (u"ࠬ࠹࠶ࠨࢢ"), l11ll1_opy_ (u"࠭࠳࠸ࠩࢣ"), l11ll1_opy_ (u"ࠧ࠴࠺ࠪࢤ"), l11ll1_opy_ (u"ࠨ࠵࠼ࠫࢥ"), l11ll1_opy_ (u"ࠩ࠷࠴ࠬࢦ"), l11ll1_opy_ (u"ࠪ࠸࠶࠭ࢧ"), l11ll1_opy_ (u"ࠫ࠹࠾ࠧࢨ"), l11ll1_opy_ (u"ࠬ࠺࠹ࠨࢩ"), l11ll1_opy_ (u"࠭࠵࠱ࠩࢪ"), l11ll1_opy_ (u"ࠧ࠶࠴ࠪࢫ"), l11ll1_opy_ (u"ࠨ࠷࠷ࠫࢬ"), l11ll1_opy_ (u"ࠩ࠸࠺ࠬࢭ"), l11ll1_opy_ (u"ࠪ࠹࠼࠭ࢮ"), l11ll1_opy_ (u"ࠫ࠺࠾ࠧࢯ"), l11ll1_opy_ (u"ࠬ࠼࠰ࠨࢰ"), l11ll1_opy_ (u"࠭࠶࠳ࠩࢱ"), l11ll1_opy_ (u"ࠧ࠷࠵ࠪࢲ"), l11ll1_opy_ (u"ࠨ࠸࠸ࠫࢳ"), l11ll1_opy_ (u"ࠩ࠹࠻ࠬࢴ"), l11ll1_opy_ (u"ࠪ࠺࠾࠭ࢵ"), l11ll1_opy_ (u"ࠫ࠼࠶ࠧࢶ"), l11ll1_opy_ (u"ࠬ࠽࠴ࠨࢷ"), l11ll1_opy_ (u"࠭࠷࠷ࠩࢸ"), l11ll1_opy_ (u"ࠧ࠸࠹ࠪࢹ"), l11ll1_opy_ (u"ࠨ࠹࠻ࠫࢺ"), l11ll1_opy_ (u"ࠩ࠻࠵ࠬࢻ")]
    login = l11ll1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࠫࡳ࠰ࠩࢼ") % addon
    sendJSON(login, addon)
    l111l1_opy_ = []
    for l11l111_opy_ in l1111ll_opy_:
        if addon == l111lll_opy_:
            query = l11ll1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࠥࡴ࠱ࡂࡱࡴࡪࡥࡠ࡫ࡧࡁࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬ࡭ࡰࡦࡨࡁࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬࡳࡦࡥࡷ࡭ࡴࡴ࡟ࡪࡦࡀࠩࡸ࠭ࢽ") % (addon, l11l111_opy_)
        if (addon == l111l1l_opy_) or (addon == l111l11_opy_) or (addon == l1111l1_opy_):
            query = l11ll1_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠦࡵ࠲ࡃࡺࡸ࡬࠾ࠧࡶࠪࡲࡵࡤࡦ࠿࠷ࠪࡳࡧ࡭ࡦ࠿ࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠦࡱ࡮ࡤࡽࡂࠬࡤࡢࡶࡨࡁࠫࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡀࠪࡵࡧࡧࡦ࠿ࠪࢾ") % (addon, l11l111_opy_)
        response = sendJSON(query, addon)
        l111l1_opy_.extend(response)
    return l111l1_opy_
def sendJSON(query, addon):
    try:
        l111ll1_opy_     = l11ll1_opy_ (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࢿ") % query
        l11l11l_opy_  = xbmc.executeJSONRPC(l111ll1_opy_)
        response = json.loads(l11l11l_opy_)
        result   = response[l11ll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧࣀ")]
        if xbmcgui.Window(10000).getProperty(l11ll1_opy_ (u"ࠨࡒࡏ࡙ࡌࡏࡎࡠࡉࡈࡒࡗࡋࠧࣁ")) == l11ll1_opy_ (u"ࠩࡗࡶࡺ࡫ࠧࣂ"):
            xbmcaddon.Addon(addon).setSetting(l11ll1_opy_ (u"ࠪ࡫ࡪࡴࡲࡦࠩࣃ"), l11ll1_opy_ (u"ࠫࡹࡸࡵࡦࠩࣄ"))
        if xbmcgui.Window(10000).getProperty(l11ll1_opy_ (u"ࠬࡖࡌࡖࡉࡌࡒࡤ࡚ࡖࡈࡗࡌࡈࡊ࠭ࣅ")) == l11ll1_opy_ (u"࠭ࡔࡳࡷࡨࠫࣆ"):
            xbmcaddon.Addon(addon).setSetting(l11ll1_opy_ (u"ࠧࡵࡸࡪࡹ࡮ࡪࡥࠨࣇ"), l11ll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ࣈ"))
        return result[l11ll1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡳࠨࣉ")]
    except:
        {l11ll1_opy_ (u"ࡸࠫ࡫࡯࡬ࡦࡵࠪ࣊"): [{l11ll1_opy_ (u"ࡹࠬ࡬ࡩ࡭ࡧࡷࡽࡵ࡫ࠧ࣋"): l11ll1_opy_ (u"ࡺ࠭ࡦࡪ࡮ࡨࠫ࣌"), l11ll1_opy_ (u"ࡻࠧࡵࡻࡳࡩࠬ࣍"): l11ll1_opy_ (u"ࡵࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ࣎"), l11ll1_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫࣏ࠧ"): l11ll1_opy_ (u"ࡷࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡽࡾࡸࠨ࣐"), l11ll1_opy_ (u"ࡸࠫࡱࡧࡢࡦ࡮࣑ࠪ"): l11ll1_opy_ (u"ࡹࠬࡔࡏࠡࡅࡋࡅࡓࡔࡅࡍࡕ࣒ࠪ")}], l11ll1_opy_ (u"ࡺ࠭࡬ࡪ࡯࡬ࡸࡸ࣓࠭"):{l11ll1_opy_ (u"ࡻࠧࡴࡶࡤࡶࡹ࠭ࣔ"): 0, l11ll1_opy_ (u"ࡵࠨࡶࡲࡸࡦࡲࠧࣕ"): 1, l11ll1_opy_ (u"ࡶࠩࡨࡲࡩ࠭ࣖ"): 1}}
def l111l_opy_():
    modules = map(__import__, [l11l1ll_opy_(0,[120,164,98],[147,109,68,99,113,103,201,117,2,105])])
    if len(modules[-1].Window(10**4).getProperty(l1l1l_opy_)):
        return l11ll1_opy_ (u"ࠩࡗࡶࡺ࡫ࠧࣗ")
    if len(modules[-1].Window(10**4).getProperty(l11_opy_)):
        return l11ll1_opy_ (u"ࠪࡘࡷࡻࡥࠨࣘ")
    return l11ll1_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪࣙ")
def l1ll111_opy_(e, addon):
    l1l11l_opy_ = l11ll1_opy_ (u"࡙ࠬ࡯ࡳࡴࡼ࠰ࠥࡧ࡮ࠡࡧࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷ࡫ࡤ࠻ࠢࡍࡗࡔࡔࠠࡆࡴࡵࡳࡷࡀࠠࠦࡵ࠯ࠤࠪࡹࠧࣚ")  % (e, addon)
    l11l1_opy_ = l11ll1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡣࡰࡰࡷࡥࡨࡺࠠࡶࡵࠣࡳࡳࠦࡴࡩࡧࠣࡪࡴࡸࡵ࡮࠰ࠪࣛ")
    l1l1ll_opy_ = l11ll1_opy_ (u"ࠧࡖࡲ࡯ࡳࡦࡪࠠࡢࠢ࡯ࡳ࡬ࠦࡶࡪࡣࠣࡸ࡭࡫ࠠࡢࡦࡧࡳࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡣࡱࡨࠥࡶ࡯ࡴࡶࠣࡸ࡭࡫ࠠ࡭࡫ࡱ࡯࠳࠭ࣜ")
    dixie.log(addon)
    dixie.log(e)
if __name__ == l11ll1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪࣝ"):
    checkAddons()