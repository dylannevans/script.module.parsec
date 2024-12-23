import xbmcaddon
import xbmcgui
import subprocess
import os

ADDON = xbmcaddon.Addon(id='script.module.parsec')
ADDON_ID = ADDON.getAddonInfo('id')
peer_id = ADDON.getSetting("peer_id")
peer_id = 'peer_id=' + peer_id

# Check if parsec is installed
parsec_installed = True
try:
        os.system('flatpak run com.parsecgaming.parsec peer_id=' + peer_id)
except:
        xbmcgui.Dialog().ok('ERROR', 'No Parsec!\nPlease install it: flatpak install com.parsecgaming.parsec')
        print('No Parsec!\nPlease install it: flatpak install com.parsecgaming.parsec')
    
    
