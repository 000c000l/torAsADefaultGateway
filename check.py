from urllib import request
import json
with request.urlopen("https://check.torproject.org/api/ip") as url:
    data=json.loads(url.read().decode())
    if(data["IsTor"]==True):
        print("Tor is activated")
    else:
        print("Tor is deactivated")
    print("IP:",data["IP"])