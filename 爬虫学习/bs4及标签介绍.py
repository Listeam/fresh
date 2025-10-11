import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"

}    #标头补充，可以伪装成浏览器，可进入更多网页
for start_num in range(0,250,25):  #豆瓣电影每页25个，要做到每页都查询到，0-250每次加25
    response = requests.get(f"http://movie.douban.com/top250?start={start_num}", headers = headers).text  #发现每页的网页链接都有一个共性，start=0,25,50,75...，用变量代替
        #请求get网页源代码文本，并打印
    #print(response)
    #print(response.status_code)
    #print(response.text)
    soup = BeautifulSoup(response, "html.parser")  #创造一个变量，为被html解析器解析网页后的内容
    all_title = soup.find_all("span", class_ = "title")  #查找所有class属性为"title"的span标签
    for title in all_title:   #用循环打印所有电影名
        if "/" not in title.string:   #排除掉带有"/"的外文名
            print(title.string)


    
"""看懂html"""

"""1:基本结构"""
#<!DOCTYPE HTML>,文件类型
#<html> ，起始，闭合标签前加/
    #<body>< ，主体内容
        #<h1>这是一个标题</h1>
        #<p>这是一段文字这是一段文字这是一段文字</p>
    #</body>
#</html>

"""2：常用标题标签"""
#h1,h2数字代表标题的逻辑顺序
#p代表文本段落标签，br为一个完整p中使用的强制换行符，无需闭合标签
#p内可以添加类，更方便找寻同类段落如<p class="review>文字</p>">
#b标签闭合，代表加粗
#i标签闭合代表斜体
#u代表加下划线
#img代表加载图片，<img src= 路径 width="" height="">
#a代表加载链接，<a href=要转到的链接地址 target = "_blank"(意为要求跳转到新的空白网页)>把网址隐藏起来的名称</a>
#div,span都是容器标签，无具体含义。区别就是div独占一块，网页中一行只能有一个div元素
#ol代表有序列表，自动标数字
#<ol>
    #<li>文字内容</li>
    #<li>文字内容</li>
    #<li>文字内容</li>
#</ol>
#table代表制表
#<table border="1"> ,表格默认无边，border=1代表加边框
    #<thead> ，表格加粗部分，表头
        #<tr> ，table row即表格行，在tr里面的元素将在一条线上，并有自己的独立空间
            #<td>表头1</td>
            #<td>表头2</td>
        #</tr>
    #</thead>
    #<tbody>，表格具体内容
        #<tr>
            #<td>111</td>
            #<td>222</td>
        #</tr>
        #<tr>
            #<td>333</td>
            #<td>444</td>
        #</tr>
    #</tbody>
#</table>
"""实践常见标签"""