import smtplib
from email.message import EmailMessage
from utils import load_emails

def send_bulk_mail(email_file, subject, body, attachment):
    SENDER_EMAIL = "laxmiprasanna229@gmail.com"
    APP_PASSWORD = "inhl sskl lluo ytql"

    emails = load_emails(email_file)
    sent = 0

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(SENDER_EMAIL, APP_PASSWORD)

    for email in emails[:100]:
        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = subject
        msg.set_content(body)

        if attachment:
            with open(attachment, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename="Resume.pdf"
                )

        server.send_message(msg)
        sent += 1

    server.quit()
    return sent
