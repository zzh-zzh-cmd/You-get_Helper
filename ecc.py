import time
import os
def read2():
    with open("./tmp/tmp.txt") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list
d=[]
a=read2()
b=len(a)
for i in range(0,b):
    c=a[i]
    if "http" or "bilibili" in c:
        continue
    else:
        d.append(c)
        print(f"发现第{i+1}个url存在错误\n原文为{c}")
        time.sleep(1)
        
pd=len(d)
if pd==0:
    print("完成查错,未发现错误...")
    time.sleep(0.5)
else:
    e=[]
    for f in a:
        if f not in d:
            e.append(f)
    workpath=os.getcwd()
    g=len(e)
    if g==0:
        with open(f'{workpath}\\tmp\\tmp.txt', 'w',encoding="utf-8") as file:

                file.write(f'')
        print("额。。。全是错误的")
        input("回车以退出")
        os.system("taskkill /IM python.exe")


    else:
        for t in e: 
            with open(f'{workpath}\\tmp\\tmp.txt', 'w',encoding="utf-8") as file:

                file.write(f'{t}\n')
    print("错误已删除")