# coding: UTF-8
import sys
l1l11l1l_opy_ = sys.version_info [0] == 2
l1llll11_opy_ = 2048
l1l1ll11_opy_ = 7
def l11ll_opy_ (l1l11l_opy_):
	global l1llllll_opy_
	l1ll1ll1_opy_ = ord (l1l11l_opy_ [-1])
	l1l1l1l1_opy_ = l1l11l_opy_ [:-1]
	l11l11l_opy_ = l1ll1ll1_opy_ % len (l1l1l1l1_opy_)
	l11ll1_opy_ = l1l1l1l1_opy_ [:l11l11l_opy_] + l1l1l1l1_opy_ [l11l11l_opy_:]
	if l1l11l1l_opy_:
		l1llll_opy_ = unicode () .join ([unichr (ord (char) - l1llll11_opy_ - (l111l11_opy_ + l1ll1ll1_opy_) % l1l1ll11_opy_) for l111l11_opy_, char in enumerate (l11ll1_opy_)])
	else:
		l1llll_opy_ = str () .join ([chr (ord (char) - l1llll11_opy_ - (l111l11_opy_ + l1ll1ll1_opy_) % l1l1ll11_opy_) for l111l11_opy_, char in enumerate (l11ll1_opy_)])
	return eval (l1llll_opy_)
import xbmc
import xbmcgui
import xbmcaddon
import json
import time
import datetime
import os
import dixie
import mapping
l1l111l_opy_  = l11ll_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡊࡱࡧࡷ࡭ࡧࡶࡷ࡙ࡼࠧࠀ")
l11lll1_opy_   = l11ll_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡭ࡵࡲࡪࡼࡲࡲ࡮ࡶࡴࡷࠩࠁ")
l1_opy_   = l11ll_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡬ࡡࡣࡪࡲࡷࡹ࡯࡮ࡨࠩࠂ")
l11llll1_opy_     = l11ll_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡡࡤࡧࡷࡺࠬࠃ")
l1lll1_opy_     = l11ll_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡳࡱࡲࡸࡎࡖࡔࡗࠩࠄ")
l1l111l1_opy_ = l11ll_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡎ࡬ࡱ࡮ࡺ࡬ࡦࡵࡶࡍࡕ࡚ࡖࠨࠅ")
l1ll_opy_     = l11ll_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡙ࡅࡉࡋࡒࠨࠆ")
l1ll111l_opy_   = l11ll_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡸࡥࡢ࡯ࡶࡹࡵࡸࡥ࡮ࡧ࠵ࠫࠇ")
l1lll1l_opy_      = l11ll_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡩࡴࡷࠩࠈ")
l111l1l_opy_   = l11ll_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡺࡶ࡬࡫ࡱ࡫ࡸ࠭ࠉ")
l11lll1l_opy_      = l11ll_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡬ࡪࡷࡻ࠲ࡹࡼࠧࠊ")
l1ll1ll_opy_    = l11ll_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡵࡩࡦࡳࡳࡦࡣࡶࡽ࠳ࡺࡶࠨࠋ")
l1ll1l_opy_  = l11ll_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡰࡥࡷࡺࡨࡶࡤࠪࠌ")
l11l11_opy_  = l11ll_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡹࡾࡧ࠲ࠨࠍ")
l1ll11ll_opy_   = [l111l1l_opy_, l1ll111l_opy_, l1lll1l_opy_, l1ll_opy_, l1l111l1_opy_, l1l111l_opy_, l11lll1_opy_, l1_opy_, l11llll1_opy_, l1lll1_opy_]
OPEN_OTT  = dixie.OPEN_OTT
CLOSE_OTT = dixie.CLOSE_OTT
def isValid(stream):
    if l11ll_opy_ (u"ࠫࡍࡕࡒࡊ࡜࠽ࠫࠎ") in stream:
        dixie.log(l11ll_opy_ (u"ࠬ࠳࠭࠮ࠢࡋࡓࡗࡏ࡚ࡐࡐࠣࡘࡗ࡛ࡅࠡ࠯࠰࠱ࠬࠏ"))
        return True
    if l11ll_opy_ (u"࠭ࡆࡍࡃ࠽ࠫࠐ") in stream:
        dixie.log(l11ll_opy_ (u"ࠧ࠮࠯࠰ࠤࡋࡒࡁࡘࡎࡈࡗࡘࠦࡔࡓࡗࡈࠤ࠲࠳࠭ࠨࠑ"))
        return True
    if l11ll_opy_ (u"ࠨࡈࡄࡆ࠿࠭ࠒ") in stream:
        dixie.log(l11ll_opy_ (u"ࠩ࠰࠱࠲ࠦࡆࡂࡄࡌࡔ࡙࡜ࠠࡕࡔࡘࡉࠥ࠳࠭࠮ࠩࠓ"))
        return True
    if l11ll_opy_ (u"ࠪࡅࡈࡋ࠺ࠨࠔ") in stream:
        dixie.log(l11ll_opy_ (u"ࠫ࠲࠳࠭ࠡࡃࡆࡉ࡙࡜ࠠࡕࡔࡘࡉࠥ࠳࠭࠮ࠩࠕ"))
        return True
    if l11ll_opy_ (u"ࠬࡘࡏࡐࡖ࠵࠾ࠬࠖ") in stream:
        dixie.log(l11ll_opy_ (u"࠭࠭࠮࠯ࠣࡖࡔࡕࡔ࠳ࠢࡗࡖ࡚ࡋࠠ࠮࠯࠰ࠫࠗ"))
        return True
    if l11ll_opy_ (u"ࠧࡍࡋࡐࡍ࡙ࡀࠧ࠘") in stream:
        dixie.log(l11ll_opy_ (u"ࠨ࠯࠰࠱ࠥࡒࡉࡎࡋࡗࡐࡊ࡙ࡓࠡࡖࡕ࡙ࡊࠦ࠭࠮࠯ࠪ࠙"))
        return True
    if l11ll_opy_ (u"࡙ࠩࡈࡗ࡚ࡖ࠻ࠩࠚ") in stream:
        dixie.log(l11ll_opy_ (u"ࠪ࠱࠲࠳ࠠࡗࡃࡇࡉࡗࠦࡔࡓࡗࡈࠤ࠲࠳࠭ࠨࠛ"))
        return True
    if l11ll_opy_ (u"ࠫࡘ࡛ࡐ࠻ࠩࠜ") in stream:
        dixie.log(l11ll_opy_ (u"ࠬ࠳࠭࠮ࠢࡖ࡙ࡕࡘࡅࡎࡇࠣࡘࡗ࡛ࡅࠡ࠯࠰࠱ࠬࠝ"))
        return True
    if l11ll_opy_ (u"࠭ࡓࡄࡖ࡙࠾ࠬࠞ") in stream:
        dixie.log(l11ll_opy_ (u"ࠧ࠮࠯࠰ࠤࡘࡉࡔࡗࠢࡗࡖ࡚ࡋࠠ࠮࠯࠰ࠫࠟ"))
        return True
    if l11ll_opy_ (u"ࠨࡖ࡙ࡏ࠿࠭ࠠ") in stream:
        dixie.log(l11ll_opy_ (u"ࠩ࠰࠱࠲ࠦࡔࡗࡍࡌࡒࡌ࡙ࠠࡕࡔࡘࡉࠥ࠳࠭࠮ࠩࠡ"))
        return True
    dixie.log(l11ll_opy_ (u"ࠪ࠱࠲࠳ࠠࡗࡃࡏࡍࡉࠦࡆࡂࡎࡖࡉࠥ࠳࠭࠮ࠩࠢ"))
    return False
def getRecording(name, title, start, stream):
    dixie.log(l11ll_opy_ (u"ࠫࡂࡃ࠽࠾࠿ࡀࠤ࡬࡫ࡴࡓࡧࡦࡳࡷࡪࡩ࡯ࡩࠣࡁࡂࡃ࠽࠾࠿ࠪࠣ"))
    l11llll_opy_   =  stream.split(l11ll_opy_ (u"ࠬࢂࠧࠤ"))
    l11ll1l_opy_    =  getAddonInfo(l11llll_opy_)
    catchup   = l11ll_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦ࡯ࡳࡣࡱ࡫ࡪࡣࠠ࡜ࡅࡤࡸࡨ࡮࠭ࡶࡲࠣࡅࡻࡧࡩ࡭ࡣࡥࡰࡪࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨࠥ")
    l11lll11_opy_ = l11ll_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࠥࡡࡎࡰࠢࡆࡥࡹࡩࡨ࠮ࡷࡳࠤࡆࡼࡡࡪ࡮ࡤࡦࡱ࡫࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࠦ")
    options = []
    l1l_opy_ = []
    for item in l11ll1l_opy_:
        l1lllll_opy_ =  item[0]
        l1lllll_opy_ = l11ll_opy_ (u"ࠨ࡝ࡅࡡࠬࠧ") + l1lllll_opy_ + l11ll_opy_ (u"ࠩ࡞࠳ࡇࡣࠧࠨ")
        addon =  item[1]
        l1l1l_opy_ = l1l1111l_opy_(addon)
        l1lll1ll_opy_ = l1l1l11l_opy_(addon, name)
        dixie.log(l1l1l_opy_)
        dixie.log(l1lll1ll_opy_)
        if not l1l1l_opy_:
            l111l1_opy_ = l1lllll_opy_ + l11lll11_opy_
            options.append(l111l1_opy_)
            l1l_opy_.append(addon)
        if l1l1l_opy_ and not l1lll1ll_opy_:
            l111l1_opy_ = l1lllll_opy_ + l11lll11_opy_
            options.append(l111l1_opy_)
            l1l_opy_.append(addon)
        if l1l1l_opy_ and l1lll1ll_opy_:
            l1lll_opy_ = l1lllll_opy_ + catchup
            options.append(l1lll_opy_)
            l1l_opy_.append(addon)
    l1llll1l_opy_ = xbmcgui.Dialog().select(l11ll_opy_ (u"ࠪࡗࡊࡒࡅࡄࡖࠣࡇࡆ࡚ࡃࡉ࠯ࡘࡔࠥࡇࡄࡅ࠯ࡒࡒࠬࠩ"), options)
    addon  = l1l_opy_[l1llll1l_opy_]
    if l1llll1l_opy_ > -1:
        return getIPTVRecording(addon, name, title, start, stream)
    dixie.DialogOK(l11ll_opy_ (u"ࠫࡓࡵࠠࡄࡣࡷࡧ࡭࠳ࡵࡱࠢࡄࡨࡩ࠳࡯࡯ࠢࡖࡩࡱ࡫ࡣࡵࡧࡧ࠲ࠬࠪ"), l11ll_opy_ (u"ࠬࡘࡥࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡏ࡭ࡻ࡫ࠠࡕࡘ࠱ࠫࠫ"))
    return
def getAddonInfo(l11llll_opy_):
    import plugins
    l11ll1l_opy_ = []
    for stream in l11llll_opy_:
        info    = plugins.getPluginInfo(stream, kodiID=True)
        l1lllll_opy_   = info[0]
        addon   = info[1]
        result  = [l1lllll_opy_, addon]
        if result not in l11ll1l_opy_:
            l11ll1l_opy_.append(result)
    dixie.log(l11ll1l_opy_)
    return l11ll1l_opy_
def l1l1111l_opy_(addon):
    for item in l1ll11ll_opy_:
        if addon == item:
            return True
    return False
def l1l1l11l_opy_(addon, name):
    l11l111_opy_ = l1l1l1l_opy_(addon)
    dixie.log(l11l111_opy_)
    for item in l11l111_opy_:
        l1ll11l1_opy_  = name.upper()
        channel = item[0].upper()
        if l1ll11l1_opy_ == channel:
            return True
    return False
def l1l1l1l_opy_(addon):
    HOME  = dixie.PROFILE
    iPATH = os.path.join(HOME, l11ll_opy_ (u"࠭ࡩ࡯࡫ࠪࠬ"))
    if addon == l1_opy_:
        l11111_opy_ = os.path.join(iPATH, l11ll_opy_ (u"ࠧࡤࡣࡷࡧ࡭ࡻࡰࡇࡃࡅ࠲࡯ࡹ࡯࡯ࠩ࠭"))
        return json.load(open(l11111_opy_))
    if (addon == l1l111l_opy_) or (addon == l11lll1_opy_):
        l11111_opy_ = os.path.join(iPATH, l11ll_opy_ (u"ࠨࡥࡤࡸࡨ࡮ࡵࡱࡈࡏࡅ࠳ࡰࡳࡰࡰࠪ࠮"))
        return json.load(open(l11111_opy_))
    if addon == l11llll1_opy_:
        l11111_opy_ = os.path.join(iPATH, l11ll_opy_ (u"ࠩࡦࡥࡹࡩࡨࡶࡲࡄࡇࡊ࠴ࡪࡴࡱࡱࠫ࠯"))
        return json.load(open(l11111_opy_))
    if (addon == l1lll1_opy_) or (addon == l1l111l1_opy_) or (addon == l111l1l_opy_):
        l11111_opy_ = os.path.join(iPATH, l11ll_opy_ (u"ࠪࡧࡦࡺࡣࡩࡷࡳࡖࡔࡕࡔ࠯࡬ࡶࡳࡳ࠭࠰"))
        return json.load(open(l11111_opy_))
    if (addon == l1ll_opy_) or (addon == l1ll111l_opy_) or (addon == l1lll1l_opy_):
        l11111_opy_ = os.path.join(iPATH, l11ll_opy_ (u"ࠫࡨࡧࡴࡤࡪࡸࡴ࡛ࡇࡄࡆࡔ࠱࡮ࡸࡵ࡮ࠨ࠱"))
        return json.load(open(l11111_opy_))
    return [[l11ll_opy_ (u"ࠧࡔ࡯࡯ࡧࠥ࠲"), l11ll_opy_ (u"ࠨࡎࡰࡰࡨࠦ࠳")]]
def getIPTVRecording(addon, name, title, start, stream):
    dixie.log(l11ll_opy_ (u"ࠧࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࠣࡇࡆ࡚ࡃࡉࠢࡘࡔࠥࡏࡐࡕࡘࠣࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥࠧ࠴"))
    dixie.log(addon)
    dixie.log(name)
    dixie.log(title)
    dixie.log(start)
    dixie.log(stream)
    l1ll111_opy_ = l1lll111_opy_(addon)
    l1l1l1_opy_  = start - datetime.timedelta(seconds=l1ll111_opy_)
    dixie.log(l11ll_opy_ (u"ࠨࡇࡓࡋ࡙ࠥࡴࡢࡴࡷࠤ࡙࡯࡭ࡦ࠰࠱࠲࠿ࠦࠥࡴࠩ࠵") % start)
    dixie.log(l11ll_opy_ (u"ࠩࡈࡔࡌࠦࡓࡵࡣࡵࡸ࡚ࠥࡩ࡮ࡧࠣࡓࡋࡌࡓࡆࡖ࠽ࠤࠪࡹࠧ࠶") % l1l1l1_opy_)
    l11l_opy_ = str(l1l1l1_opy_)
    dixie.log(l11ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡵ࡭ࡳ࡭࠺ࠡࠧࡶࠫ࠷") % l11l_opy_)
    l11_opy_   = l11l_opy_.split(l11ll_opy_ (u"ࠫࠥ࠭࠸"))[0]
    l1l1lll1_opy_  = l11l_opy_.split(l11ll_opy_ (u"ࠬࠦࠧ࠹"))[1]
    l1ll1l1_opy_   = time.strptime(l11_opy_, l11ll_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࠨ࠺"))
    theDate    = l1l11ll1_opy_(addon, l1ll1l1_opy_)
    dixie.log(l11ll_opy_ (u"ࠧࡵࡪࡨࡈࡦࡺࡥ࠻ࠢࠨࡷࠬ࠻") % theDate)
    l1ll1111_opy_  = time.strptime(l1l1lll1_opy_,  l11ll_opy_ (u"ࠨࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪ࠼"))
    theTime    = time.strftime(l11ll_opy_ (u"ࠩࠨࡌ࠿ࠫࡍࠨ࠽"),  l1ll1111_opy_)
    dixie.log(l11ll_opy_ (u"ࠪࡸ࡭࡫ࡔࡪ࡯ࡨ࠾ࠥࠫࡳࠨ࠾") % theTime)
    return getCatchupLink(addon, name, title, theDate, theTime)
def l1lll111_opy_(addon):
    l111ll1_opy_ = l1l1ll1l_opy_()
    if (addon == l1ll_opy_) or (addon == l1ll111l_opy_) or (addon == l1lll1l_opy_):
        l1ll111_opy_ = -l111ll1_opy_ - 3600
        dixie.log(l11ll_opy_ (u"࡛ࠫࡇࡄࡆࡔࠣࡘࡎࡓࡅ࡛ࡑࡑࡉ࠿ࠦࠥࡴࠩ࠿") % l111ll1_opy_)
        dixie.log(l11ll_opy_ (u"ࠬ࡜ࡁࡅࡇࡕࠤࡔࡌࡆࡔࡇࡗ࠾ࠥࠫࡳࠨࡀ") % l1ll111_opy_)
        return l1ll111_opy_
    l1ll111_opy_ = -l111ll1_opy_
    dixie.log(l11ll_opy_ (u"࠭ࡔࡊࡏࡈ࡞ࡔࡔࡅ࠻ࠢࠨࡷࠬࡁ") % l111ll1_opy_)
    dixie.log(l11ll_opy_ (u"ࠧࡐࡈࡉࡗࡊ࡚࠺ࠡࠧࡶࠫࡂ") % l1ll111_opy_)
    return l1ll111_opy_
def l1l1ll1l_opy_():
    dixie.log(l11ll_opy_ (u"ࠨࡆࡄ࡝ࡑࡏࡇࡉࡖ࠽ࠤࠪࡹࠧࡃ") % time.daylight)
    dixie.log(l11ll_opy_ (u"ࠩࡗࡍࡒࡋ࡚ࡐࡐࡈ࠾ࠥࠫࡳࠨࡄ") % time.timezone)
    return time.timezone
def l1l11ll1_opy_(addon, l1ll1l1_opy_):
    if addon == l1_opy_:
        dixie.log(l11ll_opy_ (u"ࠪࡪࡦࡨࡩࡱࡶࡹࠫࡅ"))
        l11lllll_opy_ = time.strftime(l11ll_opy_ (u"ࠫࠪࡧࠠࠦࡦࠪࡆ"), l1ll1l1_opy_)
        dixie.log(l1ll1l1_opy_)
        dixie.log(l11lllll_opy_)
        return l11lllll_opy_
    if (addon == l11llll1_opy_) or (addon == l1ll_opy_) or (addon == l1ll111l_opy_) or (addon == l1lll1l_opy_):
        return time.strftime(l11ll_opy_ (u"ࠬࠫࡤ࠯ࠧࡰࠫࡇ"), l1ll1l1_opy_)
    if (addon == l1lll1_opy_) or (addon == l1l111l1_opy_) or (addon == l111l1l_opy_):
        return time.strftime(l11ll_opy_ (u"࡚࠭ࠥ࠱ࠨࡱ࠴ࠫࡤࠨࡈ"), l1ll1l1_opy_)
    return time.strftime(l11ll_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࠩࡉ"), l1ll1l1_opy_)
def getCatchupLink(addon, channel, theShow, theDate, theTime):
    dixie.log(l11ll_opy_ (u"ࠨ࠿ࡀࡁࡂࡃ࠽ࠡࡩࡨࡸࡈࡧࡴࡤࡪࡸࡴࡑ࡯࡮࡬ࠢࡀࡁࡂࡃ࠽࠾ࠩࡊ"))
    LABELFILE = l1ll1l11_opy_(addon)
    dixie.log(l11ll_opy_ (u"ࠩࡀࡁࡂࡃ࠽࠾ࠢࡏࡅࡇࡋࡌࡇࡋࡏࡉ࠱ࠦ࡬ࡢࡤࡨࡰࡲࡧࡰࡴࠢࡀࡁࡂࡃ࠽࠾ࠩࡋ"))
    labelmaps = json.load(open(LABELFILE))
    dixie.log(LABELFILE)
    dixie.log(labelmaps)
    l1l11ll_opy_  = l11ll_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴࠭ࡌ") + addon
    l1111l_opy_ =  l111_opy_(addon)
    try:
        l11111l_opy_  = findCatchup(l11ll_opy_ (u"ࠫࡨࡧࡴࡤࡪࡸࡴࡱ࡯࡮࡬ࠩࡍ"), addon, l1l11ll_opy_, l1111l_opy_)
        l11l1l_opy_  = mapping.mapLabel(labelmaps, channel)
        l11l1l_opy_  = l11l1l_opy_.upper()
        dixie.log(l11ll_opy_ (u"ࠬࡃ࠽࠾࠿ࡀࡁࠥࡩࡡࡵࡥ࡫ࡹࡵࡲࡩ࡯࡭ࠣࡁࡂࡃ࠽࠾࠿ࠪࡎ"))
        print addon, l11111l_opy_, l11l1l_opy_
        if (addon == l1ll_opy_) or (addon == l1ll111l_opy_) or (addon == l1lll1l_opy_):
            l1l1llll_opy_ = l1l11l11_opy_(l11ll_opy_ (u"࠭ࡖࡂࡆࡈࡖࠥࡉࡨࡢࡰࡱࡩࡱࡹࠧࡏ"), addon, l11l1l_opy_)
        else:
            l1l1llll_opy_ = findCatchup(l11ll_opy_ (u"ࠧࡵࡪࡨࡇ࡭ࡧ࡮࡯ࡧ࡯ࠫࡐ"), addon, l11111l_opy_, l11l1l_opy_)
        dixie.log(l11ll_opy_ (u"ࠨ࠿ࡀࡁࡂࡃ࠽ࠡࡶ࡫ࡩࡈ࡮ࡡ࡯ࡰࡨࡰࠥ࡬ࡩ࡯ࡦࡆࡥࡹࡩࡨࡶࡲࠣࡁࡂࡃ࠽࠾࠿ࠪࡑ"))
        print addon, l11111l_opy_, l11l1l_opy_, l1l1llll_opy_
        l1l11lll_opy_ = l1l1ll_opy_(addon, theDate, theTime)
        l1lll11_opy_      = findCatchup(l11ll_opy_ (u"ࠩࡷ࡬ࡪࡒࡩ࡯࡭ࠪࡒ"), addon, l1l1llll_opy_, l1l11lll_opy_, splitlabel=True)
        dixie.CloseBusy()
        return l1lll11_opy_
    except:
        dixie.CloseBusy()
        dixie.DialogOK(l11ll_opy_ (u"ࠪࡗࡴࡸࡲࡺ࠰ࠪࡓ"), l11ll_opy_ (u"ࠫ࡜࡫ࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡪ࡮ࡴࡤࠡࡣࠣࡧࡦࡺࡣࡩࡷࡳࠤࡸࡺࡲࡦࡣࡰࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡰࡳࡱࡪࡶࡦࡳ࠮ࠨࡔ"), l11ll_opy_ (u"ࠬࡘࡥࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡏ࡭ࡻ࡫ࠠࡕࡘ࠱ࠫࡕ"))
        return l11ll_opy_ (u"࠭ࠧࡖ")
def l1l11l11_opy_(string, addon, item):
    dixie.log(l11ll_opy_ (u"ࠧ࠾࠿ࡀࡁࡂࡃࠠࡨࡧࡷࡗࡪࡩࡴࡪࡱࡱࡷࠥࡃ࠽࠾࠿ࡀࡁࠬࡗ"))
    l1111l1_opy_ = [l11ll_opy_ (u"ࠨ࠵ࠪࡘ"), l11ll_opy_ (u"ࠩ࠻࡙ࠫ"), l11ll_opy_ (u"ࠪ࠽࡚ࠬ"),l11ll_opy_ (u"ࠫ࠶࠶࡛ࠧ"), l11ll_opy_ (u"ࠬ࠸࠸ࠨ࡜")]
    l111111_opy_ = []
    for l1111l_opy_ in l1111l1_opy_:
        query = l11ll_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠧࡶ࠳ࡨࡧࡴࡤࡪࡸࡴ࠴ࡩࡡࡵࡧࡪࡳࡷࡿ࠯ࠦࡵࠪ࡝") % (addon, l1111l_opy_)
        dixie.log(l11ll_opy_ (u"ࠧ࠾࠿ࡀࡁࡂࡃࠠࡲࡷࡨࡶࡾࠦ࠽࠾࠿ࡀࡁࡂ࠭࡞"))
        dixie.log(query)
        response = sendJSON(query, addon)
        dixie.log(l11ll_opy_ (u"ࠨ࠿ࡀࡁࡂࡃ࠽ࠡࡳࡸࡩࡷࡿࠠࡓࡇࡖ࡙ࡑ࡚ࠠ࠾࠿ࡀࡁࡂࡃࠧ࡟"))
        dixie.log(response)
        l111111_opy_.extend(response)
    for file in l111111_opy_:
        l1l1lll_opy_ = file[l11ll_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࡠ")]
        dixie.log(l11ll_opy_ (u"ࠪࡁࡂࡃ࠽࠾࠿࡚ࠣࡆࡊࡅࡓࠢࡕࡅ࡜ࠦࡌࡂࡄࡈࡐࠥࡃ࠽࠾࠿ࡀࡁࠬࡡ"))
        dixie.log(l1l1lll_opy_)
        l111l_opy_ = mapping.cleanLabel(l1l1lll_opy_)
        l1lllll_opy_  = cleanPrefix(l111l_opy_)
        l1lllll_opy_  = l1lllll_opy_.upper()
        if l1lllll_opy_ == item.upper():
            dixie.log(l11ll_opy_ (u"ࠫࡂࡃ࠽࠾࠿ࡀࠤ࡛ࡇࡄࡆࡔࠣࡑࡆ࡚ࡃࡉࠢࡉࡓ࡚ࡔࡄࠡ࠿ࡀࡁࡂࡃ࠽ࠨࡢ"))
            dixie.log(item)
            dixie.log(l1lllll_opy_)
            return file[l11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪࡣ")]
def sendJSON(query, addon):
    l1111ll_opy_     = l11ll_opy_ (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࠧࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࡤ") % query
    l1111_opy_  = xbmc.executeJSONRPC(l1111ll_opy_)
    response = json.loads(l1111_opy_)
    result   = response[l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧࡥ")]
    return result[l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡹࠧࡦ")]
def l1ll1l11_opy_(addon):
    HOME  = dixie.PROFILE
    iPATH = os.path.join(HOME, l11ll_opy_ (u"ࠩ࡬ࡲ࡮࠭ࡧ"))
    if addon == l1_opy_:
         return os.path.join(iPATH, l11ll_opy_ (u"ࠪࡧࡦࡺࡣࡩࡷࡳࡊࡆࡈ࠮࡫ࡵࡲࡲࠬࡨ"))
    if (addon == l1l111l_opy_) or (addon == l11lll1_opy_):
         return os.path.join(iPATH, l11ll_opy_ (u"ࠫࡨࡧࡴࡤࡪࡸࡴࡋࡒࡁ࠯࡬ࡶࡳࡳ࠭ࡩ"))
    if addon == l11llll1_opy_:
        return os.path.join(iPATH, l11ll_opy_ (u"ࠬࡩࡡࡵࡥ࡫ࡹࡵࡇࡃࡆ࠰࡭ࡷࡴࡴࠧࡪ"))
    if (addon == l1lll1_opy_) or (addon == l1l111l1_opy_) or (addon == l111l1l_opy_):
        return os.path.join(iPATH, l11ll_opy_ (u"࠭ࡣࡢࡶࡦ࡬ࡺࡶࡒࡐࡑࡗ࠲࡯ࡹ࡯࡯ࠩ࡫"))
    if (addon == l1ll_opy_) or (addon == l1ll111l_opy_) or (addon == l1lll1l_opy_):
        return os.path.join(iPATH, l11ll_opy_ (u"ࠧࡤࡣࡷࡧ࡭ࡻࡰࡗࡃࡇࡉࡗ࠴ࡪࡴࡱࡱࠫ࡬"))
def l111_opy_(addon):
    dixie.log(l11ll_opy_ (u"ࠨ࠿ࡀࡁࡂࡃ࠽ࠡࡩࡨࡸࡈࡧࡴࡤࡪࡸࡴࡘ࡫ࡣࡵ࡫ࡲࡲࠥࡃ࠽࠾࠿ࡀࡁࠬ࡭"))
    dixie.log(addon)
    l1111l1_opy_ = [[l1_opy_, l11ll_opy_ (u"ࠩࡉࡅࡇࠦࡃࡂࡖࡆࡌ࡚ࡖࠧ࡮")], [l1l111l_opy_, l11ll_opy_ (u"ࠪࡊࡑࡇࡗࡍࡇࡖࡗࠥࡉࡁࡕࡅࡋ࡙ࡕ࠭࡯")], [l11lll1_opy_, l11ll_opy_ (u"ࠫࡍࡕࡒࡊ࡜ࡒࡒࠥࡉࡁࡕࡅࡋ࡙ࡕ࠭ࡰ")], [l11llll1_opy_, l11ll_opy_ (u"࡚ࠬࡖࠡࡅࡄࡘࡈࡎࠠࡖࡒࠪࡱ")], [l1lll1_opy_, l11ll_opy_ (u"࠭ࡃࡂࡖࡆࡌ࡚ࡖࠠࡕࡘࠪࡲ")], [l1l111l1_opy_, l11ll_opy_ (u"ࠧࡄࡃࡗࡇࡍ࡛ࡐࠡࡖ࡙ࠫࡳ")], [l1ll_opy_, l11ll_opy_ (u"ࠨࡖ࡙ࠤࡈࡇࡔࡄࡊࡘࡔࠬࡴ")], [l1ll111l_opy_, l11ll_opy_ (u"ࠩࡗ࡚ࠥࡉࡁࡕࡅࡋ࡙ࡕ࠭ࡵ")], [l1lll1l_opy_, l11ll_opy_ (u"ࠪࡘ࡛ࠦࡃࡂࡖࡆࡌ࡚ࡖࠧࡶ")], [l111l1l_opy_, l11ll_opy_ (u"ࠫࡈࡇࡔࡄࡊࡘࡔ࡚ࠥࡖࠨࡷ")]]
    for l1111l_opy_ in l1111l1_opy_:
        if addon == l1111l_opy_[0]:
            dixie.log(l11ll_opy_ (u"ࠬࡃ࠽࠾࠿ࡀࡁࠥࡹࡥࡤࡶ࡬ࡳࡳࠦࡦࡰࡷࡱࡨࠥࡃ࠽࠾࠿ࡀࡁࠬࡸ"))
            dixie.log(l1111l_opy_[1])
            return l1111l_opy_[1]
def findCatchup(string, addon, query, item, splitlabel=False):
    dixie.log(l11ll_opy_ (u"࠭࠽࠾࠿ࡀࡁࡂࠦࡆࡊࡐࡇࠤࡈࡇࡔࡄࡊࡘࡔࠥࡏࡔࡆࡏࠣࡁࡂࡃ࠽࠾࠿ࠪࡹ"))
    dixie.log(string)
    response = doJSON(query)
    l111111_opy_    = response[l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧࡺ")][l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡹࠧࡻ")]
    dixie.log(l111111_opy_)
    for file in l111111_opy_:
        l1l1lll_opy_ = file[l11ll_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࡼ")]
        dixie.log(l11ll_opy_ (u"ࠪࡁࡂࡃ࠽࠾࠿ࠣࡖࡆ࡝ࠠࡍࡃࡅࡉࡑࠦ࠽࠾࠿ࡀࡁࡂ࠭ࡽ"))
        dixie.log(l1l1lll_opy_)
        l111l_opy_   = mapping.cleanLabel(l1l1lll_opy_)
        l1lllll_opy_    = cleanPrefix(l111l_opy_)
        if splitlabel:
            l1lllll_opy_ = l1l1l111_opy_(addon, l1lllll_opy_)
        else:
            l1lllll_opy_ = l1lllll_opy_.upper()
        dixie.log(l11ll_opy_ (u"ࠫࡂࡃ࠽࠾࠿ࡀࠤࡋࡏࡎࡅࠢࡆࡅ࡙ࡉࡈࡖࡒࠣࡁࡂࡃ࠽࠾࠿ࠪࡾ"))
        dixie.log(item)
        dixie.log(l1lllll_opy_)
        if l1lllll_opy_ == item.upper():
            dixie.log(l11ll_opy_ (u"ࠬࡃ࠽࠾࠿ࡀࡁࠥࡓࡁࡕࡅࡋࠤࡋࡕࡕࡏࡆࠣࡁࡂࡃ࠽࠾࠿ࠪࡿ"))
            dixie.log(item)
            dixie.log(l1lllll_opy_)
            return file[l11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࠫࢀ")]
def l1l1l111_opy_(addon, l1lllll_opy_):
    l1lllll_opy_ = l1lllll_opy_.upper()
    if addon == l11llll1_opy_:
        return l1lllll_opy_.rsplit(l11ll_opy_ (u"ࠧࠊࠩࢁ"), 1)[0]
    return l1lllll_opy_.rsplit(l11ll_opy_ (u"ࠨࠢ࠰ࠤࠬࢂ"), 1)[0]
def l1l1ll_opy_(addon, theDate, theTime):
    if addon == l1_opy_:
        return theDate.upper() + l11ll_opy_ (u"ࠩࠣࠫࢃ") + theTime
    if addon == l11llll1_opy_:
        return theDate + l11ll_opy_ (u"ࠪࠍࠬࢄ") + theTime
    return theDate + l11ll_opy_ (u"ࠫࠥ࠳ࠠࠨࢅ") + theTime
def doJSON(query):
    l1l1l11_opy_  = (l11ll_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࢆ") % query)
    response = xbmc.executeJSONRPC(l1l1l11_opy_)
    content  = json.loads(response)
    return content
def cleanPrefix(text):
    l1l1111_opy_ = text.strip()
    l1ll1_opy_  = [l11ll_opy_ (u"࠭ࡕࡌ࠼ࠪࢇ"), l11ll_opy_ (u"ࠧࡊࡐࡗ࠾ࠥ࠭࢈"), l11ll_opy_ (u"ࠨࡎࡌ࡚ࡊࠦࠧࢉ"), l11ll_opy_ (u"ࠩࡘࡏࠥࡲࠠࠨࢊ"),l11ll_opy_ (u"ࠪࡍࡓࡀࠠࠨࢋ"), l11ll_opy_ (u"ࠫࡎࡔࠠ࡭ࠢࠪࢌ"), l11ll_opy_ (u"ࠬࡏࡎࠡࡾࠣࠫࢍ"), l11ll_opy_ (u"࠭ࡄࡆࠢ࡯ࠤࠬࢎ"), l11ll_opy_ (u"ࠧࡓࡃࡇࠤࡱࠦࠧ࢏"), l11ll_opy_ (u"ࠨࡘࡌࡔࠥࡲࠠࠨ࢐"), l11ll_opy_ (u"ࠩࠣࡐࡴࡩࡡ࡭ࠩ࢑"), l11ll_opy_ (u"࡙ࠪࡘࡇ࠯ࡄࡃࠣ࠾ࠥ࠭࢒"), l11ll_opy_ (u"࡚࡙ࠫࡁ࠰ࡅࡄ࠾ࠥ࠭࢓"), l11ll_opy_ (u"ࠬࡉࡁ࠻ࠢࠪ࢔"),l11ll_opy_ (u"࠭ࡃࡂࠢ࠽ࠤࠬ࢕"),l11ll_opy_ (u"ࠧࡄࡃࠣࠫ࢖"),l11ll_opy_ (u"ࠨࡗࡎࠤ࡛ࡏࡐࠡ࠼ࠣࠫࢗ"), l11ll_opy_ (u"ࠩࡘࡏࠥࡀࠠࠨ࢘"), l11ll_opy_ (u"࡙ࠪࡐࡀࠠࠨ࢙"), l11ll_opy_ (u"࡚ࠫࡑࠠࡽ࢚ࠢࠪ"), l11ll_opy_ (u"࡛ࠬࡓࡂࠢ࠽ࠤࡑࡏࡖࡆ࢛ࠢࠪ"), l11ll_opy_ (u"࠭ࡕࡔࡃࠣࢀࠥࡒࡉࡗࡇࠣࠫ࢜"), l11ll_opy_ (u"ࠧࡖࡕࡄࠤ࠿ࠦࠧ࢝"), l11ll_opy_ (u"ࠨࡗࡖࡅࠥࡀࠧ࢞"), l11ll_opy_ (u"ࠩࡘࡗࡆࡀࠠࠨ࢟"), l11ll_opy_ (u"࡙ࠪࡘࡇࠠࡽࠢࠪࢠ"), l11ll_opy_ (u"࡚࡙ࠫࡁࠡࠩࢡ"), l11ll_opy_ (u"࡛ࠬࡓࠡࡾࠣࠫࢢ"),l11ll_opy_ (u"࠭ࡕࡔ࠼ࠣࠫࢣ"), l11ll_opy_ (u"ࠧࡏࡑࡕࡈࡎࡉࠠࠨࢤ")]
    for prefix in l1ll1_opy_:
        if prefix in l1l1111_opy_:
            l1l1111_opy_ = l1l1111_opy_.replace(prefix, l11ll_opy_ (u"ࠨࠩࢥ"))
    return l1l1111_opy_.strip()
def l11lll_opy_(addon, name, title, start, stream):
    import time
    dixie.log(l11ll_opy_ (u"ࠩࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࠥࡉࡁࡕࡅࡋࠤ࡚ࡖࠠࡍ࡚ࡗ࡚ࠥࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࠩࢦ"))
    l1l111ll_opy_ = stream.split(l11ll_opy_ (u"ࠪࢀࠬࢧ"))
    for url in l1l111ll_opy_:
        if (l1ll1ll_opy_ in url) or (l11lll1l_opy_ in url):
            dixie.log(l11ll_opy_ (u"ࠫࡑ࡞ࡔࡗࠢࡘࡖࡑ࠴࠮࠯࠼ࠣࠩࡸ࠭ࢨ") % url)
            l1llll1_opy_ = url.split(CLOSE_OTT)[0].replace(OPEN_OTT, l11ll_opy_ (u"ࠬ࠭ࢩ"))
            break
    import urllib
    l1ll111_opy_ = l1lllll1_opy_()
    dixie.log(l11ll_opy_ (u"࠭ࡅࡑࡉࠣࡗࡹࡧࡲࡵࠢࡗ࡭ࡲ࡫࠮࠯࠰࠽ࠤࠪࡹࠧࢪ") % start)
    dixie.log(l11ll_opy_ (u"ࠧࡐࡨࡩࡷࡪࡺࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡶ࠾ࠥࠫࡳࠨࢫ") % l1ll111_opy_)
    l1l1l1_opy_  =  start - datetime.timedelta(seconds=l1ll111_opy_)
    dixie.log(l11ll_opy_ (u"ࠨࡕࡷࡥࡷࡺࠠࡕ࡫ࡰࡩࠥࡵࡦࡧࡵࡨࡸ࠿ࠦࠥࡴࠩࢬ") % l1l1l1_opy_)
    l11l1l1_opy_     = l111ll_opy_(l1llll1_opy_)
    l11l_opy_ = str(l1l1l1_opy_)
    l1l11l1_opy_   = l11l_opy_.split(l11ll_opy_ (u"ࠩࠣࠫࢭ"))[0]
    l1l1lll1_opy_  = l11l_opy_.split(l11ll_opy_ (u"ࠪࠤࠬࢮ"))[1]
    l11l1_opy_  = time.strptime(l1l1lll1_opy_,  l11ll_opy_ (u"ࠫࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ࢯ"))
    l11l1_opy_  = time.strftime(l11ll_opy_ (u"ࠬࠫࡉ࠻ࠧࡐࠤࠪࡶࠧࢰ"),  l11l1_opy_)
    l1ll1lll_opy_ = time.strptime(l1l11l1_opy_,   l11ll_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࠨࢱ"))
    l1ll1lll_opy_ = time.strftime(l11ll_opy_ (u"ࠧࠦࡃ࠯ࠤࠪࡈࠠࠦࡦࠪࢲ"), l1ll1lll_opy_)
    query = l11ll_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࠩࡸ࠵࠿ࡤࡪࡤࡲࡳ࡫࡬ࡠ࡫ࡧࡁࠪࡹࠦࡥࡣࡷࡩࡂࠫࡳࠧࡦࡤࡸࡪࡥࡴࡪࡶ࡯ࡩࡂࠫࡳࠧ࡫ࡰ࡫ࡂࠬ࡭ࡰࡦࡨࡁࡷ࡫ࡣࡰࡴࡧ࡭ࡳ࡭ࡳࠧࡶ࡬ࡸࡱ࡫࠽ࠦࡵࠪࢳ") % (addon, l11l1l1_opy_, l1l11l1_opy_, l1ll1lll_opy_, l1llll1_opy_)
    l1111ll_opy_  = l11ll_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࢴ") % query
    if not l11l1l1_opy_:
        dixie.DialogOK(l11ll_opy_ (u"ࠪࡗࡴࡸࡲࡺ࠰ࠪࢵ"), l11ll_opy_ (u"ࠫ࡜࡫ࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡪ࡮ࡴࡤࠡࡣࠣࡧࡦࡺࡣࡩࡷࡳࠤࡸ࡫ࡲࡷ࡫ࡦࡩࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡤࡪࡤࡲࡳ࡫࡬࠯ࠩࢶ"), l11ll_opy_ (u"ࠬࡘࡥࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡏ࡭ࡻ࡫ࠠࡕࡘ࠱ࠫࢷ"))
        return None
    l1111_opy_    = xbmc.executeJSONRPC(l1111ll_opy_)
    response   = json.loads(l1111_opy_)
    result     = response[l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ࢸ")]
    l1ll11l_opy_ = result[l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡸ࠭ࢹ")]
    for l1ll1l1l_opy_ in l1ll11l_opy_:
        try:
            l1l11_opy_ = l1ll1l1l_opy_[l11ll_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࢺ")]
            l1lllll_opy_   = l1ll1l1l_opy_[l11ll_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࢻ")]
            if l11l1_opy_ in l1lllll_opy_:
                dixie.DialogOK(l11ll_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡳࡷࡧ࡮ࡨࡧࡠࡇࡦࡺࡣࡩ࠯ࡸࡴࠥࡹࡴࡳࡧࡤࡱࠥ࡬࡯ࡶࡰࡧ࠲ࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࢼ"), l11ll_opy_ (u"ࠫࡔࡴ࠭ࡕࡣࡳࡴ࠳࡚ࡖࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡹࠣࡴࡱࡧࡹ࠻ࠢ࡞ࡇࡔࡒࡏࡓࠢࡲࡶࡦࡴࡧࡦ࡟࡞ࡆࡢࠫࡳ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࢽ") % (title))
                return l1l11_opy_
        except Exception, e:
            dixie.log(l11ll_opy_ (u"ࠬࡋࡒࡓࡑࡕ࠾ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡶ࡫ࡶࡴࡽ࡮ࠡ࡫ࡱࠤ࡬࡫ࡴࡍ࡚ࡗ࡚ࡗ࡫ࡣࡰࡴࡧ࡭ࡳ࡭ࠠࠦࡵࠪࢾ") % str(e))
            dixie.DialogOK(l11ll_opy_ (u"࠭ࡓࡰࡴࡵࡽ࠳࠭ࢿ"), l11ll_opy_ (u"ࠧࡘࡧࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡦࡪࡰࡧࠤࡦࠦࡣࡢࡶࡦ࡬ࡺࡶࠠࡴࡶࡵࡩࡦࡳࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡳࡶࡴ࡭ࡲࡢ࡯࠱ࠫࣀ"), l11ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡࡶࡵࡽࠥࡧࡧࡢ࡫ࡱࠤࡱࡧࡴࡦࡴ࠱ࠫࣁ"))
            return None
def l111ll_opy_(l1llll1_opy_):
    l1llll1_opy_ = l1llll1_opy_.upper()
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩ࠶ࡉࠬࣂ") : return 188
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡅࡇࡉࠠࡆࡃࡖࡘࠬࣃ") : return 363
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡆࡈࡃࠨࣄ") : return 346
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡇࡍࡄࠩࣅ") : return 375
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡁࡍࡋࡅࡍࠥࡏࡒࡆࡎࡄࡒࡉ࠭ࣆ") : return 280
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡂࡐࡌࡑࡆࡒࠠࡑࡎࡄࡒࡊ࡚ࠠࡖࡕࡄࠫࣇ") : return 386
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡃࡑࡍࡒࡇࡌࠡࡒࡏࡅࡓࡋࡔࠨࣈ") : return 19
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡄࡖࡊࡔࡁࠡࡕࡓࡓࡗ࡚ࡓࠡ࠳ࠣࡌࡉࠦࡃࡓࡑࡄࡘࡎࡇࠧࣉ") : return 403
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡅࡗࡋࡎࡂࠢࡖࡔࡔࡘࡔࡔࠢ࠵ࠤࡍࡊࠠࡄࡔࡒࡅ࡙ࡏࡁࠨ࣊") : return 404
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡆࡘࡅࡏࡃࠣࡗࡕࡕࡒࡕࡕࠣ࠷ࠥࡎࡄࠡࡅࡕࡓࡆ࡚ࡉࡂࠩ࣋") : return 405
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡇࡒࡆࡐࡄࠤࡘࡖࡏࡓࡖࡖࠤ࠹ࠦࡈࡅࠢࡆࡖࡔࡇࡔࡊࡃࠪ࣌") : return 406
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡁࡓࡇࡑࡅ࡙ࠥࡐࡐࡔࡗࡗࠥ࠻ࠠࡔࡔࡅࠫ࣍") : return 407
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡂࡖࠣࡘࡍࡋࠠࡓࡃࡆࡉࡘ࠭࣎") : return 273
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡄࡅࡇࠥࡕࡎࡆ࡝ࡋࡈࡢ࣏࠭") : return 210
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡅࡆࡈࠦࡔࡘࡑ࡞ࡌࡉࡣ࣐ࠧ") : return 211
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡆࡊࡏࡎࠡࡕࡓࡓࡗ࡚ࠠ࠲࠲ࠣࡌࡉ࠮ࡔࡆࡕࡗ࣑࠭ࠬ") : return 300
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡇࡋࡉࡏࠢࡖࡔࡔࡘࡔࠡ࠳࠴ࠤࡍࡊࠨࡕࡇࡖࡘ࠮࣒࠭") : return 389
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡈࡅࡊࡐࠣࡗࡕࡕࡒࡕࠢ࠴ࡌࡉ࠮ࡔࡆࡕࡗ࣓࠭ࠬ") : return 285
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡂࡆࡋࡑࠤࡘࡖࡏࡓࡖࠣ࠶ࠥࡎࡄࠩࡖࡈࡗ࡙࠯ࠧࣔ") : return 286
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡃࡇࡌࡒ࡙ࠥࡐࡐࡔࡗࠤ࠸ࠦࡈࡅࠪࡗࡉࡘ࡚ࠩࠨࣕ") : return 287
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡄࡈࡍࡓࠦࡓࡑࡑࡕࡘࠥ࠺ࠠࡉࡆࠫࡘࡊ࡙ࡔࠪࠩࣖ") : return 288
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡅࡉࡎࡔࠠࡔࡒࡒࡖ࡙ࠦ࠵ࠡࡊࡇ࡙ࠬࡋࡓࡕࠫࠪࣗ") : return 289
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡆࡊࡏࡎࠡࡕࡓࡓࡗ࡚ࠠ࠷ࠢࡋࡈ࡚࠭ࡅࡔࡖࠬࠫࣘ") : return 290
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡇࡋࡉࡏࠢࡖࡔࡔࡘࡔࠡ࠹ࠣࡌࡉ࠮ࡔࡆࡕࡗ࠭ࠬࣙ") : return 291
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡈࡅࡊࡐࠣࡗࡕࡕࡒࡕࠢ࠻ࠤࡍࡊࠨࡕࡇࡖࡘ࠮࠭ࣚ") : return 292
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡂࡆࡋࡑࠤࡘࡖࡏࡓࡖࠣ࠽ࠥࡎࡄࠩࡖࡈࡗ࡙࠯ࠧࣛ") : return 293
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡃࡖࠣࡗࡕࡕࡒࡕࠢ࠴ࠤࡍࡊࠠࠩࡖࡈࡗ࡙࠯ࠧࣜ") : return 306
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡄࡗࠤࡘࡖࡏࡓࡖࠣ࠵ࠬࣝ") : return 17
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡅࡘ࡙ࠥࡐࡐࡔࡗࠤ࠷ࠦࡈࡅࠢࠫࡘࡊ࡙ࡔࠪࠩࣞ") : return 307
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡆ࡙ࠦࡓࡑࡑࡕࡘࠥ࠸ࠧࣟ") : return 18
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡇ࡚ࠠࡔࡒࡒࡖ࡙ࠦࡅࡔࡒࡑࠫ࣠") : return 24
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡈࡔࠡࡕࡓࡓࡗ࡚ࠠࡆࡗࡕࡓࡕࡋࠧ࣡") : return 216
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡂࡂࡄ࡜ࠤ࡙࡜ࠧ࣢") : return 299
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡃࡎࡘࡉࠥࡎࡕࡔࡖࡏࡉࡗࠦࡅࡖࡔࡒࡔࡊࣣ࠭") : return 241
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡄࡒࡓࡒࡋࡒࡂࡐࡊࠫࣤ") : return 192
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡅࡓ࡝ࠦࡎࡂࡖࡌࡓࡓ࠭ࣥ") : return 185
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡆࡗࡏࡔࡊࡕࡋࠤࡊ࡛ࡒࡐࡕࡓࡓࡗ࡚࠲ࠨࣦ") : return 173
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡇࡘࡉࡕࡋࡖࡌࠥࡋࡕࡓࡑࡖࡔࡔࡘࡔࠨࣧ") : return 182
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡉࡂࡔࠢࡕࡉࡆࡒࡉࡕ࡛ࠪࣨ") : return 190
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡃࡏࡄࡆࣩࠫ") : return 366
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡄࡐࡑࠫ࣪") : return 365
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡅࡄࡖ࡙ࡕࡏࡏࠢࡑࡉ࡙࡝ࡏࡓࡍ࡙ࠣࡐ࠭࣫") : return 186
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡆࡅࡗ࡚ࡏࡐࡐࡌࡘࡔ࠭࣬") : return 250
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡇࡍࡋࡌࡔࡇࡄࠤ࡙࡜࣭ࠧ") : return 179
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡈࡕࡍࡆࡆ࡜ࠤࡈࡋࡎࡕࡔࡄࡐ࡛ࠥࡓࡂ࣮ࠩ") : return 374
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡉࡏࡎࡇࡇ࡝ࠥࡉࡅࡏࡖࡕࡅࡑ࣯࠭") : return 251
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡃࡐࡏࡈࡈ࡞ࠦࡘࡕࡔࡄࣰࠫ") : return 176
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡄࡔࡌࡑࡊࠦࡉࡏࡘࡈࡗ࡙ࡏࡇࡂࡖࡌࡓࡓࣱ࠭") : return 249
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡆࡄ࡚ࡊࣲ࠭") : return 230
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡇࡍࡘࡉࡏࡗࡇࡕ࡝ࠥࡎࡉࡔࡖࡒࡖ࡞࠭ࣳ") : return 20
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡈࡎ࡙ࡃࡐࡘࡈࡖ࡞ࠦࡓࡄࡋࡈࡒࡈࡋࠧࣴ") : return 103
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡉࡏࡓࡄࡑ࡙ࡉࡗ࡟ࠠࡕࡗࡕࡆࡔ࠭ࣵ") : return 102
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡊࡉࡔࡅࡒ࡚ࡊࡘ࡙࠲ࣶࠩ") : return 98
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡄࡊࡕࡆࡓ࡛ࡋࡒ࡚ࠩࣷ") : return 370
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡅࡋࡖࡒࡊ࡟ࡃࡉࡐࡏࠫࣸ") : return 117
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡆࡌࡗࡓࡋ࡙ࡋࡗࡑࡍࡔࡘࣹࠧ") : return 118
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡈࡗࡕࡔࠠ࠳ࣺࠩ") : return 349
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡉࡘࡖࡎࠨࣻ") : return 348
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡊࡊࡅࡏࠢ࠮࠵ࠬࣼ") : return 278
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡋࡉࡓࠢࡖࡔࡔࡘࡔࡔࠩࣽ") : return 30
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡅࡖࡔࡒࡒࡊ࡝ࡓࠨࣾ") : return 398
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡇࡑ࡛ࠤࡘࡖࡏࡓࡖࡖࠤ࠶࠭ࣿ") : return 352
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡈࡒ࡜ࠥࡔࡅࡘࡕࠪऀ") : return 274
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡊࡓࡑࡊࠠࡖࡍࠪँ") : return 277
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡌ࠷ࠦࡕࡌࠩं") : return 271
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡍࡈࡏࠡࡇࡄࡗ࡙࠭ः") : return 376
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡎࡂࡐࠢࡉࡅࡒࡏࡌ࡚ࠩऄ") : return 377
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡈࡃࡑࠣࡗࡎࡍࡎࡂࡖࡘࡖࡊ࠭अ") : return 378
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡉࡄࡒࠤ࡟ࡕࡎࡆࠩआ") : return 379
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡊࡊࡘ࡛࠭इ") : return 384
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡋࡍࡘ࡚ࡏࡓ࡛࡙ࠣࡐ࠭ई") : return 268
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡌࡎ࡙ࡔࡐࡔ࡜ࠤ࡚࡙ࡁࠨउ") : return 369
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡍࡕࡍࡆࠢ࠮࠵ࠬऊ") : return 279
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡎࡏࡓࡔࡒࡖࠥࡉࡈࡂࡐࡑࡉࡑࠦࡕࡌࠩऋ") : return 183
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡉࡅࠢࡘࡏࠬऌ") : return 229
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡊࡖ࡙ࠤ࠷࠭ऍ") : return 208
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡋࡗ࡚ࠥ࠹ࠧऎ") : return 207
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡌࡘ࡛ࠦ࠴ࠨए") : return 209
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡍ࡙࡜ࠧऐ") : return 206
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡑࡌࡃࠡࡖ࡙ࠫऑ") : return 180
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡓࡉࡐࠢࡖࡘࡆࡊࡉࡖࡏࠣ࠵࠵࠸ࠠࡉࡆࠪऒ") : return 334
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡍࡊࡑࠣࡗ࡙ࡇࡄࡊࡗࡐࠤ࠶࠶࠳ࠡࡊࡇࠫओ") : return 335
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡎࡋࡒࠤࡘ࡚ࡁࡅࡋࡘࡑࠥ࠷࠰࠵ࠢࡋࡈࠬऔ") : return 336
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡏࡌࡓ࡙ࠥࡔࡂࡆࡌ࡙ࡒࠦ࠱࠱࠷ࠣࡌࡉ࠭क") : return 337
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡐࡍࡔࠦࡓࡕࡃࡇࡍ࡚ࡓࠠ࠲࠲࠹ࠤࡍࡊࠧख") : return 338
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡑࡎࡕࠠࡔࡖࡄࡈࡎ࡛ࡍࠡ࠳࠳࠻ࠥࡎࡄࠨग") : return 333
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡒ࡚ࡖࠡࡄࡄࡗࡊ࠭घ") : return 132
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡓࡔࡗࠢࡇࡅࡓࡉࡅࠨङ") : return 131
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡍࡕࡘࠣࡌࡎ࡚ࡓࠢࠩच") : return 135
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡎࡖ࡙ࠤࡒ࡛ࡓࡊࡅࠪछ") : return 217
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡏࡗ࡚ࠥࡘࡏࡄࡍࡖࠫज") : return 133
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡐ࡙࡙࡜ࠧझ") : return 106
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡑࡔ࡚ࡏࡓࡕ࡙ࠣࡐ࠭ञ") : return 215
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡓࡈࡁࠨट") : return 283
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡔࡂࡄࠢࡈࡅࡘ࡚ࠧठ") : return 361
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡎࡊࡅࡎࠤ࡙ࡕࡏࡏࡕࠪड") : return 296
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡏࡃࡗࠤࡌࡋࡏ࡙ࠡࡌࡐࡉࠦࡕࡌࠩढ") : return 269
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡐࡄࡘࡎࡕࡎࡂࡎࠣࡋࡊࡕࡇࡓࡃࡓࡌࡎࡉࠠࡖࡍࠪण") : return 270
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡑࡅ࡙ࡏࡏࡏࡃࡏࠤࡌࡋࡏࡈࡔࡄࡔࡍࡏࡃࠡࡗࡖࡅࠬत") : return 371
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡒࡎࡉࡋࠡࡌࡘࡒࡎࡕࡒࠨथ") : return 297
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡓࡏࡃࡌࠢࡘࡏࠬद") : return 295
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡖࡒࡆࡏࡌࡉࡗ࡙ࡐࡐࡔࡗࡗࠬध") : return 29
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡒࡕࡇࠣࡓࡓࡋࠧन") : return 69
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡓࡖࡈࠤ࡙࡝ࡏ࡜ࡊࡇࡡࠬऩ") : return 70
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡔࡗࡉࡏࡘࠧप") : return 89
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡕࡅࡈࡏࡎࡈࠢࡘࡏࠬफ") : return 26
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡖࡊࡇࡌࠡࡎࡌ࡚ࡊ࡙ࠧब") : return 275
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡘࡑ࡙ࠡࡄࡘࡒࡉࡋࡓࡍࡋࡊࡅࠥ࠷ࠠࡉࡆ࡞ࡈࡊࡣࠧभ") : return 408
    if l1llll1_opy_ == l11ll_opy_ (u"࡙ࠬࡋ࡚ࠢࡑࡉ࡜࡙ࠧम") : return 263
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡓࡌ࡛ࠣ࠵ࠬय") : return 177
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡔࡍ࡜ࠤ࠷࠭र") : return 178
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡕࡎ࡝ࠥࡇࡃࡕࡋࡒࡒࠥࡓࡏࡗࡋࡈࡗࠬऱ") : return 16
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡖࡏ࡞ࠦࡁࡕࡎࡄࡒ࡙ࡏࡃࠨल") : return 174
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡗࡐ࡟ࠠࡄࡑࡐࡉࡉ࡟ࠠࡎࡑ࡙ࡍࡊ࡙ࠧळ") : return 34
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡘࡑ࡙ࠡࡆࡕࡅࡒࡇࡒࡐࡏࠣࡑࡔ࡜ࡉࡆࡕࠪऴ") : return 97
    if l1llll1_opy_ == l11ll_opy_ (u"࡙ࠬࡋ࡚ࠢࡉࡅࡒࡏࡌ࡚ࠢࡐࡓ࡛ࡏࡅࡔࠩव") : return 36
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡓࡌ࡛ࠣࡋࡗࡋࡁࡕࡕࠣࡑࡔ࡜ࡉࡆࡕࠪश") : return 37
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡔࡍ࡜ࠤࡒࡕࡖࡊࡇࡖࠤࡉࡏࡓࡏࡇ࡜ࠫष") : return 220
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡕࡎ࡝ࠥࡖࡒࡆࡏࡌࡉࡗࡋࠠࡎࡑ࡙ࡍࡊ࡙ࠧस") : return 40
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡖࡏ࡞ࠦࡓࡄࡈࡌࡌࡔࡘࡒࡐࡔࠣࡑࡔ࡜ࡉࡆࡕࠪह") : return 41
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡗࡐ࡟ࠠࡔࡇࡏࡉࡈ࡚ࠠࡎࡑ࡙ࡍࡊ࡙ࠧऺ") : return 42
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡘࡑ࡙ࠡࡕࡓࠤࡓࡋࡗࡔࠢࡋࡕࠬऻ") : return 175
    if l1llll1_opy_ == l11ll_opy_ (u"࡙ࠬࡋ࡚ࠢࡖࡔࡔࡘࡔࠡ࠳ࠣࡌࡉࠦࠨࡕࡇࡖࡘ࠮़࠭") : return 301
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡓࡌ࡛ࠣࡗࡕࡕࡒࡕࠢ࠵ࠤࡍࡊࠠࠩࡖࡈࡗ࡙࠯ࠧऽ") : return 302
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡔࡍ࡜ࠤࡘࡖࡏࡓࡖࠣ࠷ࠥࡎࡄࠡࠪࡗࡉࡘ࡚ࠩࠨा") : return 303
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡕࡎ࡝࡙ࠥࡐࡐࡔࡗࠤ࠹ࠦࡈࡅࠢࠫࡘࡊ࡙ࡔࠪࠩि") : return 304
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡖࡏ࡞ࠦࡓࡑࡑࡕࡘࠥ࠻ࠠࡉࡆ࡙ࠣࠬࡋࡓࡕࠫࠪी") : return 305
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡗࡐ࡟ࠠࡔࡒࡒࡖ࡙࡙ࠠ࠲ࠩु") : return 95
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡘࡑ࡙ࠡࡕࡓࡓࡗ࡚ࡓࠡ࠴ࠪू") : return 136
    if l1llll1_opy_ == l11ll_opy_ (u"࡙ࠬࡋ࡚ࠢࡖࡔࡔࡘࡔࡔࠢ࠶ࠫृ") : return 43
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡓࡌ࡛ࠣࡗࡕࡕࡒࡕࡕࠣ࠸ࠬॄ") : return 119
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡔࡍ࡜ࠤࡘࡖࡏࡓࡖࡖࠤ࠺࠭ॅ") : return 120
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡕࡎ࡝࡚ࠥࡈࡓࡋࡏࡐࡊࡘࠠࡎࡑ࡙ࡍࡊ࡙ࠧॆ") : return 96
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡖࡏ࡞ࠦࡌࡊࡘࡌࡒࡌ࠭े") : return 298
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡗࡕࡕࡒࡕࡕࠣࡊ࠶࠭ै") : return 45
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫࡘ࡟ࡆ࡚ࠢࡘࡗࡆ࠭ॉ") : return 383
    if l1llll1_opy_ == l11ll_opy_ (u"࡚ࠬࡃࡎࠢ࠮࠵࡛ࠥࡋࠨॊ") : return 189
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡔࡈ࠶ࠪो") : return 88
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡕࡕࡑࠤ࠶࠭ौ") : return 339
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡖࡖࡒࠥ࠸्ࠧ") : return 340
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡗࡗࡓࠦ࠳ࠨॎ") : return 341
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪࡘࡘࡔࠠ࠵ࠩॏ") : return 342
    if l1llll1_opy_ == l11ll_opy_ (u"࡙࡙ࠫࡎࠡ࠷ࠪॐ") : return 343
    if l1llll1_opy_ == l11ll_opy_ (u"࡚ࠬࡖ࠴ࠢࡌࡉࠬ॑") : return 87
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡔࡓࡃ࡙ࡉࡑࠦࡃࡉࡃࡑࡒࡊࡒࠫ࠲ࠢࡘࡏ॒ࠬ") : return 184
    if l1llll1_opy_ == l11ll_opy_ (u"ࠧࡖࡕࡄࠤࡋࡕࡘࠡࡕࡓࡓࡗ࡚ࡓࠨ॓") : return 347
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨࡗࡖࡅࠥࡔࡅࡕ࡙ࡒࡖࡐ࠭॔") : return 344
    if l1llll1_opy_ == l11ll_opy_ (u"ࠩࡘࡘ࡛ࠦࡉࡆࠩॕ") : return 272
    if l1llll1_opy_ == l11ll_opy_ (u"࡚ࠪࡎ࡜ࡁࠡࡖࡋࡉࠥࡎࡉࡕࡕࠤࠫॖ") : return 130
    if l1llll1_opy_ == l11ll_opy_ (u"࡛ࠫࡏࡁࡔࡃࡗࠤࡌࡕࡌࡇࠩॗ") : return 125
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬ࡝ࡁࡕࡅࡋࠤࡎࡘࡅࡍࡃࡑࡈࠬक़") : return 281
    if l1llll1_opy_ == l11ll_opy_ (u"࠭ࡘ࡙࡚࠴ࠫख़") : return 314
    if l1llll1_opy_ == l11ll_opy_ (u"࡙࡚࡛ࠧ࠶ࠬग़") : return 315
    if l1llll1_opy_ == l11ll_opy_ (u"ࠨ࡚࡛࡜࠸࠭ज़") : return 316
    if l1llll1_opy_ == l11ll_opy_ (u"࡛ࠩ࡜࡝࠺ࠧड़") : return 317
    if l1llll1_opy_ == l11ll_opy_ (u"ࠪ࡜࡝࡞࠵ࠨढ़") : return 318
    if l1llll1_opy_ == l11ll_opy_ (u"ࠫ࡞ࡋࡓࡕࡇࡕࡈࡆ࡟ࠠࠬ࠳ࠪफ़") : return 282
    if l1llll1_opy_ == l11ll_opy_ (u"ࠬࡓࡏࡗ࠶ࡐࡉࡓ࠷ࠧय़") : return 33
def getHDTVRecording(name, title, start, stream):
    l1l111ll_opy_ = stream.split(l11ll_opy_ (u"࠭ࡼࠨॠ"))
    for url in l1l111ll_opy_:
        url   = url.split(CLOSE_OTT)[1].rsplit(l11ll_opy_ (u"ࠧ࠻ࠩॡ"))
        l1l111_opy_ = url[0]
        if l1l111_opy_ == l11ll_opy_ (u"ࠨࡊࡇࡘ࡛࠭ॢ"):
            addon = l11ll_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡵࡰࡥࡷࡺࡨࡶࡤࠪॣ")
        else:
            addon = l11ll_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡹࡾࡧ࠲ࠨ।")
    dixie.log(l11ll_opy_ (u"ࠫࡆࡪࡤࡰࡰࠣࡍࡉ࠴࠮࠯࠼ࠣࠩࡸ࠭॥") % addon)
    Addon  = xbmcaddon.Addon(id=addon)
    path   = Addon.getAddonInfo(l11ll_opy_ (u"ࠬࡶࡡࡵࡪࠪ०"))
    import sys
    sys.path.insert(0, path)
    import api
    l1l1_opy_ = Addon.getSetting(l11ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࠧ१"))
    l1ll11_opy_  = Addon.getSetting(l11ll_opy_ (u"ࠧࡴࡧࡵࡺࡪࡸࠧ२"))
    l1l1ll1_opy_    = l11ll_opy_ (u"ࠨࠨࡧࡁࡰࡵࡤࡪࠨࡶࡁࠬ३") + l1l1_opy_ + l11ll_opy_ (u"ࠩࠩࡳࡂ࠭४") + l1ll11_opy_
    import urllib
    l1ll111_opy_ = l1lllll1_opy_()
    dixie.log(l11ll_opy_ (u"ࠪࡉࡕࡍࠠࡔࡶࡤࡶࡹࠦࡔࡪ࡯ࡨ࠲࠳࠴࠺ࠡࠧࡶࠫ५") % start)
    dixie.log(l11ll_opy_ (u"ࠫࡔ࡬ࡦࡴࡧࡷࠤ࡮ࡴࠠࡴࡧࡦࡳࡳࡪࡳ࠻ࠢࠨࡷࠬ६") % l1ll111_opy_)
    l1l1l1_opy_  =  start - datetime.timedelta(seconds=l1ll111_opy_)
    dixie.log(l11ll_opy_ (u"࡙ࠬࡴࡢࡴࡷࠤ࡙࡯࡭ࡦࠢࡲࡪ࡫ࡹࡥࡵ࠼ࠣࠩࡸ࠭७") % l1l1l1_opy_)
    l11l_opy_ = str(l1l1l1_opy_)
    l11l1ll_opy_  = l11l_opy_.split(l11ll_opy_ (u"࠭ࠠࠨ८"))[0]
    l1lll11l_opy_     = l1lll1l1_opy_(name)
    if not l1lll11l_opy_:
        dixie.DialogOK(l11ll_opy_ (u"ࠧࡔࡱࡵࡶࡾ࠴ࠧ९"), l11ll_opy_ (u"ࠨ࡙ࡨࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡧ࡫ࡱࡨࠥࡧࠠࡤࡣࡷࡧ࡭ࡻࡰࠡࡵࡨࡶࡻ࡯ࡣࡦࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡨ࡮ࡡ࡯ࡰࡨࡰ࠳࠭॰"), l11ll_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢࡷࡶࡾࠦࡡ࡯ࡱࡷ࡬ࡪࡸࠠࡤࡪࡤࡲࡳ࡫࡬࠯ࠩॱ"))
        return None
    l1l11111_opy_  = l11l_opy_.split(l11ll_opy_ (u"ࠪ࠱ࠬॲ"), 1)[-1].rsplit(l11ll_opy_ (u"ࠫ࠿࠭ॳ"), 1)[0]
    theTime    = urllib.quote_plus(l1l11111_opy_)
    response   = api.remote_call( l11ll_opy_ (u"ࠧࡺࡶࡢࡴࡦ࡬࡮ࡼࡥ࠰ࡩࡨࡸࡤࡨࡹࡠࡥ࡫ࡥࡳࡴࡥ࡭ࡡࡤࡲࡩࡥࡤࡢࡶࡨ࠲ࡵ࡮ࡰࠣॴ") , {l11ll_opy_ (u"ࠨࡤࡢࡶࡨࠦॵ"): l11l1ll_opy_, l11ll_opy_ (u"ࠢࡪࡦࠥॶ"): l1lll11l_opy_ } )
    l1ll11l_opy_ = response[l11ll_opy_ (u"ࠣࡤࡲࡨࡾࠨॷ")]
    if not l1ll11l_opy_:
        dixie.DialogOK(l11ll_opy_ (u"ࠩࡖࡳࡷࡸࡹ࠯ࠩॸ"), l11ll_opy_ (u"࡛ࠪࡪࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡩ࡭ࡳࡪࠠࡢࠢࡦࡥࡹࡩࡨࡶࡲࠣࡷࡹࡸࡥࡢ࡯ࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡶࡲࡰࡩࡵࡥࡲ࠴ࠧॹ"), l11ll_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡹࡸࡹࠡࡣࡪࡥ࡮ࡴࠠ࡭ࡣࡷࡩࡷ࠴ࠧॺ"))
        return None
    for l1ll1l1l_opy_ in l1ll11l_opy_:
        l1l11_opy_ = l1ll1l1l_opy_[l11ll_opy_ (u"ࠧࡶ࡬ࡰࡶࠥॻ")]
        if l1l11111_opy_ in l1l11_opy_:
            dixie.DialogOK(l11ll_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦ࡯ࡳࡣࡱ࡫ࡪࡣࡃࡢࡶࡦ࡬࠲ࡻࡰࠡࡵࡷࡶࡪࡧ࡭ࠡࡨࡲࡹࡳࡪ࠮࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩॼ"), l11ll_opy_ (u"ࠧࡐࡰ࠰ࡘࡦࡶࡰ࠯ࡖ࡙ࠤࡼ࡯࡬࡭ࠢࡱࡳࡼࠦࡰ࡭ࡣࡼ࠾ࠥࡡࡃࡐࡎࡒࡖࠥࡵࡲࡢࡰࡪࡩࡢࡡࡂ࡞ࠧࡶ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩॽ") % (title))
            return l1ll1l1l_opy_[l11ll_opy_ (u"ࠣࡷࡵࡰࠧॾ")] + l1l1ll1_opy_
def l1lll1l1_opy_(name):
    l1l1l1ll_opy_   = dixie.PROFILE
    ll_opy_ = os.path.join(l1l1l1ll_opy_, l11ll_opy_ (u"ࠩ࡬ࡲ࡮࠭ॿ"), l11ll_opy_ (u"ࠪࡧࡦࡺࡣࡩࡷࡳ࠲ࡹࡾࡴࠨঀ"))
    l11l111_opy_   = json.load(open(ll_opy_))
    for channel in l11l111_opy_:
        if name.upper() == channel[l11ll_opy_ (u"ࠫࡔ࡚ࡔࡗࠩঁ")].upper():
            return channel[l11ll_opy_ (u"࡛ࠬࡒࡍࠩং")]
def l1lllll1_opy_():
    import time
    gmt = time.gmtime()
    loc = time.localtime()
    GMT = datetime.datetime(*gmt[:6]).isoformat(l11ll_opy_ (u"࠭ࠠࠨঃ"))
    LOC = datetime.datetime(*loc[:6]).isoformat(l11ll_opy_ (u"ࠧࠡࠩ঄"))
    dixie.log(gmt)
    dixie.log(loc)
    l11ll11_opy_ = dixie.parseTime(GMT)
    l111lll_opy_ = dixie.parseTime(LOC)
    dixie.log(l11ll11_opy_)
    dixie.log(l111lll_opy_)
    dixie.log(l11ll_opy_ (u"ࠨࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࠥࡕࡆࡇࡕࡈࡘࠥࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࠪঅ"))
    l1ll111_opy_ = l11ll11_opy_ - l111lll_opy_
    dixie.log(l1ll111_opy_)
    l1ll111_opy_ = ((l1ll111_opy_.days * 86400) + (l1ll111_opy_.seconds + 1800)) / 3600
    dixie.log(l1ll111_opy_)
    l1ll111_opy_ *= -3600
    dixie.log(l1ll111_opy_)
    dixie.log(l11ll_opy_ (u"ࠩࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࠫআ"))
    return l1ll111_opy_