from twilio.rest import Client
import os
from dotenv import load_dotenv
import PokeApi as pkm

name,img = pkm.pokemon()
print(name,img)

load_dotenv()
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
num_cliente = os.environ['NUM_CLIENTE']
num_ser = os.environ['NUM_SER']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=f'Tu pokemon de hoy es: {name}',
                              media_url=img,
                              from_=f'whatsapp:{num_ser}',
                              to=f'whatsapp:{num_cliente}'
                          )