import tkinter as tk
#from Models import FolderOperations as FO
from tkinter import filedialog
import os
import random
from tracemalloc import start
# Create an instance of FolderOperations
# FOps = FO.FolderOperations


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# MODELS 
class FolderOperations():
    def chooseFolder():
        global folderName
        folderName = filedialog.askdirectory()
        fileNames = (os.listdir(folderName))
        print(folderName)
        print(fileNames)
        root.destroy()
        SecondView.nextView(fileNames,folderName)
        
    def organizeByExtension():
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
                        # if file.endswith(extension):
                            os.rename(path+"/"+file,moveInto+"/"+file)
                    else :
                        os.makedirs(moveInto)
                        os.rename(path+"/"+file,moveInto+"/"+file)
        except:
            print("error")

FOps = FolderOperations


# SECOND VIEW 
class SecondView ():
    def nextView(fileNames,folderName):
        global root2
        root2 = tk.Tk()
        frame2 = tk.Frame(root2,height=500,width=1000,bg="#343030")
        frame2.pack()
        line1 = tk.Canvas(root2,height=500,width=1000,bg="#343030")
        line1.create_line(700, 0, 700, 1000,width=3,fill="#808080")
        line1.place(x=0,y=0)
        i = 10
        j = 0
        for file in fileNames:
            label = tk.Label(line1,text=file,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
            label.place(x= 720, y=i)
            i = i + 20
            j = j +1
        totalFiles = "Total Files: " + str(j)
        dirDict = {}
        path = folderName
        for(path,dirs,files) in os.walk(path):
            for file in files :
                extension= file.split('.')[1]
                print(extension)
                #moveInto = path+"/"+extension
                if extension in dirDict.keys():
                    dirDict[extension] = dirDict[extension] + 1
                else:
                    dirDict.update({extension:1})
        print(dirDict)            
        percentageFile = 100 / j
        s = 0
        e = 0
        for ext in dirDict:
            print(dirDict.get(ext))
            percentage = percentageFile * dirDict.get(ext) 
            e = (percentage/100) * 360
            hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
            arc = line1.create_arc(200, 50, 380, 230,start=s,extent=e,fill=hexadecimal)
            s =s + e

       

        arc2 = line1.create_arc(220, 70, 360, 210,start=0,extent=359.99,fill="#343030")
        
        label = tk.Label(line1,text=totalFiles,fg="#00F0FF",bg="#343030",font=("Helvetica",15))
        label.place(x= 250, y=300)
        root2.mainloop()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# STARTUP VIEW
root = tk.Tk()
frame0 = tk.Frame(root,height=600,width=500,bg="#343030")
frame0.pack()
frame1 = tk.Frame(root,height=600,width=500,bg="#343030")
frame1.place(relheight=1,relwidth=1)
label = tk.Label(frame1,text="SimpliFyle",fg="#00F0FF",bg="#343030",font=("Helvetica",30))
label.place(x= 165, y=120) 
selectFolder = tk.Button(root,text="Select Folder",bg="#00F0FF",relief=tk.GROOVE,width=20,command=lambda: FOps.chooseFolder())
selectFolder.place(x= 180, y=400)
# selectOrganize = tk.Button(root,text="Organize",bg="#00F0FF",relief=tk.GROOVE,width=20,command=FOps.organizeByExtension)
# selectOrganize.place(x= 180, y=420)
root.mainloop()
