# flake8: noqa

REPO_BASE = 'https://github.com/aussieaddons/repo-binary/raw/master/'

WIDEVINE_CDM_URL = {
    ('Linux', 'x64'): 'https://dl.google.com/widevine-cdm/903-linux-x64.zip',
    ('Linux', 'arm'): 'http://odroidxu.leeharris.me.uk/xu3/chromium-widevine-1.4.8.823-2-armv7h.pkg.tar.xz',
    ('Linux', 'aarch64'): 'http://odroidxu.leeharris.me.uk/xu3/chromium-widevine-1.4.8.823-2-armv7h.pkg.tar.xz',
    ('Windows', 'x64'): 'https://dl.google.com/widevine-cdm/903-win-x64.zip',
    ('Windows', 'x86'): 'https://dl.google.com/widevine-cdm/903-win-ia32.zip',
    ('Darwin', 'x64'): 'https://dl.google.com/widevine-cdm/903-mac-x64.zip'
}

UNARCHIVE_COMMAND = {
    'Linux-x64': '(cd {1} && unzip {0} {2} -d {1} && chmod 755 {1}/{2} && rm -f {0})',
    'Linux-arm': '(cd {1} && tar xJfO {0} usr/lib/chromium/libwidevinecdm.so >{1}/{2} && chmod 755 {1}/{2} && rm -f {0})',
    'Linux-aarch64': '(cd {1} && tar xJfO {0} usr/lib/chromium/libwidevinecdm.so >{1}/{2} && chmod 755 {1}/{2} && rm -f {0})',
    'Darwin-x64': '(cd {1} && unzip {0} {2} -d {1} && chmod 755 {1}/{2} && rm -f {0})',
}

SSD_WV_DICT = {
    'Android': None,
    'Windows': 'ssd_wv.dll',
    'Linux': 'libssd_wv.so',
    'Darwin': 'libssd_wv.dylib'
}

WIDEVINE_CDM_DICT = {
    'Android': None,
    'Windows': 'widevinecdm.dll',
    'Linux': 'libwidevinecdm.so',
    'Darwin': 'libwidevinecdm.dylib'
}

ARCH_DICT = {
    'aarch64': 'aarch64',
    'aarch64_be': 'aarch64',
    'arm64': 'aarch64',
    'arm': 'arm',
    'armv7': 'arm',
    'armv8': 'aarch64',
    'AMD64': 'x64',
    'x86_64': 'x64',
    'x86': 'x86',
    'i386': 'x86',
    'i686': 'x86'
}

SUPPORTED_WV_DRM_PLATFORMS = [
    ('Windows', 'x64'),
    ('Windows', 'x86'),
    ('Darwin', 'x64'),
    ('Darwin', 'arm'),
    ('Darwin', 'aarch64'),
    ('Linux', 'x64'),
    ('Linux', 'arm'),
    ('Linux', 'aarch64'),
    ('Android', 'x86'),
    ('Android', 'arm'),
    ('Android', 'aarch64')
]

WINDOWS_BITNESS = {
    '32bit': 'x86',
    '64bit': 'x64'
}


KODI_NAME = {
    12: 'Frodo',
    13: 'Gotham',
    14: 'Helix',
    15: 'Isengard',
    16: 'Jarvis',
    17: 'Krypton',
    18: 'Leia'
}

MIN_IA_VERSION = {
    17: '2.0.7',
    18: '2.0.10'
}

CURRENT_IA_VERSION = {
    17: {'ver': '2.0.19', 'commit': '9af2121'},
    18: {'ver': '2.0.10', 'commit': '0c7e975'}
}

MIN_LEIA_BUILD = ('20170818', 'e6b0c83')
