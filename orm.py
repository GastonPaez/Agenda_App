from peewee import *
from PyQt5.QtWidgets import QMessageBox
import re
from decorators import *

#######################################
#############   MODELO   ##############
#######################################

db = SqliteDatabase('agenda_final.db')


class BaseModel(Model):
    class Meta:
        database = db  # This model uses the "agenda_final.db" database.


class Contacts(BaseModel):
    name = CharField(max_length=150)
    lname = CharField(max_length=150)
    number = CharField(max_length=19)
    adress = CharField(max_length=100)
    mail = CharField(max_length=150)


db.connect()
db.create_tables([Contacts])


@log_save
def save_contact(nm, ln, nb, ad, ml, mail):
    if len(nm) < 1 or len(ln) < 1 or len(nb) < 1:
        # Alerta error por no completar todos los campos
        alert_incomplete()
    else:
        patron_val_mail = "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+.[a-zA-Z]+$"

        if re.match(patron_val_mail, ml):
            contact = Contacts()
            contact.name = nm
            contact.lname = ln
            contact.number = nb
            contact.adress = ad
            contact.mail = ml
            contact.save()
            mail = mail
            # Alerta de contacto guardado exitoso
            alert_save()

        else:
            alert_error_mail()


@log_update
def update_contact(idf, nm, ln, nb, ad, ml, mail):
    mail = mail
    if len(nm) < 1 or len(ln) < 1 or len(nb) < 1:
        # Alerta error por no completar todos los campos
        alert_incomplete()
    else:
        patron_val_mail = "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+\.[a-zA-Z]+.[a-zA-Z]+$"

        if re.match(patron_val_mail, ml):
            update = Contacts.update(name=nm, lname=ln, number=nb, adress=ad, mail=ml).where(
                Contacts.id == idf)
            update.execute()
            alert_update()


@log_delete
def delete_contact(idf, nm, ln, nb, ad, ml, mail):
    mail = mail
    # Alerta de confirmacion para eliminar contacto
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(
        "¿Esta seguro de que quiere eliminar definitivamente este contacto?")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    response = msg.exec_()

    if response == 1024:
        delete = Contacts.get(Contacts.id == idf)
        delete.delete_instance()
        alert_delete_complete()
    else:
        alert_delete_incomplete()


# Mensajes de Alertas
def alert_incomplete():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setText("Complete todos los campos obligatorios.")
    #msg.setInformativeText("Informacion Adicional")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setDetailedText(
        "Estos son los detalles del error: \nDebe completar todos los campos obligatorios del formulario para que se registre el contacto. \nPresione OK y proceda a completar los campos faltantes del formulario de registro.")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def alert_save():
    # Cuando se guarda un contacto
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("El contacto ha sido registrado.")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def alert_update():
    # Cuando se modifica un contacto
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("El contacto ha sido modificado.")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def alert_error_mail():
    # Cuando se valida el correo electronico
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error en la validacion del mail. \nIngrese nuevamente el mail.")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def alert_delete_complete():
    # Cuando se elimina un registro
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("El contacto ha sido eliminado.")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def alert_delete_incomplete():
    # Cuando se cancela la eliminacion de un contacto
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("El contacto no se ha sido eliminado.")
    msg.setWindowTitle("Agenda de Contactos")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
