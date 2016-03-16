# coding: UTF-8

import sys

l1 = sys.version_info [0] == 2
l1l1l1 = 2048
l1ll1 = 7

def l1ll1l (ll):
	global l1l1ll
	
	l111l1 = ord (ll [-1])
	l111l = ll [:-1]
	
	l1ll = l111l1 % len (l111l)
	l11ll1 = l111l [:l1ll] + l111l [l1ll:]
		
	if l1:
		l1l11l = unicode () .join ([unichr (ord (char) - l1l1l1 - (l11ll + l111l1) % l1ll1) for l11ll, char in enumerate (l11ll1)])
	else:
		l1l11l = str () .join ([chr (ord (char) - l1l1l1 - (l11ll + l111l1) % l1ll1) for l11ll, char in enumerate (l11ll1)])
		
	return eval (l1l11l)




import time
import random
import base64
import requests
import re
import os
import json
import hashlib
import xbmc

import dixie

l11lll = l1ll1l (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡰ࡮ࡼࡥ࡮࡫ࡻࠫࠀ")


def checkAddons():
    if l11111(l11lll):
        l11l11()


def l11111(l11lll):
    if xbmc.getCondVisibility(l1ll1l (u"࡙ࠬࡹࡴࡶࡨࡱ࠳ࡎࡡࡴࡃࡧࡨࡴࡴࠨࠦࡵࠬࠫࠁ") % l11lll) == 1:
        return True
    return False


def getLIVETV(url):
    l1l1 = getChannels()
    stream   = url.split(l1ll1l (u"࠭࠺ࠨࠂ"), 1)[-1].lower()

    for l1lll1 in l1l1:
        l1l11 = l1lll1[l1ll1l (u"ࠧ࡭ࡣࡥࡩࡱ࠭ࠃ")]
        url   = l1lll1[l1ll1l (u"ࠨࡷࡵࡰࠬࠄ")]

        if stream == l1l11.lower():
            return url

    return None


def l11l11():
    l111 = dixie.PROFILE
    PATH = os.path.join(l111, l1ll1l (u"ࠩ࡬ࡲ࡮࠭ࠅ"))
    l11l = l1ll1l (u"ࠪࡰ࡮ࡼࡥࡵࡸ࠱࡭ࡳ࡯ࠧࠆ")
    l1l  = os.path.join(PATH, l11l)

    l1l1 = getChannels()

    l11l1l  = file(l1l, l1ll1l (u"ࠫࡼ࠭ࠇ"))

    l11l1l.write(l1ll1l (u"ࠬࡡࠧࠈ"))
    l11l1l.write(l11lll)
    l11l1l.write(l1ll1l (u"࠭࡝ࠨࠉ"))
    l11l1l.write(l1ll1l (u"ࠧ࡝ࡰࠪࠊ"))

    for l1lll1 in l1l1:
        l1l11   = l1lll1[l1ll1l (u"ࠨ࡮ࡤࡦࡪࡲࠧࠋ")]
        stream  = l1lll1[l1ll1l (u"ࠩࡸࡶࡱ࠭ࠌ")]

        l11l1l.write(l1ll1l (u"ࠪࠩࡸ࠭ࠍ") % l1l11)
        l11l1l.write(l1ll1l (u"ࠫࡂ࠭ࠎ"))
        l11l1l.write(l1ll1l (u"ࠬࡒࡉࡗࡇࡗ࡚࠿࠭ࠏ"))
        l11l1l.write(l1ll1l (u"࠭ࠥࡴࠩࠐ") % l1l11)
        l11l1l.write(l1ll1l (u"ࠧ࡝ࡰࠪࠑ"))

    l11l1l.write(l1ll1l (u"ࠨ࡞ࡱࠫࠒ"))
    l11l1l.close()


def getChannels():
    l1111l   =  l1l111(l1ll1l (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵࡶ࠮ࡶ࡭ࡷࡺࡳࡵࡷ࠯ࡰࡨࡸ࠴ࡼ࠱࠰ࡩࡨࡸࡤࡧ࡬࡭ࡡࡦ࡬ࡦࡴ࡮ࡦ࡮ࡶࠫࠓ"),l1ll1l (u"ࠪ࡫ࡴࡧࡴࠨࠔ"))
    headers =  {l1ll1l (u"࡚ࠫࡹࡥࡳ࠯ࡄ࡫ࡪࡴࡴࠨࠕ"):l1ll1l (u"࡛ࠬࡓࡆࡔ࠰ࡅࡌࡋࡎࡕ࠯ࡘࡏ࡙࡜ࡎࡐ࡙࠰ࡅࡕࡖ࠭ࡗ࠳ࠪࠖ"),
                l1ll1l (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬࠗ"):l1ll1l (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡸࡹࡺ࠱࡫ࡵࡲ࡮࠯ࡸࡶࡱ࡫࡮ࡤࡱࡧࡩࡩࡁࠠࡤࡪࡤࡶࡸ࡫ࡴ࠾ࡗࡗࡊ࠲࠾ࠧ࠘"),
                l1ll1l (u"ࠨࡃࡦࡧࡪࡶࡴ࠮ࡇࡱࡧࡴࡪࡩ࡯ࡩࠪ࠙") : l1ll1l (u"ࠩࡪࡾ࡮ࡶࠧࠚ"),
                l1ll1l (u"ࠪࡥࡵࡶ࠭ࡵࡱ࡮ࡩࡳ࠭ࠛ"):l1111l,
                l1ll1l (u"ࠫࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨࠜ"):l1ll1l (u"ࠬࡑࡥࡦࡲ࠰ࡅࡱ࡯ࡶࡦࠩࠝ"),
                l1ll1l (u"࠭ࡈࡰࡵࡷࠫࠞ"):l1ll1l (u"ࠧࡢࡲࡳ࠲ࡺࡱࡴࡷࡰࡲࡻ࠳ࡴࡥࡵࠩࠟ")}
    l1lll = {l1ll1l (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪࠠ"):l1ll1l (u"ࠩࡪࡳࡦࡺࠧࠡ")}

    l111ll = requests.post(l1ll1l (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡰ࠯ࡷ࡮ࡸࡻࡴ࡯ࡸ࠰ࡱࡩࡹ࠵ࡶ࠲࠱ࡪࡩࡹࡥࡡ࡭࡮ࡢࡧ࡭ࡧ࡮࡯ࡧ࡯ࡷࠬࠢ"), data=l1lll, headers=headers)

    l11 =  l111ll.content
    l11 =  l11.replace(l1ll1l (u"ࠫࡡ࠵ࠧࠣ"),l1ll1l (u"ࠬ࠵ࠧࠤ"))
    l1l1l = l1ll1l (u"࠭ࠢࡤࡪࡤࡲࡳ࡫࡬ࡠࡰࡤࡱࡪࠨ࠺ࠣࠪ࠱࠯ࡄ࠯ࠢ࠭ࠤ࡬ࡱ࡬ࠨ࠺ࠣࠪ࠱࠯ࡄ࠯ࠢ࠭ࠤ࡫ࡸࡹࡶ࡟ࡴࡶࡵࡩࡦࡳࠢ࠻ࠤࠫ࠲࠰ࡅࠩࠣ࠮ࠥࡶࡹࡳࡰࡠࡵࡷࡶࡪࡧ࡭ࠣ࠼ࠥࠬ࠳࠱࠿ࠪࠤ࠯ࠦࡨࡧࡴࡠ࡫ࡧࠦ࠿ࠨࠨ࠯࠭ࡂ࠭ࠧ࠭ࠥ")

    items    = re.compile(l1l1l).findall(l11)
    l1l1 = []

    for item in items:
        link = {l1ll1l (u"ࠧ࡭ࡣࡥࡩࡱ࠭ࠦ"): item[0], l1ll1l (u"ࠨࡷࡵࡰࠬࠧ"): item[2]}
        l1l1.append(link)

    return l1l1


def l1l111(url, l1ll11):
    l11l1   =  l1111()
    st   = l1ll1l (u"ࠤࡸ࡯ࡹࡼ࡮ࡰࡹ࠰ࡸࡴࡱࡥ࡯࠯ࠥࠨ")+ l11l1 + l1ll1l (u"ࠥ࠱ࠧࠩ")+ l1ll1l (u"ࠦࡤࢂ࡟࠮ࠤࠪ") + url + l1ll1l (u"ࠧ࠳ࠢࠫ") + l1ll11 +l1ll1l (u"ࠨ࠭ࠣࠬ") + l1ll1l (u"ࠢࡠࡾࡢࠦ࠭")+ l1ll1l (u"ࠣ࠯ࠥ࠮")+ base64.b64decode(l1ll1l (u"ࠤࡐࡘࡎࢀࡎࡅࡗ࠵ࡍ࡚ࡇࡪࡋࡅ࡙ࡩࡩ࡝ࡴ࠱ࡦࡰ࠹ࡻࡪ࠱࠵࡮ࡍࡇࡓࡇࡉࡕ࡛࠴ࡒࡉࡓࡹࡎࡓࡀࡁࠧ࠯"))
    return hashlib.md5(st).hexdigest()


def l1111():
    from datetime import datetime, timedelta

    l1llll = datetime.now() + timedelta(hours=5)
    return l1llll.strftime(l1ll1l (u"ࠪࠩࡇ࠳ࠥࡥ࠯ࠨ࡝ࠬ࠰"))
