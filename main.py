import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from mainwind import Ui_MainWindow
from orm import *
from pathlib import Path
from mail_log import MailLog
import threading
import subprocess
import os
import sys

# Variable Global
theproc = ""


class Server():
    # Inicia la clase para realizar conexiones con entre el servidor y el cliente
    def __init__(self,):
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, 'server', 'server.py')

    def run_server(self, var):
        the_path = self.ruta_server
        if var == True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()
        else:
            print("")


class MainWindow(QMainWindow, Ui_MainWindow, QWidget):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self,)
        Ui_MainWindow.__init__(self,)
        self.setupUi(self,)
        # Nombre de la Aplicacion
        title = "Agenda App"
        self.setWindowTitle(title)
        # Icono de la aplicacion
        ruta_icono = Path('.', 'src', 'icon.ico')
        self.setWindowIcon(QIcon(str(ruta_icono)))

        # Conexion Servidor
        self.server = Server()

        # Boton para grabar
        self.bt_save.clicked.connect(lambda: self.save_data(
            self.le_name.text(), self.le_lastname.text(), self.le_number.text(), self.le_adress.text(), self.le_mail.text(), self.le_mail_log.text()))
        # Boton update
        self.bt_update.clicked.connect(lambda: self.update_data(self.le_id.text(),
                                                                self.le_name.text(), self.le_lastname.text(), self.le_number.text(), self.le_adress.text(), self.le_mail.text(), self.le_mail_log.text()))
        # Boton Borrar
        self.bt_delete.clicked.connect(lambda: self.delete_data(self.le_id.text(),
                                                                self.le_name.text(), self.le_lastname.text(), self.le_number.text(), self.le_adress.text(), self.le_mail.text(), self.le_mail_log.text()))
        # Boton Limpiar
        self.bt_clean.clicked.connect(self.clean_data)

        # Inicia y Detiene el servidor
        self.bt_s_start.clicked.connect(self.server_start)
        self.bt_s_stop.clicked.connect(self.server_stop)

        # Enviar el registro del log al mail colocado en el casillero
        self.bt_send_log.clicked.connect(
            lambda: self.send_log_mail(self.le_mail_log.text()))

        # inicia el metodo de actualizar el Tree Widget
        self.treeview_data()

        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected):
        # Metodo para seleccionar el id del contacto respecto a su posicion de fila en el Treeview
        for index in selected.indexes():
            # print("selected location: {0}, column: {1} ".format(
            #    index.row(), index.column()))
            results = Contacts.select().dicts()
            #print("El id es :", results[index.row()]["id"])
            contact = results[index.row()]
            self.auto_complete(contact)

    def treeview_clean(self):
        # Metodo para limpiar el treewidget
        # contador de tablerow para iterar
        tablerow = 0
        # transforma los contactos en diccionarios
        results = ""
        # coloca la cantidad de filas determinadas
        self.tableWidget.setRowCount(len(results))
        # itera los contactos en forma de diccionario y los coloca en cada fila en este caso limpia
        for row in results:

            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(row))

            tablerow += 1

    def treeview_data(self):
        # Limpia el treewidget para refrescar los datos.
        self.treeview_clean()
        # contador de tablerow para iterar
        tablerow = 0
        # transforma los contactos en diccionarios
        results = Contacts.select().dicts()

        # coloca la cantidad de filas determinadas
        self.tableWidget.setRowCount(len(results))
        # itera los contactos en forma de diccionario y los coloca en cada fila
        for row in results:

            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row['id'])))
            self.tableWidget.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(row['name']))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(row['lname']))
            self.tableWidget.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(row['number']))
            self.tableWidget.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(row['adress']))
            self.tableWidget.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(row['mail']))

            tablerow += 1

    def save_data(self, nm, ln, nb, ad, ml, mail):
        # Al presionar el boton GUARDAR envia los valores ingresados en los casilleros al orm para registrar
        save_contact(nm, ln, nb, ad, ml, mail)
        self.clean_data()
        self.treeview_data()

    def update_data(self, idf, nm, ln, nb, ad, ml, mail):
        # Al presionar el boton MODIFICAR envia el valor del casilero ID al orm para modificar con los datos nuevos
        # Los parametros de datos que no son el id son necesarios para utilizarlos en el registro de log
        update_contact(idf, nm, ln, nb, ad, ml, mail)
        self.treeview_data()

    def delete_data(self, idf, nm, ln, nb, ad, ml, mail):
        # Enviar el valor del casillero ID al orm, para eliminar el registro
        # Los parametros de datos que no son el id son necesarios para utilizarlos en el registro de log
        delete_contact(idf, nm, ln, nb, ad, ml, mail)
        self.treeview_data()

    def clean_data(self,):
        # Limpia los casilleros
        self.le_name.setText("")
        self.le_lastname.setText("")
        self.le_number.setText("")
        self.le_adress.setText("")
        self.le_mail.setText("")

    def auto_complete(self, contact):
        # metodo para autocompletar los lineEdit al seleccionar contacto de la tabla
        self.le_name.setText(contact["name"])
        self.le_lastname.setText(contact["lname"])
        self.le_number.setText(contact["number"])
        self.le_adress.setText(contact["adress"])
        self.le_mail.setText(contact["mail"])
        self.le_id.setText(str(contact["id"]))

    def server_start(self):
        # Inicia el servidor para conectarse con el cliente
        if theproc != "":
            theproc.kill()
            threading.Thread(target=self.server.run_server, args=(
                True,), daemon=True).start()
            print('Server Activado')
        else:
            threading.Thread(target=self.server.run_server, args=(
                True,), daemon=True).start()
            print('Server Activado')

    def server_stop(self):
        # Detiene el servidor
        global theproc
        if theproc != "":
            theproc.kill()
            print('Servidor Detenido')

    def send_log_mail(self, email):
        # envia el log al mail ingresado en la app
        mail = MailLog()
        mail.send_log(email.split())


#######################################
###########   CONTROLADOR   ###########
#######################################

if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec())
