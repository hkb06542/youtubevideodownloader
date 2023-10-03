import _tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from pathlib import Path



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Youtube Video Downloader")
app.geometry("600x300")
app.grid_columnconfigure(0,weight=1)

#
link = str()
path = str(Path.home()/"Downloads")

def download(ytlink):
    
    try:
        #initialize https://www.youtube.com/watch?v=s5X2i3ohCg8&ab_channel=LukeStephens
        yt = YouTube(ytlink,on_progress_callback=on_progress) 
        print(yt.title)
        finishlabel.configure(text="Downloading...")
        toplabel.configure(text=yt.title)
        toplabel.update()
        stream = yt.streams.get_highest_resolution()
        
        finishlabel.configure(text="") 
        stream.download(path)
        
    except VideoUnavailable:
        print("youtube link is invalid !!")
        finishlabel.configure(text="video unavailbale")
    except:
            finishlabel.configure(text="youtube link is invalid")
    else:
        finishlabel.configure(text="Download complete !!!")       

def setLink():
    text = textbox.get(0.0,"end")
    if(len(text) >0):
        link = text
        print(link)
        download(link)

    else:
        print("please enter the text") 


#call back functio for onprogresss
def on_progress(stream,chunk,bytes_remaining):
     print(stream.filesize)
     print(bytes_remaining)
     total_size = stream.filesize
     remaing_bytes_from_total = total_size - bytes_remaining
     percentage_completed = remaing_bytes_from_total/total_size * 100
     print(f'stream.filesize: {stream.filesize} bytes remaining: {bytes_remaining} = {remaing_bytes_from_total} , percentage completed: {percentage_completed}')
     percentage_in_float = float(percentage_completed)/100
     print(f'Progress : {percentage_in_float}')
     progressbar.set(percentage_in_float)
     progressbar.update()
                    
        
toplabel = customtkinter.CTkLabel(master=app,text="Insert Youtube Link")
toplabel.grid(row=0,column=0,padx=0,pady=0)

textbox = customtkinter.CTkTextbox(master=app,border_color="white",height=25)
textbox.grid(row=1,column=0,padx=20,pady=20,sticky="nsew")

progressbar = customtkinter.CTkProgressBar(master=app)
progressbar.grid(row=2,column=0,padx=20,pady=20,sticky="ew")
progressbar.set(0)

finishlabel = customtkinter.CTkLabel(master=app,text="")
finishlabel.grid(row=3,column=0,padx=10,pady=10)

button1 = customtkinter.CTkButton(master=app,text="Download",command=setLink,width=150,)
button1.grid(row=4,column=0,padx=20,pady=20)


app.mainloop()