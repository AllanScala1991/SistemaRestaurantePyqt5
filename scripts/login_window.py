# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from new_register_window import Ui_new_register_window






class Ui_login_window(object):
        def setupUi(self, login_window):
                login_window.setObjectName("login_window")
                login_window.setEnabled(True)
                login_window.resize(1200, 700)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(login_window.sizePolicy().hasHeightForWidth())
                login_window.setSizePolicy(sizePolicy)
                login_window.setMaximumSize(QtCore.QSize(1200, 700))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/newPrefix/window_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                login_window.setWindowIcon(icon)
                login_window.setLayoutDirection(QtCore.Qt.LeftToRight)
                login_window.setStyleSheet("QWidget{\n""background: url(:/newPrefix/login_wallpaper.jpg);\n""}")
                login_window.setIconSize(QtCore.QSize(32, 32))
                self.centralwidget = QtWidgets.QWidget(login_window)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
                self.centralwidget.setSizePolicy(sizePolicy)
                self.centralwidget.setMaximumSize(QtCore.QSize(9999, 9999))
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(380, 330, 450, 350))
                self.frame.setStyleSheet("background:rgba(0,0,0,0.8);\n""border: 0.5px solid black;\n""border-radius: 10px;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(30, 90, 101, 61))
                self.label.setStyleSheet("background:transparent;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""color:white;\n""border:none;")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(30, 170, 101, 61))
                self.label_2.setStyleSheet("background:transparent;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""color:white;\n""border:none;")
                self.label_2.setObjectName("label_2")
                self.login_input = QtWidgets.QLineEdit(self.frame)
                self.login_input.setGeometry(QtCore.QRect(140, 110, 231, 20))
                self.login_input.setStyleSheet("background:transparent;\n""border:none;\n""border-bottom:0.5px solid white;\n""border-radius:0px;\n""color:white;\n""font-size:18px;")
                self.login_input.setObjectName("login_input")
                self.password_input = QtWidgets.QLineEdit(self.frame)
                self.password_input.setGeometry(QtCore.QRect(140, 190, 231, 20))
                self.password_input.setStyleSheet("background:transparent;\n""border:none;\n""border-bottom:0.5px solid white;\n""border-radius:0px;\n""color:white;\n""font-size:18px;")
                self.password_input.setInputMask("")
                self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
                self.password_input.setObjectName("password_input")
                self.login_button = QtWidgets.QPushButton(self.frame)
                self.login_button.setGeometry(QtCore.QRect(100, 262, 131, 41))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
                self.login_button.setSizePolicy(sizePolicy)
                self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                self.login_button.clicked.connect(self.login_entry)
                self.login_button.setStyleSheet("QPushButton{\n""background:#1E90FF;\n""color:white;\n""font-family: Trebuchet MS;\n""font-weight:bold;\n""font-size:14px;\n""}\n""QPushButton:hover{\n""background:#4169E1;\n""}")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/newPrefix/login_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.login_button.setIcon(icon1)
                self.login_button.setIconSize(QtCore.QSize(16, 16))
                self.login_button.setObjectName("login_button")
                self.new_register_button = QtWidgets.QPushButton(self.frame)
                self.new_register_button.clicked.connect(self.new_register)
                self.new_register_button.setGeometry(QtCore.QRect(250, 260, 131, 41))
                self.new_register_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                self.new_register_button.setStyleSheet("QPushButton{\n""background:#1E90FF;\n""color:white;\n""font-family: Trebuchet MS;\n""font-weight:bold;\n""font-size:14px\n""}\n""\n""QPushButton:hover{\n""background:#4169E1;\n""}")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/newPrefix/cadastrar_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.new_register_button.setIcon(icon2)
                self.new_register_button.setIconSize(QtCore.QSize(16, 16))
                self.new_register_button.setObjectName("new_register_button")
                self.toolButton = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton.setGeometry(QtCore.QRect(-10, 0, 1161, 221))
                self.toolButton.setStyleSheet("background: transparent;")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/newPrefix/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.toolButton.setIcon(icon3)
                self.toolButton.setIconSize(QtCore.QSize(1200, 1200))
                self.toolButton.setObjectName("toolButton")
                self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_2.setGeometry(QtCore.QRect(520, 260, 161, 121))
                self.toolButton_2.setStyleSheet("background:transparent;")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap(":/newPrefix/login_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.toolButton_2.setIcon(icon4)
                self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
                self.toolButton_2.setObjectName("toolButton_2")
                self.return_saved_label = QtWidgets.QLabel(self.frame)
                self.return_saved_label.setGeometry(QtCore.QRect(125, 310, 250, 30))
                self.return_saved_label.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:15px;\n""border:none;\n""")
                self.return_saved_label.setText("")
                self.return_saved_label.setAlignment(QtCore.Qt.AlignCenter)
                self.return_saved_label.setObjectName("return_saved_label")
                login_window.setCentralWidget(self.centralwidget)

                self.retranslateUi(login_window)
                QtCore.QMetaObject.connectSlotsByName(login_window)

#==============================FUNÇÕES DOS BOTÕES===============================================#

        def new_register(self):# FUNÇÃO PARA CHAMAR A JANELA DE REGISTRO
                self.window = QtWidgets.QMainWindow()# ATRIBUI A VARIAVEL O WINDOW
                self.ui = Ui_new_register_window()#ATRIBUI A VARIVAEL, A CLASSE DA JANELA QUE VOCE DESEJA CHAMAR
                self.ui.setupUi(self.window)#CHAMA PELA VARIAVEL O INIT DA CLASSE DA JANELA QUE VOCE DESEJA CHAMAR E ATRIBUI A PRIMEIRA VARIAVEL NELA
                self.window.show()#MOSTRA A JANELA
        def login_entry(self):
                from database import Aplication_database
                from menu import Ui_menu_window
                self.database = Aplication_database()
                self.search_user = self.database.select_user(self.login_input.text())
                try:
                        if self.search_user[0] == self.login_input.text():
                                if self.search_user[1] == self.password_input.text():
                                        self.database.create_tables()
                                        self.menu_window = QtWidgets.QMainWindow()
                                        self.menu_ui = Ui_menu_window()
                                        self.menu_ui.setupUi(self.menu_window)
                                        login_window.close()
                                        self.menu_window.show()

                                else:
                                        self.return_saved_label.setText("Senha está incorreta.")
                except Exception as error:
                        print(error)
                        self.return_saved_label.setText("Usuario está incorreto ou não existe.")


#===================================================================================================

        def retranslateUi(self, login_window):
                _translate = QtCore.QCoreApplication.translate
                login_window.setWindowTitle(_translate("login_window", "Restaurantes Requinte"))
                self.label.setText(_translate("login_window", "Usuario:"))
                self.label_2.setText(_translate("login_window", "Senha:"))
                self.login_button.setText(_translate("login_window", " Confirmar"))
                self.new_register_button.setText(_translate("login_window", " Cadastrar"))
                self.toolButton.setText(_translate("login_window", "..."))
                self.toolButton_2.setText(_translate("login_window", "..."))

import resources



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
