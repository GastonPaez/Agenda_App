from datetime import datetime
from time import strftime
from mail_log import Mail

mail_input = ""
mail_register = mail_input.split


def log_save(funcion):
    def save_log(*args):

        funcion(*args)
        with open("log.txt", "a") as logs:
            time_now = strftime('%d/%m/%y %H:%M:%S')
            logs.write(
                f"{time_now} | Registro | {args[0]}, {args[1]}, {args[2]}, {args[3]}, {args[4]} \n")
            correo = f'{args[5]}'
            correo_select = correo.split()
            if len(correo) > 5:
                correo_select = correo_select
            else:
                correo_select = ["bzjuegosdigitales@gmail.com"]

            # Envia el registro via mail
            mail = Mail()
            mail.send(
                "Se ha realizado un Nuevo Registro en la Aplicacion", f"Nuevo Registro en la aplicacion \nNombre: {args[0]}\nApellido: {args[1]}\nNumero: {args[2]}\nDireccion: {args[3]}\nE-mail: {args[4]}", correo_select)
    return save_log


def log_update(funcion):
    def updated_log(*args):
        funcion(*args)
        with open("log.txt", "a") as logs:
            time_now = strftime('%d/%m/%y %H:%M:%S')
            logs.write(
                f"{time_now} | Actualizado | {args[1]}, {args[2]}, {args[3]}, {args[4]}, {args[5]} \n")
            correo = f'{args[6]}'
            correo_select = correo.split()
            if len(correo) > 5:
                correo_select = correo_select
            else:
                correo_select = ["bzjuegosdigitales@gmail.com"]
            # Envia el registro via mail
            mail = Mail()
            mail.send(
                "Se ha realizado una Modificacion en un Registro en la Aplicacion", f"Nueva Modificacion en la aplicacion \nNombre: {args[1]}\nApellido: {args[2]}\nNumero: {args[3]}\nDireccion: {args[4]}\nE-mail: {args[5]}", correo_select)

    return updated_log


def log_delete(funcion):
    def deleted_log(*args):
        funcion(*args)
        with open("log.txt", "a") as logs:
            time_now = strftime('%d/%m/%y %H:%M:%S')
            logs.write(
                f"{time_now} | Eliminado | {args[1]}, {args[2]}, {args[3]}, {args[4]}, {args[5]} \n")
            correo = f'{args[6]}'
            correo_select = correo.split()
            if len(correo) > 5:
                correo_select = correo_select
            else:
                correo_select = ["bzjuegosdigitales@gmail.com"]
            # Envia el registro via mail
            mail = Mail()
            mail.send(
                "Se ha realizado un Elimanado Registro en la Aplicacion", f"Registro Eliminado en la aplicacion \nNombre: {args[1]}\nApellido: {args[2]}\nNumero: {args[3]}\nDireccion: {args[4]}\nE-mail: {args[5]}", correo_select)

    return deleted_log
