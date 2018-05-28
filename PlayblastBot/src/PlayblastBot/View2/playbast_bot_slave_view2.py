
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog_PlayblastBotSlave(object):
    def setupUi(self, Dialog_PlayblastBotSlave):
        Dialog_PlayblastBotSlave.setObjectName("Dialog_PlayblastBotSlave")
        Dialog_PlayblastBotSlave.resize(167, 34)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_PlayblastBotSlave)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog_PlayblastBotSlave)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog_PlayblastBotSlave)
        QtCore.QMetaObject.connectSlotsByName(Dialog_PlayblastBotSlave)

    def retranslateUi(self, Dialog_PlayblastBotSlave):
        Dialog_PlayblastBotSlave.setWindowTitle(QtWidgets.QApplication.translate("Dialog_PlayblastBotSlave", "PlayblastBot Slave", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog_PlayblastBotSlave", "Cargando...", None, -1))

