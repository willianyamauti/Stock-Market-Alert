from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
my_pone_number = ''
twillo_phone_number = ''


class Twillo:

    def send_msg(self, msg):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=msg,
                from_=twillo_phone_number,
                to=my_pone_number
            )

        print(message.status)
