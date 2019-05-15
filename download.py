from pytube import YouTube, Stream


#get video input
vid = input("Enter the video to be downloaded: ")

#create object for YouTube
yt = YouTube(vid)

ip = (int)(input("Download \n1.Audio \n2.Video"))

if ip == 1 :
    videos = yt.streams.filter(only_audio=True).all()

elif ip == 2 :
    videos = yt.streams.filter(subtype='mp4').all()

else :
    print("Enter a valid choice")
    exit()

s = 1

for v in videos :
    print(str(s) + " " + str(v))
    s += 1

quality =(int)(input("Enter quality of video: "))

vid = videos[quality-1]
vid.download("E:")
print("download completed",yt.title)