import requests

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2635053000'
response = requests.get(url)

print(response.text)
