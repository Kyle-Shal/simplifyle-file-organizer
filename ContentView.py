from mimetypes import init
import tkinter as tk
import random
import os

from Controller import SimpliFyleController

class StartupView():
    def __init__(self):
        self.window = tk.Tk()
        # self.window.state('zoomed')
        self.controller = SimpliFyleController()
        self.show
        # self.window.destroy() #Take the destroy outside of this
        # self.secondView = SecondView
        # self.secondView.show(self.controller.getFileNames,self.controller.getFolderPath)

    def show(self):
        frame0 = tk.Frame(self.window,height=500,width=1000,bg="#343030")
        frame0.pack(expand=1, fill=tk.BOTH)
        label = tk.Label(frame0,text="SimpliFyle",fg="#00F0FF",bg="#343030",font=("Helvetica",30))
        label.place(relx=0.42, rely=0.4) 

        selectFolderButton = tk.Button(self.window,text="Select Folder",bg="#00F0FF",relief=tk.GROOVE,width=20,command=lambda: self.controller.chooseFolder())
        selectFolderButton.place(relx= 0.44, rely=0.55)
        self.window.mainloop() 



# ORGANIZE VIEW 
# class SecondView():
#     def __init__(self, fileNames, folderPath):
#         self.folderPath = folderPath
#         self.fileNames = fileNames
#         self.window = tk.Tk()
#         self.show

#     def show(self):
#         frame2 = tk.Frame(self.window,height=500,width=1000,bg="#343030")
#         frame2.pack()
#         canvas1 = tk.Canvas(self.window,height=500,width=1000,bg="#343030")
#         canvas1.create_line(700, 0, 700, 500,width=3,fill="#808080")
#         canvas1.place(x=0,y=0)
#         i = 10
#         j = 0
#         fileList = []
#         arclist = []
#         boxlist = []
#         for file in self.fileNames:
#             label1 = tk.Label(canvas1,text=file,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
#             label1.place(x= 710, y=i)
#             fileList.append(label1)
#             i = i + 20
#             j = j + 1
#         totalFiles = "Total Files: " + str(j)
#         dirDict = {}
#         path = self.folderPath
#         for(path,dirs,files) in os.walk(path):
#             for file in files :
#                 extension= file.split('.')[1]
#                 if extension in dirDict.keys():
#                     dirDict[extension] = dirDict[extension] + 1
#                 else:
#                     dirDict.update({extension:1})          
#         percentageFile = 100 / j
#         s = 0
#         e = 0
#         top_x = 50
#         top_y = 300
#         bottom_x = 61
#         bottom_y = 311            
#         for ext in dirDict:
#             percentage = percentageFile * dirDict.get(ext) 
#             e = (percentage/100) * 360
#             hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
#             arc = canvas1.create_arc(200, 50, 380, 230,start=s,extent=e,fill=hexadecimal,tag="arc")
#             arclist.append(arc)
#             box = canvas1.create_rectangle(top_x,top_y,bottom_x,bottom_y,width=0,fill=hexadecimal)
#             boxlist.append(box)
#             label = tk.Label(canvas1,text=ext,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
#             label.place(x= bottom_x + 10, y=top_y-7)
#             s = s + e
#             top_y = top_y + 20
#             bottom_y = bottom_y + 20
#             if( bottom_y > 400):
#                 top_x = top_x + 60
#                 top_y = 300
#                 bottom_x = bottom_x + 60
#                 bottom_y = 311
#         arc2 = canvas1.create_oval(220, 70, 360, 210,fill="#343030")
#         label = tk.Label(canvas1,text=totalFiles,fg="#00F0FF",bg="#343030",font=("Helvetica",15))
#         label.place(x= 45, y=420)
#         selectOrganize = tk.Button(canvas1,text="Organize",bg="#00F0FF",relief=tk.GROOVE,command=lambda :self.controller.organizeByExtension(fileList))
#         selectOrganize.place(x= 200, y=250,width=180)
#         self.window.mainloop()

if __name__ == "__main__":
    app =  StartupView()
    app.show()
