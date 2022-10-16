from tkinter import *
from tkinter import messagebox
from pytube import YouTube

#Create window display
root = Tk()
root.title('YouTube Downloader')
root.geometry('600x300')
root.resizable(0,0)
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold italic').pack()

#Create link for download
link = StringVar()
Label(root, text =  'Paste the link here',  font = 'arial 15 italic').place(x=240, y=70)
link_enter = Entry(root, width = 58,textvariable = link).place(x = 32, y = 90)

#Create about botton
def about_tab():
    messagebox.showinfo("Hello", "This App was created by Laldinenga")
b1 = Button(root, text="About", command=about_tab, activeforeground="red", pady=1, padx=2)
b1.place(x=20, y=5)

#Create function to download link
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.filter(progressive=True).order_by("resolution").last()
    video.download(output_path = "/Users/valtea/downloads")
    Label(root, text='Download Completed', font='arial 12 ').place(x=240, y=190)
    messagebox.showinfo(title="Download Information",message="Your Video  has been downloaded. Go to /Users/valtea/downloads")
Button(root,text = 'DOWNLOAD', font = 'arial 18 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=230 ,y = 150)


root.mainloop()
