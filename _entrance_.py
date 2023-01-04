import time,os,uuid,hashlib
mac = uuid.UUID(int=uuid.getnode()).hex[-12:].encode("UTF-8")
md5hash = hashlib.md5(mac)
mac = md5hash.hexdigest()

def install():
    os.system("pip install .\\whl\\urllib3-1.26.13-py2.py3-none-any.whl")
    os.system("pip install .\\whl\\charset_normalizer-2.1.1-py3-none-any.whl")
    os.system("pip install .\\whl\\certifi-2022.12.7-py3-none-any.whl")
    os.system("pip install .\\whl\\idna-3.4-py3-none-any.whl")
    os.system("pip install .\\whl\\requests-2.28.1-py3-none-any.whl")
    os.system("pip install .\\whl\\soupsieve-2.3.2.post1-py3-none-any.whl")
    os.system("pip install .\\whl\\beautifulsoup4-4.11.1-py3-none-any.whl")

def check():
    print("正在检查您是否已正确安装you-get.....")
    time.sleep(1)
    c=os.system("you-get")
    os.system("cls")
    
    if c==0:
        print("已检测到you-get...")
        time.sleep(1)
        print("正在检测ffmpeg...")
        d=os.system("where ffmpeg")
        if d==0:
            with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                file.write(mac)
            print("检测环境成功，开始加载主程序")
            os.system("_main_.py")
            return 0

        else:
            print("未检测到ffmpeg\n是否现在安装\n1.现在安装\n2.不安装，直接运行(不再提示)\n3.稍后自行安装")
            e=int(input())
            if e==1:
                #os.system("md d:\ffmpeg")
                #os.system("xcopy ffmpeg d:\ffmpeg /e /i")
                os.system("Untitled-1.bat")
                #os.system("setx path '%path%;d:\ffmpeg\bin'")
                os.system("cls")
                print("安装成功")
                time.sleep(1)
                return 1
            elif e==2:
                with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                    file.write(mac)
                print("检测环境成功，开始加载主程序")
                os.system("_main_.py")
            elif e==3:
                os.system("_main_.py")
    elif c==1:
        print("未检测到you-get\n1.在线安装\n2.离线安装")
        e1=int(input())
        if e1==1:
            os.system("pip install you-get")
            print("you-get安装成功")
            time.sleep(1)
            print("正在检测ffmpeg...")
            d=os.system("where ffmpeg")
            if d==0:
                with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                    file.write(mac)
                print("检测环境成功，开始加载主程序")
                os.system("_main_.py")
                return 0

            else:
                print("未检测到ffmpeg\n是否现在安装\n1.现在安装\n2.不安装，直接运行(不再提示)\n3.稍后自行安装")
                e=int(input())
                if e==1:
                    os.system("Untitled-1.bat")
                    print("安装成功")
                    time.sleep(1)
                    return 1
                elif e==2:
                    with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                        file.write(mac)
                    print("检测环境成功，开始加载主程序")
                    os.system("_main_.py")
                elif e==3:
                    os.system("_main_.py")

        elif e1==2:
            os.system("pip install .\\whl\\you_get.whl")
            print("you-get安装成功")
            time.sleep(1)
            print("正在检测ffmpeg...")
            d=os.system("where ffmpeg")
            if d==0:
                with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                    file.write(mac)
                print("检测环境成功，开始加载主程序")
                os.system("_main_.py")
                return 0

            else:
                print("未检测到ffmpeg\n是否现在安装\n1.现在安装\n2.不安装，直接运行(不再提示)\n3.稍后自行安装")
                e=int(input())
                if e==1:
                    os.system("xcopy .\ffmpeg d:\ffmpeg /e")
                    os.system("md d:/ffmpeg")
                    os.system("set path=%path%;d:\ffmpeg\bin")
                    os.system("cls")
                    print("安装成功")
                    time.sleep(1)
                    return 1
                elif e==2:
                    with open(f'{workpath}\\config.ini','w', encoding="utf-8") as file:
                        file.write(mac)
                    print("检测环境成功，开始加载主程序")
                    os.system("_main_.py")
                elif e==3:
                    os.system("_main_.py")




z=1

os.system("rd /s /q tmp")

while z==1:

    a =os.listdir()
    b = "config.ini"
    workpath = os.getcwd()
    print("正在检查运行环境，请稍候...")
    time.sleep(1)
    if b in a:
        with open("./config.ini",encoding="utf-8") as config_file:
            config = config_file.read()
        if config==mac:
            print("检测环境成功，开始加载主程序...")
            time.sleep(1)
            os.system("cls")
            
            z=0
            os.system("_main_.py")

        else:
            
            os.system("del config.ini")
            z=check()

    else:
        
        z=check()
