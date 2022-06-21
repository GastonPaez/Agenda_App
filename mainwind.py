# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entregapyqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#######################################
##############   VISTA   ##############
#######################################
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 565)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                 "color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-family:robot;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 20, 711, 501))
        self.tableWidget.setStyleSheet("background-color:rgb(170, 170, 170);\n"
                                       "color: black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(4, 140)
        self.tableWidget.setColumnWidth(5, 180)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 181, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layout_form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout_form.setContentsMargins(0, 0, 0, 0)
        self.layout_form.setObjectName("layout_form")
        self.lb_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_name.setObjectName("lb_name")
        self.layout_form.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.lb_name)
        self.le_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_name.setStyleSheet("background-color: black;\n"
                                   "border-radius: 5px;\n"
                                   "color: white;\n"
                                   "padding: 2px;")
        self.le_name.setObjectName("le_name")
        self.layout_form.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.le_lastname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_lastname.setStyleSheet("background-color: black;\n"
                                       "border-radius: 5px;\n"
                                       "color: white;\n"
                                       "padding: 2px;")
        self.le_lastname.setObjectName("le_lastname")
        self.layout_form.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.le_lastname)
        self.lb_number = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_number.setObjectName("lb_number")
        self.layout_form.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.lb_number)
        self.le_number = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_number.setStyleSheet("background-color: black;\n"
                                     "border-radius: 5px;\n"
                                     "color: white;\n"
                                     "padding: 2px;\n"
                                     "")
        self.le_number.setObjectName("le_number")
        self.layout_form.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.le_number)
        self.le_adress = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_adress.setStyleSheet("background-color: black;\n"
                                     "border-radius: 5px;\n"
                                     "color: white;\n"
                                     "padding: 2px;")
        self.le_adress.setObjectName("le_adress")
        self.layout_form.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.le_adress)
        self.le_mail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_mail.setStyleSheet("background-color: black;\n"
                                   "border-radius: 5px;\n"
                                   "color: white;\n"
                                   "padding: 2px;")
        self.le_mail.setObjectName("le_mail")
        self.layout_form.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.le_mail)
        self.lb_lastname = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_lastname.setObjectName("lb_lastname")
        self.layout_form.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lb_lastname)
        self.lb_adress = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_adress.setObjectName("lb_adress")
        self.layout_form.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.lb_adress)
        self.lb_mail = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_mail.setObjectName("lb_mail")
        self.layout_form.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.lb_mail)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 180, 21, 20))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.layout_id = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.layout_id.setContentsMargins(0, 0, 0, 0)
        self.layout_id.setObjectName("layout_id")
        self.lb_id = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lb_id.setObjectName("lb_id")
        self.layout_id.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.lb_id)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_title = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_title.setContentsMargins(0, 0, 0, 0)
        self.layout_title.setObjectName("layout_title")
        self.lb_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_title.setObjectName("lb_title")
        self.layout_title.addWidget(self.lb_title)
        self.bt_s_start = QtWidgets.QPushButton(self.centralwidget)
        self.bt_s_start.setGeometry(QtCore.QRect(20, 460, 81, 41))
        self.bt_s_start.setStyleSheet("background-color: grey;\n"
                                      "\n"
                                      "color: white;")
        self.bt_s_start.setObjectName("bt_s_start")
        self.bt_s_stop = QtWidgets.QPushButton(self.centralwidget)
        self.bt_s_stop.setGeometry(QtCore.QRect(110, 460, 81, 41))
        self.bt_s_stop.setStyleSheet("background-color: grey;\n"
                                     "\n"
                                     "color: white;")
        self.bt_s_stop.setObjectName("bt_s_stop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 430, 51, 16))
        self.label.setObjectName("label")
        self.bt_save = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save.setGeometry(QtCore.QRect(20, 210, 92, 31))
        self.bt_save.setStyleSheet("background-color: grey;\n"
                                   "\n"
                                   "color: white;")
        self.bt_save.setObjectName("bt_save")
        self.bt_delete = QtWidgets.QPushButton(self.centralwidget)
        self.bt_delete.setGeometry(QtCore.QRect(20, 250, 92, 31))
        self.bt_delete.setStyleSheet("background-color: grey;\n"
                                     "\n"
                                     "color: white;")
        self.bt_delete.setObjectName("bt_delete")
        self.bt_update = QtWidgets.QPushButton(self.centralwidget)
        self.bt_update.setGeometry(QtCore.QRect(120, 210, 92, 31))
        self.bt_update.setStyleSheet("background-color: grey;\n"
                                     "\n"
                                     "color: white;")
        self.bt_update.setObjectName("bt_update")
        self.bt_clean = QtWidgets.QPushButton(self.centralwidget)
        self.bt_clean.setGeometry(QtCore.QRect(120, 250, 92, 31))
        self.bt_clean.setStyleSheet("background-color: grey;\n"
                                    "\n"
                                    "color: white;")
        self.bt_clean.setObjectName("bt_clean")
        self.le_id = QtWidgets.QLineEdit(self.centralwidget)
        self.le_id.setGeometry(QtCore.QRect(70, 180, 54, 20))
        self.le_id.setText("")
        self.le_id.setObjectName("le_id")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 182, 96))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_mail_log = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lb_mail_log.setStyleSheet("text-align: center;")
        self.lb_mail_log.setObjectName("lb_mail_log")
        self.verticalLayout.addWidget(self.lb_mail_log)
        self.lb_mail_log_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lb_mail_log_2.setStyleSheet("font-weight: normal;")
        self.lb_mail_log_2.setObjectName("lb_mail_log_2")
        self.verticalLayout.addWidget(self.lb_mail_log_2)
        self.le_mail_log = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.le_mail_log.setStyleSheet("background-color: black;\n"
                                       "border-radius: 5px;\n"
                                       "color: white;\n"
                                       "padding: 2px;")
        self.le_mail_log.setText("")
        self.le_mail_log.setObjectName("le_mail_log")
        self.verticalLayout.addWidget(self.le_mail_log)
        self.bt_send_log = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bt_send_log.setStyleSheet("background-color: grey;\n"
                                       "\n"
                                       "color: white;")
        self.bt_send_log.setObjectName("bt_send_log")
        self.verticalLayout.addWidget(self.bt_send_log)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Numero"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dirección"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "E-mail"))
        self.lb_name.setText(_translate("MainWindow", "Nombre"))
        self.lb_number.setText(_translate("MainWindow", "Numero"))
        self.lb_lastname.setText(_translate("MainWindow", "Apellido"))
        self.lb_adress.setText(_translate("MainWindow", "Direccion"))
        self.lb_mail.setText(_translate("MainWindow", "E-mail"))
        self.lb_id.setText(_translate("MainWindow", "ID"))
        self.lb_title.setText(_translate("MainWindow", "Agenda de Contactos:"))
        self.bt_s_start.setText(_translate("MainWindow", "Encender"))
        self.bt_s_stop.setText(_translate("MainWindow", "Apagar"))
        self.label.setText(_translate("MainWindow", "Servidor:"))
        self.bt_save.setText(_translate("MainWindow", "Guardar"))
        self.bt_delete.setText(_translate("MainWindow", "Borrar"))
        self.bt_update.setText(_translate("MainWindow", "Modificar"))
        self.bt_clean.setText(_translate("MainWindow", "Limpiar Casillas"))
        self.lb_mail_log.setText(_translate(
            "MainWindow", " Aviso de Registro vial Mail:"))
        self.lb_mail_log_2.setText(_translate(
            "MainWindow", " Ingrese su mail a continuacion:"))
        self.bt_send_log.setText(_translate(
            "MainWindow", "Enviar archivo log"))