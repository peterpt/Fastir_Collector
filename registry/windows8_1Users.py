from __future__ import unicode_literals
from registry.reg import _Reg


class Windows8_1UserReg(_Reg):
    def __init__(self, params):
        _Reg.__init__(self, params)

    def csv_open_save_mru(self):
        super(Windows8_1UserReg, self)._csv_open_save_mru(
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU")

    def csv_user_assist(self):
        super(Windows8_1UserReg, self)._csv_user_assist(0, True)