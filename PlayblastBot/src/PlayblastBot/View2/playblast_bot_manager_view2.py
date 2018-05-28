
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog_PlayblastBotManager(object):
    def setupUi(self, Dialog_PlayblastBotManager):
        Dialog_PlayblastBotManager.setObjectName("Dialog_PlayblastBotManager")
        Dialog_PlayblastBotManager.resize(683, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_PlayblastBotManager)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_table = QtWidgets.QVBoxLayout()
        self.verticalLayout_table.setObjectName("verticalLayout_table")
        self.verticalLayout_2.addLayout(self.verticalLayout_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_switch = QtWidgets.QPushButton(Dialog_PlayblastBotManager)
        self.pushButton_switch.setObjectName("pushButton_switch")
        self.horizontalLayout.addWidget(self.pushButton_switch)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_PlayblastBotManager)
        QtCore.QMetaObject.connectSlotsByName(Dialog_PlayblastBotManager)

    def retranslateUi(self, Dialog_PlayblastBotManager):
        Dialog_PlayblastBotManager.setWindowTitle(QtWidgets.QApplication.translate("Dialog_PlayblastBotManager", "PlayblastBot Manager", None, -1))
        self.pushButton_switch.setText(QtWidgets.QApplication.translate("Dialog_PlayblastBotManager", "OFF", None, -1))

