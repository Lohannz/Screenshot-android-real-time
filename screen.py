from ast import While
import time
from unicodedata import name

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    namephone = 'smartphone conectado' 
    print(f'{namephone}')

    return device, client


if __name__ == '__main__':
    device, client = connect()

screenshot = device.screencap()

import os

x = os.listdir("/home/lohan/Documentos/refugio/foto/")

i = 1

filepath = "/home/lohan/Documentos/refugio/foto/" + f"{i}print.png"
for filepath in x:
    i += 1
    filepath = "/home/lohan/Documentos/refugio/foto/" + f"{i}print.png"
    with open(filepath, 'wb') as f: 
        f.write(screenshot)
print('salvo!')
if "1print.png" in x:
    pass
else:
    with open(filepath, 'wb') as f: 
        f.write(screenshot)
        print('salvo!')


    


