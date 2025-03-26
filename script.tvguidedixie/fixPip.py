#
#      Copyright (C) 2017 On-Tapp-Networks Limited
#

import xbmc
import dixie


def setSurfaceSetting():
    dixie.DialogOK('We will now try to fix the Picture-in-Picture issue', 'that causes a "black screen" in the EPG', '')
    dixie.log('====== Fix PiP ======')
    cmd = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.usemediacodecsurface","value":false}, "id":1}'
    dixie.log(cmd)
    xbmc.executeJSONRPC(cmd)
    dixie.DialogOK('Picture-in-Picture should now work properly', '', 'Thank you')

if __name__ == '__main__':
    setSurfaceSetting()
