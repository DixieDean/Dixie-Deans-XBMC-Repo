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
def createPVRINI():
    if not dixie.PVRACTIVE:
        return
    l1ll_opy_ = dixie.PROFILE
    path = os.path.join(l1ll_opy_, l11l1_opy_ (u"࠭ࡩ࡯࡫ࠪઍ"))
    l11_opy_  = os.path.join(path, l11l1_opy_ (u"ࠧࡱࡸࡵ࠲࡮ࡴࡩࠨ઎"))
    try:
        l11l11l1l_opy_  = _getPVRChannels(l11l1_opy_ (u"ࠨࠤࡷࡺࠧ࠭એ"))
        l11l11ll1_opy_ = l11l11l1l_opy_[l11l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩઐ")]
    except: pass
    try:
        l11l11lll_opy_  = _getPVRChannels(l11l1_opy_ (u"ࠪࠦࡷࡧࡤࡪࡱࠥࠫઑ"))
        l11l11l11_opy_ = l11l11lll_opy_[l11l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ઒")]
    except: pass
    try:
        l11l1l111_opy_  = l11l11ll1_opy_[l11l1_opy_ (u"ࠬࡩࡨࡢࡰࡱࡩࡱࡹࠧઓ")]
        l11l1l1l1_opy_  = l11l11l11_opy_[l11l1_opy_ (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡳࠨઔ")]
    except: pass
    l1l11l_opy_  = file(l11_opy_, l11l1_opy_ (u"ࠧࡸࠩક"))
    l1l11l_opy_.write(l11l1_opy_ (u"ࠨ࡝ࡶࡧࡷ࡯ࡰࡵ࠰ࡲࡲ࠲ࡺࡡࡱࡲ࠱ࡸࡻࡣ࡜࡯ࠩખ"))
    try:
        for channel in l11l1l111_opy_:
            l1l11_opy_  = channel[l11l1_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨગ")]
            l1l11_opy_  = dixie.mapChannelName(l1l11_opy_)
            stream = l11l1_opy_ (u"ࠪࠩࡸ࠭ઘ") % channel[l11l1_opy_ (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡮ࡪࠧઙ")]
            l1l11l_opy_.write(l11l1_opy_ (u"ࠬࠫࡳࠨચ") % l1l11_opy_)
            l1l11l_opy_.write(l11l1_opy_ (u"࠭࠽ࠨછ"))
            l1l11l_opy_.write(l11l1_opy_ (u"ࠧࠦࡵࠪજ") % stream)
            l1l11l_opy_.write(l11l1_opy_ (u"ࠨ࡞ࡱࠫઝ"))
    except: pass
    try:
        for channel in l11l1l1l1_opy_:
            l1l11_opy_  = channel[l11l1_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨઞ")]
            l1l11_opy_  = dixie.mapChannelName(l1l11_opy_)
            stream = l11l1_opy_ (u"ࠪࠩࡸ࠭ટ") % channel[l11l1_opy_ (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡮ࡪࠧઠ")]
            l1l11l_opy_.write(l11l1_opy_ (u"ࠬࠫࡳࠨડ") % l1l11_opy_)
            l1l11l_opy_.write(l11l1_opy_ (u"࠭࠽ࠨઢ"))
            l1l11l_opy_.write(l11l1_opy_ (u"ࠧࠦࡵࠪણ") % stream)
            l1l11l_opy_.write(l11l1_opy_ (u"ࠨ࡞ࡱࠫત"))
    except: pass
    l1l11l_opy_.write(l11l1_opy_ (u"ࠩ࡟ࡲࠬથ"))
    l1l11l_opy_.close()
def _getPVRChannels(group):
    method   = l11l1_opy_ (u"ࠪࡔ࡛ࡘ࠮ࡈࡧࡷࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷࠬદ")
    params   = l11l1_opy_ (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡬ࡸ࡯ࡶࡲ࡬ࡨࠬધ")
    l11l1l11l_opy_  =  getGroupID(group)
    response =  sendJSON(method, params, l11l1l11l_opy_)
    return response
def getGroupID(group):
    method   = l11l1_opy_ (u"ࠬࡖࡖࡓ࠰ࡊࡩࡹࡉࡨࡢࡰࡱࡩࡱࡍࡲࡰࡷࡳࡷࠬન")
    params   = l11l1_opy_ (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡴࡺࡲࡨࠫ઩")
    response =  sendJSON(method, params, group)
    result   =  response[l11l1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧપ")]
    groups   =  result[l11l1_opy_ (u"ࠨࡥ࡫ࡥࡳࡴࡥ࡭ࡩࡵࡳࡺࡶࡳࠨફ")]
    for group in groups:
        l1l11_opy_ = group[l11l1_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨબ")]
        if l1l11_opy_ == l11l1_opy_ (u"ࠪࡅࡱࡲࠠࡤࡪࡤࡲࡳ࡫࡬ࡴࠩભ"):
            return group[l11l1_opy_ (u"ࠫࡨ࡮ࡡ࡯ࡰࡨࡰ࡬ࡸ࡯ࡶࡲ࡬ࡨࠬમ")]
def sendJSON(method, params, value):
    l1l1ll1_opy_  = (l11l1_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࠪࡹࠢ࠭ࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࠫࡳࠣ࠼ࠨࡷࢂ࠲ࠠࠣ࡫ࡧࠦ࠿࠷ࡽࠨય") % (method, params, value))
    response = xbmc.executeJSONRPC(l1l1ll1_opy_)
    return json.loads(response.decode(l11l1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬર"), l11l1_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧ઱")))