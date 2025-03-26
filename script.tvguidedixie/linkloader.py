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
l1llllll_opy_  = os.path.join(l1l1lll1_opy_, l1l1l_opy_ (u"ࠪ࡭ࡳ࡯ࠧं"))
l11lll1l_opy_ = os.path.join(l1llllll_opy_, l1l1l_opy_ (u"ࠫࡵࡸࡥࡧ࡫ࡻࡩࡸ࠴ࡪࡴࡱࡱࠫः"))
l111_opy_   = json.load(open(l11lll1l_opy_))
l1l1l11_opy_ = l1l1l_opy_ (u"ࠬ࠭ऄ")
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
l1l1l1l_opy_       = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡧࡣࡦࡶࡹࠫअ")
l1l11l1l_opy_  = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡂ࡭ࡣࡦ࡯ࡎࡩࡥࡕࡘࠪआ")
dexter    = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡥࡧࡻࠫइ")
l1ll11_opy_   = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡇࡱࡨࡱ࡫ࡳࡴࠩई")
l1ll1l_opy_       = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡩࡥࡧ࡮࡯ࡴࡶ࡬ࡲ࡬࠭उ")
l1l111l1_opy_  = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡪࡷ࡫ࡥࡷ࡫ࡨࡻࠬऊ")
l1l1ll_opy_    = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡬࡫ࡨࡰࡵࡷ࡭ࡳ࡭ࠧऋ")
l11llll_opy_   = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡮࡯ࡳ࡫ࡽࡳࡳ࡯ࡰࡵࡸࠪऌ")
l1ll1_opy_  = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡩࡱࡶࡹࡷࡺࡨࡳࠨऍ")
l111ll1_opy_      = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡫࡫ࡱࡼࡹࡼ࠲ࠨऎ")
l1l11l11_opy_ = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡎ࡬ࡱ࡮ࡺ࡬ࡦࡵࡶࡍࡕ࡚ࡖࠨए")
l11ll1ll_opy_    = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡏ࡭ࡲ࡯ࡴ࡭ࡧࡶࡷ࡛࠹ࠧऐ")
l11l_opy_  = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡱࡦࡺࡲࡪࡺ࡬ࡶࡪࡲࡡ࡯ࡦࠪऑ")
l1ll1ll1_opy_  = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡒࡧࡴࡴࡄࡸ࡭ࡱࡪࡳࡊࡒࡗ࡚ࠬऒ")
l1l11111_opy_   = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡳࡡࡹ࡫ࡺࡩࡧࡺࡶࠨओ")
l111lll_opy_     = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡭ࡤ࡭ࡷࡺ࠲ࡶ࡬ࡶࡵࠪऔ")
l1lllll_opy_      = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡮ࡧࡪࡥ࡮ࡶࡴࡷࠩक")
l1_opy_     = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡐࡤࡸ࡭ࡵ࠮ࡊࡒࡗ࡚ࠬख")
l1l111_opy_ = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡱࡥࡹ࡮࡯ࡢࡰࡲࡺࡦ࠭ग")
nice      = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡲࡦࡺࡨࡰࡵࡸࡦࡸ࡯ࡣࡦࠩघ")
l11ll_opy_   = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡵࡸࡥ࡮࡫ࡸࡱ࡮ࡶࡴࡷࠩङ")
l1l1111l_opy_  = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡶࡳࡢࡦࡧࡳࡳ࠭च")
root      = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡲࡰࡱࡷࡍࡕ࡚ࡖࠨछ")
l11l11l1_opy_     = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡨ࡫ࡽࡱࡴࡺࡶࠨज")
l1l11ll_opy_    = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡩ࡬ࡾࡲࡵࡳࡱࡱࡵࡸࡸ࠭झ")
l1ll1l1_opy_      = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡶࡧࡹࡼࠧञ")
l1lllll1_opy_ = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡗࡺࡶࡲࡦ࡯ࡤࡧࡾ࡚ࡖࠨट")
l1ll1lll_opy_   = l1l1l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡺࡲࡦࡣࡰࡷࡺࡶࡲࡦ࡯ࡨ࠶ࠬठ")
l1llll1l_opy_   = l1l1l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡺࡷࡪࡵࡷࡩࡩࡺࡶࠨड")
l11l11l_opy_   = l1l1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡴࡷ࡭࡬ࡲ࡬ࡹࠧढ")
l11l1ll_opy_    = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡹࡷࡱࠧण")
l1l_opy_     = l1l1l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡘࡄࡈࡊࡘࠧत")
l1lll1l1_opy_     = l1l1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡙ࡍࡕ࡙ࡵࡱࡧࡵࡗࡹࡸࡥࡢ࡯ࡶࡘ࡛࠭थ")
l1ll11ll_opy_   = l1l1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡼࡹࡸࡥࡢ࡯࠰ࡧࡴࡪࡥࡴࠩद")
l1lll11l_opy_    = [l1l111_opy_, l1lll1l1_opy_, l11ll1ll_opy_, l1_opy_, nice, l11ll_opy_, l11l11l1_opy_, l1l11ll_opy_, l1l1ll_opy_, l11l11l_opy_, l11l_opy_, l1ll11ll_opy_, l1ll1l1_opy_, l1ll1lll_opy_, l11l1ll_opy_, l1l11l11_opy_, l1ll1l_opy_, l1l1l1l_opy_, l11llll_opy_, root, l1lllll_opy_, l1l111l1_opy_, l1ll1_opy_, l111ll1_opy_, l1ll11_opy_, l1l11111_opy_, dexter, l1l_opy_, l1lllll1_opy_, l111lll_opy_, l1llll1l_opy_, l1l1111l_opy_, l1l11l1l_opy_]
def l1111_opy_(addon, l11l11_opy_):
    if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l11ll_opy_) or (addon == l11l11l1_opy_) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l1ll1l_opy_) or (addon == l1ll11ll_opy_) or (addon == l11l_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
        l1l111l_opy_ = mapping.cleanLabel(l11l11_opy_)
        l1lll1_opy_ = mapping.editPrefix(l111_opy_, l1l111l_opy_)
        return l1lll1_opy_
    l1l111l_opy_ = mapping.cleanLabel(l11l11_opy_)
    l1lll1_opy_ = mapping.cleanStreamLabel(l1l111l_opy_)
    return l1lll1_opy_
def l1lll1ll_opy_(addon, l111_opy_, labelmaps, l1ll1111_opy_, l1l1l1ll_opy_, l11l11_opy_):
    if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l11ll_opy_) or (addon == l11l11l1_opy_) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l1ll1l_opy_) or (addon == l1ll11ll_opy_) or (addon == l11l_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
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
    l1ll1ll_opy_ = file[l1l1l_opy_ (u"ࠬࡲࡡࡣࡧ࡯ࠫध")].split(l1l1l_opy_ (u"࡛࠭࠰ࡅࡒࡐࡔࡘ࡝ࠨन"), 1)[0]
    l1ll1ll_opy_ = l1ll1ll_opy_.split(l1l1l_opy_ (u"ࠧࠬࠩऩ"), 1)[0]
    l1ll1ll_opy_ = mapping.cleanLabel(l1ll1ll_opy_)
    return l1ll1ll_opy_
def getURL(url):
    if url.startswith(l1l1l_opy_ (u"ࠨࡃࡑࡓ࡛ࡇࠧप")):
        return ll_opy_(url, l1l111_opy_)
    if url.startswith(l1l1l_opy_ (u"࡙ࠩࡍࡕ࡙ࡓࠨफ")):
        return ll_opy_(url, l1lll1l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡐࡎࡓ࠲ࠨब")):
        return ll_opy_(url, l11ll1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡓࡇࡔࡉࠩभ")):
        return ll_opy_(url, l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡔࡉࡄࡇࠪम")):
        return ll_opy_(url, nice)
    if url.startswith(l1l1l_opy_ (u"࠭ࡐࡓࡇࡐࠫय")):
        return ll_opy_(url, l11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠧࡈࡋ࡝ࠫर")):
        return ll_opy_(url, l11l11l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡉࡖࡔࡗ࡚ࡓࠨऱ")):
        return ll_opy_(url, l1l11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡊࡉࡍ࠭ल")):
        return ll_opy_(url, l1l1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡘ࡛ࡑࠧळ")):
        return ll_opy_(url, l11l11l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡒ࡚ࡘࡊࡇࠪऴ")):
        return ll_opy_(url, l11l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬ࡞ࡔࡄࠩव")):
        return ll_opy_(url, l1ll11ll_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡓࡄࡖ࡙ࠫश")):
        return ll_opy_(url, l1ll1l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠧࡔࡗࡓࠫष")):
        return ll_opy_(url, l1ll1lll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡗࡎࡘࠬस")):
        return ll_opy_(url, l11l1ll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡏࡍࡒࡏࡔࠨह")):
        return ll_opy_(url, l1l11l11_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡊࡆࡈࠧऺ")):
        return ll_opy_(url, l1ll1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡆࡉࡅࠨऻ")):
        return ll_opy_(url, l1l1l1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡎࡏࡓࡋ࡝़ࠫ")):
        return ll_opy_(url, l11llll_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡒࡐࡑࡗ࠶ࠬऽ")):
        return ll_opy_(url, root)
    if url.startswith(l1l1l_opy_ (u"ࠧࡎࡇࡊࡅࠬा")):
        return ll_opy_(url, l1lllll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡈࡕࡉࡊ࠭ि")):
        return ll_opy_(url, l1l111l1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙ࡄࡎࡘ࠾ࠬी")):
        url = url.replace(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡅࡏ࡙࠿࠭ु"), l1l1l_opy_ (u"ࠫࠬू")).replace(l1l1l_opy_ (u"ࠬ࠳࠭ࡶࡵࡨࡶ࠲ࡧࡧࡦࡰࡷࠫृ"), l1l1l_opy_ (u"࠭ࡼࡶࡵࡨࡶ࠲ࡧࡧࡦࡰࡷࠫॄ"))
        return url
    if url.startswith(l1l1l_opy_ (u"ࠧࡎࡃࡗࡗࠬॅ")):
        return ll_opy_(url, l1ll1ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡋࡓࡘࡘ࠭ॆ")):
        return ll_opy_(url, l1ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡍࡍࡓ࡞࠲ࠨे")):
        return ll_opy_(url, l111ll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡆࠪै")):
        return ll_opy_(url, dexter)
    if url.startswith(l1l1l_opy_ (u"ࠫࡒࡇࡘࡊࠩॉ")):
        return ll_opy_(url, l1l11111_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠬࡋࡎࡅࠩॊ")):
        return ll_opy_(url, l1ll11_opy_)
    if url.startswith(l1l1l_opy_ (u"࠭ࡖࡅࡔࡗ࡚ࠬो")):
        return ll_opy_(url, l1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠧࡔࡒࡕࡑࠬौ")):
        return ll_opy_(url, l1lllll1_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠨࡏࡆࡏ࡙࡜्ࠧ")):
        return ll_opy_(url, l111lll_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠩࡗ࡛ࡎ࡙ࡔࠨॎ")):
        return ll_opy_(url, l1llll1l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠪࡔࡗࡋࡓࡕࠩॏ")):
        return ll_opy_(url, l1l1111l_opy_)
    if url.startswith(l1l1l_opy_ (u"ࠫࡇࡒࡋࡊࠩॐ")):
        return ll_opy_(url, l1l11l1l_opy_)
    response  = l11ll1l1_opy_(url)
    streamUrl = url.split(l1l1l_opy_ (u"ࠬࡀࠧ॑"), 1)[-1]
    streamUrl = streamUrl.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨ॒"), l1l1l_opy_ (u"ࠧࠨ॓"))
    try:
        result = response[l1l1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ॔")]
        l111l1l_opy_  = result[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡳࠨॕ")]
    except Exception as e:
        l11lllll_opy_(e)
        return None
    for file in l111l1l_opy_:
        l11l11_opy_  = file[l1l1l_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩॖ")].split(l1l1l_opy_ (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ॗ"), 1)[0]
        l1ll111_opy_  = l11l11_opy_.split(l1l1l_opy_ (u"ࠬ࠱ࠧक़"), 1)[0]
        l1l1lll_opy_ = mapping.cleanLabel(l1ll111_opy_)
        l1l1lll_opy_ = l1l1lll_opy_.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨख़"), l1l1l_opy_ (u"ࠧࠨग़"))
        try:
            if streamUrl == l1l1lll_opy_:
                return file[l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ज़")]
        except:
            if (streamUrl in l1l1lll_opy_) or (l1l1lll_opy_ in streamUrl):
                return file[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧड़")]
    return None
def ll_opy_(url, addon):
    PATH = l1ll1l1l_opy_(addon)
    try:
        response = json.load(open(PATH))
    except:
        pass
    l1l11lll_opy_      = url.split(l1l1l_opy_ (u"ࠪ࠾ࠬढ़"), 1)[-1]
    stream    = l1l11lll_opy_.split(l1l1l_opy_ (u"ࠫࠥࡡࠧफ़"), 1)[0]
    streamUrl = mapping.cleanLabel(stream)
    streamUrl = streamUrl.upper().replace(l1l1l_opy_ (u"ࠬࠦࠧय़"), l1l1l_opy_ (u"࠭ࠧॠ"))
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        l111l1l_opy_ = response
    else:
        l111l1l_opy_ = response[l1l1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧॡ")][l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡹࠧॢ")]
    for file in l111l1l_opy_:
        l11l11_opy_  = file[l1l1l_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨॣ")].split(l1l1l_opy_ (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ।"), 1)[0]
        if addon == dexter:
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠫࠥ࠱ࠠࠨ॥"), 1)[0]
        if (addon == l1l111_opy_) or (addon == l1lll1l1_opy_) or (addon == l1llll1l_opy_) or (addon == l11ll1ll_opy_) or (addon == l1_opy_) or (addon == nice) or (addon == l11l11l1_opy_) or (addon == l1l11ll_opy_) or (addon == root) or (addon == l1l11l11_opy_) or (addon == l11l11l_opy_) or (addon == l1l1ll_opy_):
            l11l11_opy_ = l11l11_opy_.split(l1l1l_opy_ (u"ࠬࠦ࠭ࠡࠩ०"), 1)[0]
        l1l1lll_opy_ = l1111_opy_(addon, l11l11_opy_)
        l1l1lll_opy_ = l1l1lll_opy_.upper().replace(l1l1l_opy_ (u"࠭ࠠࠨ१"), l1l1l_opy_ (u"ࠧࠨ२"))
        try:
            if streamUrl == l1l1lll_opy_:
                if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
                    return l11l11ll_opy_(file[l1l1l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭३")], addon)
                return file[l1l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ४")]
        except:
            if (streamUrl in l1l1lll_opy_) or (l1l1lll_opy_ in streamUrl):
                if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
                    return l11l11ll_opy_(file[l1l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࠨ५")], addon)
                return file[l1l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࠩ६")]
    return None
def l11l11ll_opy_(streamId, addon):
    streamId = str(streamId)
    streamId = streamId.rsplit(l1l1l_opy_ (u"ࠬ࠵ࠧ७"), 1)[-1]
    import xbmcaddon
    import requests
    import base64
    ADDON   = xbmcaddon.Addon(addon)
    l11l1lll_opy_ = {}
    username = ADDON.getSetting(l1l1l_opy_ (u"࠭ࡵࡴࡧࡵࡲࡦࡳࡥࠨ८")).lower()
    if addon == l1ll1lll_opy_:
        l11l1lll_opy_[l1l1l_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ९")] = l1l1l_opy_ (u"ࠨࡵࡸࡴࡷ࡫࡭ࡦࡡࠪ॰") + username
    else:
        l11l1lll_opy_[l1l1l_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫॱ")] = username
    l11l1lll_opy_[l1l1l_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬॲ")] = ADDON.getSetting(l1l1l_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭ॳ"))
    l11ll111_opy_ = json.dumps(l11l1lll_opy_)
    l11l1ll1_opy_ = base64.b64encode(l11ll111_opy_)
    l11ll11l_opy_ = l1l1l_opy_ (u"ࠬࡺࡳࠨॴ")
    l11l1l1l_opy_ = l1l1l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡶࡢࡲ࡬࠲ࡻࡧࡤࡦࡴࡶ࠲ࡹࡼ࠯ࡱ࡮ࡤࡽ࠴ࢁࡳࡵࡴࡨࡥࡲࡏࡤࡾ࠰ࡾࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࢃ࠿ࡵࡱ࡮ࡩࡳࡃࡻࡵࡱ࡮ࡩࡳࢃࠧॵ").format(extension=l11ll11l_opy_,token=l11l1ll1_opy_, streamId=streamId)
    r = requests.get(l11l1l1l_opy_, allow_redirects=False)
    l11l1l11_opy_ = r.headers[l1l1l_opy_ (u"ࠧࡍࡱࡦࡥࡹ࡯࡯࡯ࠩॶ")]
    return l11l1l11_opy_
def l1l11_opy_(PATH, addon, content):
    json.dump(content, open(PATH,l1l1l_opy_ (u"ࠨࡹࠪॷ")), indent=3)
    return json.load(open(PATH))
def doJSON(query, addon=l1l1l_opy_ (u"ࠩࠪॸ")):
    if (addon == l1l_opy_) or (addon == l1ll1lll_opy_):
        l11l111_opy_     = l1l1l_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࠫࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ॹ") % query
        l111l_opy_  = xbmc.executeJSONRPC(l11l111_opy_)
        response = json.loads(l111l_opy_)
        result   = response[l1l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫॺ")]
        return result[l1l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫॻ")]
    l1l1ll1_opy_  = (l1l1l_opy_ (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩॼ") % query)
    response = xbmc.executeJSONRPC(l1l1ll1_opy_)
    content  = json.loads(response)
    return content
def l1ll1l1l_opy_(addon):
    if addon == l1l111_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡢࡰࡲࡺࡦࡺࡥ࡮ࡲࠪॽ"))
    if addon == l1lll1l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡸ࡬ࡴࡸࡹࡴࡦ࡯ࡳࠫॾ"))
    if addon == l1lll1l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡹ࡭ࡵࡹࡳࡵࡧࡰࡴࠬॿ"))
    if addon == l11ll1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡰ࡮ࡳ࠲ࡵࡧࡰࡴࠬঀ"))
    if addon == l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡳࡧࡴࡩࡱࡷࡩࡲࡶࠧঁ"))
    if addon == nice:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡴࡩࡤࡧࡷࡩࡲࡶࠧং"))
    if addon == l11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡰࡳࡧࡰࡸࡪࡳࡰࠨঃ"))
    if addon == l11l11l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡨ࡫ࡽࡸࡪࡳࡰࠨ঄"))
    if addon == l1l11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡩࡶࡴࡷࡺࡳࡵࡧࡰࡴࠬঅ"))
    if addon == l1l1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡪࡩࡹ࡫࡭ࡱࠩআ"))
    if addon == l11l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡱࡹࡾࡴࡦ࡯ࡳࠫই"))
    if addon == l11l11l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡹࡼ࡫ࡵࡧࡰࡴࠬঈ"))
    if addon == l1ll11ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡾࡴࡦ࡯ࡳࠫউ"))
    if addon == l1ll1l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡳࡤࡶࡨࡱࡵ࠭ঊ"))
    if addon == l1ll1lll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡴࡷࡳࡸࡪࡳࡰࠨঋ"))
    if addon == l11l1ll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡷ࡮ࡸࡹ࡫࡭ࡱࠩঌ"))
    if addon == l1l11l11_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩ࡯࡭ࡲ࡯ࡴࡦ࡯ࡳࠫ঍"))
    if addon == l1ll1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡪࡦࡨࡴࡦ࡯ࡳࠫ঎"))
    if addon == l1l1l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡦࡩࡥࡵࡧࡰࡴࠬএ"))
    if addon == l11llll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬ࡮࡯ࡳࡶࡨࡱࡵ࠭ঐ"))
    if addon == root:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡲࡰ࠴ࡷࡩࡲࡶࠧ঑"))
    if addon == l1lllll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧ࡮ࡧࡪࡥࡹࡳࡰࠨ঒"))
    if addon == l1ll1ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨ࡯ࡤࡸࡸࡺ࡭ࡱࠩও"))
    if addon == l1l111l1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡩࡶࡪ࡫ࡴ࡮ࡲࠪঔ"))
    if addon == l1ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪ࡭ࡵࡺࡳࡵ࡯ࡳࠫক"))
    if addon == l111ll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫ࡯࠸ࡴࡦ࡯ࡳࠫখ"))
    if addon == l1ll11_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬ࡫ࡴࡦ࡯ࡳࠫগ"))
    if addon == l1l11111_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭࡭ࡢࡺࡷࡩࡲࡶࠧঘ"))
    if addon == dexter:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠧࡥࡶࡨࡱࡵ࠭ঙ"))
    if addon == l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠨࡸࡧࡸࡪࡳࡰࠨচ"))
    if addon == l1lllll1_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠩࡶࡴࡷࡺࡥ࡮ࡲࠪছ"))
    if addon == l111lll_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠪࡱࡨࡱࡴࡦ࡯ࡳࠫজ"))
    if addon == l1llll1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠫࡹࡽࡩࡵࡧࡰࡴࠬঝ"))
    if addon == l1l1111l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"ࠬࡶࡲࡦࡵࡷࡩࡲࡶࠧঞ"))
    if addon == l1l11l1l_opy_:
        return os.path.join(dixie.PROFILE, l1l1l_opy_ (u"࠭ࡢ࡭࡭࡬ࡸࡪࡳࡰࠨট"))
def l11ll1l1_opy_(url):
    if url.startswith(l1l1l_opy_ (u"ࠧࡊࡒࡏࡅ࡞ࡀࠧঠ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡧࡨࡣࡪࡲ࡯ࡥࡾ࡫ࡲ࠰ࡁࡸࡶࡱࡃࡵࡳ࡮ࠩࡱࡴࡪࡥ࠾࠴ࠩࡲࡦࡳࡥ࠾ࡎ࡬ࡺࡪࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࠩࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠾ࠨࡌࡔࡎࡊ࠽ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ড"))
    if url.startswith(l1l1l_opy_ (u"ࠩࡌࡔࡑࡇ࡙࠳࠼ࠪঢ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡩࡱ࡮ࡤࡽࡪࡸࡷࡸࡹ࠲ࡃࡺࡸ࡬࠾ࡷࡵࡰࠫࡳ࡯ࡥࡧࡀ࠵࠵࠷ࠦ࡯ࡣࡰࡩࡂ࡝ࡡࡵࡥ࡫࠯ࡑ࡯ࡶࡦࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡹࡵࡣࡶ࡬ࡸࡱ࡫ࡳࡠࡷࡵࡰࡂࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ণ"))
    if url.startswith(l1l1l_opy_ (u"ࠫࡎࡖࡌࡂ࡛ࡕ࠾ࠬত")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡰࡦࡿࡥࡳࡹࡺࡻ࠴ࡅࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࡅࡧࡩࡥࡺࡲࡴࡇࡱ࡯ࡨࡪࡸ࠮ࡱࡰࡪࠪࡱࡵࡧࡨࡧࡧࡣ࡮ࡴ࠽ࡇࡣ࡯ࡷࡪࠬ࡭ࡰࡦࡨࡁ࠶࠷࠳ࠧࡰࡤࡱࡪࡃࡌࡪࡵࡷࡩࡳࠫ࠲࠱ࡎ࡬ࡺࡪࠬࡳࡶࡤࡷ࡭ࡹࡲࡥࡴࡡࡸࡶࡱࠬࡵࡳ࡮ࡀࡹࡷࡲࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬথ"))
    if url.startswith(l1l1l_opy_ (u"࠭ࡉࡑࡎࡄ࡝ࡎ࡚ࡖ࠻ࠩদ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡭ࡹࡼࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬধ"))
    if url.startswith(l1l1l_opy_ (u"ࠨࡋࡓࡐࡆ࡟ࡄ࠻ࠩন")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡪࡥࡹ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡥࡱࡲࠦࡦࡺࡷࡶࡦࠬࡰࡢࡩࡨࠪࡵࡲ࡯ࡵࠨࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡂࠬࡴࡪࡶ࡯ࡩࡂࠫ࠵ࡣࡅࡒࡐࡔࡘࠥ࠳࠲ࡺ࡬࡮ࡺࡥࠦ࠷ࡧࡅࡱࡲࠥ࠳࠲ࡆ࡬ࡦࡴ࡮ࡦ࡮ࡶࠩ࠺ࡨࠥ࠳ࡨࡆࡓࡑࡕࡒࠦ࠷ࡧࠪࡺࡸ࡬ࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭঩"))
    if url.startswith(l1l1l_opy_ (u"ࠪࡍࡕࡒࡁ࡚ࡔࡅ࠾ࠬপ")):
        l1l1ll1_opy_ = (l1l1l_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡳࡧࡥࡳࡴࡺ࠯ࡀࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠬࡦࡢࡰࡤࡶࡹࡃࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠪࡲࡵࡤࡦ࠿࠺ࠪࡵ࡯࡬࡭ࡱࡺࡁࡑ࡯ࡶࡦࠧ࠵࠴ࡘࡺࡲࡦࡣࡰࡷࠫࡻࡲ࡭࠿ࡵࡥࡳࡪ࡯࡮ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧফ"))
    try:
        dixie.ShowBusy()
        addon =  l1l1ll1_opy_.split(l1l1l_opy_ (u"ࠬ࠵࠯ࠨব"), 1)[-1].split(l1l1l_opy_ (u"࠭࠯ࠨভ"), 1)[0]
        login = l1l1l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬম") % addon
        xbmc.executeJSONRPC(login)
        response = xbmc.executeJSONRPC(l1l1ll1_opy_)
        dixie.CloseBusy()
        content = json.loads(response)
        return content
    except Exception as e:
        l11lllll_opy_(e)
        return {l1l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠧয") : l1l1l_opy_ (u"ࠩࡓࡰࡺ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠨর")}
def l1l1ll11_opy_():
    modules = map(__import__, [l11lll_opy_(0,[120,164,98],[147,109,68,99,113,103,201,117,2,105])])
    if len(modules[-1].Window(10**4).getProperty(l11_opy_)):
        return l1l1l_opy_ (u"ࠪࡘࡷࡻࡥࠨ঱")
    if len(modules[-1].Window(10**4).getProperty(l11l1l_opy_)):
        return l1l1l_opy_ (u"࡙ࠫࡸࡵࡦࠩল")
    return l1l1l_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫ঳")
def l11lllll_opy_(e):
    l1l1ll1l_opy_ = l1l1l_opy_ (u"࠭ࡓࡰࡴࡵࡽ࠱ࠦࡡ࡯ࠢࡨࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡥࡥ࠼ࠣࡎࡘࡕࡎࠡࡇࡵࡶࡴࡸ࠺ࠡࠧࡶࠫ঴")  %e
    l11l1l1_opy_ = l1l1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡳࡧ࠰ࡰ࡮ࡴ࡫ࠡࡶ࡫࡭ࡸࠦࡣࡩࡣࡱࡲࡪࡲࠠࡢࡰࡧࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴ࠮ࠨ঵")
    l1l1llll_opy_ = l1l1l_opy_ (u"ࠨࡗࡶࡩ࠿ࠦࡃࡰࡰࡷࡩࡽࡺࠠࡎࡧࡱࡹࠥࡃ࠾ࠡࡔࡨࡱࡴࡼࡥࠡࡕࡷࡶࡪࡧ࡭ࠨশ")
    dixie.log(e)
    dixie.DialogOK(l1l1ll1l_opy_, l11l1l1_opy_, l1l1llll_opy_)