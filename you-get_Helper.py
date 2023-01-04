import time
import os
#os.system("说明.txt")

print("正在检测网络连接...")
a=os.system("ping -n 2 -w 100 www.baidu.com")
os.system("cls")
if a==0:
    print("网络已连接，准备检测环境...")
    time.sleep(1)
    os.system("_entrance_.py")
else:
    print("网络连接不存在\n1.仅离线配置\n2.退出配置网络")
    b=int(input())
    if b==1:
        os.system("_entrance_.py")
