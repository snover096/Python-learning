import requests
from bs4 import BeautifulSoup
import ollama # 导入 ollama 库

def scrape_quotes(url):
    count = 0
    maxCount = 10
    goodurl = f"{url}".rstrip('/')
    all_quotes = ""

    headers = {'User-Agent': 'Mozilla/5.0'}
    
    
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('span', class_='text')
            print('='*50)
            print(quotes)
            all_quotes += " ".join([q.get_text() for q in quotes])
            # print(all_quotes)  
        else:
            print("bad url") 
            break

        nextButton = soup.find('li',"next")
        if nextButton and count < maxCount:
            count += 1
            nextA = nextButton.find('a')['href']
            url = f"{goodurl}{nextA}"
            print(url)    
        else:
            break
          
    return all_quotes    
        

def analyze_with_local_ai(text):
    print("正在将数据发送给本地大模型进行分析，请稍候...\n")
    
    # 构建 Prompt (提示词)
    prompt = f"""
    我抓取了一些名人名言，内容如下：
    {text}
    
    请帮我完成以下任务：
    1. 总结这些名言主要探讨了哪几个人生主题？
    2. 从中挑选出最具有“激励人心”力量的一句话，并解释为什么。
    请用中文回答，保持排版清晰。
    """
    
    # 调用你本地的模型 (请将 model替换为你实际在 Ollama 中运行的模型名称)
    # 比如 llama3, qwen2.5:14b 等
    response = ollama.chat(model='Gemma4-8b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']

if __name__ == "__main__":
    # 1. 爬虫抓取
    scraped_text = scrape_quotes("http://quotes.toscrape.com/")
    
    
    # if scraped_text:
    #     # 2. AI 分析
    #     ai_result = analyze_with_local_ai(scraped_text)
    #     print("=== 本地 AI 分析结果 ===")
    #     print(ai_result)
    # else:
    #     print("抓取失败")