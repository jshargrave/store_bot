import smtplib
from email.mime.text import MIMEText


# hotmail class used to send emails
class hotmail:
    def send_email(self, msg):
        # msg details
        mime_msg = MIMEText(msg)
        mime_msg['Subject'] = "Email from store bot"
        mime_msg['From'] = ""
        mime_msg['To'] = ""

        try:
            # email account credentials
            smtp_obj = smtplib.SMTP('smtp-mail.outlook.com', 587)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login('store_bot@outlook.com', '123JolleyPeople')
            smtp_obj.sendmail('store_bot@outlook.com', 'happyguyhere@hotmail.com', mime_msg.as_string())
        except smtplib.SMTPException as e:
            print(e)