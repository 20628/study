import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests .get('https://movie.douban.com/chart',headers= headers)
if response.ok:
    print(response.status_code)
    print(response.text)
else:
    print('请求失败')
