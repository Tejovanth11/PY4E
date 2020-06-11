#use pycharm instead of atom 
import urllib
import json
import urllib.request
url = input("enter url:- ")
u = urllib.request.urlopen(url)
data = u.read()
data = json.loads(data)

total = 0
for tags in data["comments"]:
	total+=tags["count"]
print(total)
