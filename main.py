import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        # ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="blue")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download complete!")
    except:
        finishLabel.configure(text="Youtube link is invalid", text_color="red")


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title('YouTube Downloader')

title= customtkinter.CTkLabel(app, text='Insert Youtube link: ')
title.pack(padx=10 , pady=10)

url_var= tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height= 40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

app.mainloop()

