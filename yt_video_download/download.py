# import modules

from tkinter import *
from pytube import YouTube

# using root as Tk

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("download youtube video")

# heading label
Label(root, text='Youtube video downloader', font='arial 20 bold').pack()

link = StringVar()
Label(root,text='Paste link here', font='arial 15 bold').place(x=160, y=60)

link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# downloader function

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

# downloading button

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='light green', 
    padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()


