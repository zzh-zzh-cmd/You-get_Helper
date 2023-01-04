md C:\ffmpeg
xcopy ffmpeg C:\ffmpeg /e /i
xcopy cookies.sqlite D:\
setx path "C:\ffmpeg\bin;%path%"
#taskkill /F /im python.exe
#start _entrance_.py