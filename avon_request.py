import requests


head={
'Host': 'webeservices3.avon.com',
'Content-Length': '143',
'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="90"',
'Accept': 'application/json, text/plain, */*',
'Sec-Ch-Ua-Mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
'Content-Type': 'application/json;charset=UTF-8',
'Origin': 'https://www.avon.com.sa',
'Sec-Fetch-Site': 'cross-site',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.avon.com.sa/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'close'}
url = 'https://webeservices3.avon.com/agws/srvc/login'

n=100
for i in range(1):
    data = {"login":{"version":"4","password":"بدري6786","userId":"'","mrktCd":"SA","langCd":"ar","devKey":"oWjbgKVM7Mlvp0xQMPzS5758wDHGlxC5"}}
    response = requests.post(url,json=data, headers=head)
    print(response.json())
    print(i)
