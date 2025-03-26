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
import xbmcplugin
import datetime
import time
import urllib
import urllib2
import random
import json
import os
import threading
import dixie
import sfile
from channel import GetChannelFromFile
PROFILE = xbmc.translatePath(dixie.PROFILE)
l1llll1ll1_opy_ = dixie.RecordingFolder()
def l1llll1lll_opy_(message, length=5000):
    dixie.notify(message, length)
def l1lll1l1ll_opy_(url, size, l1lll1l1l1_opy_, l1lllllll1_opy_):
    try:
        req = urllib2.Request(url)
        if len(l1lll1l1l1_opy_) > 0:
            req.add_header(l1l1l_opy_ (u"ࠨࡔࡨࡪࡪࡸࡥࡳࠩੳ"), l1lll1l1l1_opy_)
        if len(l1lllllll1_opy_) > 0:
            req.add_header(l1l1l_opy_ (u"ࠩࡘࡷࡪࡸ࠭ࡂࡩࡨࡲࡹ࠭ੴ"), l1lllllll1_opy_)
        if size > 0:
            size = int(size)
            req.add_header(l1l1l_opy_ (u"ࠪࡖࡦࡴࡧࡦࠩੵ"), l1l1l_opy_ (u"ࠫࡧࡿࡴࡦࡵࡀࠩࡩ࠳ࠧ੶") % size)
        resp = urllib2.urlopen(req, timeout=10)
        return resp, l1l1l_opy_ (u"ࠬ࠭੷")
    except Exception, e:
        return None, str(e)
def DialogOK(l1l1ll1l_opy_, l11l1l1_opy_=l1l1l_opy_ (u"࠭ࠧ੸"), l1l1llll_opy_=l1l1l_opy_ (u"ࠧࠨ੹")):
    xbmcgui.Dialog().ok(l1l1l_opy_ (u"ࠨࠩ੺"), str(l1l1ll1l_opy_), str(l11l1l1_opy_), str(l1l1llll_opy_))
def l1llll11l1_opy_(url, dst, title, duration, pid, l1lll1l1l1_opy_=l1l1l_opy_ (u"ࠩࠪ੻"), l1lllllll1_opy_=l1l1l_opy_ (u"ࠪࠫ੼"), l1llllll1l_opy_=False):
    file = dst.rsplit(os.sep, 1)[-1]
    resp, error = l1lll1l1ll_opy_(url, 0, l1lll1l1l1_opy_, l1lllllll1_opy_)
    if not resp:
        return False
    dixie.log(l1l1l_opy_ (u"ࠫࡗ࡫ࡣࡰࡴࡧ࡭ࡳ࡭ࠠࡉࡧࡤࡨࡪࡸࠧ੽"))
    dixie.log(resp.headers)
    l1lll11ll1_opy_ = True
    size = 1024 * 1024
    total   = 0
    notify  = 0
    errors  = 0
    count   = 0
    l1lll1lll1_opy_  = 0
    sleep   = 0
    f = sfile.file(dst, type=l1l1l_opy_ (u"ࠬࡽࡢࠨ੾"))
    chunk  = None
    chunks = []
    l1lll11l11_opy_ = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
    while True:
        kill = xbmcgui.Window(10000).getProperty(l1l1l_opy_ (u"࠭ࡏࡕࡖ࠰ࡏࡎࡒࡌࡠࡔࡈࡇࡔࡘࡄࡊࡐࡊࡣࠪࡪࠧ੿") % pid).lower() == l1l1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ઀")
        if kill or datetime.datetime.now() > l1lll11l11_opy_:
            xbmcgui.Window(10000).clearProperty(l1l1l_opy_ (u"ࠨࡑࡗࡘ࠲ࡑࡉࡍࡎࡢࡖࡊࡉࡏࡓࡆࡌࡒࡌࡥࠥࡥࠩઁ") % pid)
            while len(chunks) > 0:
                c = chunks.pop(0)
                f.write(c)
                del c
            f.close()
            if datetime.datetime.now() > l1lll11l11_opy_:
                dixie.log(l1l1l_opy_ (u"ࠩࠨࡷࠥࡸࡥࡤࡱࡵࡨ࡮ࡴࡧࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࡦࠪં") % (dst))
            else:
                dixie.log(l1l1l_opy_ (u"ࠪࠩࡸࠦࡲࡦࡥࡲࡶࡩ࡯࡮ࡨࠢࡺࡥࡸࠦࡴࡦࡴࡰ࡭ࡳࡧࡴࡦࡦࠣࡩࡦࡸ࡬ࡺࠩઃ") % (dst))
            return
        chunk = None
        error = False
        try:
            chunk = resp.read(size)
            if not chunk:
                error = True
                sleep = 1
        except Exception as e:
            dixie.log(l1l1l_opy_ (u"ࠫ࠯࠰ࠪࠫࠢࡈࡖࡗࡕࡒࠡࠬ࠭࠮࠯࠭઄"))
            dixie.log(str(e))
            error = True
            sleep = 10
            errno = 0
            if hasattr(e, l1l1l_opy_ (u"ࠬ࡫ࡲࡳࡰࡲࠫઅ")):
                dixie.log(str(e.errno))
                errno = e.errno
            if errno == 10035:
                pass
            if errno == 10054:
                errors = 10
                sleep  = 30
            if errno == 11001:
                errors = 10
                sleep  = 30
        if chunk:
            errors = 0
            chunks.append(chunk)
            if len(chunks) > 5:
                c = chunks.pop(0)
                f.write(c)
                del c
        if error:
            errors += 1
            count  += 1
            dixie.log(l1l1l_opy_ (u"࠭ࠥࡥࠢࡈࡶࡷࡵࡲࠩࡵࠬࠤࡼ࡮ࡩ࡭ࡵࡷࠤࡷ࡫ࡣࡰࡴࡧ࡭ࡳ࡭ࠠࠦࡵࠪઆ") % (count, dst))
            xbmc.sleep(sleep*1000)
        if errors > 0:
            if l1lll1lll1_opy_ > 500:
                dixie.log(l1l1l_opy_ (u"ࠧࠦࡵࠣࡶࡪࡩ࡯ࡳࡦ࡬ࡲ࡬ࠦࡣࡢࡰࡦࡩࡱ࡫ࡤࠡ࠯ࠣࡸࡴࡵࠠ࡮ࡣࡱࡽࠥ࡫ࡲࡳࡱࡵࡷࠥࡽࡨࡪ࡮ࡶࡸࠥࡸࡥࡤࡱࡵࡨ࡮ࡴࡧࠨઇ") % (dst))
                if not l1llllll1l_opy_:
                    l1llllll11_opy_(title, dst, False)
                f.close()
                return
            l1lll1lll1_opy_ += 1
            errors  = 0
            chunks  = []
            dixie.log(l1l1l_opy_ (u"ࠨࡔࡨࡧࡴࡸࡤࡪࡰࡪࠤࡷ࡫ࡳࡶ࡯ࡨࡨࠥ࠮ࠥࡥࠫࠣࠩࡸ࠭ઈ") % (l1lll1lll1_opy_, dst))
            resp, error = l1lll1l1ll_opy_(url, total, l1lll1l1l1_opy_, l1lllllll1_opy_)
class l1lllll1l1_opy_(threading.Thread):
    def __init__(self, title, channel, l1111111l_opy_, duration, channelID, stream, image):
        super(l1lllll1l1_opy_, self).__init__()
        self.title     = title.replace(l1l1l_opy_ (u"ࠩࢁࠫઉ"), l1l1l_opy_ (u"ࠪ࠱ࠬઊ"))
        self.channel   = channel
        self.l1111111l_opy_ = l1111111l_opy_
        self.duration  = duration
        self.channelID = channelID
        self.stream    = stream
        self.image     = image
        self.l1llllllll_opy_ = True
        self.l1llll1l11_opy_    = False
        self.pid       = 0
        self.key       = l1l1l_opy_ (u"ࠫࠬઋ")
        self.l1lll1l111_opy_    = l1l1l_opy_ (u"ࠬ࠭ઌ")
        self.filename  = l1l1l_opy_ (u"࠭ࠧઍ")
    def run(self):
        l1lllll1ll_opy_ = self.l1lll11l1l_opy_()
        f = 1 if l1lllll1ll_opy_ else 5
        self.key      = sfile.fileSystemSafe(l1l1l_opy_ (u"ࠧࠦࡵࠣࢂࠥࠫࡳࠡࢀࠣࠩࡸ࠭઎") % (self.title, self.l1111111l_opy_, self.channelID))
        self.l1lll1l111_opy_   = os.path.join(l1llll1ll1_opy_, sfile.fileSystemSafe(self.title))
        self.filename = os.path.join(self.l1lll1l111_opy_, l1l1l_opy_ (u"ࠨࠧࡶ࠲ࡦࡼࡩࠨએ") % self.key)
        if sfile.exists(self.filename):
            return
        sfile.makedirs(self.l1lll1l111_opy_)
        sfile.remove(self.filename)
        dixie.log(l1l1l_opy_ (u"ࠩࡀࡁࡂࡃࠠࡅࡗࡕࡅ࡙ࡏࡏࡏࠢࡀࡁࡂࡃࠧઐ"))
        dixie.log(int(self.duration/f))
        msg = l1l1l_opy_ (u"ࠪࡒࡴࡽࠠࡳࡧࡦࡳࡷࡪࡩ࡯ࡩࠣࠩࡸ࠭ઑ") % self.title
        l1llll1lll_opy_(msg)
        url = self.stream
        dst = xbmc.translatePath(self.filename)
        self.pid = random.randint(1000, 10000000)
        dixie.log(l1l1l_opy_ (u"࡚ࠫࡘࡌࠡ࠿ࠣࠩࡸ࠭઒") % url)
        dixie.log(l1l1l_opy_ (u"ࠬࡊࡓࡕࠢࡀࠤࠪࡹࠧઓ") % dst)
        dixie.log(l1l1l_opy_ (u"࠭ࡐࡊࡆࠣࡁࠥࠫࡳࠨઔ") % self.pid)
        self.l1lllll11l_opy_()
        now = datetime.datetime.now()
        l1llll11l1_opy_(url, dst, self.title, self.duration, self.pid)
        self.pid = 0
        self.l1llll1l11_opy_ = not sfile.exists(self.filename)
        end    = datetime.datetime.now()
        l1lll1l11l_opy_  = end - now
        l1lll1l11l_opy_  = (l1lll1l11l_opy_.days * 86400) + l1lll1l11l_opy_.seconds
        l1lll1l11l_opy_ += 30
        self.l1llllllll_opy_ = l1lll1l11l_opy_ < self.duration
        self.l1lllll11l_opy_()
        if self.l1llllllll_opy_:
            msg = l1l1l_opy_ (u"ࠧࠦࡵࠣࡍࡸࠦࡰࡢࡴࡷ࡭ࡦࡲ࡬ࡺࠢࡵࡩࡨࡵࡲࡥࡧࡧࠫક") % self.title
            l1llll1lll_opy_(msg)
        else:
            msg = l1l1l_opy_ (u"ࠨࠧࡶࠤࡍࡧࡳࠡࡨ࡬ࡲࡸ࡯ࡨࡦࡦࠣࡶࡪࡩ࡯ࡳࡦ࡬ࡲ࡬࠭ખ") % self.title
            l1llll1lll_opy_(msg)
    def l1lll11l1l_opy_(self):
        return xbmc.getCondVisibility(l1l1l_opy_ (u"ࠩࡖࡽࡸࡺࡥ࡮࠰ࡋࡥࡸࡇࡤࡥࡱࡱࠬࡸࡩࡲࡪࡲࡷ࠲ࡹࡼࡧࡶ࡫ࡧࡩࡩ࡯ࡸࡪࡧࠬࠫગ"))
    def l1lllll11l_opy_(self):
        l1lll1llll_opy_ = os.path.join(l1llll1ll1_opy_, l1l1l_opy_ (u"ࠪࡶࡪࡩ࡯ࡳࡦ࡬ࡲ࡬ࡹ࠮ࡵࡺࡷࠫઘ"))
        try:
            info = json.loads(sfile.read(l1lll1llll_opy_))
        except Exception, e:
            info = {}
        if self.l1llll1l11_opy_:
            if self.key in info:
                info.pop(self.key)
        else:
            l1llll1111_opy_ = {}
            l1llll1111_opy_[l1l1l_opy_ (u"ࠫࡹ࡯ࡴ࡭ࡧࠪઙ")]     = self.title
            l1llll1111_opy_[l1l1l_opy_ (u"ࠬࡩࡨࡢࡰࡱࡩࡱ࠭ચ")]   = self.channel.title
            l1llll1111_opy_[l1l1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡉࡧࡴࡦࠩછ")] = self.l1111111l_opy_
            l1llll1111_opy_[l1l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩજ")]  = self.duration
            l1llll1111_opy_[l1l1l_opy_ (u"ࠨࡥ࡫ࡥࡳࡴࡥ࡭ࡋࡇࠫઝ")] = self.channelID
            l1llll1111_opy_[l1l1l_opy_ (u"ࠩࡶࡸࡷ࡫ࡡ࡮ࠩઞ")]    = self.stream
            l1llll1111_opy_[l1l1l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩટ")]     = self.image
            l1llll1111_opy_[l1l1l_opy_ (u"ࠫࡹࡸࡵ࡯ࡥࡤࡸࡪࡪࠧઠ")] = self.l1llllllll_opy_
            l1llll1111_opy_[l1l1l_opy_ (u"ࠬࡶࡩࡥࠩડ")]       = self.pid
            l1llll1111_opy_[l1l1l_opy_ (u"࠭ࡦࡰ࡮ࡧࡩࡷ࠭ઢ")]    = self.l1lll1l111_opy_
            l1llll1111_opy_[l1l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡳࡧ࡭ࡦࠩણ")]  = self.filename
            info[self.key] = l1llll1111_opy_
        try:
            sfile.write(l1lll1llll_opy_, json.dumps(info))
        except Exception, e:
            pass
def main(channelID, title, start, duration, image):
    l1lll11lll_opy_ = dixie.IsRecordingEnabled()
    if not l1lll11lll_opy_:
        return
    try:
        dixie.log(l1l1l_opy_ (u"ࠨࡔࡈࡇࡔࡘࡄࡊࡐࡊࠤࠪࡹࠠࠦࡵࠣࠩࡸࠦࡓࡕࡃࡕࡘࡊࡊࠧત") % (channelID, title, start))
        record(channelID, title, start, duration, image)
        dixie.log(l1l1l_opy_ (u"ࠩࡕࡉࡈࡕࡒࡅࡋࡑࡋࠥࠫࡳࠡࠧࡶࠤࠪࡹࠠࡑࡃࡖࡗࡊࡊࠧથ") % (channelID, title, start))
    except Exception, e:
        dixie.log(l1l1l_opy_ (u"ࠪࡖࡊࡉࡏࡓࡆࡌࡒࡌࠦࠥࡴࠢࠨࡷࠥࠫࡳࠡࡈࡄࡍࡑࡋࡄࠨદ") % (channelID, title, start))
        dixie.log(str(e))
        dixie.DialogOK(l1l1l_opy_ (u"ࠫࡋࡇࡉࡍࡇࡇࠫધ"), str(e))
def record(channelID, title, l1111111l_opy_, duration, image):
    duration  = int(duration)
    l1111111l_opy_ = dixie.parseTime(l1111111l_opy_)
    now       = datetime.datetime.now()
    l1lllll111_opy_ = l1111111l_opy_ - now
    l1lllll111_opy_ = ((l1lllll111_opy_.days * 86400) + l1lllll111_opy_.seconds)
    l1lll1ll1l_opy_   = dixie.RecordingEndPad() * 60
    l11111111_opy_  = l1111111l_opy_ + datetime.timedelta(minutes=duration) + datetime.timedelta(minutes=l1lll1ll1l_opy_)
    duration += l1lllll111_opy_ + l1lll1ll1l_opy_
    channel = l1lll1ll11_opy_(channelID)
    stream  = l1llll11ll_opy_(channel, 0)
    if not stream:
        raise Exception(l1l1l_opy_ (u"ࠬࡴ࡯ࠡࡵࡷࡶࡪࡧ࡭ࠨન"))
    l1llll111l_opy_ = l1lllll1l1_opy_(title, channel, start, duration, channelID, stream, image)
    l1llll111l_opy_.start()
def l1llll1l1l_opy_(path):
    params = {}
    path   = path.split(l1l1l_opy_ (u"࠭࠿ࠨ઩"), 1)[-1]
    pairs  = path.split(l1l1l_opy_ (u"ࠧࠧࠩપ"))
    for pair in pairs:
        split = pair.split(l1l1l_opy_ (u"ࠨ࠿ࠪફ"))
        if len(split) > 1:
            params[split[0]] = urllib.unquote_plus(split[1])
    return params
def l1llll11ll_opy_(channel, index):
    if not channel:
        dixie.log(l1l1l_opy_ (u"ࠤࡕࡉࡈࡕࡒࡅࡋࡑࡋࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡨ࡮ࡡ࡯ࡰࡨࡰࠧબ"))
        return None
    return getStreamFromChannel(channel, index)
def getStreamFromChannel(channel, index):
    streamUrl = getStreamUrl(channel, index)
    if not streamUrl:
        dixie.log(l1l1l_opy_ (u"ࠥࡖࡊࡉࡏࡓࡆࡌࡒࡌࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡹࡴࡳࡧࡤࡱ࡛ࠥࡒࡍࠤભ"))
        return None
    dixie.log(l1l1l_opy_ (u"ࠦࡗࡋࡃࡐࡔࡇࡍࡓࡍࠠࡢࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡧ࡫ࡱࡨ࡛ࠥࡒࡍࠢࡩࡶࡴࡳࠠࠦࡵࠥમ") % streamUrl)
    import resolver
    stream, play = resolver.resolve(streamUrl, recording=True)
    dixie.log(l1l1l_opy_ (u"ࠬ࠱ࠫࠬ࠭࠮ࠤࡗࡋࡃࡐࡔࡇࠤࡘ࡚ࡒࡆࡃࡑ࠰ࠥࡖࡌࡂ࡛ࠣ࠯࠰࠱ࠫࠬࠩય"))
    dixie.log(stream)
    dixie.log(play)
    if not stream:
        dixie.log(l1l1l_opy_ (u"ࠨࡒࡆࡅࡒࡖࡉࡏࡎࡈࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡸࡥࡴࡱ࡯ࡺࡪࠦࡰ࡭ࡷࡪ࡭ࡳࠦࡕࡓࡎࠥર"))
        return getStreamFromChannel(channel, index+1)
    params = l1llll1l1l_opy_(stream)
    dixie.log(l1l1l_opy_ (u"ࠧࠬ࠭࠮࠯࠰ࠦࡒࡆࡅࡒࡖࡉࠦࡐࡂࡔࡄࡑࡘࠦࠫࠬ࠭࠮࠯ࠬ઱"))
    dixie.log(params)
    if l1l1l_opy_ (u"ࠨࡷࡵࡰࠬલ") not in params:
        dixie.log(l1l1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࠫࡺࡸ࡬ࠨࠢࡳࡥࡷࡧ࡭ࠡ࡫ࡱࠤࠪࡹࠢળ") % stream)
        return getStreamFromChannel(channel, index+1)
    stream = params[l1l1l_opy_ (u"ࠪࡹࡷࡲࠧ઴")]
    dixie.log(l1l1l_opy_ (u"ࠦࡗࡋࡃࡐࡔࡇࡍࡓࡍࠠࡳࡧࡶࡳࡱࡼࡥࡥࠢࡘࡖࡑࠦ࠺ࠡࠧࡶࠦવ") % stream)
    return stream
def l1lll1ll11_opy_(channelID):
    l1lll1l111_opy_   = dixie.GetChannelFolder()
    filename = os.path.join(l1lll1l111_opy_, l1l1l_opy_ (u"ࠬࡩࡨࡢࡰࡱࡩࡱࡹࠧશ"), channelID)
    return GetChannelFromFile(filename)
def getStreamUrl(channel, index):
    try:
        import plugins
        options, l1l11lll_opy_ = plugins.getOptions(channel.streamUrl.split(l1l1l_opy_ (u"࠭ࡼࠨષ")), channel=l1l1l_opy_ (u"ࠧࠨસ"), addmore=False)
        return l1l11lll_opy_[index]
    except Exception, e:
        dixie.DialogOK(l1l1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠢહ"), str(e))
        pass
    return None
if __name__ == l1l1l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫ઺"):
    try:
        channelID  = sys.argv[1]
        title      = sys.argv[2]
        start      = sys.argv[3]
        duration   = sys.argv[4]
        image      = sys.argv[5]
        main(channelID, title, start, duration, image)
    except Exception, e:
        dixie.DialogOK(str(e))
        raise(e)