import tkinter as tk
# from PIL import Image
import os
from tkinter import filedialog
import shutil
root = tk.Tk()

frame0 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame0.pack()
frame1 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame1.place(relheight=1,relwidth=1)
fileNames = ""
def chooseFolder() :
    global folderName
    folderName = filedialog.askdirectory()
    fileNames = (os.listdir(folderName))
    print(folderName)
    print(fileNames)   
    i=0.01
    for file in fileNames :
        label = tk.Label(frame1,text=file,bg="#163dc9")
        label.pack()
    selectFolder.place_forget()

def organize():
    try: 
        path = folderName

        for(path,dirs,files) in os.walk(path):
            for file in files :
                extension= file.split('.')[1]
                print(extension)
                moveInto = path+"/"+extension
                print(path)
                print(moveInto)
                if os.path.exists(moveInto):
                    if file.endswith(extension):
                        shutil.move(file,moveInto)
                        print("working1")
                else :
                    print("working2")
                    os.system('mkdir '+extension)
                    shutil.move(file,moveInto)
    except:
        print("error")
    
    
selectFolder = tk.Button(root,text="Select Folder",bg="#0095ff",relief=tk.GROOVE,width=20,command=chooseFolder)
selectFolder.place(x= 180, y=400)
selectOrganize = tk.Button(root,text="Organize",bg="#0095ff",relief=tk.GROOVE,width=20,command=organize)
selectOrganize.place(x= 180, y=420)


# image = tk.PhotoImage(Image.open())
root.mainloop()
