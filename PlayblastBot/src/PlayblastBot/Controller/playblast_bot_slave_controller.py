from PlayblastBot.Lib import PlayblastBotSlaveLib
from PowerRing.Purple.Controller import SelectCellsTableController



try:
    from PlayblastBot.View import Ui_Dialog_PlayblastBotSlave
except ImportError:
    from PlayblastBot.View2 import Ui_Dialog_PlayblastBotSlave

try:
    from PySide import QtCore
    from PySide import QtGui
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *


class PlayblastBotSlaveController(object):
    def __init__(self):
        self._ui = Ui_Dialog_PlayblastBotSlave()
        self._dialog = QDialog()
        self._ui.setupUi(self._dialog)

        self._sct_jobs = None

        self._table = None
        print 'PlayblastBotManagerController'
        print PlayblastBotSlaveLib.GetValue()

    def Initialize(self):
        self._dialog.show()

    def Show(self):
        self._dialog.show()
        self._dialog.exec_()

    def Close(self):
        self._dialog.close()

    @property
    def Table(self):
        return self._table

    @Table.setter
    def Table(self, value=0):
        self._table = value
        PlayblastBotSlaveLib.MakePlayblast()

    def _SwitchClicked(self):
        self._ui.pushButton_switch.setText('ON') if self._ui.pushButton_switch.text() == 'OFF' else self._ui.pushButton_switch.setText('OFF')
