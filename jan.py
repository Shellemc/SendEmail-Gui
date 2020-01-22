# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jan.ui',
# licensing of 'jan.ui' applies.
#
# Created: Wed Dec 25 22:19:59 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mensagem.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("image: None;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Mensagem = QtWidgets.QLabel(self.centralwidget)
        self.Mensagem.setObjectName("Mensagem")
        self.gridLayout_2.addWidget(self.Mensagem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.Para = QtWidgets.QLabel(self.frame)
        self.Para.setObjectName("Para")
        self.gridLayout.addWidget(self.Para, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.De = QtWidgets.QLabel(self.frame)
        self.De.setObjectName("De")
        self.gridLayout.addWidget(self.De, 0, 0, 1, 1)
        self.Assunto = QtWidgets.QLabel(self.frame)
        self.Assunto.setObjectName("Assunto")
        self.gridLayout.addWidget(self.Assunto, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.Senha = QtWidgets.QLabel(self.frame)
        self.Senha.setObjectName("Senha")
        self.gridLayout.addWidget(self.Senha, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionVers_o = QtWidgets.QAction(MainWindow)
        self.actionVers_o.setObjectName("actionVers_o")
        self.menuOp_es.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionVers_o)
        self.menubar.addAction(self.menuOp_es.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL("triggered(bool)"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Envio de E-mails", None, -1))
        self.Mensagem.setText(QtWidgets.QApplication.translate("MainWindow", "Mensagem:", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "ENVIAR", None, -1))
        self.lineEdit_3.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Digite o e-mail de destino", None, -1))
        self.Para.setText(QtWidgets.QApplication.translate("MainWindow", "Para:", None, -1))
        self.lineEdit_4.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Assunto do e-mail", None, -1))
        self.De.setText(QtWidgets.QApplication.translate("MainWindow", "De:", None, -1))
        self.Assunto.setText(QtWidgets.QApplication.translate("MainWindow", "Assunto:", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Digite seu e-mail", None, -1))
        self.Senha.setText(QtWidgets.QApplication.translate("MainWindow", "Senha:", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Digite sua senha", None, -1))
        self.menuOp_es.setTitle(QtWidgets.QApplication.translate("MainWindow", "Opções", None, -1))
        self.menuSobre.setTitle(QtWidgets.QApplication.translate("MainWindow", "Sobre", None, -1))
        self.actionSair.setText(QtWidgets.QApplication.translate("MainWindow", "Sair", None, -1))
        self.actionVers_o.setText(QtWidgets.QApplication.translate("MainWindow", "Versão", None, -1))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
