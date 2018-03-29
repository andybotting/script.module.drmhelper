import platform

import config


import xbmc


class DRMHelper(object):

    def __init__(self):
        self.system = None
        self.arch = None

    def _get_info_label(self, label, attempts=0):
        """Get XBMC info label

        In some cases, Kodi will return a value of 'Busy' if the value is not
        yet available. Loop a maximum of 10 attempts with a small sleep until
        we get the value, or return nothing.
        """
        if attempts > 10:
            return  # fail after 10 attempts

        value = xbmc.getInfoLabel(label)
        if value == 'Busy':
            xbmc.sleep(100)
            attempts += 1
            return self._get_info_label(label, attempts=attempts)

        return value

    def _get_system(self):
        """Get the system platform information"""

        if self.system:
            return self.system

        self.system = platform.system()

        if xbmc.getCondVisibility('system.platform.android'):
            self.system = 'Android'

        return self.system

    def _get_arch(self):

        if self.arch:
            return self.arch

        arch = platform.machine()
        if arch.startswith('arm'):
            # strip armv6l down to armv6
            arch = arch[:5]

        if self.system == 'Windows':
            try:
                arch = config.WINDOWS_BITNESS.get(platform.architecture()[0])
            except ImportError:  # No module named _subprocess on Xbox One
                arch = 'x86_64'

        self.arch = arch
        return self.arch

    def _get_platform(self):
        """Return a tuple for our system/arch

        For example:
            ('Windows', 'x86_64')
            ('Linux', 'arm')
            ('Android', 'aarch64')
        """
        return (self._get_system(), self._get_arch())

    def _is_drm_supported(self):
        if self._get_platform() in config.SUPPORTED_PLATFORMS:
            return True
        return False

    def _get_ssd_filename(self):
        return config.SSD_WV_DICT.get(self._get_system())

    def _get_wvcdm_filename(self):
        return config.WIDEVINECDM_DICT.get(self._get_system())
