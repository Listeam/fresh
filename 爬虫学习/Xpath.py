from lxml import etree   #导入etree模块
import requests
from pprint import pprint
import time
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}
response = requests.get("https://www.baidu.com/index.php?tn=68018901_58_oem_dg",headers = headers)
text = response.text
text_html = etree.HTML(text) #用etree.HTML()方法解析网页，区别于bs4的BeautifulSoup()借用lxml的etree模块，速度更快
#print(text_html)  #打印解析后的内容，目前还打印不出想要的结果
trendings = text_html.xpath('//span[@class="title-content-title"]/text()')#用xpath插件在网页内试出所需的标签，并提取标签内的文本，如果要提取属性值只需要/@属性名
for trending in trendings:
    #html_trending = etree.tostring(trending, encoding = "utf8").decode("utf8")
    print(trending)  #etree的tostring只应用于需要打印每一个标题的完整标签的时候，如果只想要文本，直接在xpath语法里加/text()即可
    print("*"*50)

Urls = []
for i in range(0,100,20):
    response = requests.get(f"https://movie.douban.com/review/best/?start={i}",headers = headers)
    text = response.text
    text_html = etree.HTML(text)
    links = text_html.xpath('//h2/a/@href')
    time.sleep(2)   #每次请求间隔2秒，防止被封IP
    for link in links:   #提取每页每个影评的链接
        Urls.append(link)
        
#print(Urls)
for url in Urls:
    response = requests.get(url,headers = headers)
    text = response.text
    text_html = etree.HTML(text)

    name = text_html.xpath('//div[@class="subject-title"]/a/text()')[0][2:]  #提取电影名，发现前面有两个空格字符，所以用切片去掉
    director = text_html.xpath('//*[@id="content"]/div/div[2]/div[4]/div[4]/ul/li[1]/span[2]/text()')
    main_actors = text_html.xpath('//*[@id="content"]/div/div[2]/div[4]/div[4]/ul/li[2]/span[2]/text()')
    type0 = text_html.xpath('//*[@id="content"]/div/div[2]/div[4]/div[4]/ul/li[3]/span[2]/text()')
    area = text_html.xpath('//*[@id="content"]/div/div[2]/div[4]/div[4]/ul/li[4]/span[2]/text()')
    screen_time = text_html.xpath('//*[@id="content"]/div/div[2]/div[4]/div[4]/ul/li[5]/span[2]/text()')
    film_info = {
        "影名":name,   #strip()方法去掉字符串前后不需要的字符
        "导演": director,
        "主演": main_actors,
        "类型": type0,
        "地区": area,
        "上映时间": screen_time
    }
    pprint(film_info,indent=4)  #特殊打印，间隔四空格
    print("-" * 80)
    time.sleep(2)  #每次请求间隔2秒，防止被封IP
    



