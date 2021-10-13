import datetime
import socket

host = socket.gethostname()
now = datetime.datetime.now()
nowS = now.strftime("%m/%d/%Y, %H:%M:%S")

import requests
r = requests.get('http://Echo4Advini.eu-de.mybluemix.net/v1/echo?host=' + host + '&time=' + nowS)
print(r.status_code)