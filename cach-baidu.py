import requests

# from 漫画.web import headers

head = {
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
response = requests.get('https://www.baidu.com', headers=head)
with open('baidu.html', 'w',encoding='utf-8') as f:
    f.write(response.text)