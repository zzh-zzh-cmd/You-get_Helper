from bs4 import BeautifulSoup
import requests,os
while True:
    url=input("请输入url")
    workpath=os.getcwd()
    req=requests.get(url)
    req.encoding = "utf-8"
    soup = BeautifulSoup(req.text,features="html.parser")
    with open(f'{workpath}\\tmp\\info.txt', 'w',encoding="utf-8") as file:
        file.write(soup.text)

    with open(".\\tmp\\info.txt", encoding="utf-8") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    txt=url_initial_list[0]
    txt=list(txt)[1:11]
    text=""
    for i in range(10):
        text=text+txt[i]
    text=text+"..."
    print(text)

# company_item = soup.find("title",class_="data-vue-meta")
# dd = company_item.text.strip()
# print(dd)
