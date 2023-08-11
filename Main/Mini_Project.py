from tkinter import (Button, Canvas, PhotoImage, StringVar, Tk, ttk , filedialog, OptionMenu,Text)
from moviepy.editor import VideoFileClip
from pytube import YouTube
root = Tk()
root.geometry("800x600")
root.resizable(width=1024,height=768)  # type: ignore
root.title("YouTube Video Cliper")
bg = PhotoImage(file = "Z:\images\i.ppm")
bg2 = PhotoImage(file = "Z:\images\youtubevanced.png")
canvas1 = Canvas(root,width=1024,height=768)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0 , 0 , image = bg , anchor = "nw")
canvas1.create_image(0,-65,image = bg2 , anchor = "nw" )

l1 = canvas1.create_text((400,50),text = "Youtube Video Cliper", font =('Helvetica',30,'bold','underline'),fill="red")
##enter link
link = StringVar()

l2 = canvas1.create_text((400,115), text = 'Paste Link Here:', font =('arial',20,'bold'),fill="black")
link_enter = ttk.Entry(root, width = 80,textvariable = link).place(x = 32, y = 125)


'''stream_list = Text(root, width= 100, height=30,).place(x=32, y=400)
c =YouTube(str(link.get()))
if link.get() ==" ":
    stream_list.insert(c.streams.all()) #type:ignore'''

#path where to save the video
folder=None
def get_save_path():
   global folder
   yt =YouTube(str(link.get()))
   folder = filedialog.asksaveasfilename(initialdir="/",initialfile=yt.title,title="save the file",defaultextension=".mp4")

progress = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress.place(x=200 , y=375)

##for clipping video
l3 = canvas1.create_text((100,215), text='Start', font=('arial',20,'bold'),fill='red')
Start = StringVar()
start_time = ttk.Entry(root, width=10,textvariable=Start).place(x=150 , y=200)
l4 = canvas1.create_text((550,215), text='End', font =('arial',20,'bold'),fill='red')
End = StringVar()
end_time = ttk.Entry(root, width=10 ,textvariable=End).place(x=600, y=200)

l5 = canvas1.create_text((325,215), text='Resolution', font=('arial',20,'bold'), fill='red')
Resolution = StringVar()
Resolution.set("----")
Res = OptionMenu(root, Resolution, "240p", "360p", "480p", "720p", "1080p").place(x=400, y=205)

def clip_video():
    import time
    for i in range(10,110,10): 
        progress['value'] = i
        root.update_idletasks()
        time.sleep(1)
    
    if (progress['value']==100):
        l5 = canvas1.create_text((400,400), text = 'DOWNLOADED', font = ('arial',15,'bold'), fill ='red')
    url =YouTube(str(link.get()))
    print(url.streams.all())
    stream =url.streams.filter(progressive=True)
    #stream =url.streams.get_by_itag(22)
    stream = url.streams.get_by_resolution(Resolution.get())
    clip = VideoFileClip(stream.download()) # type:ignore
    clip = clip.subclip(Start.get(),End.get())
    clip.write_videofile(filename=folder , codec='libx264' , fps=30 , audio=True,audio_codec="aac")
Download = Button(root,text = 'DOWNLOAD', font = ('arial',15,'bold') ,background = "blue", padx = 10, command =lambda: [get_save_path(),clip_video()],pady=3).place(x=340 ,y = 240)
#for downloading whole video
def Downloader():
    import time
    for i in range(10,110,10): 
        progress['value'] = i
        time.sleep(1)
        root.update_idletasks()
    
    if (progress['value']==100):
        l5 = canvas1.create_text((400,400), text = 'DOWNLOADED', font = ('arial',15,'bold'), fill ='red')
    
    url =YouTube(str(link.get()))
    print(url.streams.all() )
    stream =url.streams.filter(progressive=True)
    #stream =url.streams.get_by_itag(22)
    stream = url.streams.get_by_resolution(Resolution.get())
    stream.download(filename=folder) # type:ignore
bton_for_whole_video = Button(root,text="DOWNLOAD\nFULL VIDEO",font=('arial',15,'bold'),bg="red",padx=10,command=lambda:[get_save_path(),Downloader()]).place(x=340,y=280)
'''# For preview of the video:
def preview():
    url = str(link.get())
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url) #type:ignore
    media.play() #type:ignore
pre = Button(root,text="PREVIEW",font=('arial',15,'bold'),bg="red",padx=20,command=preview).place(x=340,y=330)'''

root.mainloop()