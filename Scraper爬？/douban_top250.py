import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import re
import os

# ==================== 配置区 ====================
BASE_URL = "https://movie.douban.com/top250"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
OUTPUT_DIR = os.path.dirname(__file__)  # 输出到当前脚本所在目录


def fetch_page(start: int) -> str | None:
    """抓取单页HTML，start=0/25/50..."""
    url = f"{BASE_URL}?start={start}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            print(f"  [OK] 第 {start // 25 + 1} 页抓取成功 - {url}")
            return resp.text
        else:
            print(f"  [FAIL] 第 {start // 25 + 1} 页失败，状态码: {resp.status_code}")
            return None
    except Exception as e:
        print(f"  [FAIL] 第 {start // 25 + 1} 页请求异常: {e}")
        return None


def parse_movie(item) -> dict:
    """解析单个电影条目，返回字段字典"""
    movie = {}

    # 排名
    em = item.find("em")
    movie["排名"] = em.get_text(strip=True) if em else ""

    # 片名 — .title 是中文名，后面的 .title 可能是英文/港台译名
    titles = item.find_all("span", class_="title")
    movie["中文片名"] = titles[0].get_text(strip=True) if len(titles) > 0 else ""
    movie["外文片名"] = titles[1].get_text(strip=True).lstrip("/").strip() if len(titles) > 1 else ""

    # 信息行 — 导演 / 主演 / 年份 / 国家 / 类型
    bd = item.find("div", class_="bd")
    if bd:
        # bd 下第一个 <p> 含导演和年份信息，分两行
        info_p = bd.find("p")
        if info_p:
            info_text = info_p.get_text().strip()
            lines = [l.strip() for l in info_text.split("\n") if l.strip()]

            # 第一行: "导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /..."
            if lines:
                dir_match = re.search(r"导演:\s*(.+?)(?:\s{2,}主演:)", lines[0])
                movie["导演"] = dir_match.group(1).strip() if dir_match else ""

            # 第二行: "1994 / 美国 / 犯罪 剧情"
            if len(lines) >= 2:
                parts = [p.strip() for p in lines[1].split("/")]
                movie["年份"] = parts[0] if len(parts) >= 1 else ""
                movie["国家"] = parts[1] if len(parts) >= 2 else ""
                movie["类型"] = parts[2] if len(parts) >= 3 else ""
            else:
                movie["年份"] = ""
                movie["国家"] = ""
                movie["类型"] = ""

        # 金句 — 在 p.quote 里
        quote = bd.find("p", class_="quote")
        movie["金句"] = quote.get_text(strip=True) if quote else ""

        # 评分
        rating = bd.find("span", class_="rating_num")
        movie["评分"] = rating.get_text(strip=True) if rating else ""

        # 评价人数 — 在评分 span 后的文本节点里
        # div 文本类似 "9.7  3291983人评价"，保留空格防止小数点粘连
        bd_divs = bd.find_all("div", recursive=False)
        if bd_divs:
            div_text = bd_divs[0].get_text(separator=" ")
            count_match = re.search(r"(\d+)\s*人评价", div_text)
            movie["评价人数"] = count_match.group(1) if count_match else ""
        else:
            movie["评价人数"] = ""

    return movie


def scrape_all(pages: int = 10) -> list[dict]:
    """爬取全部250条"""
    all_data = []
    for i in range(pages):
        start = i * 25
        html = fetch_page(start)
        if html is None:
            continue

        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all("div", class_="item")
        for item in items:
            movie = parse_movie(item)
            all_data.append(movie)

        # 礼貌爬虫 — 每页间隔2秒
        if i < pages - 1:
            print(f"  [*] 等待 2秒...")
            time.sleep(2)

    return all_data


def save_csv(data: list[dict], filepath: str):
    """写入CSV"""
    if not data:
        print("无数据可写入CSV")
        return
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[FILE] CSV已保存: {filepath}")


def save_json(data: list[dict], filepath: str):
    """写入JSON"""
    if not data:
        print("无数据可写入JSON")
        return
    with open(filepath, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[FILE] JSON已保存: {filepath}")


def print_summary(data: list[dict]):
    """打印统计摘要"""
    if not data:
        return
    print("\n" + "=" * 50)
    print("[STATS] 数据摘要")
    print(f"  共爬取电影数: {len(data)}")
    ratings = [float(m["评分"]) for m in data if m["评分"]]
    if ratings:
        print(f"  最高评分: {max(ratings):.1f}")
        print(f"  最低评分: {min(ratings):.1f}")
        print(f"  平均评分: {sum(ratings) / len(ratings):.2f}")
    # 评分最高的3部
    print("\n[TOP] TOP 3:")
    sorted_data = sorted(data, key=lambda m: float(m["评分"] if m["评分"] else 0), reverse=True)
    for m in sorted_data[:3]:
        print(f"  {m['排名']}. {m['中文片名']} - {m['评分']}分")


def main():
    print("=== 开始爬取豆瓣电影 Top 250 ===\n")
    data = scrape_all(pages=10)

    if not data:
        print("\n:( 啥也没抓到，豆瓣可能把你ban了...")
        return

    csv_path = os.path.join(OUTPUT_DIR, "douban_top250.csv")
    json_path = os.path.join(OUTPUT_DIR, "douban_top250.json")

    # save_csv(data, csv_path)
    # save_json(data, json_path)
    print_summary(data)

    print("\n[DONE] 搞定！")


if __name__ == "__main__":
    main()