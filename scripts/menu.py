# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from database import Aplication_database
from datetime import date, datetime
from api import cep_select
import json

class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.setWindowModality(QtCore.Qt.NonModal)
        menu_window.setEnabled(True)
        menu_window.resize(1200, 700)
        menu_window.setMaximumSize(QtCore.QSize(1200, 700))
        icon = QtGui.QIcon.fromTheme(":/menu/window_icon.ico")
        menu_window.setWindowIcon(icon)
        menu_window.setStyleSheet("QWidget{\n"
"background:url(:/menu/menu_wallpaper.jpg);\n"
"}")
        menu_window.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 700))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_bar = QtWidgets.QFrame(self.centralwidget)
        self.frame_bar.setGeometry(QtCore.QRect(0, 0, 1200, 52))
        self.frame_bar.setMaximumSize(QtCore.QSize(1200, 100))
        self.frame_bar.setStyleSheet("border: 1px solid black;\n"
"background: transparent;\n"
"border:none;")
        self.frame_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bar.setObjectName("frame_bar")
        self.label_welcome = QtWidgets.QLabel(self.frame_bar)
        self.label_welcome.setGeometry(QtCore.QRect(30, 30, 260, 23))
        self.label_welcome.setStyleSheet("font-family: Trebuchet MS;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border:none;\n"
"text-decoration:underline;\n"
"")
        self.label_welcome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.button_pedido = QtWidgets.QPushButton(self.frame_bar)
        self.button_pedido.setGeometry(QtCore.QRect(300, 30, 101, 23))
        self.button_pedido.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_pedido.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/pedido_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pedido.setIcon(icon)
        self.button_pedido.setObjectName("button_pedido")
        self.button_caixa = QtWidgets.QPushButton(self.frame_bar)
        self.button_caixa.setGeometry(QtCore.QRect(410, 30, 101, 23))
        self.button_caixa.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_caixa.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left: 1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/caixa_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_caixa.setIcon(icon1)
        self.button_caixa.setObjectName("button_caixa")
        self.button_mesas = QtWidgets.QPushButton(self.frame_bar)
        self.button_mesas.setGeometry(QtCore.QRect(520, 30, 101, 23))
        self.button_mesas.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_mesas.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/mesa_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mesas.setIcon(icon2)
        self.button_mesas.setIconSize(QtCore.QSize(20, 20))
        self.button_mesas.setObjectName("button_mesas")
        self.button_produtos = QtWidgets.QPushButton(self.frame_bar)
        self.button_produtos.setGeometry(QtCore.QRect(630, 30, 101, 23))
        self.button_produtos.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_produtos.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/produtos_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_produtos.setIcon(icon3)
        self.button_produtos.setObjectName("button_produtos")
        self.button_relatorio = QtWidgets.QPushButton(self.frame_bar)
        self.button_relatorio.setGeometry(QtCore.QRect(740, 30, 101, 23))
        self.button_relatorio.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_relatorio.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/relatorio_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_relatorio.setIcon(icon4)
        self.button_relatorio.setObjectName("button_relatorio")
        self.button_cliente = QtWidgets.QPushButton(self.frame_bar)
        self.button_cliente.setGeometry(QtCore.QRect(850, 30, 101, 23))
        self.button_cliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_cliente.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu/icon-estoque.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_cliente.setIcon(icon5)
        self.button_cliente.setIconSize(QtCore.QSize(20, 20))
        self.button_cliente.setObjectName("button_cliente")
        self.button_usuario = QtWidgets.QPushButton(self.frame_bar)
        self.button_usuario.setGeometry(QtCore.QRect(960, 30, 101, 23))
        self.button_usuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_usuario.setStyleSheet("QPushButton{\n"
"border:none;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border-left:1px solid white;\n"
"border-right: 1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/menu/developer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_usuario.setIcon(icon6)
        self.button_usuario.setObjectName("button_usuario")
        self.f_inicio = QtWidgets.QFrame(self.centralwidget)
        self.f_inicio.setEnabled(True)
        self.f_inicio.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_inicio.setStyleSheet("background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"")
        self.f_inicio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_inicio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_inicio.setObjectName("f_inicio")
        self.toolButton_4 = QtWidgets.QToolButton(self.f_inicio)
        self.toolButton_4.setGeometry(QtCore.QRect(400, 100, 400, 400))
        self.toolButton_4.setStyleSheet("QToolButton{\n"
"background:transparent;\n"
"color:white;\n"
"}")
        self.toolButton_4.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/menu/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon12)
        self.toolButton_4.setIconSize(QtCore.QSize(400, 400))
        self.toolButton_4.setObjectName("toolButton_4")

        self.f_pedidos = QtWidgets.QFrame(self.centralwidget)
        self.f_pedidos.setEnabled(True)
        self.f_pedidos.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_pedidos.setStyleSheet("background:rgba(0,0,0,0.5);\n"
"border-radius:10px;")
        self.f_pedidos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_pedidos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_pedidos.setObjectName("f_pedidos")

        self.frame_table = QtWidgets.QFrame(self.f_pedidos)
        self.frame_table.setGeometry(QtCore.QRect(400, 200, 250, 200))
        self.frame_table.setStyleSheet("background:rgba(0,0,0,0.95);\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.label_table = QtWidgets.QLabel(self.frame_table)
        self.label_table.setGeometry(QtCore.QRect(0, 20, 100, 40))
        self.label_table.setAlignment(QtCore.Qt.AlignCenter)
        self.label_table.setObjectName("label_table")
        self.label_table.setText("MESA:")
        self.label_table.setStyleSheet("color:white;"  "background:transparent;")
        self.table_entry  = QtWidgets.QLineEdit(self.frame_table)
        self.table_entry.setGeometry(QtCore.QRect(90, 30, 120, 20))
        self.table_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.table_entry.setObjectName("table_entry")
        self.table_entry.setStyleSheet("color:white ;"  "background:transparent;" "border-radius:none;"  "border:none;" "border-bottom:1px solid white")
        self.button_table_confirm = QtWidgets.QPushButton(self.frame_table)
        self.button_table_confirm.setGeometry(QtCore.QRect(80, 100, 100, 30))
        self.button_table_confirm.setObjectName("button_table_confirm")
        self.button_table_confirm.setText("CONFIRMAR")
        self.button_table_confirm.setStyleSheet("color:white;"  "background:#1E90FF;")
        self.button_table_confirm.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))




        self.frame = QtWidgets.QFrame(self.f_pedidos)
        self.frame.setGeometry(QtCore.QRect(10, 10, 231, 111))
        self.frame.setStyleSheet("background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 41))
        self.label.setStyleSheet("background:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.box_mesas = QtWidgets.QComboBox(self.frame)
        self.box_mesas.setGeometry(QtCore.QRect(70, 50, 81, 31))
        self.box_mesas.setStyleSheet("background:white;\n"
"border-radius:2px;\n"
"border:1px solid white;")
        self.box_mesas.setObjectName("box_mesas")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.box_mesas.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.f_pedidos)
        self.frame_2.setGeometry(QtCore.QRect(280, 10, 891, 111))
        self.frame_2.setStyleSheet("background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.adicionar_button = QtWidgets.QPushButton(self.frame_2)
        self.adicionar_button.setGeometry(QtCore.QRect(50, 20, 101, 71))
        self.adicionar_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.adicionar_button.setStyleSheet("QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        self.adicionar_button.setText("")
        self.adicionar_button.clicked.connect(self.add_sales)
        self.adicionar_frame = QtWidgets.QFrame(self.f_pedidos)
        self.adicionar_frame.setGeometry(QtCore.QRect(100,150,300,150))
        self.adicionar_frame.setStyleSheet("background:rgba(0,0,0,0.95);")
        self.adicionar_box = QtWidgets.QComboBox(self.adicionar_frame)
        self.adicionar_box.setGeometry(QtCore.QRect(50,50,200,20))
        self.adicionar_box.setStyleSheet("background:white;")
        self.adicionar_label = QtWidgets.QLabel(self.adicionar_frame)
        self.adicionar_label.setGeometry(QtCore.QRect(70,10,200,20))
        self.adicionar_label.setStyleSheet("color:white;" "font-family:Trebuchet MS;" "font-size:16px;")
        self.adicionar_label.setText("Selecione um produto:")
        self.adicionar_confirmar = QtWidgets.QPushButton(self.adicionar_frame)
        self.adicionar_confirmar.setGeometry(QtCore.QRect(30,100,100,30))
        self.adicionar_confirmar.setStyleSheet("color:white;" "font-family:Trebuchet MS;" "font-size:12px;" "background: blue;")
        self.adicionar_confirmar.setText("CONFIRMAR")
        self.adicionar_confirmar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.adicionar_confirmar.clicked.connect(self.insert_sale)

        self.adicionar_hidden = QtWidgets.QPushButton(self.adicionar_frame)
        self.adicionar_hidden.setGeometry(QtCore.QRect(160,100,100,30))
        self.adicionar_hidden.setStyleSheet("color:white;" "font-family:Trebuchet MS;" "font-size:12px;" "background: blue;")
        self.adicionar_hidden.setText("FECHAR")
        self.adicionar_hidden.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.adicionar_hidden.clicked.connect(self.hidden_sale)


        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/menu/adicionar_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adicionar_button.setIcon(icon7)
        self.adicionar_button.setIconSize(QtCore.QSize(64, 64))
        self.adicionar_button.setObjectName("adicionar_button")
        self.delete_button = QtWidgets.QPushButton(self.frame_2)
        self.delete_button.setGeometry(QtCore.QRect(260, 20, 101, 71))
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delete_button.setStyleSheet("QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        self.delete_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/menu/deletar_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon9)
        self.delete_button.setIconSize(QtCore.QSize(64, 64))
        self.delete_button.setObjectName("delete_button")
        self.table_button = QtWidgets.QPushButton(self.frame_2)
        self.table_button.setGeometry(QtCore.QRect(470, 20, 101, 71))
        self.table_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.table_button.setStyleSheet("QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        self.table_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/menu/mesa2_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.table_button.setIcon(icon10)
        self.table_button.setIconSize(QtCore.QSize(64, 64))
        self.table_button.setObjectName("table_button")
        self.table_button_2 = QtWidgets.QPushButton(self.frame_2)
        self.table_button_2.setGeometry(QtCore.QRect(690, 20, 101, 71))
        self.table_button_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.table_button_2.setStyleSheet("QPushButton{\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight: bold;\n"
"border:1px solid white;\n"
"background-color:rgba(255,255,255,0.2);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"background-color:rgba(255,255,255,0.6);\n"
"\n"
"}\n"
"")
        self.table_button_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/menu/entrega_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.table_button_2.setIcon(icon11)
        self.table_button_2.setIconSize(QtCore.QSize(64, 64))
        self.table_button_2.setObjectName("table_button_2")
        self.frame_3 = QtWidgets.QFrame(self.f_pedidos)
        self.frame_3.setGeometry(QtCore.QRect(10, 160, 1161, 421))
        self.frame_3.setStyleSheet("background:#6959CD;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.close_table = QtWidgets.QPushButton(self.frame_3)
        self.close_table.setGeometry(QtCore.QRect(555, 200, 131, 41))
        self.close_table.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.close_table.setStyleSheet("QPushButton{\n"
"background: red;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.close_table.setObjectName("close_table")
        self.close_table.setText("FECHAR MESA")

        self.table_label2 = QtWidgets.QLabel(self.frame_3)
        self.table_label2.setGeometry(QtCore.QRect(550, 340, 181, 20))
        self.table_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.table_label2.setObjectName("table_label")
        self.table_label2.setText("")
        self.table_label2.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")

        self.f_buy = QtWidgets.QFrame(self.frame_3)
        self.f_buy.setGeometry(QtCore.QRect(10, 30, 441, 381))
        self.f_buy.setStyleSheet("background:#E0EEEE;\n"
"font-family: Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"")
        self.f_buy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_buy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_buy.setObjectName("f_buy")
        self.tableView = QtWidgets.QListWidget(self.f_buy)
        self.tableView.setGeometry(QtCore.QRect(15, 11, 411, 361))
        self.tableView.setStyleSheet("background:white;")
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 441, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setGeometry(QtCore.QRect(470, 40, 331, 161))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(3, 20, 321, 131))
        self.textEdit.setStyleSheet("background:white;\n"
"border-radius:10px;\n"
"border:none")
        self.textEdit.setObjectName("textEdit")
        self.produto_confirmar = QtWidgets.QPushButton(self.frame_3)
        self.produto_confirmar.setGeometry(QtCore.QRect(490, 200, 131, 41))
        self.produto_confirmar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.produto_confirmar.setStyleSheet("QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.produto_confirmar.setObjectName("produto_confirmar")
        self.produto_limpar = QtWidgets.QPushButton(self.frame_3)
        self.produto_limpar.setGeometry(QtCore.QRect(640, 200, 131, 41))
        self.produto_limpar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.produto_limpar.setStyleSheet("QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 16px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.produto_limpar.setObjectName("produto_limpar")
        self.total_frame = QtWidgets.QFrame(self.frame_3)
        self.total_frame.setGeometry(QtCore.QRect(460,260,360,150))
        self.total_frame.setStyleSheet('background: rgba(0,0,0,0.5)')
        self.label_total = QtWidgets.QLabel(self.total_frame)
        self.label_total.setGeometry(QtCore.QRect(10,10,60,40))
        self.label_total.setStyleSheet('color:white;''font-family:Trebuchet MS;' 'background:transparent;')
        self.label_total.setText("TOTAL:")
        self.label2_total = QtWidgets.QLabel(self.total_frame)
        self.label2_total.setGeometry(QtCore.QRect(80,10,150,40))
        self.label2_total.setStyleSheet('color:white;''font-family:Trebuchet MS;' 'background:transparent;')
        self.label2_total.setText("0,00")
        self.label_recebido = QtWidgets.QLabel(self.total_frame)
        self.label_recebido.setGeometry(QtCore.QRect(10,40,150,40))
        self.label_recebido.setStyleSheet('color:white;''font-family:Trebuchet MS;' 'background:transparent;')
        self.label_recebido.setText("RECEBIDO:")
        self.input_recebido = QtWidgets.QLineEdit(self.total_frame)
        self.input_recebido.setGeometry(QtCore.QRect(90, 50, 150, 20))
        self.input_recebido.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"border-radius:none;\n"
"color:white;")
        self.input_recebido.setObjectName("input_recebido")
        self.troco_calcular = QtWidgets.QPushButton(self.total_frame)
        self.troco_calcular.setGeometry(QtCore.QRect(120, 80, 80, 20))
        self.troco_calcular.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.troco_calcular.setStyleSheet("QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 12px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.troco_calcular.setObjectName("calcular_troco")
        self.troco_calcular.setText("Calcular Troco")
        self.label_troco = QtWidgets.QLabel(self.total_frame)
        self.label_troco.setGeometry(QtCore.QRect(10,100,150,40))
        self.label_troco.setStyleSheet('color:white;''font-family:Trebuchet MS;' 'background:transparent;')
        self.label_troco.setText("TROCO:")
        self.label2_troco = QtWidgets.QLabel(self.total_frame)
        self.label2_troco.setGeometry(QtCore.QRect(80,100,150,40))
        self.label2_troco.setStyleSheet('color:white;''font-family:Trebuchet MS;' 'background:transparent;')
        self.label2_troco.setText("0,00")
        self.endereco_box = QtWidgets.QGroupBox(self.frame_3)
        self.endereco_box.setGeometry(QtCore.QRect(830, 60, 311, 351))
        self.endereco_box.setStyleSheet("border:1px solid black;\n"
"background:rgba(0,0,0,0.5);\n"
"color:white;\n"
"font-family:Trebuchet MS;")
        self.endereco_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.endereco_box.setFlat(False)
        self.endereco_box.setCheckable(False)
        self.endereco_box.setObjectName("endereco_box")
        self.label_3 = QtWidgets.QLabel(self.endereco_box)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 41, 21))
        self.label_3.setStyleSheet("background:transparent;\n"
"border:none;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.endereco_box)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_4.setStyleSheet("background:transparent;\n"
"border:none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.endereco_box)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 101, 16))
        self.label_5.setStyleSheet("background:transparent;\n"
"border:none;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.endereco_box)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 101, 16))
        self.label_6.setStyleSheet("background:transparent;\n"
"border:none;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.endereco_box)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 101, 16))
        self.label_7.setStyleSheet("background:transparent;\n"
"border:none;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.endereco_box)
        self.label_8.setGeometry(QtCore.QRect(110, 170, 190, 16))
        self.label_8.setStyleSheet("background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLineEdit(self.endereco_box)
        self.label_9.setGeometry(QtCore.QRect(110, 210, 190, 16))
        self.label_9.setStyleSheet("background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.endereco_box)
        self.label_10.setGeometry(QtCore.QRect(110, 250, 190, 16))
        self.label_10.setStyleSheet("background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.endereco_box)
        self.label_11.setGeometry(QtCore.QRect(110, 290, 180, 16))
        self.label_11.setStyleSheet("background: transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.input_cep = QtWidgets.QLineEdit(self.endereco_box)
        self.input_cep.setGeometry(QtCore.QRect(70, 60, 221, 20))
        self.input_cep.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"border-radius:none;\n"
"")
        self.input_cep.setObjectName("input_cep")
        self.produto_buscar = QtWidgets.QPushButton(self.endereco_box)
        self.produto_buscar.setGeometry(QtCore.QRect(110, 100, 101, 31))
        self.produto_buscar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.produto_buscar.setStyleSheet("QPushButton{\n"
"background: blue;\n"
"font-family: Trebuchet MS;\n"
"font-size: 12px;\n"
"color: white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#1E90FF;\n"
"}\n"
"")
        self.produto_buscar.setObjectName("produto_buscar")
        self.f_caixa = QtWidgets.QFrame(self.centralwidget)
        self.f_caixa.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_caixa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.f_caixa.setStyleSheet("background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"")
        self.f_caixa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_caixa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_caixa.setObjectName("f_caixa")
        self.groupBox_2 = QtWidgets.QGroupBox(self.f_caixa)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 1151, 281))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border: 1px solid white;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(320, 70, 81, 21))
        self.label_12.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(320, 120, 81, 21))
        self.label_13.setStyleSheet("border:none;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.label_13.setObjectName("label_13")
        self.abertura_valor = QtWidgets.QLineEdit(self.groupBox_2)
        self.abertura_valor.setGeometry(QtCore.QRect(380, 70, 221, 20))
        self.abertura_valor.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.abertura_valor.setObjectName("abertura_valor")

        self.abertura_data = QtWidgets.QDateEdit(self.groupBox_2)
        self.abertura_data.setGeometry(QtCore.QRect(390, 120, 111, 22))
        self.abertura_data.setStyleSheet("border-radius:5px;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.abertura_data.setObjectName("abertura_data")

        self.abertura_label = QtWidgets.QLabel(self.groupBox_2)
        self.abertura_label.setGeometry(QtCore.QRect(370, 160, 191, 20))
        self.abertura_label.setStyleSheet("border-radius:5px;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.abertura_label.setObjectName("abertura_label")
        self.abertura_label.setText("")



        self.confirmar_abertura = QtWidgets.QPushButton(self.groupBox_2)
        self.confirmar_abertura.setGeometry(QtCore.QRect(400, 200, 121, 41))
        self.confirmar_abertura.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.confirmar_abertura.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.confirmar_abertura.setObjectName("confirmar_abertura")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setGeometry(QtCore.QRect(730, 40, 381, 221))
        self.calendarWidget.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.f_caixa)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 310, 1151, 281))
        self.groupBox_3.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border: 1px solid white;")
        self.groupBox_3.setObjectName("groupBox_3")

        self.fechamento_label = QtWidgets.QLabel(self.groupBox_3)
        self.fechamento_label.setGeometry(QtCore.QRect(770, 150, 191, 20))
        self.fechamento_label.setStyleSheet("border-radius:5px;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;" "border:none;")
        self.fechamento_label.setObjectName("fechamento_label")
        self.fechamento_label.setText("")

        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(100, 60, 331, 21))
        self.label_14.setStyleSheet("border:none;")
        self.label_14.setObjectName("label_14")
        self.fecha_data = QtWidgets.QDateEdit(self.groupBox_3)
        self.fecha_data.setGeometry(QtCore.QRect(440, 60, 120, 21))
        self.fecha_data.setStyleSheet("border:none;\n"
"text-decoration: underline;\n"
"color:yellow;\n"
"font-weight:bold;")
        self.fecha_data.setObjectName("fecha_data")
        self.fecha_buscar = QtWidgets.QPushButton(self.groupBox_3)
        self.fecha_buscar.setGeometry(QtCore.QRect(580, 60, 111, 23))
        self.fecha_buscar.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.fecha_buscar.setObjectName("fecha_buscar")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(300, 120, 121, 31))
        self.label_15.setStyleSheet("border:none;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(360, 160, 61, 31))
        self.label_16.setStyleSheet("border:none;")
        self.label_16.setObjectName("label_16")
        self.fecha_confirmar = QtWidgets.QPushButton(self.groupBox_3)
        self.fecha_confirmar.setGeometry(QtCore.QRect(410, 220, 111, 41))
        self.fecha_confirmar.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline\n"
"}")
        self.fecha_confirmar.setObjectName("fecha_confirmar")
        self.fecha_status = QtWidgets.QLabel(self.groupBox_3)
        self.fecha_status.setGeometry(QtCore.QRect(440, 170, 141, 16))
        self.fecha_status.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"")
        self.fecha_status.setText("")
        self.fecha_status.setObjectName("fecha_status")
        self.fecha_valor = QtWidgets.QLabel(self.groupBox_3)
        self.fecha_valor.setGeometry(QtCore.QRect(440, 130, 141, 16))
        self.fecha_valor.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"")
        self.fecha_valor.setText("")
        self.fecha_valor.setObjectName("fecha_valor")
        self.f_mesas = QtWidgets.QFrame(self.centralwidget)
        self.f_mesas.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_mesas.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.f_mesas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_mesas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_mesas.setObjectName("f_mesas")




        self.f_produtos = QtWidgets.QFrame(self.centralwidget)
        self.f_produtos.setEnabled(True)
        self.f_produtos.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_produtos.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}\n"
"QGroupBox{\n"
"font-family: Trebuchet MS;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"")
        self.f_produtos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_produtos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_produtos.setObjectName("f_produtos")
        self.groupBox_5 = QtWidgets.QGroupBox(self.f_produtos)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 20, 351, 541))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_67 = QtWidgets.QLabel(self.groupBox_5)
        self.label_67.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.label_67.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_5)
        self.label_68.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_68.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_5)
        self.label_69.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.label_69.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_5)
        self.label_70.setGeometry(QtCore.QRect(20, 200, 81, 21))
        self.label_70.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.groupBox_5)
        self.label_71.setGeometry(QtCore.QRect(20, 240, 81, 21))
        self.label_71.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.groupBox_5)
        self.label_72.setGeometry(QtCore.QRect(20, 280, 81, 21))
        self.label_72.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_72.setObjectName("label_72")
        self.novo_prod_nome = QtWidgets.QLineEdit(self.groupBox_5)
        self.novo_prod_nome.setGeometry(QtCore.QRect(120, 80, 221, 20))
        self.novo_prod_nome.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_nome.setObjectName("novo_prod_nome")
        self.novo_prod_marca = QtWidgets.QLineEdit(self.groupBox_5)
        self.novo_prod_marca.setGeometry(QtCore.QRect(120, 120, 221, 20))
        self.novo_prod_marca.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_marca.setObjectName("novo_prod_marca")
        self.novo_prod_qtd = QtWidgets.QLineEdit(self.groupBox_5)
        self.novo_prod_qtd.setGeometry(QtCore.QRect(120, 160, 221, 20))
        self.novo_prod_qtd.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_qtd.setObjectName("novo_prod_qtd")
        self.novo_prod_valor = QtWidgets.QLineEdit(self.groupBox_5)
        self.novo_prod_valor.setGeometry(QtCore.QRect(120, 200, 221, 20))
        self.novo_prod_valor.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.novo_prod_valor.setObjectName("novo_prod_valor")
        self.novo_prod_categ = QtWidgets.QComboBox(self.groupBox_5)
        self.novo_prod_categ.setGeometry(QtCore.QRect(120, 240, 221, 22))
        self.novo_prod_categ.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.novo_prod_categ.setObjectName("novo_prod_categ")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_categ.addItem("")
        self.novo_prod_descri = QtWidgets.QTextEdit(self.groupBox_5)
        self.novo_prod_descri.setGeometry(QtCore.QRect(120, 280, 221, 151))
        self.novo_prod_descri.setStyleSheet("background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.novo_prod_descri.setObjectName("novo_prod_descri")
        self.novo_prod_cadastrar = QtWidgets.QPushButton(self.groupBox_5)
        self.novo_prod_cadastrar.setGeometry(QtCore.QRect(10, 490, 111, 41))
        self.novo_prod_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.novo_prod_cadastrar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.novo_prod_cadastrar.setObjectName("novo_prod_cadastrar")
        self.groupBox_6 = QtWidgets.QGroupBox(self.f_produtos)
        self.groupBox_6.setGeometry(QtCore.QRect(420, 20, 351, 541))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_73 = QtWidgets.QLabel(self.groupBox_6)
        self.label_73.setGeometry(QtCore.QRect(0, 30, 351, 21))
        self.label_73.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setObjectName("label_73")
        self.edit_prod_nome_input = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_prod_nome_input.setGeometry(QtCore.QRect(70, 60, 221, 20))
        self.edit_prod_nome_input.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_nome_input.setInputMask("")
        self.edit_prod_nome_input.setObjectName("edit_prod_nome_input")
        self.edit_prod_buscar = QtWidgets.QPushButton(self.groupBox_6)
        self.edit_prod_buscar.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.edit_prod_buscar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.edit_prod_buscar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.edit_prod_buscar.setObjectName("edit_prod_buscar")
        self.label_74 = QtWidgets.QLabel(self.groupBox_6)
        self.label_74.setGeometry(QtCore.QRect(20, 210, 91, 21))
        self.label_74.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_74.setObjectName("label_74")
        self.edit_prod_marca = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_prod_marca.setGeometry(QtCore.QRect(120, 170, 221, 20))
        self.edit_prod_marca.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_marca.setObjectName("edit_prod_marca")
        self.label_75 = QtWidgets.QLabel(self.groupBox_6)
        self.label_75.setGeometry(QtCore.QRect(20, 290, 81, 21))
        self.label_75.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.groupBox_6)
        self.label_76.setGeometry(QtCore.QRect(20, 170, 81, 21))
        self.label_76.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_76.setObjectName("label_76")
        self.edit_prod_nome = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_prod_nome.setGeometry(QtCore.QRect(120, 130, 221, 20))
        self.edit_prod_nome.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_nome.setObjectName("edit_prod_nome")
        self.edit_prod_categ = QtWidgets.QComboBox(self.groupBox_6)
        self.edit_prod_categ.setGeometry(QtCore.QRect(120, 290, 221, 22))
        self.edit_prod_categ.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.edit_prod_categ.setObjectName("edit_prod_categ")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_categ.addItem("")
        self.edit_prod_descri = QtWidgets.QTextEdit(self.groupBox_6)
        self.edit_prod_descri.setGeometry(QtCore.QRect(120, 330, 221, 151))
        self.edit_prod_descri.setStyleSheet("background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.edit_prod_descri.setObjectName("edit_prod_descri")
        self.label_77 = QtWidgets.QLabel(self.groupBox_6)
        self.label_77.setGeometry(QtCore.QRect(20, 130, 81, 21))
        self.label_77.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.groupBox_6)
        self.label_78.setGeometry(QtCore.QRect(20, 330, 81, 21))
        self.label_78.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.groupBox_6)
        self.label_79.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.label_79.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_79.setObjectName("label_79")
        self.edit_prod_valor = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_prod_valor.setGeometry(QtCore.QRect(120, 250, 221, 20))
        self.edit_prod_valor.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_valor.setObjectName("edit_prod_valor")
        self.edit_prod_qtd = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_prod_qtd.setGeometry(QtCore.QRect(120, 210, 221, 20))
        self.edit_prod_qtd.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.edit_prod_qtd.setObjectName("edit_prod_qtd")
        self.edit_prod_salvar = QtWidgets.QPushButton(self.groupBox_6)
        self.edit_prod_salvar.setGeometry(QtCore.QRect(10, 490, 111, 41))
        self.edit_prod_salvar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.edit_prod_salvar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.edit_prod_salvar.setObjectName("edit_prod_salvar")
        self.groupBox_7 = QtWidgets.QGroupBox(self.f_produtos)
        self.groupBox_7.setGeometry(QtCore.QRect(810, 20, 351, 541))
        self.groupBox_7.setObjectName("groupBox_7")
        self.delete_prod_nome = QtWidgets.QLineEdit(self.groupBox_7)
        self.delete_prod_nome.setGeometry(QtCore.QRect(120, 130, 221, 20))
        self.delete_prod_nome.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_nome.setReadOnly(True)
        self.delete_prod_nome.setObjectName("delete_prod_nome")
        self.delete_prod_valor = QtWidgets.QLineEdit(self.groupBox_7)
        self.delete_prod_valor.setGeometry(QtCore.QRect(120, 250, 221, 20))
        self.delete_prod_valor.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_valor.setReadOnly(True)
        self.delete_prod_valor.setObjectName("delete_prod_valor")
        self.delete_prod_nome_input = QtWidgets.QLineEdit(self.groupBox_7)
        self.delete_prod_nome_input.setGeometry(QtCore.QRect(70, 60, 221, 20))
        self.delete_prod_nome_input.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_nome_input.setInputMask("")
        self.delete_prod_nome_input.setObjectName("delete_prod_nome_input")
        self.label_80 = QtWidgets.QLabel(self.groupBox_7)
        self.label_80.setGeometry(QtCore.QRect(20, 130, 81, 21))
        self.label_80.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.groupBox_7)
        self.label_81.setGeometry(QtCore.QRect(20, 170, 81, 21))
        self.label_81.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_81.setObjectName("label_81")
        self.delete_prod_deletar = QtWidgets.QPushButton(self.groupBox_7)
        self.delete_prod_deletar.setGeometry(QtCore.QRect(10, 490, 111, 41))
        self.delete_prod_deletar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delete_prod_deletar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.delete_prod_deletar.setObjectName("delete_prod_deletar")
        self.label_82 = QtWidgets.QLabel(self.groupBox_7)
        self.label_82.setGeometry(QtCore.QRect(20, 330, 81, 21))
        self.label_82.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.groupBox_7)
        self.label_83.setGeometry(QtCore.QRect(20, 210, 91, 21))
        self.label_83.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_83.setObjectName("label_83")
        self.delete_prod_descri = QtWidgets.QTextEdit(self.groupBox_7)
        self.delete_prod_descri.setGeometry(QtCore.QRect(120, 330, 221, 151))
        self.delete_prod_descri.setStyleSheet("background:white;\n"
"color:black;\n"
"font-size:16px;\n"
"font-family: Trebuchet MS;\n"
"font-weight: bold;")
        self.delete_prod_descri.setReadOnly(True)
        self.delete_prod_descri.setObjectName("delete_prod_descri")
        self.label_84 = QtWidgets.QLabel(self.groupBox_7)
        self.label_84.setGeometry(QtCore.QRect(20, 290, 81, 21))
        self.label_84.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.groupBox_7)
        self.label_85.setGeometry(QtCore.QRect(0, 30, 351, 21))
        self.label_85.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.delete_prod_buscar = QtWidgets.QPushButton(self.groupBox_7)
        self.delete_prod_buscar.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.delete_prod_buscar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delete_prod_buscar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.delete_prod_buscar.setObjectName("delete_prod_buscar")
        self.delete_prod_marca = QtWidgets.QLineEdit(self.groupBox_7)
        self.delete_prod_marca.setGeometry(QtCore.QRect(120, 170, 221, 20))
        self.delete_prod_marca.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_marca.setReadOnly(True)
        self.delete_prod_marca.setObjectName("delete_prod_marca")
        self.label_86 = QtWidgets.QLabel(self.groupBox_7)
        self.label_86.setGeometry(QtCore.QRect(20, 250, 81, 21))
        self.label_86.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_86.setObjectName("label_86")
        self.delete_prod_qtd = QtWidgets.QLineEdit(self.groupBox_7)
        self.delete_prod_qtd.setGeometry(QtCore.QRect(120, 210, 221, 20))
        self.delete_prod_qtd.setStyleSheet("background:transparent;\n"
"font-family: Trebuchet MS;\n"
"font-size:16px;\n"
"color:white;\n"
"border:none;\n"
"border-bottom: 1px solid white;")
        self.delete_prod_qtd.setReadOnly(True)
        self.delete_prod_qtd.setObjectName("delete_prod_qtd")
        self.delete_prod_categ = QtWidgets.QComboBox(self.groupBox_7)
        self.delete_prod_categ.setGeometry(QtCore.QRect(120, 290, 221, 22))
        self.delete_prod_categ.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"font-weight:bold;")
        self.delete_prod_categ.setObjectName("delete_prod_categ")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.delete_prod_categ.addItem("")
        self.f_relatorios = QtWidgets.QFrame(self.centralwidget)
        self.f_relatorios.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_relatorios.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}")
        self.f_relatorios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_relatorios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_relatorios.setObjectName("f_relatorios")
        self.label_87 = QtWidgets.QLabel(self.f_relatorios)
        self.label_87.setGeometry(QtCore.QRect(130, 10, 171, 21))
        self.label_87.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_87.setObjectName("label_87")
        self.rel_dia_data = QtWidgets.QDateEdit(self.f_relatorios)
        self.rel_dia_data.setGeometry(QtCore.QRect(320, 10, 101, 22))
        self.rel_dia_data.setStyleSheet("background:transparent;\n"
"border:none;\n"
"font-family:Trebuchet MS;\n"
"font-size:14px;\n"
"color:white;\n"
"font-weight:bold;\n"
"text-decoration:underline;")
        self.rel_dia_data.setObjectName("rel_dia_data")
        self.rel_dia_buscar = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_dia_buscar.setGeometry(QtCore.QRect(200, 50, 101, 31))
        self.rel_dia_buscar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_dia_buscar.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_dia_buscar.setObjectName("rel_dia_buscar")
        self.rel_buscar_mes = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_buscar_mes.setGeometry(QtCore.QRect(490, 70, 101, 20))
        self.rel_buscar_mes.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_buscar_mes.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_buscar_mes.setObjectName("rel_buscar_mes")

        self.rel_busca_aberto = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_busca_aberto.setGeometry(QtCore.QRect(620, 70, 101, 20))
        self.rel_busca_aberto.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_busca_aberto.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_busca_aberto.setObjectName("rel_busca_aberto")
        self.rel_busca_aberto.setText("EM ABERTO")

        self.rel_buscar_fechados = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_buscar_fechados.setGeometry(QtCore.QRect(750, 70, 101, 20))
        self.rel_buscar_fechados.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_buscar_fechados.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_buscar_fechados.setObjectName("rel_buscar_fechados")
        self.rel_buscar_fechados.setText("FECHADOS")

        self.rel_buscar_balcao = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_buscar_balcao.setGeometry(QtCore.QRect(880, 70, 101, 20))
        self.rel_buscar_balcao.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_buscar_balcao.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_buscar_balcao.setObjectName("rel_buscar_balcao")
        self.rel_buscar_balcao.setText("BALCÃO")

        self.rel_buscar_entregas = QtWidgets.QPushButton(self.f_relatorios)
        self.rel_buscar_entregas.setGeometry(QtCore.QRect(1010, 70, 101, 20))
        self.rel_buscar_entregas.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rel_buscar_entregas.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.rel_buscar_entregas.setObjectName("rel_buscar_entregas")
        self.rel_buscar_entregas.setText("ENTREGAS")

        self.rel_total_filtrado = QtWidgets.QLabel(self.f_relatorios)
        self.rel_total_filtrado.setGeometry(520,10,581,41)
        self.rel_total_filtrado.setStyleSheet("background:transparent;" "font-family:Trebuchet MS;" "font-size:18px;" "color:white;")
        self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO:")

        self.groupBox_8 = QtWidgets.QGroupBox(self.f_relatorios)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 90, 1171, 501))
        self.groupBox_8.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.groupBox_8.setObjectName("groupBox_8")
        self.rel_busca_resultado = QtWidgets.QTableWidget(self.groupBox_8)
        self.rel_busca_resultado.setGeometry(QtCore.QRect(10, 30, 1151, 461))
        self.rel_busca_resultado.setStyleSheet("background:#1C86EE;\n"
"color:black;\n"
"font-family: Trebuchet MS;\n"
"font-size: 12px;\n"
"font-weight:bold;")
        self.rel_busca_resultado.setObjectName("rel_busca_resultado")
        self.rel_busca_resultado.setColumnCount(11)
        self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])
        self.f_estoque = QtWidgets.QFrame(self.centralwidget)
        self.f_estoque.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_estoque.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.5);\n"
"border-radius:10px;\n"
"}")
        self.f_estoque.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_estoque.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_estoque.setObjectName("f_estoque")
        self.label_90 = QtWidgets.QLabel(self.f_estoque)
        self.label_90.setGeometry(QtCore.QRect(100, 20, 221, 21))
        self.label_90.setStyleSheet("font-family:Trebuchet MS;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"color:white;\n"
"background:transparent;\n"
"border:none;")
        self.label_90.setObjectName("label_90")
        self.estoque_nome_produto = QtWidgets.QLineEdit(self.f_estoque)
        self.estoque_nome_produto.setGeometry(QtCore.QRect(330, 20, 221, 20))
        self.estoque_nome_produto.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;")
        self.estoque_nome_produto.setObjectName("estoque_nome_produto")


        self.estoque_buscar_produto = QtWidgets.QPushButton(self.f_estoque)
        self.estoque_buscar_produto.setGeometry(QtCore.QRect(270, 60, 101, 31))
        self.estoque_buscar_produto.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.estoque_buscar_produto.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"background:#1C86EE;\n"
"font-family:Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:16px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;\n"
"}\n"
"")
        self.estoque_buscar_produto.setObjectName("estoque_buscar_produto")

        self.groupBox_9 = QtWidgets.QGroupBox(self.f_estoque)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 100, 1171, 491))
        self.groupBox_9.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font-size:18px;\n"
"font-family: Trebuchet MS;\n"
"")
        self.groupBox_9.setObjectName("groupBox_9")
        self.estoque_produtos = QtWidgets.QTableWidget(self.groupBox_9)
        self.estoque_produtos.setGeometry(QtCore.QRect(10, 20, 1151, 461))
        self.estoque_produtos.setStyleSheet("background:#1C86EE;\n"
"color:black;\n"
"font-family: Trebuchet MS;\n"
"font-size: 12px;\n"
"font-weight:bold;")
        self.estoque_produtos.setObjectName("estoque_produtos")
        self.f_developer = QtWidgets.QFrame(self.centralwidget)
        self.f_developer.setGeometry(QtCore.QRect(5, 90, 1190, 600))
        self.f_developer.setStyleSheet("background:rgba(0,0,0,0.5);\n"
"border-radius:10px;")
        self.f_developer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_developer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_developer.setObjectName("f_developer")
        self.toolButton = QtWidgets.QToolButton(self.f_developer)
        self.toolButton.setGeometry(QtCore.QRect(10, 20, 321, 171))
        self.toolButton.setStyleSheet("background:transparent;\n"
"")
        self.toolButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/menu/developer2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon13)
        self.toolButton.setIconSize(QtCore.QSize(256, 256))
        self.toolButton.setObjectName("toolButton")
        self.label_92 = QtWidgets.QLabel(self.f_developer)
        self.label_92.setGeometry(QtCore.QRect(240, 90, 681, 91))
        self.label_92.setStyleSheet("color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_92.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_92.setObjectName("label_92")
        self.label_93 = QtWidgets.QLabel(self.f_developer)
        self.label_93.setGeometry(QtCore.QRect(100, 210, 301, 41))
        self.label_93.setStyleSheet("color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_93.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.f_developer)
        self.label_94.setGeometry(QtCore.QRect(100, 260, 391, 41))
        self.label_94.setStyleSheet("color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_94.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.f_developer)
        self.label_95.setGeometry(QtCore.QRect(100, 320, 691, 41))
        self.label_95.setStyleSheet("color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_95.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_95.setObjectName("label_95")
        self.label_96 = QtWidgets.QLabel(self.f_developer)
        self.label_96.setGeometry(QtCore.QRect(100, 370, 931, 41))
        self.label_96.setStyleSheet("color:white;\n"
"font-family:Trebuchet MS;\n"
"font-size:30px;\n"
"font-weight:bold;\n"
"background:transparent;")
        self.label_96.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_96.setObjectName("label_96")
        self.groupBox_10 = QtWidgets.QGroupBox(self.f_developer)
        self.groupBox_10.setGeometry(QtCore.QRect(100, 419, 1041, 181))
        self.groupBox_10.setStyleSheet("color:white;\n"
"font-size:18px;\n"
"")
        self.groupBox_10.setObjectName("groupBox_10")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_10)
        self.toolButton_2.setGeometry(QtCore.QRect(280, 10, 51, 51))
        self.toolButton_2.setStyleSheet("background:transparent;")
        self.toolButton_2.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/menu/facebook_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon14)
        self.toolButton_2.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_97 = QtWidgets.QLabel(self.groupBox_10)
        self.label_97.setGeometry(QtCore.QRect(370, 40, 421, 16))
        self.label_97.setStyleSheet("background:transparent;")
        self.label_97.setObjectName("label_97")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_10)
        self.toolButton_3.setGeometry(QtCore.QRect(280, 70, 51, 41))
        self.toolButton_3.setStyleSheet("background:white;")
        self.toolButton_3.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/menu/github_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon15)
        self.toolButton_3.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_98 = QtWidgets.QLabel(self.groupBox_10)
        self.label_98.setGeometry(QtCore.QRect(370, 90, 421, 21))
        self.label_98.setStyleSheet("background:transparent;")
        self.label_98.setObjectName("label_98")
        self.toolButton_54 = QtWidgets.QToolButton(self.groupBox_10)
        self.toolButton_54.setGeometry(QtCore.QRect(280, 120, 51, 51))
        self.toolButton_54.setStyleSheet("background:transparent;")
        self.toolButton_54.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/menu/youtube_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_54.setIcon(icon16)
        self.toolButton_54.setIconSize(QtCore.QSize(64, 64))
        self.toolButton_54.setObjectName("toolButton_54")
        self.label_99 = QtWidgets.QLabel(self.groupBox_10)
        self.label_99.setGeometry(QtCore.QRect(370, 140, 531, 21))
        self.label_99.setStyleSheet("background:transparent;")
        self.label_99.setObjectName("label_99")
        self.f_pedidos.raise_()

        self.adicionar_frame.hide()
        self.f_pedidos.hide()
        self.frame_bar.raise_()
        self.f_caixa.raise_()
        self.f_caixa.hide()
        self.f_mesas.raise_()
        self.f_mesas.hide()
        self.f_produtos.raise_()
        self.f_produtos.hide()
        self.f_relatorios.raise_()
        self.f_relatorios.hide()
        self.f_estoque.raise_()
        self.f_estoque.hide()
        self.f_developer.raise_()
        self.f_developer.hide()
        self.f_inicio.show()
        self.f_inicio.activateWindow()
        self.f_inicio.raise_()
        menu_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

#================================= BOTOES CHAMANDO FUNCOES ========================================#

        self.button_pedido.clicked.connect(self.open_pedidos)
        self.button_caixa.clicked.connect(self.open_caixa)
        self.button_mesas.clicked.connect(self.open_mesas)
        self.button_produtos.clicked.connect(self.open_produtos)
        self.button_relatorio.clicked.connect(self.open_relatorios)
        self.button_usuario.clicked.connect(self.open_developer)
        self.novo_prod_cadastrar.clicked.connect(self.register_product)
        self.delete_button.clicked.connect(self.delete_item)
        self.troco_calcular.clicked.connect(self.troco)
        self.produto_confirmar.clicked.connect(self.save_products)
        self.produto_limpar.clicked.connect(self.clear_new_sale)
        self.table_button.clicked.connect(self.select_table)
        self.button_table_confirm.clicked.connect(self.select_table_confirm)
        self.produto_buscar.clicked.connect(self.address_verification)
        self.table_button_2.clicked.connect(self.insert_address)
        self.confirmar_abertura.clicked.connect(self.open_cashier)
        self.calendarWidget.clicked.connect(self.get_calendar)
        self.fecha_buscar.clicked.connect(self.search_cashier)
        self.fecha_confirmar.clicked.connect(self.confirm_cashier)
        self.close_table.clicked.connect(self.table_close)
        self.edit_prod_buscar.clicked.connect(self.edit_product_search)
        self.edit_prod_salvar.clicked.connect(self.save_edit_product)
        self.delete_prod_buscar.clicked.connect(self.select_delete_product)
        self.delete_prod_deletar.clicked.connect(self.delete_confirm)
        self.rel_dia_buscar.clicked.connect(self.select_day_rel)
        self.rel_buscar_mes.clicked.connect(self.update_info)
        self.rel_busca_aberto.clicked.connect(self.select_open_rel)
        self.rel_buscar_fechados.clicked.connect(self.select_close_rel)
        self.rel_buscar_balcao.clicked.connect(self.select_balcao_rel)
        self.rel_buscar_entregas.clicked.connect(self.select_entrega_rel)
        self.button_cliente.clicked.connect(self.open_estoque)
        self.estoque_buscar_produto.clicked.connect(self.get_product_name)


#====================== PEDIDOS =================================
    def open_pedidos(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_mesas.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.produto_buscar.hide()
        self.input_cep.hide()
        self.f_pedidos.show()
        self.f_pedidos.activateWindow()
        self.f_pedidos.raise_()
        self.produto_confirmar.show()
        self.produto_limpar.show()
        self.close_table.hide()
        self.table_label2.setText("")
        self.total_frame.show()
        self.clear_new_sale()
        self.update_info()
    def add_sales(self):
        self.adicionar_frame.show()
        self.adicionar_frame.activateWindow()
        self.adicionar_frame.raise_()
    def insert_sale(self):
        try:
            self.tableView.insertItem(0,self.adicionar_box.currentText())
            self.database = Aplication_database()
            self.valor_product = self.database.select_product_valor(self.adicionar_box.currentText())
            self.get_valor = str(self.valor_product[0]).replace(",", ".")
            self.valor_atual = float(self.get_valor) + float(self.label2_total.text().replace(",", "."))
            self.label2_total.setText(str(self.valor_atual).replace(".",","))
        except Exception as error:
            print(error)

    def hidden_sale(self):
        self.adicionar_frame.hide()

    def delete_item(self):
        self.tableView.takeItem(self.tableView.currentRow())
        self.database = Aplication_database()
        try:
            self.valor_product = self.database.select_product_valor(self.tableView.currentItem().text())
            self.get_valor = str(self.valor_product[0]).replace(",", ".")
            self.valor_atual = float(self.label2_total.text().replace(",", ".")) - float(self.get_valor)
            self.label2_total.setText(str(self.valor_atual).replace(".",","))
        except Exception as error:
            self.label2_total.setText("0,00")
            print(error)

    def troco(self):
        try:
            self.recebido = self.input_recebido.text().replace(",",".")
            self.total_gasto = self.label2_total.text().replace(",",".")
            self.get_troco = float(self.recebido) - float(self.total_gasto)
            self.label2_troco.setText(str(self.get_troco).replace(".",","))
        except Exception as error:
            print(error)

    def save_products(self):
        try:
            self.data_atual = date.today()
            if self.data_atual.day <=9 and self.data_atual.month <=9 :
                self.full_date = "{}-{}{}-{}{}".format(  self.data_atual.year,"0",self.data_atual.month,"0",self.data_atual.day)

            if self.data_atual.day <=9  and self.data_atual.month>=10:
                self.full_date = "{}-{}-{}{}".format(  self.data_atual.year,self.data_atual.month,"0",self.data_atual.day)

            if self.data_atual.day >=10  and self.data_atual.month<=9:
                self.full_date = "{}-{}{}-{}".format(  self.data_atual.year,"0",self.data_atual.month,self.data_atual.day)

            if self.data_atual.day >=10 and self.data_atual.month>=10:
                self.full_date = "{}-{}-{}".format(  self.data_atual.year,self.data_atual.month,self.data_atual.day)

            self.get_table = self.box_mesas.currentText()
            self.get_products = [str(self.tableView.item(i).text()) for i in range(self.tableView.count())]
            for product in self.get_products:
                self.prod_qtd = self.database.product_used(product)

            self.get_obs = self.textEdit.toPlainText()
            self.get_adress = self.label_8.text()
            self.get_number = self.label_9.text()
            self.get_village = self.label_10.text()
            self.get_complement = self.label_11.text()

            self.total = self.label2_total.text()
            if self.get_table != "Balcão" and self.get_table != "Entrega":
                self.get_condition = "ABERTO"
            if self.get_table == "Balcão" or self.get_table == "Entrega":
                self.get_condition = "FECHADO"
            self.database  = Aplication_database()
            self.register_sales = self.database.sales_register(self.full_date, self.get_table, self.get_products, self.get_obs,self.get_adress,\
                                                               self.get_number, self.get_village, self.get_complement, str(self.total).replace(",","."), self.get_condition)
            self.clear_new_sale()
            self.produto_buscar.hide()
            self.input_cep.hide()
        except Exception as error:
            print(error)

    def clear_new_sale(self):
        self.tableView.clear()
        self.textEdit.clear()
        self.input_recebido.setText("")
        self.label2_total.setText("0,00")
        self.label2_troco.setText('0,00')
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.produto_buscar.hide()
        self.input_cep.hide()

    def select_table(self):
        self.frame_table.raise_()
        self.frame_table.show()


    def select_table_confirm(self):
        try:
            self.produto_confirmar.hide()
            self.produto_limpar.hide()
            self.close_table.show()
            self.search_table = self.database.search_table_products(self.table_entry.text())

            for i in self.search_table[0]:
                self.tableView.addItems(i)
            self.textEdit.append(str(self.search_table[1][0]))
            self.total_valor = 0
            for valor in self.search_table[2]:
                self.total_valor += float(".".join(map(str,valor)))

            self.label2_total.setText(str(self.total_valor))
            self.frame_table.hide()
            self.total_frame.hide()
        except Exception as error:
            print(error)
            self.frame_table.hide()
            self.close_table.hide()

    def table_close(self):
        try:
            self.table = self.database.close_table("ABERTO",self.table_entry.text())
            self.table_label2.setText(self.table)
        except Exception as error:
            print(error)
            self.table_label2.setText("Erro ao fechar!")

    def address_verification(self):
        self.my_cep = self.input_cep.text()
        self.api_cep = cep_select(self.my_cep)
        self.label_8.setText(self.api_cep['logradouro'])
        self.label_10.setText(self.api_cep['bairro'])
        self.label_11.setText(self.api_cep['localidade'])

    def insert_address(self):
        self.produto_buscar.show()
        self.input_cep.show()
        self.input_cep.clear()
        self.label_8.clear()
        self.label_9.clear()
        self.label_10.clear()
        self.label_11.clear()



#=================== CAIXA =======================================

    def open_caixa(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_mesas.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_caixa.show()
        self.f_caixa.activateWindow()
        self.f_caixa.raise_()
        self.fechamento_label.clear()
        self.update_info()

    def open_cashier(self):
        try:
            self.db_cash = self.database.open_cash_box("ABERTO", self.abertura_data.date().toPyDate(), self.abertura_valor.text().replace(",","."))
            self.abertura_label.setText("Abertura realizada!")
            self.clear_cashier()
        except Exception as error:
            print(error)


    def clear_cashier(self):
        self.abertura_valor.setText("")


    def get_calendar(self):
        self.abertura_data.setDate(self.calendarWidget.selectedDate())

    def search_cashier(self):
        try:
            self.total_day = self.database.profit(self.fecha_data.date().toPyDate())
            self.add_total = 0
            for valor in self.total_day:
                self.add_total += float(".".join(map(str,valor)))# converte tupla em string
            self.search = self.database.search_cashier_open(self.fecha_data.date().toPyDate())
            self.actual_valor = self.add_total + self.search[0][1]
            self.fecha_valor.setText(str(self.actual_valor))
            self.fecha_status.setText(self.search[0][0])
        except Exception as error:
            print(error)

    def confirm_cashier(self):
        try:
            self.search2 = self.database.search_cashier_open(self.fecha_data.date().toPyDate())
            self.get_close = self.database.close_cashier("FECHADO", self.actual_valor, self.fecha_data.date().toPyDate())
            self.result =  self.actual_valor - self.search2[0][1]
            self.fechamento_label.setText("Seu ganho foi de: {}".format(str(self.result)))
            self.fecha_status.setText(self.get_close)
            self.clear_close()
        except Exception as error:
            print(error)

    def clear_close(self):
        self.fecha_valor.clear()
        self.fecha_status.clear()



#====================== MESAS ==================================

    def open_mesas(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_mesas.show()
        self.f_mesas.activateWindow()
        self.f_mesas.raise_()
        self.update_info()


#================ PRODUTOS ===========================


    def open_produtos(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_mesas.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_produtos.show()
        self.f_produtos.activateWindow()
        self.f_produtos.raise_()
        self.edit_prod_salvar.hide()
        self.delete_prod_deletar.hide()
        self.update_info()

    def register_product(self):
        self.prod_1 = self.novo_prod_nome.text()
        self.prod_2 = self.novo_prod_marca.text()
        self.prod_3 = self.novo_prod_qtd.text()
        self.prod_4 = self.novo_prod_valor.text()
        self.prod_5 = self.novo_prod_categ.currentText()
        self.prod_6 = self.novo_prod_descri.toPlainText()
        self.database = self.database.register_new_product(self.prod_1, self.prod_2, self.prod_3, self.prod_4, self.prod_5, self.prod_6)
        self.label_register_ok = QtWidgets.QLabel(self.groupBox_5)
        self.label_register_ok.setGeometry(140,500,191,21)
        self.label_register_ok.setText(str(self.database))
        self.label_register_ok.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")
        self.label_register_ok.show()
        self.clear_all_products_register()
        self.update_info()

    def clear_all_products_register(self):
        self.novo_prod_nome.setText("")
        self.novo_prod_marca.setText("")
        self.novo_prod_qtd.setText("")
        self.novo_prod_valor.setText("")
        self.novo_prod_descri.clear()
        self.label_register_ok.setText("")


    def edit_product_search(self):
        try:
            self.edit_prod_search_var = self.database.select_product_edit(self.edit_prod_nome_input.text())
            self.edit_prod_nome.setText(self.edit_prod_search_var[0][1])
            self.edit_prod_marca.setText(self.edit_prod_search_var[0][2])
            self.edit_prod_qtd.setText(str(self.edit_prod_search_var[0][3]))
            self.edit_prod_valor.setText(self.edit_prod_search_var[0][4])
            self.edit_prod_categ.setCurrentText(self.edit_prod_search_var[0][5])
            self.edit_prod_descri.setPlainText(self.edit_prod_search_var[0][6])
            self.label_search_ok = QtWidgets.QLabel(self.groupBox_6)
            self.label_search_ok.setGeometry(140,500,191,21)
            self.label_search_ok.setText("")
            self.label_search_ok.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")
            self.label_search_ok.show()
            self.edit_prod_salvar.show()

        except Exception as error:
            print(error)
            self.label_search_ok = QtWidgets.QLabel(self.groupBox_6)
            self.label_search_ok.setGeometry(140,500,191,21)
            self.label_search_ok.setText("Produto NÃO localizado!!")
            self.label_search_ok.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")
            self.label_search_ok.show()


    def save_edit_product(self):
        try:
            self.get_edit_name = self.edit_prod_nome.text()
            self.get_edit_marca = self.edit_prod_marca.text()
            self.get_edit_qtd = self.edit_prod_qtd.text()
            self.get_edit_valor = self.edit_prod_valor.text()
            self.get_edit_categ = self.edit_prod_categ.currentText()
            self.get_edit_description = self.edit_prod_descri.toPlainText()
            self.edit_saved = self.database.edit_product_base(self.get_edit_name, self.get_edit_marca, self.get_edit_qtd, self.get_edit_valor, self.get_edit_categ, self.get_edit_description,\
                                                                                self.edit_prod_nome_input.text())
            self.label_search_ok.setText("Produto editado com sucesso!")
            self.clear_product_edit()
        except Exception as error:
            print(error)
            self.label_search_ok.setText("Erro ao editar o produto!")
            self.clear_product_edit()

    def clear_product_edit(self):
        self.edit_prod_nome.clear()
        self.edit_prod_marca.clear()
        self.edit_prod_qtd.clear()
        self.edit_prod_valor.clear()
        self.edit_prod_descri.clear()
        self.edit_prod_nome_input.clear()

    def select_delete_product(self):
        try:
            self.delete_select = self.database.select_product_edit(self.delete_prod_nome_input.text())
            self.delete_prod_nome.setText(self.delete_select[0][1])
            self.delete_prod_marca.setText(self.delete_select[0][2])
            self.delete_prod_qtd.setText(str(self.delete_select[0][3]))
            self.delete_prod_valor.setText(self.delete_select[0][4])
            self.delete_prod_categ.setCurrentText(self.delete_select[0][5])
            self.delete_prod_descri.setPlainText(self.delete_select[0][6])
            self.label_delete_ok = QtWidgets.QLabel(self.groupBox_7)
            self.label_delete_ok.setGeometry(140,500,191,21)
            self.label_delete_ok.setText("")
            self.label_delete_ok.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")
            self.label_delete_ok.show()
            self.delete_prod_deletar.show()
        except Exception as error:
            print(error)
            self.label_delete_ok = QtWidgets.QLabel(self.groupBox_7)
            self.label_delete_ok.setGeometry(140,500,191,21)
            self.label_delete_ok.setText("Produto NÃO localizado!")
            self.label_delete_ok.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;")
            self.label_delete_ok.show()

    def delete_confirm(self):
        try:
            self.delete_product_get = self.delete_prod_nome.text()
            self.delete_init = self.database.delete_product_base(self.delete_product_get)
            self.label_delete_ok.setText(self.delete_init)
            self.clear_product_delete()
        except Exception as error:
            print(error)
            self.label_delete_ok.setText("Erro ao deletar o produto!")

    def clear_product_delete(self):
        self.delete_prod_nome.clear()
        self.delete_prod_marca.clear()
        self.delete_prod_qtd.clear()
        self.delete_prod_valor.clear()
        self.delete_prod_descri.clear()
        self.delete_prod_nome_input.clear()


#================== RELATÓRIOS ==========================

    def open_relatorios(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_mesas.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_relatorios.show()
        self.f_relatorios.activateWindow()
        self.f_relatorios.raise_()
        self.update_info()

    def select_day_rel(self):
        try:
            self.get_sales_day = self.database.select_sales_all_day(self.rel_dia_data.date().toPyDate())
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            for row_number , row_data in enumerate(self.get_sales_day):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])
            self.get_valor_for_sales_day = self.database.select_valor_day_sales(self.rel_dia_data.date().toPyDate())
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales_day:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))
        except Exception as error:
            print(error)

    def select_open_rel(self):
        try:
            self.get_sales_open = self.database.select_open_sales("ABERTO")
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            for row_number , row_data in enumerate(self.get_sales_open):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])

            self.get_valor_for_sales_condition = self.database.select_valor_condition_sales("ABERTO")
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales_condition:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))
        except Exception as error:
            print(error)

    def select_close_rel(self):
        try:
            self.get_sales_close = self.database.select_open_sales("FECHADO")
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            for row_number , row_data in enumerate(self.get_sales_close):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])

            self.get_valor_for_sales_condition = self.database.select_valor_condition_sales("FECHADO")
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales_condition:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))
        except Exception as error:
            print(error)

    def select_balcao_rel(self):
        try:
            self.get_sales_balcao = self.database.select_table_sales("Balcão")
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            for row_number , row_data in enumerate(self.get_sales_balcao):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])

            self.get_valor_for_sales_condition = self.database.select_valor_table_sales("Balcão")
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales_condition:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))
        except Exception as error:
            print(error)

    def select_entrega_rel(self):
        try:
            self.get_sales_entrega = self.database.select_table_sales("Entrega")
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            for row_number , row_data in enumerate(self.get_sales_entrega):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])

            self.get_valor_for_sales_condition = self.database.select_valor_table_sales("Entrega")
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales_condition:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))
        except Exception as error:
            print(error)








#FAZER FILTRO POR APENAS EM ABERTO , FECHADOS, BALCÃO, ENTREGAS, TODOS EXIBINDO SEUS TOTAIS



#================ ESTOQUE ==============================

    def open_estoque(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_mesas.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_estoque.show()
        self.f_estoque.activateWindow()
        self.f_estoque.raise_()
        self.update_info()

    def get_product_name(self):
        self.estoque_produtos.clear()
        self.estoque_produtos.setRowCount(0)
        self.estoque_produtos.setColumnCount(7)
        self.get_name_products = self.database.select_product_edit(self.estoque_nome_produto.text())
        for row_number , row_data in enumerate(self.get_name_products):
            self.estoque_produtos.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.estoque_produtos. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
        self.estoque_produtos.setHorizontalHeaderLabels(["ID","Nome","Marca", "Quantidade","Valor", "Categoria", "Descrição"])


#================ DEVELOPER =============================

    def open_developer(self):
        self.f_pedidos.hide()
        self.f_inicio.hide()
        self.f_caixa.hide()
        self.f_mesas.hide()
        self.f_produtos.hide()
        self.f_relatorios.hide()
        self.f_estoque.hide()
        self.f_developer.hide()
        self.f_developer.show()
        self.f_developer.activateWindow()
        self.f_developer.raise_()
        self.update_info()

#=================== ATUALIZAR ITENS DO SISTEMA =========================
    def update_info(self):
        try:
            # insere os produtos cadastrados , no box do pedido
            self.adicionar_box.clear()
            self.database = Aplication_database()
            self.read_products = self.database.select_all_products_name()
            for i in self.read_products:
                self.adicionar_box.insertItems(0,i)

            # verifica as mesas em aberto
            self.tables_open = self.database.tables_opened()

            x = 10
            y = 100
            tables = []
            if len(self.tables_open) != 0:
                for i in self.tables_open:
                    for mesa in i:
                        if mesa not in tables:
                            tables.append(mesa)
                            self.label_mesa = QtWidgets.QLabel(self.f_mesas)
                            self.label_mesa.setGeometry(480,1,500,100)
                            self.label_mesa.setText("MESAS EM ABERTO:")
                            self.label_mesa.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;" "text-decoration:underline;" "font-size:28px;")
                            self.label_mesa.show()

                            self.table_img = QtWidgets.QToolButton(self.f_mesas)
                            self.table_img.setGeometry(QtCore.QRect(x, y, 150, 150))
                            self.table_img.setStyleSheet("QToolButton{\n"
                    "background:green;\n"
                    "color:white;\n"
                    "border-radius:10px;" "}")
                            self.table_img.setText("")
                            icon12 = QtGui.QIcon()
                            icon12.addPixmap(QtGui.QPixmap(":/menu/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                            self.table_img.setIcon(icon12)
                            self.table_img.setIconSize(QtCore.QSize(130, 130))
                            self.table_img.setObjectName("table_img")
                            self.table_label = QtWidgets.QLabel(self.table_img)
                            self.table_label.setText("Mesa: " + str(mesa))
                            self.table_label.setStyleSheet("background:transparent;" "font-family:Trebuchet MS;" "color:white;" "font-size:18px;" "font-weight:bold;")
                            self.table_label.setGeometry(10,100,100,50)
                            self.table_img.show()
                            x +=200
            else:
                for i in range(len(self.f_mesas.children())):
                    self.f_mesas.children()[i].deleteLater()
                self.label_mesa = QtWidgets.QLabel(self.f_mesas)
                self.label_mesa.setGeometry(480,1,500,100)
                self.label_mesa.setText("MESAS EM ABERTO:")
                self.label_mesa.setStyleSheet("background:transparent;" "color:white;" "font-family:Trebuchet MS;" "text-decoration:underline;" "font-size:28px;")
                self.label_mesa.show()

            # pega todas as vendas do db e joga no Relatórios
            self.rel_busca_resultado.clear()
            self.rel_busca_resultado.setRowCount(0)
            self.get_total_sales = self.database.total_sales()
            self.get_all_sales = self.database.select_all_sales()
            for row_number , row_data in enumerate(self.get_all_sales):
                self.rel_busca_resultado.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.rel_busca_resultado. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.rel_busca_resultado.setHorizontalHeaderLabels(["ID","Data","Mesa", "Produtos","Observações", "Endereço", "Numero", "Bairro", "Complemento", "Total", "Condição"])
            self.get_valor_for_sales = self.database.select_valor_all_sales()
            self.get_sales_valor = 0
            for get_value in self.get_valor_for_sales:
                for value in get_value:
                    self.get_sales_valor += value
            self.rel_total_filtrado.setText("VALOR TOTAL FILTRADO: {}".format(str(self.get_sales_valor)))


            # pega todos os produtos do db e joga no estoque_produtos
            self.estoque_produtos.clear()
            self.estoque_produtos.setRowCount(0)
            self.estoque_produtos.setColumnCount(7)
            self.get_all_products = self.database.select_all_products()
            for row_number , row_data in enumerate(self.get_all_products):
                self.estoque_produtos.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.estoque_produtos. setItem(row_number,colum_number, QtWidgets.QTableWidgetItem(str(data)))
            self.estoque_produtos.setHorizontalHeaderLabels(["ID","Nome","Marca", "Quantidade","Valor", "Categoria", "Descrição"])









        except Exception as error:
            print(error)






    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Restaurante Requinte - MENU"))
        self.label_welcome.setText(_translate("menu_window", "Restaurante Requinte"))
        self.button_pedido.setText(_translate("menu_window", " Pedidos"))
        self.button_caixa.setText(_translate("menu_window", " Caixa"))
        self.button_mesas.setText(_translate("menu_window", " Mesas"))
        self.button_produtos.setText(_translate("menu_window", " Produtos"))
        self.button_relatorio.setText(_translate("menu_window", " Relatórios"))
        self.button_cliente.setText(_translate("menu_window", " Estoque"))
        self.button_usuario.setText(_translate("menu_window", " Developer"))
        self.label.setText(_translate("menu_window", "SELECIONE A MESA:"))
        self.box_mesas.setItemText(0, _translate("menu_window", "Balcão"))
        self.box_mesas.setItemText(1, _translate("menu_window", "Entrega"))
        self.box_mesas.setItemText(2, _translate("menu_window", "1"))
        self.box_mesas.setItemText(3, _translate("menu_window", "2"))
        self.box_mesas.setItemText(4, _translate("menu_window", "3"))
        self.box_mesas.setItemText(5, _translate("menu_window", "4"))
        self.box_mesas.setItemText(6, _translate("menu_window", "5"))
        self.box_mesas.setItemText(7, _translate("menu_window", "6"))
        self.box_mesas.setItemText(8, _translate("menu_window", "7"))
        self.box_mesas.setItemText(9, _translate("menu_window", "8"))
        self.box_mesas.setItemText(10, _translate("menu_window", "9"))
        self.box_mesas.setItemText(11, _translate("menu_window", "10"))
        self.box_mesas.setItemText(12, _translate("menu_window", "11"))
        self.box_mesas.setItemText(13, _translate("menu_window", "12"))
        self.box_mesas.setItemText(14, _translate("menu_window", "13"))
        self.box_mesas.setItemText(15, _translate("menu_window", "14"))
        self.box_mesas.setItemText(16, _translate("menu_window", "15"))
        self.box_mesas.setItemText(17, _translate("menu_window", "16"))
        self.box_mesas.setItemText(18, _translate("menu_window", "17"))
        self.box_mesas.setItemText(19, _translate("menu_window", "18"))
        self.box_mesas.setItemText(20, _translate("menu_window", "19"))
        self.box_mesas.setItemText(21, _translate("menu_window", "20"))
        self.box_mesas.setItemText(22, _translate("menu_window", "21"))
        self.box_mesas.setItemText(23, _translate("menu_window", "22"))
        self.box_mesas.setItemText(24, _translate("menu_window", "23"))
        self.box_mesas.setItemText(25, _translate("menu_window", "24"))
        self.box_mesas.setItemText(26, _translate("menu_window", "25"))
        self.box_mesas.setItemText(27, _translate("menu_window", "26"))
        self.box_mesas.setItemText(28, _translate("menu_window", "27"))
        self.box_mesas.setItemText(29, _translate("menu_window", "28"))
        self.box_mesas.setItemText(30, _translate("menu_window", "29"))
        self.box_mesas.setItemText(31, _translate("menu_window", "30"))
        self.box_mesas.setItemText(32, _translate("menu_window", "31"))
        self.box_mesas.setItemText(33, _translate("menu_window", "32"))
        self.box_mesas.setItemText(34, _translate("menu_window", "33"))
        self.box_mesas.setItemText(35, _translate("menu_window", "34"))
        self.box_mesas.setItemText(36, _translate("menu_window", "35"))
        self.box_mesas.setItemText(37, _translate("menu_window", "36"))
        self.box_mesas.setItemText(38, _translate("menu_window", "37"))
        self.box_mesas.setItemText(39, _translate("menu_window", "38"))
        self.box_mesas.setItemText(40, _translate("menu_window", "39"))
        self.box_mesas.setItemText(41, _translate("menu_window", "40"))
        self.box_mesas.setItemText(42, _translate("menu_window", "41"))
        self.box_mesas.setItemText(43, _translate("menu_window", "42"))
        self.box_mesas.setItemText(44, _translate("menu_window", "43"))
        self.box_mesas.setItemText(45, _translate("menu_window", "44"))
        self.box_mesas.setItemText(46, _translate("menu_window", "45"))
        self.box_mesas.setItemText(47, _translate("menu_window", "46"))
        self.box_mesas.setItemText(48, _translate("menu_window", "47"))
        self.box_mesas.setItemText(49, _translate("menu_window", "48"))
        self.box_mesas.setItemText(50, _translate("menu_window", "49"))
        self.box_mesas.setItemText(51, _translate("menu_window", "50"))
        self.label_2.setText(_translate("menu_window", "PRODUTOS ADQUIRIDOS:"))
        self.groupBox.setTitle(_translate("menu_window", "Observações"))
        self.produto_confirmar.setText(_translate("menu_window", "CONFIRMAR"))
        self.produto_limpar.setText(_translate("menu_window", "LIMPAR"))
        self.endereco_box.setTitle(_translate("menu_window", "Endereço para entrega"))
        self.label_3.setText(_translate("menu_window", "CEP:"))
        self.label_4.setText(_translate("menu_window", "ENDEREÇO:"))
        self.label_5.setText(_translate("menu_window", "NUMERO:"))
        self.label_6.setText(_translate("menu_window", "BAIRRO:"))
        self.label_7.setText(_translate("menu_window", "CIDADE:"))
        self.produto_buscar.setText(_translate("menu_window", "BUSCAR"))
        self.groupBox_2.setTitle(_translate("menu_window", "CADASTRO DE ABERTURA DE CAIXA"))
        self.label_12.setText(_translate("menu_window", "Valor:"))
        self.label_13.setText(_translate("menu_window", "Data:"))
        self.confirmar_abertura.setText(_translate("menu_window", "CONFIRMAR"))
        self.groupBox_3.setTitle(_translate("menu_window", "FECHAMENTO DE CAIXA"))
        self.label_14.setText(_translate("menu_window", "Selecione uma data para o fechamento:"))
        self.fecha_buscar.setText(_translate("menu_window", "BUSCAR"))
        self.label_15.setText(_translate("menu_window", "Valor do caixa:"))
        self.label_16.setText(_translate("menu_window", "Status:"))
        self.fecha_confirmar.setText(_translate("menu_window", "CONFIRMAR"))
        self.groupBox_5.setTitle(_translate("menu_window", "CADASTRAR PRODUTOS"))
        self.label_67.setText(_translate("menu_window", "Nome:"))
        self.label_68.setText(_translate("menu_window", "Marca:"))
        self.label_69.setText(_translate("menu_window", "Quantidade:"))
        self.label_70.setText(_translate("menu_window", "Valor:"))
        self.label_71.setText(_translate("menu_window", "Categoria:"))
        self.label_72.setText(_translate("menu_window", "Descrição:"))
        self.novo_prod_categ.setItemText(0, _translate("menu_window", "Bebidas"))
        self.novo_prod_categ.setItemText(1, _translate("menu_window", "Lanches"))
        self.novo_prod_categ.setItemText(2, _translate("menu_window", "Refeições"))
        self.novo_prod_categ.setItemText(3, _translate("menu_window", "Porções"))
        self.novo_prod_categ.setItemText(4, _translate("menu_window", "Diversos"))
        self.novo_prod_categ.setItemText(5, _translate("menu_window", "Sobremesas"))
        self.novo_prod_cadastrar.setText(_translate("menu_window", "CADASTRAR"))
        self.groupBox_6.setTitle(_translate("menu_window", "EDITAR PRODUTOS"))
        self.label_73.setText(_translate("menu_window", "Busca pelo nome do produto:"))
        self.edit_prod_nome_input.setPlaceholderText(_translate("menu_window", "Digite o nome do produto"))
        self.edit_prod_buscar.setText(_translate("menu_window", "BUSCAR"))
        self.label_74.setText(_translate("menu_window", "Quantidade:"))
        self.label_75.setText(_translate("menu_window", "Categoria:"))
        self.label_76.setText(_translate("menu_window", "Marca:"))
        self.edit_prod_categ.setItemText(0, _translate("menu_window", "Bebidas"))
        self.edit_prod_categ.setItemText(1, _translate("menu_window", "Lanches"))
        self.edit_prod_categ.setItemText(2, _translate("menu_window", "Refeições"))
        self.edit_prod_categ.setItemText(3, _translate("menu_window", "Porções"))
        self.edit_prod_categ.setItemText(4, _translate("menu_window", "Diversos"))
        self.edit_prod_categ.setItemText(5, _translate("menu_window", "Sobremesas"))
        self.label_77.setText(_translate("menu_window", "Nome:"))
        self.label_78.setText(_translate("menu_window", "Descrição:"))
        self.label_79.setText(_translate("menu_window", "Valor:"))
        self.edit_prod_salvar.setText(_translate("menu_window", "SALVAR"))
        self.groupBox_7.setTitle(_translate("menu_window", "DELETAR PRODUTO"))
        self.delete_prod_nome_input.setPlaceholderText(_translate("menu_window", "Digite o nome do produto"))
        self.label_80.setText(_translate("menu_window", "Nome:"))
        self.label_81.setText(_translate("menu_window", "Marca:"))
        self.delete_prod_deletar.setText(_translate("menu_window", "DELETAR"))
        self.label_82.setText(_translate("menu_window", "Descrição:"))
        self.label_83.setText(_translate("menu_window", "Quantidade:"))
        self.label_84.setText(_translate("menu_window", "Categoria:"))
        self.label_85.setText(_translate("menu_window", "Busca pelo nome do produto:"))
        self.delete_prod_buscar.setText(_translate("menu_window", "BUSCAR"))
        self.label_86.setText(_translate("menu_window", "Valor:"))
        self.delete_prod_categ.setItemText(0, _translate("menu_window", "Bebidas"))
        self.delete_prod_categ.setItemText(1, _translate("menu_window", "Lanches"))
        self.delete_prod_categ.setItemText(2, _translate("menu_window", "Refeições"))
        self.delete_prod_categ.setItemText(3, _translate("menu_window", "Porções"))
        self.delete_prod_categ.setItemText(4, _translate("menu_window", "Diversos"))
        self.delete_prod_categ.setItemText(5, _translate("menu_window", "Sobremesas"))
        self.label_87.setText(_translate("menu_window", "Buscar vendas por dia:"))
        self.rel_dia_buscar.setText(_translate("menu_window", "FILTRAR"))
        self.rel_buscar_mes.setText(_translate("menu_window", "EXIBIR TODOS"))
        self.groupBox_8.setTitle(_translate("menu_window", "Vendas"))
        self.label_90.setText(_translate("menu_window", "Buscar estoque por produto:"))
        self.estoque_buscar_produto.setText(_translate("menu_window", "BUSCAR"))
        self.groupBox_9.setTitle(_translate("menu_window", "Produtos"))
        self.label_92.setText(_translate("menu_window", "Developer: Allan Scala"))
        self.label_93.setText(_translate("menu_window", "Age: 29 years"))
        self.label_94.setText(_translate("menu_window", "Programmer: 6 Months ago."))
        self.label_95.setText(_translate("menu_window", "Skills: Python 3 , Html 5 , Css 3 and JavaScript."))
        self.label_96.setText(_translate("menu_window", "Frameworks: Tkinter, Pyqt5, Flask, Django, React and Bootstrap."))
        self.groupBox_10.setTitle(_translate("menu_window", "Social Networks"))
        self.label_97.setText(_translate("menu_window", "facebook.com/allan.christianscala"))
        self.label_98.setText(_translate("menu_window", "github.com/AllanScala1991"))
        self.label_99.setText(_translate("menu_window", "https://www.youtube.com/channel/ASDeveloper"))
import menu_img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec_())
