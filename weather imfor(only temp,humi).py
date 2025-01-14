import requests
import re

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2635053000'
response = requests.get(url)

temp = re.findall(r'<temp>(.+)</temp>',response.text)
humi = re.findall(r'<reh>(.+)</reh>',response.text)


print(temp)
print(humi)