# coding: UTF-8
import sys
l1l11lll_opy_ = sys.version_info [0] == 2
l1111l1_opy_ = 2048
l1ll11l1_opy_ = 7
def l1l1l_opy_ (l11lll_opy_):
	global l111l11_opy_
	l1llll11_opy_ = ord (l11lll_opy_ [-1])
	l1l1l1l1_opy_ = l11lll_opy_ [:-1]
	l11ll1l_opy_ = l1llll11_opy_ % len (l1l1l1l1_opy_)
	l111ll_opy_ = l1l1l1l1_opy_ [:l11ll1l_opy_] + l1l1l1l1_opy_ [l11ll1l_opy_:]
	if l1l11lll_opy_:
		l1llll_opy_ = unicode () .join ([unichr (ord (char) - l1111l1_opy_ - (l1lll_opy_ + l1llll11_opy_) % l1ll11l1_opy_) for l1lll_opy_, char in enumerate (l111ll_opy_)])
	else:
		l1llll_opy_ = str () .join ([chr (ord (char) - l1111l1_opy_ - (l1lll_opy_ + l1llll11_opy_) % l1ll11l1_opy_) for l1lll_opy_, char in enumerate (l111ll_opy_)])
	return eval (l1llll_opy_)
import xbmc
import xbmcaddon
def getURL(url):
    l11l1l11_opy_ = l1l1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡇ࡮ࡤࡻࡱ࡫ࡳࡴࡖࡹࠫज")
    ADDON   =  xbmcaddon.Addon(l11l1l11_opy_)
    path    =  ADDON.getAddonInfo(l1l1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧझ"))
    import sys
    sys.path.insert(0, path)
    import iptv2
    url    = url.split(l1l1l_opy_ (u"ࠪ࠾ࠬञ"), 1)[-1]
    stream = iptv2.GetStreamURLByChannelID(url)
    return stream