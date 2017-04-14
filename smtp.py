import smtplib

class hotmail:
    def __init__(self):
        self.smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()

        # email account credentials
        self.smtpObj.login('store_bot@outlook.com', '123JolleyPeople')

    def send_email(self, msg):
        # insert from and to email address
        self.smtpObj.sendmail('store_bot@outlook.com', 'happyguyhere@hotmail.com', msg)

