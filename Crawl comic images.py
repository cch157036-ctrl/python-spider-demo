import requests
import parsel
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from parsel import selector

#漫画网址
url = 'https://www.mkzhan.com/215596/'

#请求头
headers = {
    'cookie':'_c_WBKFRo=twqM6HpiU04JtrJ1YJnFicrXOBeMdr2MyDfV4w2D; __login_his_sync=0; redirect_url=%2F215596%2F',
    'referer':'https://www.mkzhan.com/',
    'host':'www.mkzhan.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

#向漫画网址发送请求
resp = requests.get(url, headers=headers)

#解析数据，处理网页源代码
Selector = parsel.Selector(resp.text)
#通过Selector对象来选择源代码中的特定元素
li_list = Selector.css('.chapter__list-box li')
#print(li_list)  #返回的列表，列表里面每一个元素都是selector对象，这个对象可以调用css的语法

#通过for循环遍历，并且进行了排序  从第一话开始
for li in list(reversed(li_list[2:])):
    #拿到章节ID
    img_id = li.css('a::attr(data-chapterid)').get()
    #拿到章节标题
    title = li.css('a::text').get().strip()

    if not title:
        title = li.css('a::text').getall()[1].strip()

    file_name=f'{title}\\'
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    #章节网址
    index_url ='https://comic.mkzcdn.com/chapter/content'
    #配置数据参数
    data={
        'chapter_id':img_id,
        'comic_id':'215596',
        'format':'1',
        'quality':'1',
        'type':'1',
    }
    #向每一章漫画网址发送请求，获取图片数据

    json_data=requests.get(index_url,params=data).json()
    # print(json_data)
    imgs = json_data['data']
    # imgs=json_data['data']['page']
    print(imgs)
    page=0
    folder_name=title
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    #拿到图片url地址
    for img in imgs:
        img_url=img['image']
        #重要  给文件名加上后缀，防止重名或无法打开
        #使用page变量作为文件名，保证顺序（0.jpg,1.jpg...）
        file_path=os.path.join(folder_name,f"{page}.jpg")
        try:
            #发送请求获取图片内容（加上timeout防止卡死）
          img_content=requests.get(img_url,timeout=10).content
            #核心动作  将图片内容写入文件
          with open(file_path,'wb') as f:
            f.write(img_content)

            print(f"已保存：{file_path}")
        except Exception as e:
               print(f"下载失败：{img_url},错误：{e}")
        #每下载一张，页码+1，这样下一张就是1.jpg 2.jpg....
        page+=1

        #向图片网址发送请求，获取。content数据
        img_content=requests.get(img_url).content
        #打印标题和漫画图片网址
        print(title,img_url)
