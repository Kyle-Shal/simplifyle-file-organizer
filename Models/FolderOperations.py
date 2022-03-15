import tkinter as tk
import os
from tkinter import filedialog
import shutil


class FolderOperations():
    def chooseFolder() :
        global folderName
        folderName = filedialog.askdirectory()
        fileNames = (os.listdir(folderName))
        print(folderName)
        print(fileNames)   

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
                        if file.endswith(extension):
                            shutil.move(file,moveInto)
                            print("working1")
                    else :
                        print("working2")
                        os.system('mkdir '+extension)
                        shutil.move(file,moveInto)
        except:
            print("error")
    
    