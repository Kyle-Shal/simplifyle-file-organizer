import os
from tkinter import filedialog


class FolderOperations():
    def __init__(self):
        self.folderPath = ""
        self.fileNames = [""]

    def chooseFolder(self):
        self.folderPath = filedialog.askdirectory()
        self.fileNames = (os.listdir(self.folderPath))
        print ("this is the folder path:")

    
    def organizeByExtension(self,filelist): 
        try:
            path = self.folderPath
            for files in os.listdir(path):
                if(os.path.isdir(files) == False):
                    extension= files.split('.')[1]
                    moveInto = path+"/"+extension
                    if (os.path.exists(moveInto)):
                            if files.endswith(extension):
                                os.rename(path+"/"+files,moveInto+"/"+files)
                    else :
                            os.makedirs(moveInto)
                            os.rename(path+"/"+files,moveInto+"/"+files)
            for i in filelist:
                i.destroy()
        except:
            print("error")

    def getFolderPath(self):
        return self.folderPath

    def getFileNames(self):
        return self.fileNames

    
    