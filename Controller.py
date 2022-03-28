import tkinter as tk
from Models.FolderOperations import FolderOperations

# Create an instance of FolderOperations
FO = FolderOperations()

# STARTUP VIEW
root = tk.Tk()
frame0 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame0.pack()
frame1 = tk.Frame(root,height=600,width=500,bg="#163dc9")
frame1.place(relheight=1,relwidth=1)
 
  
selectFolder = tk.Button(root,text="Select Folder",bg="#0095ff",relief=tk.GROOVE,width=20,command=FOps.chooseFolder)
selectFolder.place(x= 180, y=400)
selectOrganize = tk.Button(root,text="Organize",bg="#0095ff",relief=tk.GROOVE,width=20,command=FOps.organizeByExtension)
selectOrganize.place(x= 180, y=420)


root.mainloop()
