import smtplib
import os


class NotificationManager:
    def __init__(self):
        self.smtp_address = os.environ.get("SMTP_ADDRESS")
        self.email = os.environ.get("EMAIL")
        self.password = os.environ.get("PASSWORD")
        self.connection = smtplib.SMTP(os.environ.get("SMTP_ADDRESS"), port=587)

    def send_email(self, emails, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.password)
            for email in emails:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode(
                        "utf-8"
                    ),
                )
