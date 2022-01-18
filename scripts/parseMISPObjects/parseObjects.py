# This script is for parsing object attributes from MISP Events & send it to ELK through Logstash
# Example of data sent to logstash: {"test1": "hello", "test2": "here we are"}
import requests
import json
import socket
import sys

# Some global variables
# ids is list with all event IDs in MISP
# Note: Authorization header has the auth-key of MISP
# Host variable is for the IP of the machine that has Logstash
global header
global ids
HOST = 'localhost'
PORT = 5000
ids = []
header = {
'Host': 'localhost',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': '<your_token_here>',
'Connection': 'close'
}


# getEvents function: get all event IDs from MISP
# Note: Verify variable in get requests is for disabling the SSL Verification
def getEvents():
    try:
        urlLen = "https://localhost/events/"
        rsp = requests.get(urlLen, headers=header, verify=False)
        data = rsp.text
        jsonData = json.loads(data)
        for i in jsonData:
            ids.append(i["id"])
    except requests.exceptions.HTTPError as err:
        print(err)


# sendData function: send the object's attributes to Logstash by stablishing Socket.
def sendData(parsedDic):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(1)
    try:
        sock.connect((HOST, PORT))
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(2)
    sock.send(str(json.dumps(parsedDic)).encode('utf-8'))
    sock.close()


# getAttributes: get all object attributes from all Events in MISP
# Note: attrs is a list of attributes for spacefic object for spaceif event.

def getAttributes():
    restricted = [1,2,3,18,21]  
    for i in ids:
        if int(i) in restricted:
            continue
        url = "https://localhost/events/" + str(i) + "/"
        rsp = requests.post(url, headers=header, verify=False)
        data = rsp.text
        jsonData = json.loads(data)
        for attInd in jsonData['Event']['Object']: 
            attrs = attInd['Attribute']
            for attribute in attrs:
                parsedDic = attribute
                parsedDic['event_id'] = i
                sendData(parsedDic)

        
def main():
    getEvents()
    getAttributes()


main()
