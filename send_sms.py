# twilio is the go-to API for communications
# Copied from twilio

from twilio.rest import Client

account_sid = 'AC7cd4174ef96e7484da5483546b2d65bf'
auth_token = 'a838d0df2e03c1a586bc5e28f6963ee0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15674065934',
  body='meow',
  to='+64277485192'
)

print(message.sid)
