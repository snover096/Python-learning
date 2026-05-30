import requests
from bs4 import BeautifulSoup

# 1. 目标网址
url = 'http://quotes.toscrape.com/'

# 2. 发送请求，获取网页内容 (就像用浏览器打开网页)
# 加上 headers 伪装成正常的浏览器，防止被简单的反爬拦截
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url, headers=headers)
#print(response.text)

# 3. 检查是否请求成功 (状态码 200 表示成功)
if response.status_code == 200:
    # 4. 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 5. 提取数据：在网页源码中，名言都包含在 <span class="text"> 标签里
    quotes = soup.find_all('span', class_='text')
    
    print(f"成功抓取了 {len(quotes)} 条名言：\n")
    for i, quote in enumerate(quotes, 1):
        # get_text() 可以去除 HTML 标签，只保留纯文本
        print(f"{i}. {quote.get_text()}")
else:
    print(f"请求失败，状态码: {response.status_code}")