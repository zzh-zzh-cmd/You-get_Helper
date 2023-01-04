from tkinter   import *
from threading import Thread
from bs4       import BeautifulSoup
import time,os,requests,ctypes

def screen():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(1)
    return screensize

#视频信息查看
def info(url):
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
    txt=list(txt)[1:31]
    text=""
    for i in range(30):
        text=text+txt[i]
    text=text+"..."
    return text

#GUI绘制
root = Tk()
root.title('You-get GUI Version(alpha)')
_screen=screen()
if _screen<=1080:
    _screen+=300
elif _screen>=2000:
    _screen=_screen*0.8

screen_size=_screen//2+50
root.geometry(f'{screen_size}x{screen_size}')
loadimage = PhotoImage(file="button.png")
s=screen_size
workpath=os.getcwd()

l1=Label(root,text='You-get GUI Version').place(x=s*190//500,y=s*5//500)
l2=Label(root,text='*请输入数字，不输入即为默认').place(x=s*10//500,y=70*s//500)
l3=Label(root,text='身份').place(x=50*s//500,y=130*s//500)
l4=Label(root,text='下载地址').place(x=220*s//500,y=130*s//500)
l5=Label(root,text='列表下载').place(x=390*s//500,y=130*s//500)
l7=Label(root,text='1.会员（默认）').place(x=5*s//500,y=170*s//500)
l8=Label(root,text='1.you-get\\download（默认）').place(x=170*s//500,y=170*s//500)
l9=Label(root,text='1.禁用（默认）').place(x=355*s//500,y=170*s//500)
l10=Label(root,text='2.非会员').place(x=5*s//500,y=190*s//500)
l11=Label(root,text='2.键入完整路径（例：D:\\video）').place(x=170*s//500,y=190*s//500)
l12=Label(root,text='2.启用').place(x=355*s//500,y=190*s//500)
l13=Label(root,text='上次：')
l13.place(x=5*s//500,y=210*s//500)
l14=Label(root,text='上次：')
l14.place(x=170*s//500,y=210*s//500)
l15=Label(root,text='上次：')
l15.place(x=355*s//500,y=210*s//500)
l16=Label(root,text='画质').place(x=50*s//500,y=250*s//500)
l17=Label(root,text='0.最高画质（默认）1.8k超高清  2.4k超清  3.1080p+  4.1080p  5.720p').place(x=10*s//550+1,y=340*s//500)
l18=Label(root,text='视频链接内容：')
l19=Label(root,text='*按下<获取视频链接>按钮后按照提示获取').place(x=s*10//500,y=320*s//500)
l18.place(x=s*10//500,y=300*s//500)
l20=Label(root,text='上次：')
l20.place(x=200*s//500,y=275*s//500)

#输入框
v1 = StringVar()
e1 = Entry(root,textvariable=v1)
e1.place(x=10*s//500,y=150*s//500)

v2 = StringVar()
e2 = Entry(root,textvariable=v2)
e2.place(x=180*s//500,y=150*s//500)

v3 = StringVar()
e3 = Entry(root,textvariable=v3)
e3.place(x=350*s//500,y=150*s//500)

v4 = StringVar()
e4 = Entry(root,textvariable=v4)
e4.place(x=10*s//500,y=275*s//500)

#自动填充示例
# v2.set('D:\\')
# e2.configure(textvariable=v2)


def choice1(n1):
        if n1==1:
            return "8k超高清"
        elif n1==0:
            return "最高画质"
        elif n1==2:
            return "4k超清"
        elif n1==3:
            return "1080p+"
        elif n1==4:
            return "1080p"
        elif n1==5:
            return "720p"

def choice_try(n1):
        if n1==1:
            return "8k超高清  "
        elif n1==0:
            return "最高画质  "
        elif n1==2:
            return "4k超清   "
        elif n1==3:
            return "1080p+ "
        elif n1==4:
            return "1080p  "
        elif n1==5:
            return "720p  "

def fetch(a,b):
    if a==1:
        if b=="1" or b=="\n":
            return "会员"
        elif b=="2":
            return "非会员"
    elif a==2:
        if b=="\n":
            return "默认"
        else:
            return b
    elif a==3:
        if b=="" or b=="1":
            return "禁用"
        elif b=="2":
            return "启用"
    elif a==4:
        if b=="":
            return "默认"
        else:
            return choice1(eval(b))

def fetch_try(a,b):
    if a==1:
        if b=="1" or b=="\n":
            return "会员"
        elif b=="2":
            return "非会员"
    elif a==2:
        if b=="\n":
            return "默认"
        else:
            return b
    elif a==3:
        if b=="" or b=="1":
            return "禁用"
        elif b=="2":
            return "启用"
    elif a==4:
        if b=="":
            return "默认"
        else:
            return choice_try(eval(b))
#read函数
def read(n):
    n=n-1
    with open("./tmp/config_.txt") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list[n]

def read1():
    with open(".\\tmp\\tmp.txt", encoding="utf-8") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list[0]


def read2():
    with open(".\\tmp\\tmp.txt", encoding="utf-8") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list


#后台检测与等待函数

#获取返回值
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
def wait():
    time.sleep(1)
    taskmoniter()
    x=read2()
    if len(x)==1:
        url=read1()
        inf=info(url)
        l18.configure(text=f'视频连接地址：{inf}')
    elif len(x)>=2:
        l18.configure(text='视频连接地址：多个（建议批量下载）')


#下载地址获取
def open1():
    x=v2.get()
    if x=="":
        add=".\\download"
    else:
        add=x.replace("\\","\\\\")
    a="start "+add
    os.system(a)

#链接自动获取
def hq():
    os.system("start urlmonitor.py")
    wait()
    # url=read1()
    # l18.configure(text=f'视频连接地址：{url}')

def write(a):
    with open(f'{workpath}\\tmp\\command_tmp.txt','w', encoding="utf-8") as file:
        file.write(a)

#命令运行函数
def run(a):
    workpath = os.getcwd()
    with open(f'{workpath}\\tmp\\command_tmp.py','w', encoding="utf-8") as file:
                file.write('import os\n')
                file.write(f"os.system('{a}')\n")
                file.write('workpath = os.getcwd()+"\\\\tmp"\n')
                file.write(f'os.remove(os.path.join(workpath,"command_tmp.py"))')
    os.system(f"start {workpath}\\tmp\\command_tmp.py")


def apply():
    v1.set(read(1))
    v2.set(read(2))
    v3.set(read(3))
    v4.set(read(4))
    e1.configure(textvariable=v1)
    e2.configure(textvariable=v2)
    e3.configure(textvariable=v3)
    e4.configure(textvariable=v4)
    
#读取上次
def default():
    v1=read(1)
    v2=read(2)
    v3=read(3)
    v4=read(4)
    l13.configure(text=f"上次：{fetch(1,v1)}")
    l14.configure(text=f"上次：{fetch(2,v2)}")
    l15.configure(text=f"上次：{fetch(3,v3)}")
    l20.configure(text=f"上次：{fetch(4,v4)}")

def air():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
    
#主函数
def main():
    b1= " --format=dash-hdflv2_8k"
    b2= " --format=dash-hdflv2_4k"
    b3= " --format=dash-hdflv2"
    b4= " --format=dash-flv"
    b5= " --format=dash-flv720p"
    sf=v1.get()
    add=v2.get()
    ls=v3.get()
    hz=v4.get()
    b=[]
    b.append(sf)
    b.append(add)
    b.append(ls)
    b.append(hz)
    workpath=os.getcwd()
    with open(f'{workpath}\\tmp\\config_.txt','w', encoding="utf-8") as file:
            file.write("")
    for i in b:
        with open(f'{workpath}\\tmp\\config_.txt','a+', encoding="utf-8") as file:
            file.write(f"{i}\n")
    a=[]
    workpath=os.getcwd()
    workpath=workpath+"\\download"

    def choice(n1):
        if n1==1:
            return b1
        elif n1==2:
            return b2
        elif n1==3:
            return b3
        elif n1==4:
            return b4
        elif n1==5:
            return b5
    
    if sf=="" or sf=="1":
        a.append("-c ")
        a.append("d:\\cookies.sqlite ")
    else:
        a.append("")
        a.append("")
    if add==""or add=="1":
        a.append("-o ")
        a.append(workpath)
    else:
        a.append("-o ")
        a.append(add)
    if ls==""or ls=="1":
        a.append("")
    else:
        a.append(" --playlist")
    if hz=="" or eval(hz)==0:
        a.append("")
    else:
        hz=eval(hz)
        a.append(choice(hz))
    url=read1()
    b="you-get "
    for i in a :
        b=b+i
    b=b+" --no-caption "+url
    run(b)

#批量下载
def pl():
    def read2():
        with open(".\\tmp\\tmp.txt", encoding="utf-8") as url_file:
            urls = url_file.read()
            url_initial_list = urls.splitlines(keepends=False)
        return url_initial_list 
    
    b1= " --format=dash-hdflv2_8k"
    b2= " --format=dash-hdflv2_4k"
    b3= " --format=dash-hdflv2"
    b4= " --format=dash-flv"
    b5= " --format=dash-flv720p"
    b6= " --format=dash-flv480p"
    b7= " --format=dash-flv360p"
    workpath=os.getcwd()
    
    #字典初始化
    global _hz,_dz,_sf
    _hz={}
    _dz={}
    _sf={}
    x=len(read2())
    for i in range (x):
        _hz[i]=0
        _dz[i]=0
        _sf[i]=0

    def choice(n1):
        if n1==1:
            return b1
        elif n1==0:
            return ""
        elif n1==2:
            return b2
        elif n1==3:
            return b3
        elif n1==4:
            return b4
        elif n1==5:
            return b5
        elif n1==6:
            return b6
        elif n1==7:
            return b7

    def screen():
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(1)
        return screensize

    #read函数
    def read3(n):
        with open("./tmp/tmp.txt") as url_file:
            urls = url_file.read()
            url_initial_list = urls.splitlines(keepends=False)
        return url_initial_list[n]

    def default_pl():
        v2=read(2)
        v3=read(3)
        v4=read(4)
        l13.configure(text=f"上次：{fetch(1,v1)}")
        l14.configure(text=f"上次：{fetch(2,v2)}")
        l15.configure(text=f"上次：{fetch(3,v3)}")
        l20.configure(text=f"上次：{fetch(4,v4)}")

    def apply_pl():
        v1.set(read(1))
        v2.set(read(2))
        v3.set(read(3))
        v4.set(read(4))
        e1.configure(textvariable=v1)
        e2.configure(textvariable=v2)
        e3.configure(textvariable=v3)
        e4.configure(textvariable=v4)


    def conf():
        x=len(read2())
        xh=int(e24.get())
        hz=e21.get()
        dz=e22.get()
        sf=e23.get()
        if xh==0:
            if hz!="":
                for xh in range(x):
                    _hz[xh]=int(hz)
                    Label(branch,text=f"画质：{fetch_try(4,hz)}",background="Grey").place(x=140*s//500,y=s*95//500+50*(xh))
            if dz!="":
                for xh in range(x):
                    _dz[xh]=dz
                    Label(branch,text=f"下载地址：{fetch(2,dz)}",background="Grey").place(x=280*s//500,y=s*95//500+50*(xh))
            if sf!="":
                for xh in range(x):
                    _sf[xh]=int(sf)
                    Label(branch,text=f"会员：{fetch(1,sf)}",background="Grey").place(x=10*s//500,y=s*95//500+50*(xh))
            
        else:    
            if hz!="":
                _hz[xh-1]=int(hz)
                Label(branch,text=f"画质：{fetch_try(4,hz)}",background="Grey").place(x=140*s//500,y=s*95//500+50*(xh-1))
            if dz!="":
                _dz[xh-1]=dz
                Label(branch,text=f"下载地址：{fetch(2,dz)}",background="Grey").place(x=280*s//500,y=s*95//500+50*(xh-1))
            if sf!="":
                _sf[xh-1]=int(sf)
                Label(branch,text=f"会员：{fetch(1,sf)}",background="Grey").place(x=10*s//500,y=s*95//500+50*(xh-1))
    
    
    
    def download():
        workpath = os.getcwd()
        workpath1 = workpath.replace('\\','\\\\')
        global workpath2
        workpath2 = workpath1+"\\tmp\\"
        x=len(read2())
        for i in range(x):
            hz=_hz[i]
            dz=_dz[i]
            sf=_sf[i]
            url=read3(i)
            hz=choice(hz)
            if sf==0:
                sf=" -c D:\\cookies.sqlite"
            else:
                sf=""
            if dz==0:
                dz=workpath1+"\\download"
            else:
                dz=dz.replace('\\','\\\\')
            with open(f'{workpath}\\tmp\\{i}.py','w', encoding="utf-8") as file:
                file.write('import os\n')
                file.write(f'os.system("you-get{sf} -o {dz}{hz} --no-caption {url}")\n')
        for i in range(x):
            i1=str(i)
            os.system(f"start {workpath2}{i1}.py")
                



    #GUI绘制
    _screen=screen()
    if _screen<=1080:
        _screen+=300
    screen_size=_screen//2+50
    branch = Tk()
    branch.title('You-get GUI Version(批量下载)')
    branch.geometry(f'{screen_size}x{screen_size}')
    s=screen_size
    l1=Label(branch,text='批量下载模式').place(x=s*210//500,y=s*5//500)
    l2=Label(branch,text='读取到的链接如下：').place(x=s*10//500,y=s*50//500)
    Label(branch,text='（将查询输入的序号对应的视频，需等待一段时间）').place(x=5*s//500,y=380*s//500+1)
    Button(branch,text='读取上一次配置',width=12,command=default_pl).place(x=10*s//500,y=25*s//500+1)
    #l3=Label(branch,text='*仅限全局画质').place(x=s*210//500,y=s*25//500)
    Button(branch,text='加载上一次配置',width=12,command=apply_pl).place(x=400*s//500,y=25*s//500+1)
    Button(branch,text='修改配置',width=12,command=conf).place(x=400*s//500,y=400*s//500+1)
    Button(branch,text='下载',width=12,command=download).place(x=200*s//500,y=450*s//500+1)
    Button(branch,text='查询视频信息',width=12,command=download).place(x=10*s//500,y=360*s//500+1)
    
    #链接展示
    x=read2()
    x1=len(x)
    for i in range(0,x1):
        nr=read3(i)
        inf=info(nr)
        inf=f'第{i+1}个：'+inf
        Label(branch,text=inf).place(x=10*s//500,y=s*80//500+50*i)
        Label(branch,text="画质：").place(x=140*s//500,y=s*95//500+50*i)
        Label(branch,text="会员：").place(x=10*s//500,y=s*95//500+50*i)
        Label(branch,text="下载地址：").place(x=280*s//500,y=s*95//500+50*i)
    
    #配置选项
    
    l24=Label(branch,text='序号：').place(x=s*5//500,y=s*400//500+1)
    v24 = StringVar()
    e24 = Entry(branch,textvariable=v24,width=10)
    e24.place(x=35*s//500,y=s*400//500+1)
    
    l21=Label(branch,text='画质：').place(x=s*90//500,y=s*400//500+1)
    v21 = StringVar()
    e21 = Entry(branch,textvariable=v21,width=10)
    e21.place(x=120*s//500,y=s*400//500+1)

    l22=Label(branch,text='下载地址：').place(x=s*180//500,y=s*400//500+1)
    v22 = StringVar()
    e22 = Entry(branch,textvariable=v22,width=10)
    e22.place(x=230*s//500,y=s*400//500+1)

    l23=Label(branch,text='身份：').place(x=s*280//500,y=s*400//500+1)
    v23 = StringVar()
    e23 = Entry(branch,textvariable=v23,width=10)
    e23.place(x=320*s//500,y=s*400//500+1)
    
    Label(branch,text=f"共选择了{x1}个视频").place(x=s*100//500,y=s*50//500)
    Label(branch,text="*输入样例见前一窗口，序号“0”为全选").place(x=s*5//500,y=s*450//500)


        









        
#Button(root,text='查看视频画质信息',width=13,command=read).place(x=400*s//500-10,y=300*s//400+1)
Button(root,text='读取上一次配置',width=12,command=default).place(x=10*s//500,y=25*s//500+1)
Button(root,text='清空输入内容',width=10,command=air).place(x=400*s//500,y=25*s//500+1)
Button(root,text='批量下载',width=10,command=pl).place(x=10*s//500,y=350*s//400+1)
Button(root,text='下载',width=10,command=main).place(x=200*s//500,y=350*s//400+1)
Button(root,text='获取视频链接',width=10,command=hq).place(x=200*s//500,y=300*s//400+1)
Button(root,text='加载上一次配置',width=12,command=apply).place(x=200*s//500,y=25*s//500+1)
Button(root,text='打开下载文件夹',width=12,command=open1).place(x=400*s//500-10,y=350*s//400+1)
#default()
mainloop()
    

