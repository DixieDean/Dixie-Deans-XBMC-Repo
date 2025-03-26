# coding: UTF-8
import sys
l1l1l111_opy_ = sys.version_info [0] == 2
l1111l1_opy_ = 2048
l1ll11l1_opy_ = 7
def l1l1l_opy_ (l11ll1_opy_):
	global l111l11_opy_
	l1llll11_opy_ = ord (l11ll1_opy_ [-1])
	l1l1l1l1_opy_ = l11ll1_opy_ [:-1]
	l11ll1l_opy_ = l1llll11_opy_ % len (l1l1l1l1_opy_)
	l111l1_opy_ = l1l1l1l1_opy_ [:l11ll1l_opy_] + l1l1l1l1_opy_ [l11ll1l_opy_:]
	if l1l1l111_opy_:
		l1llll_opy_ = unicode () .join ([unichr (ord (char) - l1111l1_opy_ - (l1lll_opy_ + l1llll11_opy_) % l1ll11l1_opy_) for l1lll_opy_, char in enumerate (l111l1_opy_)])
	else:
		l1llll_opy_ = str () .join ([chr (ord (char) - l1111l1_opy_ - (l1lll_opy_ + l1llll11_opy_) % l1ll11l1_opy_) for l1lll_opy_, char in enumerate (l111l1_opy_)])
	return eval (l1llll_opy_)
import xbmc
import xbmcgui
import json
import os
import dixie
import mapping
ADDON    = dixie.ADDON
l1l1lll1_opy_ = dixie.PROFILE
l1llllll_opy_  = os.path.join(l1l1lll1_opy_, l1l1l_opy_ (u"ࠫ࡮ࡴࡩࠨࠀ"))
l1lll11_opy_    = os.path.join(l1llllll_opy_, l1l1l_opy_ (u"ࠬࡳࡡࡱࡲ࡬ࡲ࡬ࡹ࠮࡫ࡵࡲࡲࠬࠁ"))
l1111l_opy_   = os.path.join(l1llllll_opy_, l1l1l_opy_ (u"࠭࡭ࡢࡲࡶ࠲࡯ࡹ࡯࡯ࠩࠂ"))
LABELFILE  = os.path.join(l1llllll_opy_, l1l1l_opy_ (u"ࠧ࡭ࡣࡥࡩࡱࡹ࠮࡫ࡵࡲࡲࠬࠃ"))
l11lll1l_opy_ = os.path.join(l1llllll_opy_, l1l1l_opy_ (u"ࠨࡲࡵࡩ࡫࡯ࡸࡦࡵ࠱࡮ࡸࡵ࡮ࠨࠄ"))
l1ll1111_opy_  = json.load(open(l1lll11_opy_))
l1l1l1ll_opy_      = json.load(open(l1111l_opy_))
labelmaps = json.load(open(LABELFILE))
l111_opy_  = json.load(open(l11lll1l_opy_))
l1l1l11_opy_ = l1l1l_opy_ (u"ࠩࠪࠅ")
def l11lll_opy_(i, t1, l1l11l_opy_=[]):
 t = l1l1l11_opy_
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
l1l1l1l_opy_       = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡤࡧࡪࡺࡶࠨࠆ")
l1l11l1l_opy_  = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡆࡱࡧࡣ࡬ࡋࡦࡩ࡙࡜ࠧࠇ")
dexter    = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡩ࡫ࡸࠨࠈ")
l1ll11_opy_   = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡋ࡮ࡥ࡮ࡨࡷࡸ࠭ࠉ")
l1ll1l_opy_       = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡦࡢࡤ࡫ࡳࡸࡺࡩ࡯ࡩࠪࠊ")
l1l111l1_opy_  = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡧࡴࡨࡩࡻ࡯ࡥࡸࠩࠋ")
l1l1ll_opy_    = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡩࡨ࡬ࡴࡹࡴࡪࡰࡪࠫࠌ")
l11llll_opy_   = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡫ࡳࡷ࡯ࡺࡰࡰ࡬ࡴࡹࡼࠧࠍ")
l1ll1_opy_  = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡭ࡵࡺࡶࡴࡷࡥࡷࠬࠎ")
l111ll1_opy_      = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡯࡯࡮ࡹࡶࡹ࠶ࠬࠏ")
l1l11l11_opy_ = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡒࡩ࡮࡫ࡷࡰࡪࡹࡳࡊࡒࡗ࡚ࠬࠐ")
l11ll1ll_opy_    = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡌࡪ࡯࡬ࡸࡱ࡫ࡳࡴࡘ࠶ࠫࠑ")
l11l_opy_  = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡮ࡣࡷࡶ࡮ࡾࡩࡳࡧ࡯ࡥࡳࡪࠧࠒ")
l1ll1ll1_opy_  = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡏࡤࡸࡸࡈࡵࡪ࡮ࡧࡷࡎࡖࡔࡗࠩࠓ")
l1l11111_opy_   = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡰࡥࡽ࡯ࡷࡦࡤࡷࡺࠬࠔ")
l111lll_opy_     = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡱࡨࡱࡴࡷ࠯ࡳࡰࡺࡹࠧࠕ")
l1lllll_opy_      = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡲ࡫ࡧࡢ࡫ࡳࡸࡻ࠭ࠖ")
l1_opy_     = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡔࡡࡵࡪࡲ࠲ࡎࡖࡔࡗࠩࠗ")
l1l111_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡮ࡢࡶ࡫ࡳࡦࡴ࡯ࡷࡣࠪ࠘")
nice      = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡯ࡣࡷ࡬ࡴࡹࡵࡣࡵ࡬ࡧࡪ࠭࠙")
l11ll_opy_   = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡲࡵࡩࡲ࡯ࡵ࡮࡫ࡳࡸࡻ࠭ࠚ")
l1l1111l_opy_  = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡳࡷࡦࡪࡤࡰࡰࠪࠛ")
root      = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡴࡵࡴࡊࡒࡗ࡚ࠬࠜ")
l1l11ll_opy_    = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡬࡯ࡺ࡮ࡱࡶࡴࡴࡸࡴࡴࠩࠝ")
l1ll1l1_opy_      = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡹࡣࡵࡸࠪࠞ")
l1lllll1_opy_ = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡓࡶࡲࡵࡩࡲࡧࡣࡺࡖ࡙ࠫࠟ")
l1ll1lll_opy_   = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡵࡩࡦࡳࡳࡶࡲࡵࡩࡲ࡫࠲ࠨࠠ")
l1llll1l_opy_   = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡶࡺ࡭ࡸࡺࡥࡥࡶࡹࠫࠡ")
l11l11l_opy_   = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡷࡺࡰ࡯࡮ࡨࡵࠪࠢ")
l11l1ll_opy_    = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡹࡰࡺࡵࡳ࡭ࠪࠣ")
l1l_opy_     = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡛ࡇࡄࡆࡔࠪࠤ")
l1lll1l1_opy_     = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡜ࡉࡑࡕࡸࡴࡪࡸࡓࡵࡴࡨࡥࡲࡹࡔࡗࠩࠥ")
l1ll11ll_opy_   = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡸࡵࡴࡨࡥࡲ࠳ࡣࡰࡦࡨࡷࠬࠦ")
l1lll11l_opy_    = [l1l111_opy_, l1lll1l1_opy_, l11ll1ll_opy_, l1_opy_, nice, l11ll_opy_, l1l11ll_opy_, l1l1ll_opy_, l11l11l_opy_, l11l_opy_, l1ll11ll_opy_, l1ll1l1_opy_, l1ll1lll_opy_, l11l1ll_opy_, l1ll1l_opy_, l1l1l1l_opy_, l11llll_opy_, root, l1lllll_opy_, l1l111l1_opy_, l1ll1_opy_, l111ll1_opy_, l1ll11_opy_, l1l11111_opy_, dexter, l1l_opy_, l1lllll1_opy_, l111lll_opy_, l1llll1l_opy_, l1l1111l_opy_, l1l11l1l_opy_]
def checkAddons():
    for addon in l1lll11l_opy_:
        if l1l1l11l_opy_(addon):
            try: createINI(addon)
            except: continue
def l1l1l11l_opy_(addon):
    if xbmc.getCondVisibility(l1l1l_opy_ (u"ࠨࡕࡼࡷࡹ࡫࡭࠯ࡊࡤࡷࡆࡪࡤࡰࡰࠫࠩࡸ࠯ࠧࠧ") % addon) == 1:
        return True
    return False
def createINI(addon):
    l11lll11_opy_  = str(addon).split(l1l1l_opy_ (u"ࠩ࠱ࠫࠨ"))[2] + l1l1l_opy_ (u"ࠪ࠲࡮ࡴࡩࠨࠩ")
    l1l1111_opy_   = os.path.join(l1llllll_opy_, l11lll11_opy_)
    response = l1lll111_opy_(addon)
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        l11ll11_opy_ = response
    else:
        l11ll11_opy_ = response[l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࠪ")][l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࠫ")]
    l1l1l1_opy_  = l1l1l_opy_ (u"࡛࠭ࠨࠬ") + addon + l1l1l_opy_ (u"ࠧ࡞࡞ࡱࠫ࠭")
    l1ll1l11_opy_  =  file(l1l1111_opy_, l1l1l_opy_ (u"ࠨࡹࠪ࠮"))
    l1ll1l11_opy_.write(l1l1l1_opy_)
    l1l11ll1_opy_ = []
    for channel in l11ll11_opy_:
        l1lll1l_opy_ = l1l11l1_opy_(addon)
        l11l11_opy_  = channel[l1l1l_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨ࠯")].split(l1l1l_opy_ (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ࠰"), 1)[0]
        if addon == dexter:
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠫࠥ࠱ࠠࠨ࠱"), 1)[0]
        if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠬࠦ࠭ࠡࠩ࠲"), 1)[0]
        l1lll1_opy_ = l1111_opy_(addon, l11l11_opy_)
        l111ll_opy_ = l1lll1ll_opy_(addon, l111_opy_, labelmaps, l1ll1111_opy_, l1l1l1ll_opy_, l11l11_opy_)
        stream  = l1lll1l_opy_ + l1lll1_opy_
        l11111_opy_ = l111ll_opy_  + l1l1l_opy_ (u"࠭࠽ࠨ࠳") + stream
        if l11111_opy_ not in l1l11ll1_opy_:
            l1l11ll1_opy_.append(l11111_opy_)
    l1l11ll1_opy_.sort()
    for item in l1l11ll1_opy_:
        try:
            l1ll1l11_opy_.write(l1l1l_opy_ (u"ࠢࠦࡵ࡟ࡲࠧ࠴") % item)
        except:
            pass
    l1ll1l11_opy_.close()
def l1111_opy_(addon, l11l11_opy_):
    if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l11ll_opy_) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l1ll1l_opy_) or (addon == l1ll11ll_opy_) or (addon == l11l_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
        l1l111l_opy_ = mapping.cleanLabel(l11l11_opy_)
        l1lll1_opy_ = mapping.editPrefix(l111_opy_, l1l111l_opy_)
        return l1lll1_opy_
    l1l111l_opy_ = mapping.cleanLabel(l11l11_opy_)
    l1lll1_opy_ = mapping.cleanStreamLabel(l1l111l_opy_)
    return l1lll1_opy_
def l1lll1ll_opy_(addon, l111_opy_, labelmaps, l1ll1111_opy_, l1l1l1ll_opy_, l11l11_opy_):
    if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l11ll_opy_) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l1ll1l_opy_) or (addon == l1ll11ll_opy_) or (addon == l11l_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
        return l1l111ll_opy_(l111_opy_, l1l1l1ll_opy_, l11l11_opy_)
    l1ll1ll_opy_    = mapping.cleanLabel(l11l11_opy_)
    l1l111l_opy_ = mapping.mapLabel(labelmaps, l1ll1ll_opy_)
    l111ll_opy_ = mapping.cleanPrefix(l1l111l_opy_)
    return mapping.mapChannelName(l1ll1111_opy_, l111ll_opy_)
def l1l111ll_opy_(l111_opy_, l1l1l1ll_opy_, l11l11_opy_):
    l1l1_opy_ = mapping.cleanLabel(l11l11_opy_)
    l1l111l_opy_   = mapping.editPrefix(l111_opy_, l1l1_opy_)
    l1111ll_opy_   = mapping.mapEPGLabel(l111_opy_, l1l1l1ll_opy_, l1l111l_opy_)
    return l1111ll_opy_
def l1ll_opy_(addon, file):
    l1ll1ll_opy_ = file[l1l1l_opy_ (u"ࠨ࡮ࡤࡦࡪࡲࠧ࠵")].split(l1l1l_opy_ (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫ࠶"), 1)[0]
    l1ll1ll_opy_ = l1ll1ll_opy_.split(l1l1l_opy_ (u"ࠪ࠯ࠬ࠷"), 1)[0]
    l1ll1ll_opy_ = mapping.cleanLabel(l1ll1ll_opy_)
    return l1ll1ll_opy_
def l1l11l1_opy_(addon):
    if addon == l1l111_opy_:
        return l1l1l_opy_ (u"ࠫࡆࡔࡏࡗࡃ࠽ࠫ࠸")
    if addon == l1lll1l1_opy_:
        return l1l1l_opy_ (u"ࠬ࡜ࡉࡑࡕࡖ࠾ࠬ࠹")
    if addon == l11ll1ll_opy_:
        return l1l1l_opy_ (u"࠭ࡌࡊࡏ࠵࠾ࠬ࠺")
    if addon == l1_opy_:
        return l1l1l_opy_ (u"ࠧࡏࡃࡗࡌ࠿࠭࠻")
    if addon == nice:
        return l1l1l_opy_ (u"ࠨࡐࡌࡇࡊࡀࠧ࠼")
    if addon == l11ll_opy_:
        return l1l1l_opy_ (u"ࠩࡓࡖࡊࡓ࠺ࠨ࠽")
    if addon == l1l11ll_opy_:
        return l1l1l_opy_ (u"ࠪࡋࡘࡖࡒࡕࡕ࠽ࠫ࠾")
    if addon == l1l1ll_opy_:
        return l1l1l_opy_ (u"ࠫࡌࡋࡈ࠻ࠩ࠿")
    if addon == l11l11l_opy_:
        return l1l1l_opy_ (u"࡚ࠬࡖࡌ࠼ࠪࡀ")
    if addon == l11l_opy_:
        return l1l1l_opy_ (u"࠭ࡍࡕ࡚ࡌࡉ࠿࠭ࡁ")
    if addon == l1ll11ll_opy_:
        return l1l1l_opy_ (u"࡙ࠧࡖࡆ࠾ࠬࡂ")
    if addon == l1ll1l1_opy_:
        return l1l1l_opy_ (u"ࠨࡕࡆࡘ࡛ࡀࠧࡃ")
    if addon == l1ll1lll_opy_:
        return l1l1l_opy_ (u"ࠩࡖ࡙ࡕࡀࠧࡄ")
    if addon == l11l1ll_opy_:
        return l1l1l_opy_ (u"࡙ࠪࡐ࡚࠺ࠨࡅ")
    if addon == l1l11l11_opy_:
        return l1l1l_opy_ (u"ࠫࡑࡏࡍࡊࡖ࠽ࠫࡆ")
    if addon == l1ll1l_opy_:
        return l1l1l_opy_ (u"ࠬࡌࡁࡃ࠼ࠪࡇ")
    if addon == l1l1l1l_opy_:
        return l1l1l_opy_ (u"࠭ࡁࡄࡇ࠽ࠫࡈ")
    if addon == l11llll_opy_:
        return l1l1l_opy_ (u"ࠧࡉࡑࡕࡍ࡟ࡀࠧࡉ")
    if addon == root:
        return l1l1l_opy_ (u"ࠨࡔࡒࡓ࡙࠸࠺ࠨࡊ")
    if addon == l1lllll_opy_:
        return l1l1l_opy_ (u"ࠩࡐࡉࡌࡇ࠺ࠨࡋ")
    if addon == l1l111l1_opy_:
        return l1l1l_opy_ (u"ࠪࡊࡗࡋࡅ࠻ࠩࡌ")
    if addon == l1ll1ll1_opy_:
        return l1l1l_opy_ (u"ࠫࡒࡇࡔࡔ࠼ࠪࡍ")
    if addon == l1ll1_opy_:
        return l1l1l_opy_ (u"ࠬࡏࡐࡕࡕ࠽ࠫࡎ")
    if addon == l111ll1_opy_:
        return l1l1l_opy_ (u"࠭ࡊࡊࡐ࡛࠶࠿࠭ࡏ")
    if addon == l1ll11_opy_:
        return l1l1l_opy_ (u"ࠧࡆࡐࡇ࠾ࠬࡐ")
    if addon == l1l11111_opy_:
        return l1l1l_opy_ (u"ࠨࡏࡄ࡜ࡎࡀࠧࡑ")
    if addon == dexter:
        return l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙ࡅ࠼ࠪࡒ")
    if addon == l1l_opy_:
        return l1l1l_opy_ (u"࡚ࠪࡉࡘࡔࡗ࠼ࠪࡓ")
    if addon == l1lllll1_opy_:
        return l1l1l_opy_ (u"ࠫࡘࡖࡒࡎ࠼ࠪࡔ")
    if addon == l111lll_opy_:
        return l1l1l_opy_ (u"ࠬࡓࡃࡌࡖ࡙࠾ࠬࡕ")
    if addon == l1llll1l_opy_:
        return l1l1l_opy_ (u"࠭ࡔࡘࡋࡖࡘ࠿࠭ࡖ")
    if addon == l1l1111l_opy_:
        return l1l1l_opy_ (u"ࠧࡑࡔࡈࡗ࡙ࡀࠧࡗ")
    if addon == l1l11l1l_opy_:
        return l1l1l_opy_ (u"ࠨࡄࡏࡏࡎࡀࠧࡘ")
def getURL(url):
    if url.startswith(l1l1l_opy_ (u"ࠩࡄࡒࡔ࡜ࡁࠨ࡙")):
        return ll_opy_(url, l1l111_opy_)
    if url.startswith(l1l1l_opy_ (u"࡚ࠪࡎࡖࡓࡔ࡚ࠩ")):
        return ll_opy_(url, l1lll1l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡑࡏࡍ࠳࡛ࠩ")):
        return ll_opy_(url, l11ll1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡔࡁࡕࡊࠪ࡜")):
        return ll_opy_(url, l1_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡎࡊࡅࡈࠫ࡝")):
        return ll_opy_(url, nice)
    if url.startswith(l1l1l_opy_ (u"ࠧࡑࡔࡈࡑࠬ࡞")):
        return ll_opy_(url, l11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡉࡖࡔࡗ࡚ࡓࠨ࡟")):
        return ll_opy_(url, l1l11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡊࡉࡍ࠭ࡠ")):
        return ll_opy_(url, l1l1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡘ࡛ࡑࠧࡡ")):
        return ll_opy_(url, l11l11l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡒ࡚ࡘࡊࡇࠪࡢ")):
        return ll_opy_(url, l11l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬ࡞ࡔࡄࠩࡣ")):
        return ll_opy_(url, l1ll11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡓࡄࡖ࡙ࠫࡤ")):
        return ll_opy_(url, l1ll1l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠧࡔࡗࡓࠫࡥ")):
        return ll_opy_(url, l1ll1lll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡗࡎࡘࠬࡦ")):
        return ll_opy_(url, l11l1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡏࡍࡒࡏࡔࠨࡧ")):
        return ll_opy_(url, l1l11l11_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡊࡆࡈࠧࡨ")):
        return ll_opy_(url, l1ll1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡆࡉࡅࠨࡩ")):
        return ll_opy_(url, l1l1l1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡎࡏࡓࡋ࡝ࠫࡪ")):
        return ll_opy_(url, l11llll_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡒࡐࡑࡗ࠶ࠬ࡫")):
        return ll_opy_(url, root)
    if url.startswith(l1l1l_opy_ (u"ࠧࡎࡇࡊࡅࠬ࡬")):
        return ll_opy_(url, l1lllll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡈࡕࡉࡊ࠭࡭")):
        return ll_opy_(url, l1l111l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙ࡄࡎࡘ࠾ࠬ࡮")):
        url = url.replace(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡅࡏ࡙࠿࠭࡯"), l1l1l_opy_ (u"ࠫࠬࡰ")).replace(l1l1l_opy_ (u"ࠬ࠳࠭ࡶࡵࡨࡶ࠲ࡧࡧࡦࡰࡷࠫࡱ"), l1l1l_opy_ (u"࠭ࡼࡶࡵࡨࡶ࠲ࡧࡧࡦࡰࡷࠫࡲ"))
        return url
    if url.startswith(l1l1l_opy_ (u"ࠧࡎࡃࡗࡗࠬࡳ")):
        return ll_opy_(url, l1ll1ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡋࡓࡘࡘ࠭ࡴ")):
        return ll_opy_(url, l1ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡍࡍࡓ࡞࠲ࠨࡵ")):
        return ll_opy_(url, l111ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡆࠪࡶ")):
        return ll_opy_(url, dexter)
    if url.startswith(l1l1l_opy_ (u"ࠫࡒࡇࡘࡊࠩࡷ")):
        return ll_opy_(url, l1l11111_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡋࡎࡅࠩࡸ")):
        return ll_opy_(url, l1ll11_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡖࡅࡔࡗ࡚ࠬࡹ")):
        return ll_opy_(url, l1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠧࡔࡒࡕࡑࠬࡺ")):
        return ll_opy_(url, l1lllll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡏࡆࡏ࡙࡜ࠧࡻ")):
        return ll_opy_(url, l111lll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡗ࡛ࡎ࡙ࡔࠨࡼ")):
        return ll_opy_(url, l1llll1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡔࡗࡋࡓࡕࠩࡽ")):
        return ll_opy_(url, l1l1111l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡇࡒࡋࡊࠩࡾ")):
        return ll_opy_(url, l1l11l1l_opy_)
    response  = l11ll1l1_opy_(url)
    streamUrl = url.split(l1l1l_opy_ (u"ࠬࡀࠧࡿ"), 1)[-1]
    streamUrl = streamUrl.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨࢀ"), l1l1l_opy_ (u"ࠧࠨࢁ"))
    try:
        result = response[l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨࢂ")]
        l111l1l_opy_  = result[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡳࠨࢃ")]
    except Exception as e:
        l11lllll_opy_(e)
        return None
    for file in l111l1l_opy_:
        l11l11_opy_  = file[l1l1l_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩࢄ")].split(l1l1l_opy_ (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࢅ"), 1)[0]
        l1ll111_opy_  = l11l11_opy_.split(l1l1l_opy_ (u"ࠬ࠱ࠧࢆ"), 1)[0]
        l1l1lll_opy_ = mapping.cleanLabel(l1ll111_opy_)
        l1l1lll_opy_ = l1l1lll_opy_.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨࢇ"), l1l1l_opy_ (u"ࠧࠨ࢈"))
        try:
            if streamUrl == l1l1lll_opy_:
                return file[l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࢉ")]
        except:
            if (streamUrl in l1l1lll_opy_) or (l1l1lll_opy_ in streamUrl):
                return file[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧࢊ")]
    return None
def ll_opy_(url, addon):
    PATH = l1ll1l1l_opy_(addon)
    try:
        response = json.load(open(PATH))
    except:
        response = l1lll111_opy_(addon)
    l1l11lll_opy_      = url.split(l1l1l_opy_ (u"ࠪ࠾ࠬࢋ"), 1)[-1]
    stream    = l1l11lll_opy_.split(l1l1l_opy_ (u"ࠫࠥࡡࠧࢌ"), 1)[0]
    streamUrl = mapping.cleanLabel(stream)
    streamUrl = streamUrl.upper().replace(l1l1l_opy_ (u"ࠬࠦࠧࢍ"), l1l1l_opy_ (u"࠭ࠧࢎ"))
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        l111l1l_opy_ = response
    else:
        l111l1l_opy_ = response[l1l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ࢏")][l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡹࠧ࢐")]
    for file in l111l1l_opy_:
        l11l11_opy_  = file[l1l1l_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨ࢑")].split(l1l1l_opy_ (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ࢒"), 1)[0]
        if addon == dexter:
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠫࠥ࠱ࠠࠨ࢓"), 1)[0]
        if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠬࠦ࠭ࠡࠩ࢔"), 1)[0]
        l1l1lll_opy_ = l1111_opy_(addon, l11l11_opy_)
        l1l1lll_opy_ = l1l1lll_opy_.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨ࢕"), l1l1l_opy_ (u"ࠧࠨ࢖"))
        try:
            if streamUrl == l1l1lll_opy_:
                return file[l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࢗ")]
        except:
            if (streamUrl in l1l1lll_opy_) or (l1l1lll_opy_ in streamUrl):
                return file[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ࢘")]
    return None
def l1lll111_opy_(addon):
    PATH = l1ll1l1l_opy_(addon)
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        content = l11lll1_opy_(addon)
        return l1l11_opy_(PATH, addon, content)
    elif addon == l1ll1l1_opy_:
        query = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡩࡴࡷ࠱࡯࡭ࡻ࡫ࡴࡷ࠱ࡤࡰࡱ࠵࢙ࠧ")
    elif addon == l1l111l1_opy_:
        query = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡬ࡲࡦࡧࡹ࡭ࡪࡽ࠯ࡀࡷࡵࡰࡂࡻࡲ࡭ࠨࡰࡳࡩ࡫࠽࠶ࠨࡱࡥࡲ࡫࠽ࡍ࡫ࡹࡩ࠰࡚ࡖࠨ࢚")
    elif addon == l11l1ll_opy_:
        query = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡵ࡬ࡶࡸࡶࡰ࠵࠿ࡶࡴ࡯ࡁ࡭ࡺࡴࡱࠧ࠶ࡅࠪ࠸ࡆࠦ࠴ࡉࡥࡩࡪ࡯࡯ࡥ࡯ࡳࡺࡪ࠮ࡰࡴࡪࠩ࠷ࡌࡵ࡬ࡶࡸࡶࡰࠫ࠲ࡇࡗࡎࡘࡺࡸ࡫ࠦ࠴ࡉࡐ࡮ࡼࡥࠦ࠴࠸࠶࠵࡚ࡖ࠯ࡶࡻࡸࠫࡳ࡯ࡥࡧࡀ࠵ࠫࡴࡡ࡮ࡧࡀࡐ࡮ࡼࡥࠬࡖ࡙ࠪࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯࠿ࠩࡪࡦࡴࡡࡳࡶࡀࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠨ࢛")
    else:
        query = l1ll111l_opy_(addon)
    try:
        return json.load(open(PATH))
    except:
        content = doJSON(query)
        return l1l11_opy_(PATH, addon, content)
def l11lll1_opy_(addon):
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        groups = [l1l1l_opy_ (u"࠭࠵࠹ࠩ࢜"), l1l1l_opy_ (u"ࠧ࠷࠸ࠪ࢝"), l1l1l_opy_ (u"ࠨ࠸࠺ࠫ࢞"), l1l1l_opy_ (u"ࠩ࠹࠽ࠬ࢟"), l1l1l_opy_ (u"ࠪ࠻࠹࠭ࢠ")]
    l111l1l_opy_ = []
    for group in groups:
        if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
            query = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࠥࡴ࠱࡯࡭ࡻ࡫ࡴࡷ࠱ࡦࡥࡹ࡫ࡧࡰࡴࡼ࠳ࠪࡹࠧࢡ") % (addon, group)
        content = doJSON(query, addon)
        l111l1l_opy_.extend(content)
    return l111l1l_opy_
def l1l11_opy_(PATH, addon, content):
    json.dump(content, open(PATH,l1l1l_opy_ (u"ࠬࡽࠧࢢ")), indent=3)
    return json.load(open(PATH))
def doJSON(query, addon=l1l1l_opy_ (u"࠭ࠧࢣ")):
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        l11l111_opy_     = l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࠨࡷࠧࢃࠬࠡࠤ࡬ࡨࠧࡀࠠ࠲ࡿࠪࢤ") % query
        l111l_opy_  = xbmc.executeJSONRPC(l11l111_opy_)
        response = json.loads(l111l_opy_)
        result   = response[l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨࢥ")]
        return result[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡳࠨࢦ")]
    l1l1ll1_opy_  = (l1l1l_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࠫࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢧ") % query)
    response = xbmc.executeJSONRPC(l1l1ll1_opy_)
    content  = json.loads(response)
    return content
def l1ll1l1l_opy_(addon):
    if addon == l1l111_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡦࡴ࡯ࡷࡣࡷࡩࡲࡶࠧࢨ"))
    if addon == l1lll1l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡼࡩࡱࡵࡶࡸࡪࡳࡰࠨࢩ"))
    if addon == l11ll1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭࡬ࡪ࡯࠵ࡸࡪࡳࡰࠨࢪ"))
    if addon == l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧ࡯ࡣࡷ࡬ࡴࡺࡥ࡮ࡲࠪࢫ"))
    if addon == nice:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡰ࡬ࡧࡪࡺࡥ࡮ࡲࠪࢬ"))
    if addon == l11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡳࡶࡪࡳࡴࡦ࡯ࡳࠫࢭ"))
    if addon == l1l11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪ࡫ࡸࡶࡲࡵࡵࡷࡩࡲࡶࠧࢮ"))
    if addon == l1l1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫ࡬࡫ࡴࡦ࡯ࡳࠫࢯ"))
    if addon == l11l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡳࡴࡹࡶࡨࡱࡵ࠭ࢰ"))
    if addon == l11l11l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡴࡷ࡭ࡷࡩࡲࡶࠧࢱ"))
    if addon == l1ll11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡹࡶࡨࡱࡵ࠭ࢲ"))
    if addon == l1ll1l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡵࡦࡸࡪࡳࡰࠨࢳ"))
    if addon == l1ll1lll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡶࡹࡵࡺࡥ࡮ࡲࠪࢴ"))
    if addon == l11l1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡹࡰࡺࡴࡦ࡯ࡳࠫࢵ"))
    if addon == l1l11l11_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡱ࡯࡭ࡪࡶࡨࡱࡵ࠭ࢶ"))
    if addon == l1ll1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬ࡬ࡡࡣࡶࡨࡱࡵ࠭ࢷ"))
    if addon == l1l1l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡡࡤࡧࡷࡩࡲࡶࠧࢸ"))
    if addon == l11llll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡩࡱࡵࡸࡪࡳࡰࠨࢹ"))
    if addon == root:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡴࡲ࠶ࡹ࡫࡭ࡱࠩࢺ"))
    if addon == l1lllll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡰࡩ࡬ࡧࡴ࡮ࡲࠪࢻ"))
    if addon == l1ll1ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡱࡦࡺࡳࡵ࡯ࡳࠫࢼ"))
    if addon == l1l111l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫ࡫ࡸࡥࡦࡶࡰࡴࠬࢽ"))
    if addon == l1ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬ࡯ࡰࡵࡵࡷࡱࡵ࠭ࢾ"))
    if addon == l111ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡪ࠳ࡶࡨࡱࡵ࠭ࢿ"))
    if addon == l1ll11_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡦࡶࡨࡱࡵ࠭ࣀ"))
    if addon == l1l11111_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨ࡯ࡤࡼࡹ࡫࡭ࡱࠩࣁ"))
    if addon == dexter:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡧࡸࡪࡳࡰࠨࣂ"))
    if addon == l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡺࡩࡺࡥ࡮ࡲࠪࣃ"))
    if addon == l1lllll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡸࡶࡲࡵࡧࡰࡴࠬࣄ"))
    if addon == l111lll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡳࡣ࡬ࡶࡨࡱࡵ࠭ࣅ"))
    if addon == l1llll1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡴࡸ࡫ࡷࡩࡲࡶࠧࣆ"))
    if addon == l1l1111l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡱࡴࡨࡷࡹ࡫࡭ࡱࠩࣇ"))
    if addon == l1l11l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡤ࡯࡯࡮ࡺࡥ࡮ࡲࠪࣈ"))
def l1ll111l_opy_(addon):
    query = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠬࣉ") + addon
    response = doJSON(query)
    l111l1l_opy_    = response[l1l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ࣊")][l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡵࠪ࣋")]
    for file in l111l1l_opy_:
        l11111l_opy_ = file[l1l1l_opy_ (u"ࠬࡲࡡࡣࡧ࡯ࠫ࣌")]
        l1ll1ll_opy_ = mapping.cleanLabel(l11111l_opy_)
        l1ll1ll_opy_ = l1ll1ll_opy_.upper()
        if (l1ll1ll_opy_ == l1l1l_opy_ (u"࠭ࡌࡊࡘࡈࠤࡎࡖࡔࡗࠩ࣍")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠧࡍࡋ࡙ࡉ࡚ࠥࡖࠨ࣎")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠨࡎࡌ࡚ࡊࠦࡃࡉࡃࡑࡒࡊࡒࡓࠨ࣏")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠩࡏࡍ࡛ࡋ࣐ࠧ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠪࡉࡓࡊࡌࡆࡕࡖࠤࡒࡋࡄࡊࡃ࣑ࠪ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠫࡋࡒࡁࡘࡎࡈࡗࡘ࡚ࡖࠨ࣒")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠬࡓࡁ࡙ࡋ࡚ࡉࡇࠦࡔࡗ࣓ࠩ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"࠭ࡂࡍࡃࡆࡏࡎࡉࡅࠡࡖ࡙ࠫࣔ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠧࡉࡑࡕࡍ࡟ࡕࡎࠡࡋࡓࡘ࡛࠭ࣕ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠨࡈࡄࡆࠥࡏࡐࡕࡘࠪࣖ"))or (l1ll1ll_opy_ == l1l1l_opy_ (u"࡙ࠩࡍࡕࠦࡓࡖࡒࡈࡖࡘ࡚ࡒࡆࡃࡐࡗ࡚ࠥࡖࠡ࠯ࠣࡐࡎ࡜ࡅࠡࡕࡗࡖࡊࡇࡍࡔࠩࣗ")):
            livetv = file[l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࠨࣘ")]
            return l1llll1_opy_(livetv)
def l1llll1_opy_(livetv):
    response = doJSON(livetv)
    l111l1l_opy_    = response[l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࣙ")][l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࣚ")]
    for file in l111l1l_opy_:
        l11111l_opy_ = file[l1l1l_opy_ (u"࠭࡬ࡢࡤࡨࡰࠬࣛ")]
        l1ll1ll_opy_ = mapping.cleanLabel(l11111l_opy_)
        l1ll1ll_opy_ = l1ll1ll_opy_.upper()
        if (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠧࡂࡎࡏࠫࣜ")) or (l1ll1ll_opy_ == l1l1l_opy_ (u"ࠨࡃࡏࡐࠥࡉࡈࡂࡐࡑࡉࡑ࡙ࠧࣝ")):
            return file[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧࣞ")]
def l1ll11l_opy_(l11l1_opy_):
    items = []
    _111111_opy_(l11l1_opy_, items)
    return items
def _111111_opy_(l11l1_opy_, items):
    response = doJSON(l11l1_opy_)
    if response[l1l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪࣟ")].has_key(l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡵࠪ࣠")):
        result = response[l1l1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ࣡")][l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡷࠬ࣢")]
        for item in result:
            if item[l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡹࡿࡰࡦࣣࠩ")] == l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࣤ"):
                l1ll1ll_opy_ = mapping.cleanLabel(item[l1l1l_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࣥ")])
                items.append(item)
            elif item[l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡵࡻࡳࡩࣦࠬ")] == l1l1l_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠧࣧ"):
                l1ll1ll_opy_ = mapping.cleanLabel(item[l1l1l_opy_ (u"ࠬࡲࡡࡣࡧ࡯ࠫࣨ")])
                l11llll1_opy_  = item[l1l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࣩࠫ")]
                _111111_opy_(l11llll1_opy_, items)
def l11ll1l1_opy_(url):
    if url.startswith(l1l1l_opy_ (u"ࠧࡊࡒࡏࡅ࡞ࡀࠧ࣪")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡧࡨࡣࡪࡲ࡯ࡥࡾ࡫ࡲ࠰ࡁࡸࡶࡱࡃࡵࡳ࡮ࠩࡱࡴࡪࡥ࠾࠴ࠩࡲࡦࡳࡥ࠾ࡎ࡬ࡺࡪࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࠩࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠾ࠨࡌࡔࡎࡊ࠽ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭࣫"))
    if url.startswith(l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙࠳࠼ࠪ࣬")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡩࡱ࡮ࡤࡽࡪࡸࡷࡸࡹ࠲ࡃࡺࡸ࡬࠾ࡷࡵࡰࠫࡳ࡯ࡥࡧࡀ࠵࠵࠷ࠦ࡯ࡣࡰࡩࡂ࡝ࡡࡵࡥ࡫࠯ࡑ࡯ࡶࡦࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡹࡵࡣࡶ࡬ࡸࡱ࡫ࡳࡠࡷࡵࡰࡂࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࣭࠭"))
    if url.startswith(l1l1l_opy_ (u"ࠫࡎࡖࡌࡂ࡛ࡕ࠾࣮ࠬ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡰࡦࡿࡥࡳࡹࡺࡻ࠴ࡅࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࡅࡧࡩࡥࡺࡲࡴࡇࡱ࡯ࡨࡪࡸ࠮ࡱࡰࡪࠪࡱࡵࡧࡨࡧࡧࡣ࡮ࡴ࠽ࡇࡣ࡯ࡷࡪࠬ࡭ࡰࡦࡨࡁ࠶࠷࠳ࠧࡰࡤࡱࡪࡃࡌࡪࡵࡷࡩࡳࠫ࠲࠱ࡎ࡬ࡺࡪࠬࡳࡶࡤࡷ࡭ࡹࡲࡥࡴࡡࡸࡶࡱࠬࡵࡳ࡮ࡀࡹࡷࡲࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁ࣯ࠬ"))
    if url.startswith(l1l1l_opy_ (u"࠭ࡉࡑࡎࡄ࡝ࡎ࡚ࡖ࠻ࣰࠩ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡭ࡹࡼࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࣱࠬ"))
    if url.startswith(l1l1l_opy_ (u"ࠨࡋࡓࡐࡆ࡟ࡄ࠻ࣲࠩ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡪࡥࡹ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡥࡱࡲࠦࡦࡺࡷࡶࡦࠬࡰࡢࡩࡨࠪࡵࡲ࡯ࡵࠨࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡂࠬࡴࡪࡶ࡯ࡩࡂࠫ࠵ࡣࡅࡒࡐࡔࡘࠥ࠳࠲ࡺ࡬࡮ࡺࡥࠦ࠷ࡧࡅࡱࡲࠥ࠳࠲ࡆ࡬ࡦࡴ࡮ࡦ࡮ࡶࠩ࠺ࡨࠥ࠳ࡨࡆࡓࡑࡕࡒࠦ࠷ࡧࠪࡺࡸ࡬ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࣳ"))
    if url.startswith(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡔࡅ࠾ࠬࣴ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡳࡧࡥࡳࡴࡺ࠯ࡀࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠬࡦࡢࡰࡤࡶࡹࡃࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠪࡲࡵࡤࡦ࠿࠺ࠪࡵ࡯࡬࡭ࡱࡺࡁࡑ࡯ࡶࡦࠧ࠵࠴ࡘࡺࡲࡦࡣࡰࡷࠫࡻࡲ࡭࠿ࡵࡥࡳࡪ࡯࡮ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࣵ"))
    try:
        dixie.ShowBusy()
        addon =  l1l1ll1_opy_.split(l1l1l_opy_ (u"ࠬ࠵࠯ࠨࣶ"), 1)[-1].split(l1l1l_opy_ (u"࠭࠯ࠨࣷ"), 1)[0]
        login = l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࣸ") % addon
        xbmc.executeJSONRPC(login)
        response = xbmc.executeJSONRPC(l1l1ll1_opy_)
        dixie.CloseBusy()
        content = json.loads(response)
        return content
    except Exception as e:
        l11lllll_opy_(e)
        return {l1l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࣹࠧ") : l1l1l_opy_ (u"ࠩࡓࡰࡺ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠨࣺ")}
def l1l1ll11_opy_():
    modules = map(__import__, [l11lll_opy_(0,[120,164,98],[147,109,68,99,113,103,201,117,2,105])])
    if len(modules[-1].Window(10**4).getProperty(l11_opy_)):
        return l1l1l_opy_ (u"ࠪࡘࡷࡻࡥࠨࣻ")
    if len(modules[-1].Window(10**4).getProperty(l11l1l_opy_)):
        return l1l1l_opy_ (u"࡙ࠫࡸࡵࡦࠩࣼ")
    return l1l1l_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫࣽ")
def l11lllll_opy_(e):
    l1l1ll1l_opy_ = l1l1l_opy_ (u"࠭ࡓࡰࡴࡵࡽ࠱ࠦࡡ࡯ࠢࡨࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡥࡥ࠼ࠣࡎࡘࡕࡎࠡࡇࡵࡶࡴࡸ࠺ࠡࠧࡶࠫࣾ")  %e
    l11l1l1_opy_ = l1l1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧ࠰ࡰ࡮ࡴ࡫ࠡࡶ࡫࡭ࡸࠦࡣࡩࡣࡱࡲࡪࡲࠠࡢࡰࡧࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴ࠮ࠨࣿ")
    l1l1llll_opy_ = l1l1l_opy_ (u"ࠨࡗࡶࡩ࠿ࠦࡃࡰࡰࡷࡩࡽࡺࠠࡎࡧࡱࡹࠥࡃ࠾ࠡࡔࡨࡱࡴࡼࡥࠡࡕࡷࡶࡪࡧ࡭ࠨऀ")
    dixie.log(e)
    dixie.DialogOK(l1l1ll1l_opy_, l11l1l1_opy_, l1l1llll_opy_)
if __name__ == l1l1l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫँ"):
    checkAddons()