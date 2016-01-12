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

PATH    = os.path.join(dixie.PROFILE, 'temp')
SETTING = 'LOGIN_HDTV'


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 8): 
        l1l1l11l = json.load(open(PATH))
    else:
        l1l1l11l = l1ll111ll(url)
        l1l1lllll(SETTING)

    stream = url.split(l1lll1 (u"ࠫ࠿࠭࢓"), 1)[-1].lower()
    
    try:
        result = l1l1l11l[l1lll1 (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ࢔")]
        l11l111l  = result[l1lll1 (u"࠭ࡦࡪ࡮ࡨࡷࠬ࢕")]
    
    except Exception as e:
        l1l1llll1(e)
        return None
        
        

    for file in l11l111l:
        l1ll111l1   = file[l1lll1 (u"ࠧ࡭ࡣࡥࡩࡱ࠭࢖")]
        l1ll111l1   = l1ll111l1.replace(l1lll1 (u"ࠨࠢࠣࠫࢗ"), l1lll1 (u"ࠩࠣࠫ࢘")).replace(l1lll1 (u"ࠪࠤࡠ࠵ࡃࡐࡎࡒࡖࡢ࢙࠭"), l1lll1 (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࢚࠭"))
        l1ll11111 = l1ll111l1.rsplit(l1lll1 (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣ࢛ࠧ"), 1)[0].split(l1lll1 (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢ࠭࢜"), 1)[-1]

        if stream == l1ll11111.lower():
            return file[l1lll1 (u"ࠧࡧ࡫࡯ࡩࠬ࢝")]

    return None
    

def l1ll111ll(url):
    l1lll11l    = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡄࡅ࠿ࡀ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡱࡦ࡯࡮ࡠ࡮࡬ࡷࡹࠬࡴࡪࡶ࡯ࡩࡂࠬࡵࡳ࡮ࡀࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩ࢞"))
    l1ll11l11  = (l1lll1 (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡅ࠿ࡀࡁ࠲ࡃࡦࡩࡴࡪࡱࡱࡁࡱ࡯ࡶࡦࡶࡹࡣࡦࡲ࡬ࠧࡶ࡬ࡸࡱ࡫࠽ࡂ࡮࡯࠯ࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬࡵࡳ࡮ࡀࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩ࢟"))

    if url.startswith(l1lll1 (u"ࠪࡌࡉ࡚ࡖ࠻ࠩࢠ")):
        l1lll11l    = l1lll11l.replace(  l1lll1 (u"ࠫࡄࡅ࠿ࡀࠩࢡ"), l1lll1 (u"ࠬ࡮ࡤࡵࡸࠪࢢ"))
        l1ll11l11  = l1ll11l11.replace(l1lll1 (u"࠭࠿ࡀࡁࡂࠫࢣ"), l1lll1 (u"ࠧࡩࡦࡷࡺࠬࢤ"))

    if url.startswith(l1lll1 (u"ࠨࡊࡇࡘ࡛࠸࠺ࠨࢥ")):
        l1lll11l    = l1lll11l.replace(  l1lll1 (u"ࠩࡂࡃࡄࡅࠧࢦ"), l1lll1 (u"ࠪࡶࡺࡿࡡࡪࡲࡷࡺࠬࢧ"))
        l1ll11l11  = l1ll11l11.replace(l1lll1 (u"ࠫࡄࡅ࠿ࡀࠩࢨ"), l1lll1 (u"ࠬࡸࡵࡺࡣ࡬ࡴࡹࡼࠧࢩ"))

    try:
        message = l1lll1 (u"࠭ࡌࡰࡩࡪ࡭ࡳ࡭ࠠࡪࡰࡷࡳࠥࡹࡥࡳࡸࡨࡶ࠳ࠦࡏ࡯ࡧࠣࡱࡴࡳࡥ࡯ࡶࠣࡴࡱ࡫ࡡࡴࡧ࠱ࠫࢪ")
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(l1lll11l)
        l1l1l11l = xbmc.executeJSONRPC(l1ll11l11)
        
        dixie.CloseBusy()
    
        content = json.loads(l1l1l11l.decode(l1lll1 (u"ࠧ࡭ࡣࡷ࡭ࡳ࠳࠱ࠨࢫ"), l1lll1 (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨࢬ")))
    
        json.dump(content, open(PATH,l1lll1 (u"ࠩࡺࠫࢭ")))

        return content
    
    except Exception as e:
        l1l1llll1(e)
        return {l1lll1 (u"ࠪࡉࡷࡸ࡯ࡳࠩࢮ") : l1lll1 (u"ࠫࡕࡲࡵࡨ࡫ࡱࠤࡊࡸࡲࡰࡴࠪࢯ")}


def l1l1lllll(l1ll1111l):
    now = datetime.datetime.today()
    dixie.SetSetting(l1ll1111l, str(now))


def l1l1llll1(e):
    l111111l = l1lll1 (u"࡙ࠬ࡯ࡳࡴࡼ࠰ࠥࡧ࡮ࠡࡧࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷ࡫ࡤ࠻ࠢࡍࡗࡔࡔࠠࡆࡴࡵࡳࡷࡀࠠࠦࡵࠪࢰ")  %e
    l11111l1 = l1lll1 (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡲࡦ࠯࡯࡭ࡳࡱࠠࡵࡪ࡬ࡷࠥࡩࡨࡢࡰࡱࡩࡱࠦࡡ࡯ࡦࠣࡸࡷࡿࠠࡢࡩࡤ࡭ࡳ࠴ࠧࢱ")
    l11111ll = l1lll1 (u"ࠧࡖࡵࡨ࠾ࠥࡉ࡯࡯ࡶࡨࡼࡹࠦࡍࡦࡰࡸࠤࡂࡄࠠࡓࡧࡰࡳࡻ࡫ࠠࡔࡶࡵࡩࡦࡳࠧࢲ")
    
    dixie.l1l1l1ll(e)
    dixie.l111l1l(l111111l, l11111l1, l11111ll)    
    dixie.SetSetting(SETTING, l1lll1 (u"ࠨࠩࢳ"))
    
    