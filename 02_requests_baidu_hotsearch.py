"""
抓取百度热搜榜标题
技术点：requests 发送 HTTP 请求 + BeautifulSoup 解析 HTML
"""

import requests
from bs4 import BeautifulSoup


def get_baidu_hotsearch():
    url = "https://www.baidu.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/150.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 请求失败时抛出异常
        response.encoding = "utf-8"
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    hot_items = soup.find_all("span", class_="title-content-title")

    results = [item.text for item in hot_items]
    return results


if __name__ == "__main__":
    hotsearch = get_baidu_hotsearch()

    print(f"百度热搜共 {len(hotsearch)} 条:")
    print("-" * 30)
    for idx, title in enumerate(hotsearch, 1):
        print(f"{idx}. {title}")
