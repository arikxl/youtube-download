import tkinter
import customtkinter
from pytube import YouTube

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



app.mainloop()

