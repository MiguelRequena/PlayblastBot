from PlayblastBot.Lib import PlayblastBotManagerLib
from PowerRing.Purple.Controller import SelectCellsTableController


try:
    from PlayblastBot.View import Ui_Dialog_PlayblastBotManager
except ImportError:
    from PlayblastBot.View2 import Ui_Dialog_PlayblastBotManager

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


class PlayblastBotManagerController(object):
    def __init__(self):
        self._ui = Ui_Dialog_PlayblastBotManager()
        self._dialog = QDialog()
        self._ui.setupUi(self._dialog)

        self._sct_jobs = None

        self._table = None
        print 'PlayblastBotManagerController'
        print PlayblastBotManagerLib.GetValue()

    def Initialize(self):
        self._ui.pushButton_switch.clicked.connect(self._SwitchClicked)

        self._sct_jobs = SelectCellsTableController()
        # self._sct_cache.SetHeaderLabels(['Sequence', 'Shot', 'Cache', 'Status', 'Priority', 'Complexity', 'Size', 'Progress'])
        self._sct_jobs.SetHeaderLabels(['Name'])
        self._sct_jobs.Initialize()
        self._ui.verticalLayout_table.addWidget(self._sct_jobs.GetWidget())

        self._sct_jobs.SetRows(PlayblastBotManagerLib.GetJobsData())
        self._sct_jobs.Fill()
        self._sct_jobs.GetTableWidget().resizeColumnsToContents()
        self._sct_jobs.GetTableWidget().resizeRowsToContents()

        #print self._sct_jobs.GetRows()

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
        PlayblastBotManagerLib.MakePlayblast()

    def _SwitchClicked(self):
        self._ui.pushButton_switch.setText('ON') if self._ui.pushButton_switch.text() == 'OFF' else self._ui.pushButton_switch.setText('OFF')
