# https://github.com/sendgrid/sendgrid-python
# import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings 


def send_mail(user,article):
    content='<strong>{0} liked article: {1}</strong>'
    content=content.format(user,article)
    message = Mail(
        from_email=settings.SENDER_EMAIL,
        to_emails=settings.RECIEVER_EMAIL,
        subject='like notification',
        html_content=content)
    try:
        """uncomment the belwo line to get sendgri api key 
        from your environment varliable if it is configured"""
        # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg = SendGridAPIClient('SENDGRID_API_KEY')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)