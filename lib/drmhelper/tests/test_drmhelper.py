from drmhelper import drmhelper

import mock

import testtools


class DRMHelperTests(testtools.TestCase):

    def test_get_info_label(self):
        dh = drmhelper.DRMHelper()
        with mock.patch('xbmc.getInfoLabel', return_value='foo'):
            dh._get_info_label('test_label')
            self.assertEqual(dh._get_info_label('test_label'), 'foo')

    def test_get_info_label_busy(self):
        dh = drmhelper.DRMHelper()
        with mock.patch('xbmc.getInfoLabel', return_value='Busy'):
            dh._get_info_label('test_label')
            self.assertEqual(dh._get_info_label('test_label'), None)

    def test_get_system(self):
        # dh = drmhelper.DRMHelper()
        pass
