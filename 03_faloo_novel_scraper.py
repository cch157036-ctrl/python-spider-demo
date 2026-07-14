"""
批量下载飞卢小说章节
技术点：多级页面抓取（目录页 -> 详情页）+ CSS 选择器 + 文件写入
"""

import os
import time
import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/150.0.0.0 Safari/537.36"
}

# 保存小说的文件夹
NOVEL_DIR = "novel_output"


def get_chapter_list(novel_url):
    """从小说目录页获取章节名称和链接"""
    response = requests.get(novel_url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    chapter_tags = soup.select(".DivTd3 a")

    chapters = []
    for tag in chapter_tags:
        name = tag.text.strip()
        url = "https:" + tag.get("href", "")
        if name and url:
            chapters.append({"name": name, "url": url})

    return chapters


def download_chapter(chapter, save_dir):
    """下载单个章节正文并保存为文本文件"""
    response = requests.get(chapter["url"], headers=HEADERS, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.select(".noveContent p")

    # 替换文件名中的非法字符
    safe_name = chapter["name"].replace("/", "_").replace("\\", "_")
    filepath = os.path.join(save_dir, f"{safe_name}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        for p in paragraphs:
            f.write(p.text + "\n")

    print(f"{chapter['name']} -- 下载成功")


def main():
    novel_url = "https://b.faloo.com/1534584.html"
    max_chapters = 10  # 最多下载章节数

    # 创建输出文件夹
    os.makedirs(NOVEL_DIR, exist_ok=True)

    print("正在获取章节列表...")
    chapters = get_chapter_list(novel_url)
    print(f"共找到 {len(chapters)} 章，开始下载前 {max_chapters} 章\n")

    for chapter in chapters[:max_chapters]:
        try:
            download_chapter(chapter, NOVEL_DIR)
            time.sleep(1)  # 每章间隔 1 秒，避免请求过快被封 IP
        except Exception as e:
            print(f"{chapter['name']} -- 下载失败: {e}")

    print("\n下载完成！")


if __name__ == "__main__":
    main()
