import smtplib
from config import SMTP_USER, SMTP_PWD

def notify(recipients, subject, body):
    FROM = SMTP_USER
    TO = recipients
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(SMTP_USER, SMTP_PWD)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
