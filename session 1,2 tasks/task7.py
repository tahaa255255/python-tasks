#get your puplic ip and you location
import requests
import pprint
ip=requests.get("https://api.ipify.org/?format=json")
print("my puplic ip is :",ip.json()["ip"])
geo=requests.get("https://ipinfo.io/"+str(ip.json()["ip"])+"/geo")
print("my loacation is :",geo.json()["loc"])