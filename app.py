
import tkinter as tk
# from PIL import Image
import os
from tkinter import filedialog
root = tk.Tk()

frame0 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame0.pack()
frame1 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame1.place(relheight=1,relwidth=1)
fileNames = ""
def chooseFolder() :
    folderName = filedialog.askdirectory()
    fileNames = (os.listdir(folderName))
    print(folderName)
    print(fileNames)   
    i=0.01
    for file in fileNames :
        print(file)
        label = tk.Label(frame1,text=file,bg="#163dc9")
        label.pack()
        i=i+1
    selectFolder.place_forget()
def Folder():
    print("working")
    
selectFolder = tk.Button(root,text="Select Folder",bg="#0095ff",relief=tk.GROOVE,width=20,command=chooseFolder)
selectFolder.place(x= 180, y=400)
Folder = tk.Button(root,text="Folder",bg="#0095ff",relief=tk.GROOVE,width=20,command=Folder)
Folder.place(x= 180, y=420)


# image = tk.PhotoImage(Image.open())
root.mainloop()