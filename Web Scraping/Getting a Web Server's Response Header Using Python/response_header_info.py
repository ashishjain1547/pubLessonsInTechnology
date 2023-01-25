from datetime import datetime 
import requests

url = 'http://survival8.blogspot.com/'

x = requests.get(url)

#print(x.text)
print(x.headers)

curr_time = datetime.now()

with open("s8_" + str(curr_time).replace(":", "_") + ".log", mode='w') as f:
    f.write(x.text)