# coding: UTF-8

import sys

l1lllll11 = sys.version_info [0] == 2
l1l111l1 = 2048
l111l11l = 7

def l1lll1 (l1ll111):
	global l1l111ll
	
	l11l1ll1 = ord (l1ll111 [-1])
	l1111111 = l1ll111 [:-1]
	
	l1ll11ll = l11l1ll1 % len (l1111111)
	l1l11ll = l1111111 [:l1ll11ll] + l1111111 [l1ll11ll:]
		
	if l1lllll11:
		l11lll = unicode () .join ([unichr (ord (char) - l1l111l1 - (l1111 + l11l1ll1) % l111l11l) for l1111, char in enumerate (l1l11ll)])
	else:
		l11lll = str () .join ([chr (ord (char) - l1l111l1 - (l1111 + l11l1ll1) % l111l11l) for l1111, char in enumerate (l1l11ll)])
		
	return eval (l11lll)




import xbmc
import xbmcgui
import json
import time
import datetime
import os

import dixie

PATH     =  os.path.join(dixie.PROFILE, l1lll1 (u"ࠩࡷࡩࡲࡶࠧ࢑"))
SETTING  = l1lll1 (u"ࠪࡐࡔࡍࡉࡏࡡࡋࡈ࡙࡜ࠧ࢒")
l1ll11111 =  80


def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 8):
        l1l1l1l1 = json.load(open(PATH))

    else:
        l1l1l1l1 = l1l1ll1l1(url)
        l1l1l1ll1(SETTING)

    stream = url.split(l1lll1 (u"ࠫ࠿࠭࢓"), 1)[-1].lower()

    try:
        result = l1l1l1l1[l1lll1 (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ࢔")]
        l11l11l1  = result[l1lll1 (u"࠭ࡦࡪ࡮ࡨࡷࠬ࢕")]

    except Exception as e:
        l1l1ll111(e)
        return None


    for file in l11l11l1:
        l1l1lll1l   = file[l1lll1 (u"ࠧ࡭ࡣࡥࡩࡱ࠭࢖")]
        l1l1lll1l   = l1l1lll1l.replace(l1lll1 (u"ࠨࠢࠣࠫࢗ"), l1lll1 (u"ࠩࠣࠫ࢘")).replace(l1lll1 (u"ࠪࠤࡠ࠵ࡃࡐࡎࡒࡖࡢ࢙࠭"), l1lll1 (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࢚࠭"))
        l1l1l1l1l = l1l1lll1l.rsplit(l1lll1 (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣ࢛ࠧ"), 1)[0].split(l1lll1 (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢ࠭࢜"), 1)[-1]

        if stream == l1l1l1l1l.lower():
            return file[l1lll1 (u"ࠧࡧ࡫࡯ࡩࠬ࢝")]

    return None


def l1l1ll1l1(url):
    try:
        message = l1lll1 (u"ࠨࡎࡲ࡫࡬࡯࡮ࡨࠢ࡬ࡲࡹࡵࠠࡴࡧࡵࡺࡪࡸ࠮ࠡࡑࡱࡩࠥࡳ࡯࡮ࡧࡱࡸࠥࡶ࡬ࡦࡣࡶࡩ࠳࠭࢞")
        dixie.notify(message)

        dixie.ShowBusy()
        l1l1l1l1 = l1ll1111l(url)
        dixie.CloseBusy()

        return l1l1l1l1
    
    except Exception as e:
        l1l1ll111(e)
        return {l1lll1 (u"ࠩࡈࡶࡷࡵࡲࠨ࢟") : l1lll1 (u"ࠪࡔࡱࡻࡧࡪࡰࠣࡉࡷࡸ࡯ࡳࠩࢠ")}


def l1ll1111l(url):
    l1ll11l11(url)
    return json.load(open(PATH))


def l1ll11l11(url):
    l1lll1l1 = l1l1l1l11(url)
    xbmc.executeJSONRPC(l1lll1l1)

    l1ll111ll  = l1l1lllll(url)
    l1l1l1l1 = xbmc.executeJSONRPC(l1ll111ll)

    content = json.loads(l1l1l1l1.decode(l1lll1 (u"ࠫࡱࡧࡴࡪࡰ࠰࠵ࠬࢡ"), l1lll1 (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬࢢ")))

    json.dump(content, open(PATH,l1lll1 (u"࠭ࡷࠨࢣ")))

    l1l1llll1(url)


def l1l1l1l11(url):
    l1l1ll11l = l1l1l1lll(url)
    l1lll1l1   = (l1lll1 (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࠪࡹ࠯ࡀࡣࡦࡸ࡮ࡵ࡮࠾࡯ࡤ࡭ࡳࡥ࡬ࡪࡵࡷࠪࡹ࡯ࡴ࡭ࡧࡀࠪࡺࡸ࡬࠾ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢤ") % l1l1ll11l)
    return l1lll1l1


def l1l1lllll(url):
    l1l1ll11l = l1l1l1lll(url)
    l1ll111ll = (l1lll1 (u"ࠨࡽࠥ࡮ࡸࡵ࡮ࡳࡲࡦࠦ࠿ࠨ࠲࠯࠲ࠥ࠰ࠥࠨ࡭ࡦࡶ࡫ࡳࡩࠨ࠺ࠣࡈ࡬ࡰࡪࡹ࠮ࡈࡧࡷࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠨࠬࠡࠤࡳࡥࡷࡧ࡭ࡴࠤ࠽ࡿࠧࡪࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠼ࠥࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࠫࡳ࠰ࡁࡤࡧࡹ࡯࡯࡯࠿࡯࡭ࡻ࡫ࡴࡷࡡࡤࡰࡱࠬࡴࡪࡶ࡯ࡩࡂࡇ࡬࡭࠭ࡦ࡬ࡦࡴ࡮ࡦ࡮ࡶࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࢥ") % l1l1ll11l)
    return l1ll111ll


def l1l1l1lll(url):
    if url.startswith(l1lll1 (u"ࠩࡋࡈ࡙࡜࠺ࠨࢦ")):
        return l1lll1 (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡫ࡨࡹࡼࠧࢧ")

    if url.startswith(l1lll1 (u"ࠫࡍࡊࡔࡗ࠴࠽ࠫࢨ")):
        return l1lll1 (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡷࡻࡹࡢ࡫ࡳࡸࡻ࠭ࢩ")

    if url.startswith(l1lll1 (u"࠭ࡈࡅࡖ࡙࠷࠿࠭ࢪ")):
        return l1lll1 (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡲࡶࡻࡤࡸࡻ࠭ࢫ")


def l1l1llll1(url):
    
    name   = dixie.TITLE + ' HDTV Update'
    l1ll111l1 = os.path.join(dixie.HOME, l1lll1 (u"ࠩ࡫ࡨࡹࡼ࠮ࡱࡻࠪࢭ"))
    args   = url
    cmd    = l1lll1 (u"ࠪࡅࡱࡧࡲ࡮ࡅ࡯ࡳࡨࡱࠨࠦࡵ࠯ࠤࡗࡻ࡮ࡔࡥࡵ࡭ࡵࡺࠨࠦࡵ࠯ࠤࠪࡹࠩ࠭ࠢࠨࡨ࠱ࠦࡔࡳࡷࡨ࠭ࠬࢮ") % (name, l1ll111l1, args, l1ll11111)

    xbmc.executebuiltin(l1lll1 (u"ࠫࡈࡧ࡮ࡤࡧ࡯ࡅࡱࡧࡲ࡮ࠪࠨࡷ࠱࡚ࡲࡶࡧࠬࠫࢯ") % name)
    xbmc.executebuiltin(cmd)


def l1l1l1ll1(l1l1ll1ll):
    now = datetime.datetime.today()
    dixie.SetSetting(l1l1ll1ll, str(now))


def l1l1ll111(e):
    l11111l1 = l1lll1 (u"࡙ࠬ࡯ࡳࡴࡼ࠰ࠥࡧ࡮ࠡࡧࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷ࡫ࡤ࠻ࠢࡍࡗࡔࡔࠠࡆࡴࡵࡳࡷࡀࠠࠦࡵࠪࢰ")  %e
    l11111ll = l1lll1 (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡲࡦ࠯࡯࡭ࡳࡱࠠࡵࡪ࡬ࡷࠥࡩࡨࡢࡰࡱࡩࡱࠦࡡ࡯ࡦࠣࡸࡷࡿࠠࡢࡩࡤ࡭ࡳ࠴ࠧࢱ")
    l1111l11 = l1lll1 (u"ࠧࡖࡵࡨ࠾ࠥࡉ࡯࡯ࡶࡨࡼࡹࠦࡍࡦࡰࡸࠤࡂࡄࠠࡓࡧࡰࡳࡻ࡫ࠠࡔࡶࡵࡩࡦࡳࠧࢲ")
    
    dixie.log(e)
    dixie.DialogOK(l11111l1, l11111ll, l1111l11)
    dixie.SetSetting(SETTING, l1lll1 (u"ࠨࠩࢳ"))


if __name__ == '__main__':
    url = sys.argv[1]
    l1ll11l11(url)