# coding: UTF-8
import sys
l1l11ll1_opy_ = sys.version_info [0] == 2
l1llll1l_opy_ = 2048
l1l1ll1l_opy_ = 7
def l11ll_opy_ (l1l11l_opy_):
	global l111111_opy_
	l1ll1lll_opy_ = ord (l1l11l_opy_ [-1])
	l1l1l1ll_opy_ = l1l11l_opy_ [:-1]
	l11l11l_opy_ = l1ll1lll_opy_ % len (l1l1l1ll_opy_)
	l11ll1_opy_ = l1l1l1ll_opy_ [:l11l11l_opy_] + l1l1l1ll_opy_ [l11l11l_opy_:]
	if l1l11ll1_opy_:
		l1llll_opy_ = unicode () .join ([unichr (ord (char) - l1llll1l_opy_ - (l111l1l_opy_ + l1ll1lll_opy_) % l1l1ll1l_opy_) for l111l1l_opy_, char in enumerate (l11ll1_opy_)])
	else:
		l1llll_opy_ = str () .join ([chr (ord (char) - l1llll1l_opy_ - (l111l1l_opy_ + l1ll1lll_opy_) % l1l1ll1l_opy_) for l111l1l_opy_, char in enumerate (l11ll1_opy_)])
	return eval (l1llll_opy_)
import xbmc
import xbmcaddon
import json
import os
import dixie
l1lll1lll1_opy_ = l11ll_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡸ࡯ࡰࡶ࡬ࡴࡹࡼࠧ઩")
l1llll1l1l_opy_   = l11ll_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡘࡵࡴࡨࡥࡲࡏࡐࡕࡘࠪપ")
l1lll1llll_opy_  = l11ll_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡶࡵࡩࡦࡳ࠭ࡤࡱࡧࡩࡸ࠭ફ")
l1llll11ll_opy_     = l11ll_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡱࡷࡸࡦࡲࡰࡩࡣࠪબ")
l1ll1l11_opy_ = [l1llll1l1l_opy_, l1lll1llll_opy_, l1llll11ll_opy_]
HOME = dixie.PROFILE
PATH = os.path.join(HOME, l11ll_opy_ (u"ࠪ࡭ࡳ࡯ࠧભ"))
OPEN_OTT  = dixie.OPEN_OTT
CLOSE_OTT = dixie.CLOSE_OTT
l1ll1l1ll_opy_ = l11ll_opy_ (u"ࠫࠬમ")
def l1ll11l1l_opy_(i, t1, l1ll1l1l1_opy_=[]):
 t = l1ll1l1ll_opy_
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 for c in l1ll1l1l1_opy_:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t
l11l11ll_opy_ = l1ll11l1l_opy_(0,[79,98,84,141,84,68,95,248,82],[189,85,0,78,245,78,83,73,147,78,11,71])
l11ll1ll_opy_ = l1ll11l1l_opy_(191,[106,79,109,84,70,84,112,95,252,79,57,83,3,68,163,95,50,82,125,85,51,78,28,78],[215,73,180,78,40,71])
def checkAddons():
    for addon in l1ll1l11_opy_:
        if l1ll11ll1_opy_(addon):
            createINI(addon)
def l1ll11ll1_opy_(addon):
    if xbmc.getCondVisibility(l11ll_opy_ (u"࡙ࠬࡹࡴࡶࡨࡱ࠳ࡎࡡࡴࡃࡧࡨࡴࡴࠨࠦࡵࠬࠫય") % addon) == 1:
        return True
    return False
def createINI(addon):
    l1llll11l_opy_ = str(addon).rsplit(l11ll_opy_ (u"࠭࠮ࠨર"), 1)[1] + l11ll_opy_ (u"ࠧ࠯࡫ࡱ࡭ࠬ઱")
    l1111111_opy_  = os.path.join(PATH, l1llll11l_opy_)
    try:
        l11l111_opy_ = l1l11l1l_opy_(addon)
    except KeyError:
        dixie.log(l11ll_opy_ (u"ࠨ࠯࠰࠱࠲࠳ࠠࡌࡧࡼࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡈ࡬ࡰࡪࡹࠠ࠮࠯࠰࠱࠲ࠦࠧલ") + addon)
        result = {l11ll_opy_ (u"ࡷࠪࡪ࡮ࡲࡥࡴࠩળ"): [{l11ll_opy_ (u"ࡸࠫ࡫࡯࡬ࡦࡶࡼࡴࡪ࠭઴"): l11ll_opy_ (u"ࡹࠬ࡬ࡩ࡭ࡧࠪવ"), l11ll_opy_ (u"ࡺ࠭ࡴࡺࡲࡨࠫશ"): l11ll_opy_ (u"ࡻࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨષ"), l11ll_opy_ (u"ࡵࠨࡨ࡬ࡰࡪ࠭સ"): l11ll_opy_ (u"ࡶࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡼࡽࡾࠧહ"), l11ll_opy_ (u"ࡷࠪࡰࡦࡨࡥ࡭ࠩ઺"): l11ll_opy_ (u"ࡸࠫࡓࡕࠠࡄࡊࡄࡒࡓࡋࡌࡔࠩ઻")}], l11ll_opy_ (u"ࡹࠬࡲࡩ࡮࡫ࡷࡷ઼ࠬ"):{l11ll_opy_ (u"ࡺ࠭ࡳࡵࡣࡵࡸࠬઽ"): 0, l11ll_opy_ (u"ࡻࠧࡵࡱࡷࡥࡱ࠭ા"): 1, l11ll_opy_ (u"ࡵࠨࡧࡱࡨࠬિ"): 1}}
    l11111l1_opy_  = l11ll_opy_ (u"ࠨ࡝ࠪી") + addon + l11ll_opy_ (u"ࠩࡠࡠࡳ࠭ુ")
    l11l1l1l_opy_  = file(l1111111_opy_, l11ll_opy_ (u"ࠪࡻࠬૂ"))
    l11l1l1l_opy_.write(l11111l1_opy_)
    l1lllll1l_opy_ = []
    try:
        for channel in l11l111_opy_:
            l1l1111_opy_ = l11l11l1_opy_(addon, channel)
            l11l1ll1_opy_ = dixie.mapChannelName(l1l1111_opy_)
            stream   = channel[l11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࠩૃ")]
            l11l111l_opy_ = l11l1ll1_opy_ + l11ll_opy_ (u"ࠬࡃࠧૄ") + stream
            l1lllll1l_opy_.append(l11l111l_opy_)
            l1lllll1l_opy_.sort()
        for item in l1lllll1l_opy_:
            l11l1l1l_opy_.write(l11ll_opy_ (u"ࠨࠥࡴ࡞ࡱࠦૅ") % item)
        l11l1l1l_opy_.close()
    except Exception as e:
        l1lll111l_opy_(e, addon)
        return {l11ll_opy_ (u"ࡵࠨࡨ࡬ࡰࡪࡹࠧ૆"): [{l11ll_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫ࡴࡺࡲࡨࠫે"): l11ll_opy_ (u"ࡷࠪࡪ࡮ࡲࡥࠨૈ"), l11ll_opy_ (u"ࡸࠫࡹࡿࡰࡦࠩૉ"): l11ll_opy_ (u"ࡹࠬࡻ࡮࡬ࡰࡲࡻࡳ࠭૊"), l11ll_opy_ (u"ࡺ࠭ࡦࡪ࡮ࡨࠫો"): l11ll_opy_ (u"ࡻࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡺࡻࡼࠬૌ"), l11ll_opy_ (u"ࡵࠨ࡮ࡤࡦࡪࡲ્ࠧ"): l11ll_opy_ (u"ࡶࠩࡑࡓࠥࡉࡈࡂࡐࡑࡉࡑ࡙ࠧ૎")}], l11ll_opy_ (u"ࡷࠪࡰ࡮ࡳࡩࡵࡵࠪ૏"):{l11ll_opy_ (u"ࡸࠫࡸࡺࡡࡳࡶࠪૐ"): 0, l11ll_opy_ (u"ࡹࠬࡺ࡯ࡵࡣ࡯ࠫ૑"): 1, l11ll_opy_ (u"ࡺ࠭ࡥ࡯ࡦࠪ૒"): 1}}
def l11l11l1_opy_(addon, file):
    l1lllll_opy_ = file[l11ll_opy_ (u"࠭࡬ࡢࡤࡨࡰࠬ૓")].split(l11ll_opy_ (u"ࠧ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ૔"), 1)[0]
    l1lllll_opy_ = dixie.cleanLabel(l1lllll_opy_)
    return dixie.cleanPrefix(l1lllll_opy_)
def l1l11l1l_opy_(addon):
    login = l11ll_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࠩࡸ࠵ࠧ૕") % addon
    sendJSON(login, addon)
    if (addon == l1lll1llll_opy_) or (addon == l1llll11ll_opy_):
        return l11lll1l_opy_(addon)
    if addon == l1llll1l1l_opy_:
        l1111ll_opy_ = [l11ll_opy_ (u"ࠩ࠶ࠫ૖"), l11ll_opy_ (u"ࠪ࠸ࠬ૗"), l11ll_opy_ (u"ࠫ࠻࠭૘"), l11ll_opy_ (u"ࠬ࠽ࠧ૙"), l11ll_opy_ (u"࠭࠸ࠨ૚"), l11ll_opy_ (u"ࠧ࠲࠳ࠪ૛"), l11ll_opy_ (u"ࠨ࠳࠵ࠫ૜"), l11ll_opy_ (u"ࠩ࠴࠸ࠬ૝"), l11ll_opy_ (u"ࠪ࠵࠺࠭૞"), l11ll_opy_ (u"ࠫ࠸࠹ࠧ૟"), l11ll_opy_ (u"ࠬ࠿࠱ࠨૠ"), l11ll_opy_ (u"࠭࠹࠳ࠩૡ")]
    l11111l_opy_ = []
    for l1111l_opy_ in l1111ll_opy_:
        if (addon == l1llll1l1l_opy_) or (addon == l1llll1l11_opy_):
            query = l11ll_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠨࡷ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃࡳࡵࡴࡨࡥࡲࡥࡶࡪࡦࡨࡳࠫ࡫ࡸࡵࡴࡤࠪࡵࡧࡧࡦࠨࡳࡰࡴࡺࠦࡵࡪࡸࡱࡧࡴࡡࡪ࡮ࡀࠪࡹ࡯ࡴ࡭ࡧࡀࠪࡺࡸ࡬࠾ࠧࡶࠫૢ") % (addon, l1111l_opy_)
        response = sendJSON(query, addon)
        l11111l_opy_.extend(response)
    return l11111l_opy_
def l11lll1l_opy_(addon):
    query = l1llll1ll1_opy_(addon)
    return sendJSON(query, addon)
def l1llll1ll1_opy_(addon):
    Addon = xbmcaddon.Addon(addon)
    l1lllll111_opy_, l1llll1111_opy_  = l1llll1lll_opy_(Addon, addon)
    l1llll11l1_opy_, l1lllll11l_opy_ = l1lll1ll1l_opy_(Addon, addon)
    return l1llll111l_opy_(addon, l1lllll111_opy_, l1llll1111_opy_, l1llll11l1_opy_, l1lllll11l_opy_)
def l1llll1lll_opy_(Addon, addon):
    if addon == l1llll11ll_opy_:
        l1lllll111_opy_  = l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡱࡷࡸࡹࡼ࠮ࡨࡣࠪૣ")
        l1llll1111_opy_ = l11ll_opy_ (u"ࠩ࠵࠴࠾࠻ࠧ૤")
        return l1lllll111_opy_, l1llll1111_opy_
    l1lllll111_opy_  = Addon.getSetting(l11ll_opy_ (u"ࠪࡰࡪ࡮ࡥ࡬ࡻ࡯࡫ࠬ૥"))
    l1llll1111_opy_ = Addon.getSetting(l11ll_opy_ (u"ࠫࡵࡵࡲࡥ࡫ࡱࡹࡲࡨࡥࡳࠩ૦"))
    return l1lllll111_opy_, l1llll1111_opy_
def l1lll1ll1l_opy_(Addon, addon):
    if addon == l1llll11ll_opy_:
        l1llll11l1_opy_ = Addon.getSetting(l11ll_opy_ (u"࡛ࠬࡳࡦࡴࡱࡥࡲ࡫ࠧ૧"))
        l1lllll11l_opy_ = Addon.getSetting(l11ll_opy_ (u"࠭ࡐࡢࡵࡶࡻࡴࡸࡤࠨ૨"))
        return l1llll11l1_opy_, l1lllll11l_opy_
    l1llll11l1_opy_ = Addon.getSetting(l11ll_opy_ (u"ࠧ࡬ࡣࡶࡹࡹࡧࡪࡢࡰ࡬ࡱ࡮࠭૩"))
    l1lllll11l_opy_ = Addon.getSetting(l11ll_opy_ (u"ࠨࡵࡤࡰࡦࡹ࡯࡯ࡣࠪ૪"))
    return l1llll11l1_opy_, l1lllll11l_opy_
def l1llll111l_opy_(addon, l1lllll111_opy_, l1llll1111_opy_, l1llll11l1_opy_, l1lllll11l_opy_):
    action  = l11ll_opy_ (u"ࠩࡶࡸࡷ࡫ࡡ࡮ࡡࡹ࡭ࡩ࡫࡯ࠨ૫")
    l1l11ll_opy_  = l11ll_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴࠭૬")
    l1l11ll_opy_ +=  addon
    l1l11ll_opy_ += l11ll_opy_ (u"ࠫ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃࠥࡴࠨࡨࡼࡹࡸࡡࠧࡲࡤ࡫ࡪࠬࡰ࡭ࡱࡷࠪࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲ࠽ࠧࡶ࡬ࡸࡱ࡫࠽ࡂ࡮࡯ࠪࡺࡸ࡬࠾ࠩ૭") % (action)
    params  =  l1lllll111_opy_
    params += l11ll_opy_ (u"ࠬࡀࠧ૮") + l1llll1111_opy_
    params += l11ll_opy_ (u"࠭࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄࡻࡳࡦࡴࡱࡥࡲ࡫࠽ࠨ૯")
    params +=  l1llll11l1_opy_
    params += l11ll_opy_ (u"ࠧࠧࡲࡤࡷࡸࡽ࡯ࡳࡦࡀࠫ૰")
    params +=  l1lllll11l_opy_
    params += l11ll_opy_ (u"ࠨࠨࡷࡽࡵ࡫࠽ࡨࡧࡷࡣࡱ࡯ࡶࡦࡡࡶࡸࡷ࡫ࡡ࡮ࡵࠩࡧࡦࡺ࡟ࡪࡦࡀ࠴ࠬ૱")
    import urllib
    params = urllib.quote_plus(params)
    url = l1l11ll_opy_ + params
    return url
def login(addon):
    login = l11ll_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠪࡹ࠯ࠨ૲") % addon
    sendJSON(login, addon)
def sendJSON(query, addon):
    l111l11_opy_     = l11ll_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࠫࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭૳") % query
    l1111_opy_  = xbmc.executeJSONRPC(l111l11_opy_)
    response = json.loads(l1111_opy_)
    result   = response[l11ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ૴")]
    return result[l11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫ૵")]
def l1111ll1_opy_():
    modules = map(__import__, [l1ll11l1l_opy_(0,[120,164,98],[147,109,68,99,113,103,201,117,2,105])])
    if len(modules[-1].Window(10**4).getProperty(l11l11ll_opy_)):
        return l11ll_opy_ (u"࠭ࡔࡳࡷࡨࠫ૶")
    if len(modules[-1].Window(10**4).getProperty(l11ll1ll_opy_)):
        return l11ll_opy_ (u"ࠧࡕࡴࡸࡩࠬ૷")
    return l11ll_opy_ (u"ࠨࡈࡤࡰࡸ࡫ࠧ૸")
def l1lll111l_opy_(e, addon):
    l1111lll_opy_ = l11ll_opy_ (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡨࡨ࠿ࠦࡊࡔࡑࡑࠤࡊࡸࡲࡰࡴ࠽ࠤࠪࡹࠬࠡࠧࡶࠫૹ")  % (e, addon)
    l11l1111_opy_ = l11ll_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡧࡴࡴࡴࡢࡥࡷࠤࡺࡹࠠࡰࡰࠣࡸ࡭࡫ࠠࡧࡱࡵࡹࡲ࠴ࠧૺ")
    l111l11l_opy_ = l11ll_opy_ (u"࡚ࠫࡶ࡬ࡰࡣࡧࠤࡦࠦ࡬ࡰࡩࠣࡺ࡮ࡧࠠࡵࡪࡨࠤࡦࡪࡤࡰࡰࠣࡷࡪࡺࡴࡪࡰࡪࡷࠥࡧ࡮ࡥࠢࡳࡳࡸࡺࠠࡵࡪࡨࠤࡱ࡯࡮࡬࠰ࠪૻ")
    dixie.log(addon)
    dixie.log(e)
if __name__ == l11ll_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧૼ"):
    checkAddons()