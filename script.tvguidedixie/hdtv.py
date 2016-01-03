# coding: UTF-8

import sys

l1llll1ll = sys.version_info [0] == 2
l1l1111l = 2048
l111l111 = 7

def l1lll1 (l1l1lll):
	global l1l111l1
	
	l11l1l1l = ord (l1l1lll [-1])
	l1lllllll = l1l1lll [:-1]
	
	l1ll11l1 = l11l1l1l % len (l1lllllll)
	l1l11l1 = l1lllllll [:l1ll11l1] + l1lllllll [l1ll11l1:]
		
	if l1llll1ll:
		l11lll = unicode () .join ([unichr (ord (char) - l1l1111l - (l1111 + l11l1l1l) % l111l111) for l1111, char in enumerate (l1l11l1)])
	else:
		l11lll = str () .join ([chr (ord (char) - l1l1111l - (l1111 + l11l1l1l) % l111l111) for l1111, char in enumerate (l1l11l1)])
		
	return eval (l11lll)




import xbmc
import json
import time
import datetime
import os

import dixie

PATH    = os.path.join(dixie.PROFILE, l1lll1 (u"ࠩࡷࡩࡲࡶࠧ࢑"))
SETTING = l1lll1 (u"ࠪࡐࡔࡍࡉࡏࡡࡋࡈ࡙࡜ࠧ࢒")


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 8): 
        l1l1l11l = json.load(open(PATH))
    else:
        l1l1l11l = l1ll111ll(url)
        l1ll11111(SETTING)

    stream = url.split(l1lll1 (u"ࠫ࠿࠭࢓"), 1)[-1].lower()
    result = l1l1l11l[l1lll1 (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ࢔")]
    l11l111l  = result[l1lll1 (u"࠭ࡦࡪ࡮ࡨࡷࠬ࢕")]

    for file in l11l111l:
        l1ll111l1   = file[l1lll1 (u"ࠧ࡭ࡣࡥࡩࡱ࠭࢖")]
        l1ll111l1   = l1ll111l1.replace(l1lll1 (u"ࠨࠢ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࢗ"), l1lll1 (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫ࢘"))
        l1l1lllll = l1ll111l1.rsplit(l1lll1 (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡ࢙ࠬ"), 1)[0].split(l1lll1 (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠ࢚ࠫ"), 1)[-1]

        if stream == l1l1lllll.lower():
            return file[l1lll1 (u"ࠬ࡬ࡩ࡭ࡧ࢛ࠪ")]

    return None
    

def l1ll111ll(url):
    l1lll11l    = (l1lll1 (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡂࡃࡄࡅ࠯ࡀࡣࡦࡸ࡮ࡵ࡮࠾࡯ࡤ࡭ࡳࡥ࡬ࡪࡵࡷࠪࡹ࡯ࡴ࡭ࡧࡀࠪࡺࡸ࡬࠾ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧ࢜"))
    l1ll11l11  = (l1lll1 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡃࡄࡅ࠿࠰ࡁࡤࡧࡹ࡯࡯࡯࠿࡯࡭ࡻ࡫ࡴࡷࡡࡤࡰࡱࠬࡴࡪࡶ࡯ࡩࡂࡇ࡬࡭࠭ࡦ࡬ࡦࡴ࡮ࡦ࡮ࡶࠪࡺࡸ࡬࠾ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧ࢝"))

    if url.startswith(l1lll1 (u"ࠨࡊࡇࡘ࡛ࡀࠧ࢞")):
        l1lll11l    = l1lll11l.replace(  l1lll1 (u"ࠩࡂࡃࡄࡅࠧ࢟"), l1lll1 (u"ࠪ࡬ࡩࡺࡶࠨࢠ"))
        l1ll11l11  = l1ll11l11.replace(l1lll1 (u"ࠫࡄࡅ࠿ࡀࠩࢡ"), l1lll1 (u"ࠬ࡮ࡤࡵࡸࠪࢢ"))

    if url.startswith(l1lll1 (u"࠭ࡈࡅࡖ࡙࠶࠿࠭ࢣ")):
        l1lll11l    = l1lll11l.replace(  l1lll1 (u"ࠧࡀࡁࡂࡃࠬࢤ"), l1lll1 (u"ࠨࡴࡸࡽࡦ࡯ࡰࡵࡸࠪࢥ"))
        l1ll11l11  = l1ll11l11.replace(l1lll1 (u"ࠩࡂࡃࡄࡅࠧࢦ"), l1lll1 (u"ࠪࡶࡺࡿࡡࡪࡲࡷࡺࠬࢧ"))

    try:
        message = l1lll1 (u"ࠫࡑࡵࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡵࡱࠣࡷࡪࡸࡶࡦࡴ࠱ࠤࡔࡴࡥࠡ࡯ࡲࡱࡪࡴࡴࠡࡲ࡯ࡩࡦࡹࡥ࠯ࠩࢨ")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll11l)
        l1l1l11l = xbmc.executeJSONRPC(l1ll11l11)
        
        dixie.CloseBusy()
    
        content = json.loads(l1l1l11l.decode(l1lll1 (u"ࠬࡲࡡࡵ࡫ࡱ࠱࠶࠭ࢩ"), l1lll1 (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ࢪ")))
    
        json.dump(content, open(PATH,l1lll1 (u"ࠧࡸࠩࢫ")))

        return content
    
    except Exception:
        dixie.CloseBusy()
        return {l1lll1 (u"ࠨࡇࡵࡶࡴࡸࠧࢬ") : l1lll1 (u"ࠩࡓࡰࡺ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠨࢭ")}


def l1ll11111(l1ll1111l):
    now = datetime.datetime.today()
    dixie.SetSetting(l1ll1111l, str(now))