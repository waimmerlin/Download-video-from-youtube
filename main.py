import pytube
video_url = input('Input youtube video link: ') #get link
try:
    yt = pytube.YouTube(video_url)  #to make the code more readable
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() #request link
    video.download()  # download file
    print('Video download successfully')#ssuccessfully
except:
    print('Somthing went wrong')#call error