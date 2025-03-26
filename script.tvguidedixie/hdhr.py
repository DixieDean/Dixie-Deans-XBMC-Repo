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
import json
import os
import dixie
def createHDHRINI():
    l1ll_opy_ = dixie.PROFILE
    path = os.path.join(l1ll_opy_, l11l1_opy_ (u"ࠫ࡮ࡴࡩࠨࠀ"))
    l11_opy_  = os.path.join(path, l11l1_opy_ (u"ࠬ࡮ࡤࡩࡴ࠱࡭ࡳ࡯ࠧࠁ"))
    response = getHDHRChannels()
    result   = response[l11l1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ࠂ")]
    l1l_opy_ = result[l11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡸ࠭ࠃ")]
    l1l11l_opy_  = file(l11_opy_, l11l1_opy_ (u"ࠨࡹࠪࠄ"))
    l1l11l_opy_.write(l11l1_opy_ (u"ࠩ࡞ࡷࡨࡸࡩࡱࡶ࠱࡬ࡩ࡮࡯࡮ࡧࡵࡹࡳ࠴ࡶࡪࡧࡺࡡࡡࡴࠧࠅ"))
    for channel in l1l_opy_:
        l1l11_opy_  = channel[l11l1_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩࠆ")]
        l1l11_opy_  = dixie.mapChannelName(l1l11_opy_)
        stream = l11l1_opy_ (u"ࠫࠪࡹࠧࠇ") % channel[l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪࠈ")]
        l1l11l_opy_.write(l11l1_opy_ (u"࠭ࠥࡴࠩࠉ") % l1l11_opy_)
        l1l11l_opy_.write(l11l1_opy_ (u"ࠧ࠾ࠩࠊ"))
        l1l11l_opy_.write(l11l1_opy_ (u"ࠨࠧࡶࠫࠋ") % stream)
        l1l11l_opy_.write(l11l1_opy_ (u"ࠩ࡟ࡲࠬࠌ"))
    l1l11l_opy_.write(l11l1_opy_ (u"ࠪࡠࡳ࠭ࠍ"))
    l1l11l_opy_.close()
def getHDHRChannels():
    l1ll1l_opy_ = getHDHRDevices()
    l1l_opy_   = getChannels(l1ll1l_opy_)
    return l1l_opy_
def getHDHRDevices():
    l1l111_opy_ = getUPNP()
    l111l_opy_  = l1l111_opy_[l11l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࠎ")]
    l11lll_opy_     = l111l_opy_[l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࠏ")]
    for l1l1ll_opy_ in l11lll_opy_:
        l1l11_opy_   = l1l1ll_opy_[l11l1_opy_ (u"࠭࡬ࡢࡤࡨࡰࠬࠐ")]
        l1lll_opy_ = l11l1_opy_ (u"ࠧࠦࡵࠪࠑ") % l1l1ll_opy_[l11l1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࠒ")]
        if l11l1_opy_ (u"ࠩࡋࡈࡍࡵ࡭ࡦࡔࡸࡲࠬࠓ") in l1l11_opy_:
            return l1lll_opy_
def getUPNP():
    l1l1_opy_   = (l11l1_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡹࡵࡴࡰ࠻࠱࠲ࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿࠷ࡽࠨࠔ"))
    result = sendJSON(l1l1_opy_)
    return result
def getChannels(l1ll1l_opy_):
    l111_opy_ = (l11l1_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࡃࡩࡣࡱࡲࡪࡲࡳ࠰ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽࠵ࢂ࠭ࠕ") % l1ll1l_opy_)
    l1l_opy_  = sendJSON(l111_opy_)
    return l1l_opy_
def sendJSON(l1l1l_opy_):
    response = xbmc.executeJSONRPC(l1l1l_opy_)
    return json.loads(response.decode(l11l1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫࠖ"), l11l1_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ࠗ")))