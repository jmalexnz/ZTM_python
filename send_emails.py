import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# kiaora.its.jane@gmail.com
#itsjane123
html = Template(Path('index.html').read_text())



email = EmailMessage()
email['from'] = 'Jane Alexander'
email['to'] = 'jmalex.nz@gmail.com'
email['subject'] = 'You won $10,000,000!!'
email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com',
                  port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kiaora.its.jane@gmail.com', 'xdwckfsmmubpxamf')
    smtp.send_message(email)
    print('all good boss!')
# you can also set up a html template
# that can be customised
