Python 爬虫学习项目
个人学习 Python 爬虫过程中的实践代码，从基础请求到多页数据抓取。
项目内容
      文件
      说明
      技术点
      02_requests_baidu_hotsearch.py
      抓取百度热搜榜
      requests + BeautifulSoup，静态页面解析
      03_faloo_novel_scraper.py
      批量下载飞卢小说章节
      多级页面抓取，CSS 选择器，文件写入
环境依赖
Python 3.10+
requests
beautifulsoup4
快速开始
# 1. 克隆仓库
git clone https://github.com/cch157036-ctrl/python-spider-demo.git

# 2. 进入目录
cd python-spider-demo

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行
python 02_requests_baidu_hotsearch.py
技术说明
使用 requests 发送 HTTP 请求，通过 User-Agent 伪装浏览器避免被拦截
使用 BeautifulSoup 解析 HTML，通过 CSS 选择器定位目标数据
小说爬虫实现多级页面抓取：先从目录页获取章节列表，再逐章访问详情页提取正文
抓取结果保存为本地文本文件，使用 UTF-8 编码避免中文乱码
学习中
正在持续学习和完善中，后续计划：
添加异常处理和重试机制
学习 Selenium 处理动态渲染页面
加入数据清洗和结构化存储（CSV / SQLite）
