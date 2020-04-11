# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_register_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets






class Ui_new_register_window(object):
        def setupUi(self, new_register_window):
                new_register_window.setObjectName("new_register_window")
                new_register_window.resize(800, 600)
                new_register_window.setMaximumSize(QtCore.QSize(800, 600))
                new_register_window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 97, 117, 255), stop:1 rgba(255, 255, 255, 255));")
                self.centralwidget = QtWidgets.QWidget(new_register_window)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(10, 10, 771, 581))
                self.frame.setStyleSheet("background:rgba(0,0,0,0.5);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(0, 0, 771, 81))
                self.label.setStyleSheet("background:transparent;\n""font-family: Trebuchet MS;\n""font-weight: bold;\n""font-size:25px;\n""color:white;\n""text-decoration:underline;")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(50, 120, 141, 31))
                self.label_2.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(50, 150, 141, 31))
                self.label_3.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(50, 180, 141, 31))
                self.label_4.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.frame)
                self.label_5.setGeometry(QtCore.QRect(30, 210, 181, 31))
                self.label_5.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(50, 240, 141, 31))
                self.label_6.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.frame)
                self.label_7.setGeometry(QtCore.QRect(50, 270, 141, 31))
                self.label_7.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
                self.label_7.setObjectName("label_7")
                self.new_name = QtWidgets.QLineEdit(self.frame)
                self.new_name.setGeometry(QtCore.QRect(260, 120, 321, 21))
                self.new_name.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_name.setObjectName("new_name")
                self.new_email = QtWidgets.QLineEdit(self.frame)
                self.new_email.setGeometry(QtCore.QRect(260, 150, 321, 21))
                self.new_email.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_email.setObjectName("new_email")
                self.new_text = QtWidgets.QLineEdit(self.frame)
                self.new_text.setGeometry(QtCore.QRect(260, 180, 321, 21))
                self.new_text.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_text.setObjectName("new_text")
                self.new_dateofbirth = QtWidgets.QLineEdit(self.frame)
                self.new_dateofbirth.setGeometry(QtCore.QRect(260, 210, 321, 21))
                self.new_dateofbirth.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_dateofbirth.setObjectName("new_dateofbirth")
                self.new_user = QtWidgets.QLineEdit(self.frame)
                self.new_user.setGeometry(QtCore.QRect(260, 240, 321, 21))
                self.new_user.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_user.setObjectName("new_user")
                self.new_password = QtWidgets.QLineEdit(self.frame)
                self.new_password.setGeometry(QtCore.QRect(260, 270, 321, 21))
                self.new_password.setStyleSheet("background:transparent;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:18px;\n""border:none;\n""border-bottom:0.5px solid white;")
                self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.new_password.setObjectName("new_password")
                self.new_register_save_button = QtWidgets.QPushButton(self.frame)
                self.new_register_save_button.setGeometry(QtCore.QRect(250, 360, 131, 41))
                self.new_register_save_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                self.new_register_save_button.setStyleSheet("QPushButton{\n""background:#1E90FF;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:16px;\n""font-weight:bold;\n""border-radius:10px;\n""}\n""QPushButton:hover{\n""background:#4169E1;\n""}")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.new_register_save_button.setIcon(icon)
                self.new_register_save_button.setIconSize(QtCore.QSize(16, 16))
                self.new_register_save_button.setObjectName("new_register_save_button")
                self.new_register_save_button.clicked.connect(self.save_new_register)
                self.new_register_close_button = QtWidgets.QPushButton(self.frame)
                self.new_register_close_button.setGeometry(QtCore.QRect(440, 360, 131, 41))
                self.new_register_close_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                self.new_register_close_button.setStyleSheet("QPushButton{\n""background:#1E90FF;\n""color:white;\n""font-family:Trebuchet MS;\n""font-size:16px;\n""font-weight:bold;\n""border-radius:10px;\n""}\n""QPushButton:hover{\n""background:#4169E1;\n""}")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.new_register_close_button.setIcon(icon1)
                self.new_register_close_button.setIconSize(QtCore.QSize(28, 28))
                self.new_register_close_button.setObjectName("new_register_close_button")
                self.new_register_close_button.clicked.connect(self.clear_inputs)
                self.return_saved_label = QtWidgets.QLabel(self.frame)
                self.return_saved_label.setGeometry(QtCore.QRect(150, 470, 511, 31))
                self.return_saved_label.setStyleSheet("background:transparent;\n""color:white;\n""font-family: Trebuchet MS;\n""font-size:18px;\n""")
                self.return_saved_label.setText("")
                self.return_saved_label.setAlignment(QtCore.Qt.AlignCenter)
                self.return_saved_label.setObjectName("return_saved_label")
                new_register_window.setCentralWidget(self.centralwidget)

                self.retranslateUi(new_register_window)
                QtCore.QMetaObject.connectSlotsByName(new_register_window)
                
                
                
        #========================= FUNÇÕES DOS BOTÕES ====================================================#
        def clear_inputs(self):
                self.new_name.setText("")
                self.new_email.setText("")
                self.new_text.setText("")
                self.new_dateofbirth.setText("")
                self.new_user.setText("")
                self.new_password.setText("")
                self.return_saved_label.setText("")
        
        def save_new_register(self):
                from database import Aplication_database
                if self.new_user.text() != "" and self.new_password.text() != "" and self.new_name.text() != "":
                        self.base = Aplication_database()
                        self.insert  = self.base.insert_user(self.new_name.text(),self.new_email.text(),self.new_text.text(),self.new_dateofbirth.text(),\
                                        self.new_user.text(),self.new_password.text())
                        self.return_saved_label.setText(self.insert)
                        self.new_name.setText("")
                        self.new_email.setText("")
                        self.new_text.setText("")
                        self.new_dateofbirth.setText("")
                        self.new_user.setText("")
                        self.new_password.setText("")
                else:
                        self.return_saved_label.setText("Os campos NOME, USUARIO e SENHA são obrigatórios")
        #===================================================================================================#            
                
                
        
        

        def retranslateUi(self, new_register_window):
                _translate = QtCore.QCoreApplication.translate
                new_register_window.setWindowTitle(_translate("new_register_window", "MainWindow"))
                self.label.setText(_translate("new_register_window", "CADASTRAR NOVO USUARIO"))
                self.label_2.setText(_translate("new_register_window", "Nome:"))
                self.label_3.setText(_translate("new_register_window", "Email:"))
                self.label_4.setText(_translate("new_register_window", "Telefone:"))
                self.label_5.setText(_translate("new_register_window", "Data de nascimento:"))
                self.label_6.setText(_translate("new_register_window", "Usuario:"))
                self.label_7.setText(_translate("new_register_window", "Senha:"))
                self.new_register_save_button.setText(_translate("new_register_window", " Salvar"))
                self.new_register_close_button.setText(_translate("new_register_window", "Limpar"))
import new_register_img



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_register_window = QtWidgets.QMainWindow()
    ui = Ui_new_register_window()
    ui.setupUi(new_register_window)
    sys.exit(app.exec_())
