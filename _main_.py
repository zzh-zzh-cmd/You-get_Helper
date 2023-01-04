import time
import os

def read1():
    with open("./tmp/tmp.txt") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list[0]

def read2():
    with open("./tmp/tmp.txt") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list

def respond(cmd): 
    result = os.popen(cmd)
    res = result.buffer.read()
    return res
    
def taskmoniter():
    
    txt=respond("tasklist").splitlines(keepends=False)
    n=0
    for i in txt:
        if "python" in str(i):
            n+=1
    n1=n
    n=0
    while True:
        txt=respond("tasklist").splitlines(keepends=False)
        for i in txt:
            if "python" in str(i):
                n+=1
        cha=n1-n
        
        if cha==1:
            break
        else :
            n=0
            
            continue
    os.system("cls")    
    print("已获取")
    time.sleep(1)


def wait():
    time.sleep(1)
    
    while True:
        x=read2()

        if len(x)==0:
            continue
        else:
            break


def get():
    print("准备输入url\n等待中")
    os.system("start urlmonitor.py")
    wait()
    return read1()

def get1():
    print("准备输入url\n等待中")
    os.system("start urlmonitor.py")


print("欢迎使用you-get向导")
time.sleep(1)
a=1

if a==1:
    z="y"
    while z=="y":
        print("请选择版本\n1.命令行版本\n2.窗口版本")
        ch=int(input())
        if ch==2:
            os.system("GUI.py")
            break
    
        print("开始运行....")
        time.sleep(1)    
        print("请选择\n1.默认\n2.仅画质自定义\n3.仅会员身份自定义\n4.自定义\n5.批量并行下载（测试）")
        a=int(input())
        
        b1= "--format=dash-hdflv2_8k "
        b2= "--format=dash-hdflv2_4k "
        b3= "--format=dash-hdflv2 "
        b4= "--format=dash-hdflv "
        b5= "--format=dash-hdflv720p "
        c="you-get"
        d1=" -c"
        d2=" -i "
        d3=" -o"
        e1=" --no-caption "
        e2=" --playlist"
        f1=os.getcwd()+"/download"
        f2=" d:/cookies.sqlite"
        if a==1:
            z=get()
            aa=c+d1+f2+d3+f1+e1+z
            os.system(aa)
            z=input("是否继续 (y/n)")
        elif a==2:
            z=get()
            print("1.8k超高清")
            print("2.4k超清")
            print("3.1080p+")
            print("4.1080p")
            print("5.720p")
            f=int(input("请选择"))
            if f==1:
                o=c+d1+f2+d3+f1+e1+b1+z
                os.system(o)
            elif f==2:
                o=c+d1+f2+d3+f1+e1+b2+z
                os.system(o)
            elif f==3:
                o=c+d1+f2+d3+f1+e1+b3+z
                os.system(o)
            elif f==4:
                o=c+d1+f2+d3+f1+e1+b4+z
                os.system(o)
            elif f==5:
                o=c+d1+f2+d3+f1+e1+b5+z
                os.system(o)
            z=input("是否继续 (y/n)")
        elif a==3:
            z=get()
            print("1.使用会员")
            print("2.不使用会员")
            ac=int(input())
            if ac==1:
                ad=input("请输入cookies地址")
                o=c+d1+ad+d3+f1+e1+z
                os.system(o)
            elif ac==2:
                o=c+d3+f1+e1+z
                os.system(o)
            z=input("是否继续 (y/n)")
        elif a==4:
            z=get()
            print("1.使用会员")
            print("2.不使用会员")
            ac=int(input())
            if ac==1:
                ad=input("请输入cookies地址")
                print("1.仅查看信息")
                print("2.不查看信息")
                ae=int(input())
                if ae==1:
                    o=c+d1+ad+d2+z
                    os.system(o)
                else:
                    print("1.请输入下载文件夹地址(不含中文)")
                    af=input()
                    print("1.默认画质")
                    print("2.自定义")
                    ag=int(input())
                    if ag==1:
                        print("1.列表下载")
                        print("2.非列表下载")
                        ah=int(input())
                        if ah==1:
                            o=c+d1+ad+d3+af+e1+e2+z
                            os.system(o)
                        else:
                            o=c+d1+ad+d3+af+e1+z
                            os.system(o)
                    else:
                        print("1.8k超高清")
                        print("2.4k超清")
                        print("3.1080p+")
                        print("4.1080p")
                        print("5.720p")
                        f=int(input("请选择"))
                        if f==1:
                            o=c+d1+ad+d3+af+e1+b1+z
                            os.system(o)
                        elif f==2:
                            o=c+d1+ad+d3+af+e1+b2+z
                            os.system(o)
                        elif f==3:
                            o=c+d1+ad+d3+af+e1+b3+z
                            os.system(o)
                        elif f==4:
                            o=c+d1+ad+d3+af+e1+b4+z
                            os.system(o)
                        elif f==5:
                            o=c+d1+ad+d3+af+e1+b5+z
                            os.system(o)

            elif ac==2:
                print("1.仅查看信息")
                print("2.不查看信息")
                ae=int(input())
                if ae==1:
                    o=c+d2+z
                    os.system(o)
                else:
                    print("1.请输入下载文件夹地址(不含中文)")
                    af=input()
                    print("1.默认画质")
                    print("2.自定义")
                    ag=int(input())
                    if ag==1:
                        print("1.列表下载")
                        print("2.非列表下载")
                        ah=int(input())
                        if ah==1:
                            o=c+d3+af+e1+e2+z
                            os.system(o)
                        else:
                            o=c+d3+af+e1+z
                            os.system(o)
                    else:
                        print("1.8k超高清")
                        print("2.4k超清") 
                        print("3.1080p+")
                        print("4.1080p")
                        print("5.720p")
                        f=int(input("请选择"))
                        if f==1:
                            o=c+d3+af+e1+b1+z
                            os.system(o)
                        elif f==2:
                            o=c+d3+af+e1+b2+z
                            os.system(o)
                        elif f==3:
                            o=c+d3+af+e1+b3+z
                            os.system(o)
                        elif f==4:
                            o=c+d3+af+e1+b4+z
                            os.system(o)
                        elif f==5:
                            o=c+d3+af+e1+b5+z
                            os.system(o)
            z=input("是否继续 (y/n)")
        elif a==5:
            get1()
            time.sleep(2)
            taskmoniter()
            #input()
            os.system("ecc.py")
            workpath=os.getcwd()

            p=open(f'{workpath}\\tmp\\tmp.txt', encoding="utf-8")
            p1=p.readlines()
            n=len(p1)
            def pi(n,zt,h):
                a="start "
                c=".py"
                if zt==0:
                    for i in range(1,n+1):
                        i1=str(i)
                        ix="tmp\\"
                        o=a+ix+i1+c
                        os.system(o)
                elif zt==1:
                    g=n//h
                    for x in range(1,g+1):
                        e=1
                        for i in range(e,e+h-1):
                            i1=str(i)
                            o=a+i1+c
                            os.system(o)
                        i=e+h
                        i1=str(i)
                        o=i1+c
                        os.system(o)
                        e=e+h
                    for i in range(h*g,n+1):
                        i1=str(i)
                        o=a+i1+c
                        os.system(o)
            os.system("you-get.py")
            print("1.全部并行")
            print("2.自定义并行数")
            x=int(input())
            if x==1:
                zt=0
                h=0
            else:
                h=int(input("请输入并行数"))
                zt=1
            pi(n,zt,h)
            z=input("是否继续 (y/n)")
