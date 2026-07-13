#requests:用于发送HTTP请求获取网页内容
import requests  #导入网络请求库，作用是访问网页、下载网页源代码
#beautifulsoup:用于解析HTML文档和提取数据
from bs4 import BeautifulSoup   #导入网页解析工具，用来拆分、筛选网页里面的文字、链接等内容

#定义url地址
url = "https://b.faloo.com/1534584.html"  #保存要爬取的小说主页网址
#定义header  请求头补全规范格式
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/149.0.0.0 Safari/537.36 "
}  #headers请求头：伪装成chrome浏览器访问网站，避免网站识别出爬虫并拦截访问
#获取小说主页
response = requests.get(url, headers=headers) #带着浏览器伪装头访问小说主页，拿到网页完整源码，存入response
soup = BeautifulSoup(response.text, "html.parser") #把杂乱的网页源码格式化，生成可筛选的解析对象soup

chapter_list = soup.select(".DivTd3")    #筛选全部章节标签
for i in range(10):  #循环读取前10章（外层循环）/循环只取前10个章节，批量处理每一章
    chapter_name = chapter_list[i].select_one("a").text #找到章节块里的链接文字，提取章节名称（比如：第一章 开篇）
    chapter_url ="https:" + chapter_list[i].select_one("a").get("href") #提取章节链接的后半段，拼接完整网址，得到单章阅读页面地址
    details_response = requests.get(chapter_url, headers=headers)#访问当前章节的详情页，下载章节正文网页源码
    details_soup = BeautifulSoup(details_response.text, "html.parser")#解析章节详情页的网页代码，方便提取正文
    p_list = details_soup.select(".noveContent>p")#筛选正文区域所有<p>段落标签，所有小说段落存入p_list
#内层循环
    for p in p_list:  #遍历当前章节每一段文字
       with open(chapter_name + ".text","a",encoding="utf-8") as file:#新建/追加写入文本文件，文件名字是章节名：a代表追加模式，不会覆盖旧内容：utf_8防止中文乱码
        file.write(p.text +"\n")#把段落文字写入文件，每段结束换行
    print(chapter_name + "--下载成功！")#控制台打印提示，告知当前章节已经下载保存完成
