import sys
import requests

print
print (sys.executable)

r = requests.get("http://google.com")
print (r.status_code)


