import requests
import re
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}
response = requests.get("https://www.baidu.com/index.php?tn=68018901_58_oem_dg",headers = headers)
trendings = re.findall('<span class="title-content-title">(.*?)</span>',response.text)
for trending in trendings:
    print(trending)
    print("*"*50)