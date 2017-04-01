import smtplib

class email:
    pass

class hotmail(email):
    def __init__(self):
        self.smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.login('store_bot@outlook.com', '123JolleyPeople')

    def send_email(self, msg):
        self.smtpObj.sendmail('store_bot@outlook.com', '6602816177@txt.att.net', msg)
