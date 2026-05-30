import requests
from bs4 import BeautifulSoup
import ollama # 导入 ollama 库

def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        # 将抓取到的名言合并成一段长文本
        return " ".join([q.get_text() for q in quotes])
    return ""

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
    
    # 调用你本地的模型 (请将 'qwen2.5:7b' 替换为你实际在 Ollama 中运行的模型名称)
    # 比如 llama3, qwen2.5:14b 等
    response = ollama.chat(model='Gemma4-8b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']

if __name__ == "__main__":
    # 1. 爬虫抓取
    scraped_text = scrape_quotes()
    if scraped_text:
        # 2. AI 分析
        ai_result = analyze_with_local_ai(scraped_text)
        print("=== 本地 AI 分析结果 ===")
        print(ai_result)
    else:
        print("抓取失败")