from drmhelper import helper

import fakes

import mock

import testtools


def get_xbmc_cond_visibility(cond):
    global HACK_PLATFORMS
    if cond in HACK_PLATFORMS:
        return True


class DRMHelperTests(testtools.TestCase):

    @mock.patch('xbmc.getCondVisibility')
    def test_get_system(self, mock_cond_vis):
        for system in fakes.SYSTEMS:
            with mock.patch('platform.system', return_value=system['system']):
                global HACK_PLATFORMS
                HACK_PLATFORMS = system['platforms']
                mock_cond_vis.side_effect = get_xbmc_cond_visibility
                h = helper.DRMHelper()
                sys = h._get_system()
                self.assertEqual(sys, system['expected_system'])
