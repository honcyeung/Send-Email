# send email with python

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '***'
email['to'] = '***@gmail.com'
email['subject'] = 'testing'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('***@gmail.com', '********')
    smtp.send_message(email)
    print('done')
