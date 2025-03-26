#
#       Copyright (C) 2018 On-Tapp-Networks Limited
#

import xbmc
import xbmcaddon

import dixie


#-------------------------------------------------------------


def enableRecord():
    if dixie.DialogYesNo('Would you like to enable the On-Tapp.TV Recording feature?', '', '', noLabel='DISABLE', yesLabel='ENABLE'):
        xbmcaddon.Addon(dixie.OTT_RECORD).setSetting('ENABLED', 'true')
        dixie.DialogOK('On-Tapp.TV Recording has been enabled')
        dixie.log('============ Record ON ============')
    else:
        xbmcaddon.Addon(dixie.OTT_RECORD).setSetting('ENABLED', 'false')
        dixie.DialogOK('On-Tapp.TV Recording has been disabled')
        dixie.log('============ Record OFF ============')
        
if __name__ == '__main__':
    enableRecord()
