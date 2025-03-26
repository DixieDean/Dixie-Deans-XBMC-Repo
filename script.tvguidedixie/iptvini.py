# coding: UTF-8
import sys
l1_opy_ = sys.version_info [0] == 2
l11_opy_ = 2048
l11ll_opy_ = 7
def l1lll_opy_ (ll_opy_):
	global l1l_opy_
	l1l1_opy_ = ord (ll_opy_ [-1])
	l1l1l_opy_ = ll_opy_ [:-1]
	l1l11_opy_ = l1l1_opy_ % len (l1l1l_opy_)
	l11l_opy_ = l1l1l_opy_ [:l1l11_opy_] + l1l1l_opy_ [l1l11_opy_:]
	if l1_opy_:
		l1ll_opy_ = unicode () .join ([unichr (ord (char) - l11_opy_ - (l111_opy_ + l1l1_opy_) % l11ll_opy_) for l111_opy_, char in enumerate (l11l_opy_)])
	else:
		l1ll_opy_ = str () .join ([chr (ord (char) - l11_opy_ - (l111_opy_ + l1l1_opy_) % l11ll_opy_) for l111_opy_, char in enumerate (l11l_opy_)])
	return eval (l1ll_opy_)
import xbmc
import xbmcaddon
import xbmcgui
import json
import os
import requests
import dixie
import mapping
ADDON    = dixie.ADDON
l11l1l_opy_ = dixie.PROFILE
l1ll1ll_opy_  = os.path.join(l11l1l_opy_, l1lll_opy_ (u"ࠧࡪࡰ࡬ࠫࠃ"))
l11ll1_opy_    = os.path.join(l1ll1ll_opy_, l1lll_opy_ (u"ࠨ࡯ࡤࡴࡵ࡯࡮ࡨࡵ࠱࡮ࡸࡵ࡮ࠨࠄ"))
l1ll11_opy_   = os.path.join(l1ll1ll_opy_, l1lll_opy_ (u"ࠩࡰࡥࡵࡹ࠮࡫ࡵࡲࡲࠬࠅ"))
LABELFILE  = os.path.join(l1ll1ll_opy_, l1lll_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࡵ࠱࡮ࡸࡵ࡮ࠨࠆ"))
l1l1lll_opy_ = os.path.join(l1ll1ll_opy_, l1lll_opy_ (u"ࠫࡵࡸࡥࡧ࡫ࡻࡩࡸ࠴ࡪࡴࡱࡱࠫࠇ"))
l11lll_opy_  = json.load(open(l11ll1_opy_))
l111l1_opy_      = json.load(open(l1ll11_opy_))
labelmaps = json.load(open(LABELFILE))
l111ll_opy_  = json.load(open(l1l1lll_opy_))
l1l1l1l_opy_  = l1lll_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡋࡲࡡࡸ࡮ࡨࡷࡸ࡚ࡶࠨࠈ")
l1l11l1_opy_    = [l1l1l1l_opy_]
def checkAddons():
    for addon in l1l11l1_opy_:
        if l1l11ll_opy_(addon):
            try: createINI(addon)
            except: continue
def l1l11ll_opy_(addon):
    if xbmc.getCondVisibility(l1lll_opy_ (u"࠭ࡓࡺࡵࡷࡩࡲ࠴ࡈࡢࡵࡄࡨࡩࡵ࡮ࠩࠧࡶ࠭ࠬࠉ") % addon) == 1:
        return True
    return False
def createINI(addon):
    l1l1ll_opy_  = str(addon).split(l1lll_opy_ (u"ࠧ࠯ࠩࠊ"))[2] + l1lll_opy_ (u"ࠨ࠰࡬ࡲ࡮࠭ࠋ")
    l1lllll_opy_   = os.path.join(l1ll1ll_opy_, l1l1ll_opy_)
    l1ll1l_opy_ = []
    response = l11l1_opy_(addon)
    for item in response:
        channel = item[l1lll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧࠌ")]
        l1ll1l_opy_.append(channel)
    dixie.log(l1lll_opy_ (u"ࠪࡁࡂࡃ࠽࠾ࠢࡆ࡬ࡦࡴ࡮ࡦ࡮ࡶࠤࡂࡃ࠽࠾࠿ࠪࠍ"))
    dixie.log(l1ll1l_opy_)
    l11111_opy_  = l1lll_opy_ (u"ࠫࡠ࠭ࠎ") + addon + l1lll_opy_ (u"ࠬࡣ࡜࡯ࠩࠏ")
    l1ll111_opy_  =  file(l1lllll_opy_, l1lll_opy_ (u"࠭ࡷࠨࠐ"))
    l1ll111_opy_.write(l11111_opy_)
    l1llll1_opy_ = []
    for channel in l1ll1l_opy_:
        l1l111_opy_ = l1l11l_opy_(addon)
        l1111_opy_  = channel
        l1lll11_opy_  = l1lll1l_opy_(addon, l1111_opy_)
        l1lll1_opy_  = l1l1ll1_opy_(addon, l111ll_opy_, labelmaps, l11lll_opy_, l111l1_opy_, l1111_opy_)
        stream  = l1l111_opy_ + l1lll11_opy_
        l1l1l1_opy_ = l1lll1_opy_  + l1lll_opy_ (u"ࠧ࠾ࠩࠑ") + stream
        if l1l1l1_opy_ not in l1llll1_opy_:
            l1llll1_opy_.append(l1l1l1_opy_)
    l1llll1_opy_.sort()
    for item in l1llll1_opy_:
        l1ll111_opy_.write(l1lll_opy_ (u"ࠣࠧࡶࡠࡳࠨࠒ") % item)
    l1ll111_opy_.close()
def l1lll1l_opy_(addon, l1111_opy_):
    l1l1l11_opy_ = mapping.cleanLabel(l1111_opy_)
    l1lll11_opy_ = mapping.cleanStreamLabel(l1l1l11_opy_)
    return l1lll11_opy_
def l1l1ll1_opy_(addon, l111ll_opy_, labelmaps, l11lll_opy_, l111l1_opy_, l1111_opy_):
    l11l11_opy_    = mapping.cleanLabel(l1111_opy_)
    l1l1l11_opy_ = mapping.mapLabel(labelmaps, l11l11_opy_)
    l1lll1_opy_ = mapping.cleanPrefix(l1l1l11_opy_)
    return mapping.mapChannelName(l11lll_opy_, l1lll1_opy_)
def l1l11l_opy_(addon):
    if addon == l1l1l1l_opy_:
        return l1lll_opy_ (u"ࠩࡉࡐࡆࡀࠧࠓ")
def l11l1_opy_(addon):
    PATH = l1llll_opy_(addon)
    Addon = xbmcaddon.Addon(addon)
    l1ll11l_opy_, l111l_opy_ = l1ll1l1_opy_(Addon)
    url = l1lll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࡯ࡴࡪࡩ࠯ࡨ࡯ࡥࡼࡲࡥࡴࡵ࠰࡬ࡴࡹࡴࡪࡰࡪ࠲ࡸࡵ࡬ࡶࡶ࡬ࡳࡳࡹ࠯ࡱ࡮ࡤࡽࡪࡸ࡟ࡢࡲ࡬࠲ࡵ࡮ࡰࡀࡷࡶࡩࡷࡴࡡ࡮ࡧࡀࠩࡸࠬࡰࡢࡵࡶࡻࡴࡸࡤ࠾ࠧࡶࠪࡦࡩࡴࡪࡱࡱࡁ࡬࡫ࡴࡠ࡮࡬ࡺࡪࡥࡳࡵࡴࡨࡥࡲࡹࠧࠔ") % (l1ll11l_opy_, l111l_opy_)
    request = requests.get(url)
    content = request.json()
    return l1111l_opy_(PATH, addon, content)
def l1ll1l1_opy_(Addon):
    l1ll11l_opy_ = Addon.getSetting(l1lll_opy_ (u"࡚࡙ࠫࡅࡓࡐࡄࡑࡊ࠭ࠕ"))
    l111l_opy_ = Addon.getSetting(l1lll_opy_ (u"ࠬࡖࡁࡔࡕ࡚ࡓࡗࡊࠧࠖ"))
    return l1ll11l_opy_, l111l_opy_
def l1111l_opy_(PATH, addon, content):
    json.dump(content, open(PATH,l1lll_opy_ (u"࠭ࡷࠨࠗ")), indent=3)
    return json.load(open(PATH))
def l1llll_opy_(addon):
    if addon == l1l1l1l_opy_:
        path = os.path.join(dixie.PROFILE, l1lll_opy_ (u"ࠧࡧࡶࡨࡱࡵ࠭࠘"))
        return path
if __name__ == l1lll_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ࠙"):
    checkAddons()