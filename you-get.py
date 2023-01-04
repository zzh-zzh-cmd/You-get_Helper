import os,pyperclip,time


    
b1= "--format=dash-hdflv2_8k "
b2= "--format=dash-hdflv2_4k "
b3= "--format=dash-hdflv2 "
b4= "--format=dash-hdflv "
b5= "--format=dash-hdflv720p "
b6= "--format=dash-hdflv480p "
b7= "--format=dash-hdflv360p "
def you_get(url,i,hz,dz,zt):
    workpath = os.getcwd()
    workpath1 = workpath.replace('\\','\\\\')
    dz1=workpath1+"\\download"
    if zt==1:
        with open(f'{workpath}\\tmp\{i}.py','w', encoding="utf-8") as file:
                file.write('import os\n')
                if hz=="":
                    file.write(f'os.system("you-get -c D:\cookies.sqlite -o {dz1} --no-caption {url}")\n')
                else:
                    file.write(f'os.system("you-get -c D:\cookies.sqlite -o {dz1} {hz} --no-caption {url}")\n')
                file.write('workpath = os.getcwd()\n')
                file.write(f'os.remove(os.path.join(workpath,"{i}.py"))')
    elif zt==2:
        with open(f'{workpath}\\tmp\{i}.py','w', encoding="utf-8") as file:
                file.write('import os\n')
                if hz=="":
                    file.write(f'os.system("you-get -c D:\cookies.sqlite -o {dz1} --no-caption {url}")\n')
                else:
                    file.write(f'os.system("you-get -c D:\cookies.sqlite -o {dz1} {hz} --no-caption {url}")\n')
                file.write('workpath = os.getcwd()\n')
                file.write(f'os.remove(os.path.join(workpath,"{i}.py"))')
    #origin = os.path.join(os.getcwd(),f'tmp\{i}.txt')
    #current = os.path.join(os.getcwd(),f'tmp\{i}.py')
    #os.rename(origin, current)
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
    
def read2():
    with open("./tmp/tmp.txt") as url_file:
        urls = url_file.read()
        url_initial_list = urls.splitlines(keepends=False)
    return url_initial_list


print("设置下载地址：")
print("1.默认")
print("2.自定义")
zt=int(input())
dz=0
if zt==2:
    dz=input()
workpath=os.getcwd()
p=open(f'{workpath}\\tmp\\tmp.txt', encoding="utf-8")
p1=p.readlines()
n2=len(p1)
a=[]
print("0.默认")
print("1.8k超高清")
print("2.4k超清")
print("3.1080p+")
print("4.1080p")
print("5.720p")
print("6.480p")
for i in range(1,n2+1):
    print("请选择第",i,"个视频的画质")
    n1=int(input())
    a.append(choice(n1))


for i1 in range(0,n2):
    hz=a[i1]
    url_list = []
    with open("./tmp/tmp.txt") as url_file:
        urls = url_file.read()
    url_initial_list = urls.splitlines(keepends=False)
    for i in url_initial_list:
        url = i.replace("&",r"\"&\"")
        url_list.append(url)
n = int(len(url_list))

for i in range(n):
    url = url_list[i]
    you_get(url,i+1,hz,dz,zt)

# workpath = os.getcwd()
# file_list = os.listdir(workpath)
# for i in file_list:
#     while i.find("download") != -1:
#         pass
#     os.remove(os.path.join(workpath,i))



