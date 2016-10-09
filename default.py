import subprocess
import xbmc
import xbmcaddon
import xbmcvfs
import re

class Monitor(xbmc.Monitor):

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
        self.id = xbmcaddon.Addon().getAddonInfo('id')

    def onSettingsChanged(self):
        filename = 'special://home/addons/service.webgrabplus/system.d/service.webgrabplus.timer'
        OnCalendar = xbmcaddon.Addon('service.webgrabplus').getSetting('OnCalendar')
        if OnCalendar:
            f = xmbcvfs.File(filename,'rb')
            data = f.read()
            f.close()
            data = re.sub(r'OnCalendar.*', 'OnCalendar=%s' % OnCalendar, data)
            f = xmbcvfs.File(filename,'wb')
            f.write(data)
            f.close()
            subprocess.call(['systemctl', 'start', 'service.webgrabplus.timer'])


if __name__ == "__main__":
    Monitor().waitForAbort()
