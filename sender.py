import smtplib
from config import SMTP_USER, SMTP_PWD

def notify(recipients, subject, body):
    # build smtp message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % \
              (SMTP_USER, ", ".join(recipients), subject, body)

    # send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(SMTP_USER, SMTP_PWD)
        server.sendmail(SMTP_USER, recipients, message)
        server.close()
        print 'Email sent'
    except:
        print "Failed to send mail"
