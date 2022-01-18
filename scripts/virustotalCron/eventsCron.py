from bs4 import BeautifulSoup
import requests
import json
import os
global header
global ids
header = {
'Host': '127.0.0.1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': '<your_token>',
'Connection': 'close'
}
ids = []

def getEvents():
    try:
        url = "https://127.0.0.1/events/"
        rsp = requests.get(url, headers=header, verify=False)
        data = rsp.text
        jsonData = json.loads(data)
        for i in jsonData:
            ids.append(i["id"])
    except requests.exceptions.HTTPError as err:
        print(err)


def runVirusToal():
    for i in ids:
        if int(i) <= 26:
            continue
        cmd = '''/var/www/MISP/app/Console/cake Event enrichment 1 ''' + i + ''' '{"modules": "virustotal_public"}' '''
        cmdResult = os.system(cmd)

getEvents()
runVirusToal()


