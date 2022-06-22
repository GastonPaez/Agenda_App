import smtplib
import ssl


class Mail:
    # Clase para utilizar el servicio de correo electronico Gmail
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "theagreatdoug.t@gmail.com"
        self.password = ""

    def send(self, subject, content, emails):
        # Funcion para enviar el correo electronico
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(
            self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            # Se fija si hay uno o mas email para enviar diferentes correos
            result = service.sendmail(
                self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()


class MailLog:
    # Clase para utilizar el servicio de correo electronico Gmail
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "theagreatdoug.t@gmail.com"
        self.password = ""

    def send_log(self, emails):
        # Funcion para enviar el correo electronico
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(
            self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        content = ""
        # Envia el contenido de log.txt por mail
        with open("log.txt", "r") as logs:
            for linea in logs:
                content += linea
        subject = "Envio de Log",

        for email in emails:
            result = service.sendmail(
                self.sender_mail, email, f"Subject: {subject}\n\n{content}")

        service.quit()
