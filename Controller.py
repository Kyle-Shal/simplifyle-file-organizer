import os
from FolderOperationsModel import FolderOperations


class SimpliFyleController():
    def __init__(self):
        self.model = FolderOperations() #create an instance of the model
        # self.folderName = self.StartupView.folder
        # self.fileNames = [""]
        

    def chooseFolder(self):
        print("choosing folder")
        self.model.chooseFolder()
        print(os.listdir(self.getFolderPath()))

    def organizeByExtension(self):
        self.model.organizeByExtension()

    def getFolderPath(self):
        return self.model.folderPath

    def getFileNames(self):
        return self.model.fileNames

