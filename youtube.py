from tkinter import *
from pytube import YouTube

def downloader():
    yt = YouTube(e1_value.get())
    print('Downloading {}....'.format(yt.title))
    stream = yt.streams.first()
    stream.download()

window = Tk()

l1 = Label(window, text='YouTube Downloader')
l1.grid(row=0, column=1)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=1,column=0)

b1 = Button(window, text='Download', command=downloader)
b1.grid(row=1,column=1)

window.mainloop()
