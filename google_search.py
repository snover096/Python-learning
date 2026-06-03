# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

def google_search(query, num_results=10):
    """
    在Google上搜索指定查询并返回结果
    
    参数:
    query (str): 搜索查询
    num_results (int): 返回结果的数量，默认为10
    
    返回:
    list: 包含搜索结果的字典列表
    """
    # Google搜索URL
    base_url = "https://www.google.com/search"
    
    # 设置搜索参数
    params = {
        'q': query,
        'num': num_results
    }
    
    # URL编码
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    # 设置headers伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers, timeout=10)
        
        # 检查响应状态
        if response.status_code == 200:
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 查找搜索结果
            results = []
            # Google搜索结果通常在<div class="g">元素中
            search_results = soup.find_all('div', class_='g')[:num_results]
            
            for result in search_results:
                # 提取标题
                title_element = result.find('h3')
                title = title_element.get_text() if title_element else "无标题"
                
                # 提取链接
                link_element = result.find('a')
                link = ""
                if link_element and link_element.has_attr('href'):
                    href = link_element['href']
                    # 过滤掉无效链接
                    if href.startswith('/url?q='):
                        # 处理重定向链接
                        link = urllib.parse.unquote(href.split('/url?q=')[1].split('&')[0])
                    elif href.startswith('http'):
                        link = href
                
                # 添加到结果列表（过滤无效结果）
                if title != "无标题" and link:
                    results.append({
                        'title': title,
                        'link': link
                    })
            
            return results
        else:
            print(f"搜索失败，状态码: {response.status_code}")
            if response.status_code == 429:
                print("请求过于频繁，请稍后再试")
            return []
            
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络连接")
        return []
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
        return []
    except Exception as e:
        print(f"搜索过程中出现错误: {e}")
        return []

def main():
    # 获取用户输入
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        try:
            query = input("请输入要搜索的内容: ")
        except EOFError:
            query = "Python编程"
    
    # 设置返回结果数量
    try:
        num_results = int(input("请输入要返回的结果数量 (默认10): ") or "10")
    except (ValueError, EOFError):
        num_results = 10
    
    print(f"\n正在搜索: {query}")
    print("=" * 50)
    
    # 执行搜索
    results = google_search(query, num_results)
    
    # 显示结果
    if results:
        print(f"找到了 {len(results)} 条结果：\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}")
            print(f"   链接: {result['link']}")
            print()
    else:
        print("未找到搜索结果或搜索失败。")
        print("\n提示：")
        print("1. 如果持续出现问题，可能是触发了Google的反爬虫机制")
        print("2. 可以尝试以下替代方案：")
        print("   - 等待一段时间后再试")
        print("   - 更换网络环境")
        print("   - 使用其他搜索引擎的API")

if __name__ == "__main__":
    print("Google搜索工具")
    print("-" * 30)
    main()

if __name__ == "__main__":
    main()