# coding: UTF-8

import sys

l1lll11ll = sys.version_info [0] == 2
l11ll1l1 = 2048
l1111111 = 7

def l1ll11 (l1l1l1l):
	global l11ll1ll
	
	l111lll1 = ord (l1l1l1l [-1])
	l1lll1lll = l1l1l1l [:-1]
	
	l1l1ll1l = l111lll1 % len (l1lll1lll)
	l1l1111 = l1lll1lll [:l1l1ll1l] + l1lll1lll [l1l1ll1l:]
		
	if l1lll11ll:
		l11l1l = unicode () .join ([unichr (ord (char) - l11ll1l1 - (l1lll1 + l111lll1) % l1111111) for l1lll1, char in enumerate (l1l1111)])
	else:
		l11l1l = str () .join ([chr (ord (char) - l11ll1l1 - (l1lll1 + l111lll1) % l1111111) for l1lll1, char in enumerate (l1l1111)])
		
	return eval (l11l1l)




import xbmc
import json
import dixie

def getPVRChannels():
    if not dixie.PVRACTIVE:
        return
    
    l1lll1l11l = list()
    try:
        l1lll1l111  = _1lll1lll1(l1ll11 (u"ࠫࠧࡺࡶࠣࠩࣼ"))
        l1lll1l1l1 = l1lll1l111[l1ll11 (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࣽ")]

        l1lll1ll11  = l1lll1l1l1[l1ll11 (u"࠭ࡣࡩࡣࡱࡲࡪࡲࡳࠨࣾ")]

        for l1l1l1ll1 in l1lll1ll11:
            l1l1l1lll  = l1l1l1ll1[l1ll11 (u"ࠧ࡭ࡣࡥࡩࡱ࠭ࣿ")]
            stream = l1ll11 (u"ࠨࠧࡶࠫऀ") % l1l1l1ll1[l1ll11 (u"ࠩࡦ࡬ࡦࡴ࡮ࡦ࡮࡬ࡨࠬँ")]

            l1lll1l11l.append((l1l1l1lll, stream))
    except: pass

    try:
        l1lll1l1ll  = _1lll1lll1(l1ll11 (u"ࠪࠦࡷࡧࡤࡪࡱࠥࠫं"))
        l1lll11lll = l1lll1l1ll[l1ll11 (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫः")]

        l1llll1111  = l1lll11lll[l1ll11 (u"ࠬࡩࡨࡢࡰࡱࡩࡱࡹࠧऄ")]

        for l1l1l1ll1 in l1llll1111:
            l1l1l1lll  = l1l1l1ll1[l1ll11 (u"࠭࡬ࡢࡤࡨࡰࠬअ")]
            stream = l1ll11 (u"ࠧࠦࡵࠪआ") % l1l1l1ll1[l1ll11 (u"ࠨࡥ࡫ࡥࡳࡴࡥ࡭࡫ࡧࠫइ")]
            
            l1lll1l11l.append((l1l1l1lll, stream))
    except: pass

    return l1lll1l11l


def _1lll1lll1(group):
    method   = l1ll11 (u"ࠩࡓ࡚ࡗ࠴ࡇࡦࡶࡆ࡬ࡦࡴ࡮ࡦ࡮ࡶࠫई")
    params   = l1ll11 (u"ࠪࡧ࡭ࡧ࡮࡯ࡧ࡯࡫ࡷࡵࡵࡱ࡫ࡧࠫउ")
    l1lll1ll1l  =  l1lll1llll(group)
    l1l111ll =  l1llll111l(method, params, l1lll1ll1l)
    
    return l1l111ll
        
    
def l1lll1llll(group):
    method   = l1ll11 (u"ࠫࡕ࡜ࡒ࠯ࡉࡨࡸࡈ࡮ࡡ࡯ࡰࡨࡰࡌࡸ࡯ࡶࡲࡶࠫऊ")
    params   = l1ll11 (u"ࠬࡩࡨࡢࡰࡱࡩࡱࡺࡹࡱࡧࠪऋ")
    l1l111ll =  l1llll111l(method, params, group)
    result   =  l1l111ll[l1ll11 (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ऌ")]
    groups   =  result[l1ll11 (u"ࠧࡤࡪࡤࡲࡳ࡫࡬ࡨࡴࡲࡹࡵࡹࠧऍ")]

    for group in groups:
        l1l1l1lll = group[l1ll11 (u"ࠨ࡮ࡤࡦࡪࡲࠧऎ")]
        
        if l1l1l1lll == l1ll11 (u"ࠩࡄࡰࡱࠦࡣࡩࡣࡱࡲࡪࡲࡳࠨए"):
            return group[l1ll11 (u"ࠪࡧ࡭ࡧ࡮࡯ࡧ࡯࡫ࡷࡵࡵࡱ࡫ࡧࠫऐ")]
    
    
def l1llll111l(method, params, value):
    l1l1ll1ll  = (l1ll11 (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࠩࡸࠨࠬࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࠪࡹࠢ࠻ࠧࡶࢁ࠱ࠦࠢࡪࡦࠥ࠾࠶ࢃࠧऑ") % (method, params, value))
    l1l111ll = xbmc.executeJSONRPC(l1l1ll1ll)
    
    return json.loads(l1ll11 (u"ࡺࠨࠢऒ") + (l1l111ll.decode(l1ll11 (u"࠭ࡵࡵࡨ࠰࠼ࠬओ"), l1ll11 (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧऔ"))))
