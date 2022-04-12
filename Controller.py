import tkinter as tk

from tkinter import filedialog
import os
import random




#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# MODELS 
class FolderOperations():
    def chooseFolder():
        global folderName
        folderName = filedialog.askdirectory()
        fileNames = (os.listdir(folderName))
        root.destroy()
        SecondView.nextView(fileNames,folderName)
        
    def organizeByExtension(filelist):
        try:
            
            path = folderName
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
        except:
            print("error")

    def organizeByAcademic(courses,deliverables):
        try:
            path = folderName
            
            for subject in courses:
                            for things in deliverables:
                                for files in os.listdir(folderName):
                                    if(os.path.isdir(files) == False):
                                        if subject in files and things in files :
                                            moveInto = path+"/"+subject+"/"+things
                                            if (os.path.exists(moveInto)):
                                                os.rename(path+"/"+files,moveInto+"/"+files)
                                            else :
                                                os.makedirs(moveInto)
                                                os.rename(path+"/"+files,moveInto+"/"+files)
        except:
            print("error")


FOps = FolderOperations


# SECOND VIEW 
class SecondView ():
    subjects = []
    courses = []
    deliverables = []
    assignments = []
    def showAcademic(frame3,frame5):
        frame3.tkraise()
        frame5.tkraise()
    def showExtension(frame2,frame4):
        frame2.tkraise()
        frame4.tkraise()
    def coursess(canvas1,course):
            string = course.get()
            if string.strip():
                SecondView.courses.append(string)
            Coursess = list(dict.fromkeys(SecondView.courses))
            SecondView.subjects = Coursess
            i = 75
            for names in Coursess:
                label3 = tk.Label(canvas1,text=names,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
                label3.place(x= 0, y=i)
                
                # fileList.append(label3)
                i = i + 20
    def deliverabless(canvas1,deliverable):
            string = deliverable.get()
            if string.strip():
                SecondView.deliverables.append(string)
            i = 75
            Deliverabless = list(dict.fromkeys(SecondView.deliverables))
            SecondView.assignments = Deliverabless
            for names in Deliverabless:
                label3 = tk.Label(canvas1,text=names,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
                label3.place(x= 140, y=i)
                
                # fileList.append(label3)
                i = i + 20
    def nextView(fileNames,folderName):
        
        root2 = tk.Tk()

        frame2 = tk.Frame(root2,height=500,width=1000,bg="#343030")
        frame2.pack()
        canvas1 = tk.Canvas(frame2,height=500,width=1000,bg="#343030")
        canvas1.create_line(700, 0, 700, 500,width=3,fill="#808080")
        canvas1.place(x=0,y=0)
        frame4 = tk.Frame(root2,height=35,bg="#343030")
        frame4.place(x= 200, y=245,width=180)
        frame5 = tk.Frame(root2,height=35,bg="#343030")
        frame5.place(x= 200, y=245,width=180)
        frame3 = tk.Frame(root2,height=500,width=300,bg="#343030")
        frame3.place(x = 701,y =1)
        
        i = 10
        j = 0
        fileList = []
        arclist = []
        boxlist = []

        #########################################################################################
        # ACADEMIC VIEW
        
        
        
       
        course = tk.Entry(frame3)
        course.place(x = 0,y=10,width=130 )
        deliverable = tk.Entry(frame3)
        deliverable.place (x = 140,y = 10,width=130)
        AddCourse = tk.Button(frame3,text="Add Course",bg="#00F0FF",relief=tk.GROOVE,command= lambda: SecondView.coursess(frame3,course))
        AddCourse.focus_set()
        AddCourse.place(x= 0, y=35,width=130)
        AddDeliverables = tk.Button(frame3,text="Add Deliverables",bg="#00F0FF",relief=tk.GROOVE,command= lambda:SecondView.deliverabless(frame3,deliverable))
        AddDeliverables.place(x= 140, y=35,width=130)

        for file in fileNames:
            label1 = tk.Label(frame2,text=file,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
            label1.place(x= 710, y=i)
            fileList.append(label1)
            i = i + 20
            j = j + 1
        totalFiles = "Total Files: " + str(j)
        dirDict = {}
        path = folderName
        for(path,dirs,files) in os.walk(path):
            for file in files :
                extension= file.split('.')[1]
                if extension in dirDict.keys():
                    dirDict[extension] = dirDict[extension] + 1
                else:
                    dirDict.update({extension:1})          
        percentageFile = 100 / j
        s = 0
        e = 0
        top_x = 50
        top_y = 300
        bottom_x = 61
        bottom_y = 311            
        for ext in dirDict:
            percentage = percentageFile * dirDict.get(ext) 
            e = (percentage/100) * 360
            hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
            arc = canvas1.create_arc(200, 50, 380, 230,start=s,extent=e,fill=hexadecimal,tag="arc")
            arclist.append(arc)
            box = canvas1.create_rectangle(top_x,top_y,bottom_x,bottom_y,width=0,fill=hexadecimal)
            boxlist.append(box)
            label = tk.Label(canvas1,text=ext,fg="#00F0FF",bg="#343030",font=("Helvetica",10))
            label.place(x= bottom_x + 10, y=top_y-7)
            s = s + e
            top_y = top_y + 20
            bottom_y = bottom_y + 20
            if( bottom_y > 400):
                top_x = top_x + 60
                top_y = 300
                bottom_x = bottom_x + 60
                bottom_y = 311
        arc2 = canvas1.create_oval(220, 70, 360, 210,fill="#343030")
        label = tk.Label(canvas1,text=totalFiles,fg="#00F0FF",bg="#343030",font=("Helvetica",15))
        label.place(x= 45, y=420)
        selectOrganizeAcademic = tk.Button(frame5,text="Organize1",bg="#00F0FF",relief=tk.GROOVE,command=lambda :FOps.organizeByAcademic(SecondView.subjects,SecondView.assignments))
        selectOrganizeAcademic.place(x= 0, y=0,width=180)
        selectOrganizeExtension = tk.Button(frame4,text="Organize2",bg="#00F0FF",relief=tk.GROOVE,command=lambda :FOps.organizeByExtension(fileNames))
        selectOrganizeExtension.place(x= 0, y=0,width=180)
        selectAcademic = tk.Button(canvas1,text="Academic",bg="#00F0FF",relief=tk.GROOVE,command=lambda :SecondView.showAcademic(frame3,frame5))
        selectAcademic.place(x= 200, y=15,width=90)
        selectExtension = tk.Button(canvas1,text="Extension",bg="#00F0FF",relief=tk.GROOVE,command=lambda :SecondView.showExtension(frame2,frame4))
        selectExtension.place(x= 295, y=15,width=90)
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
root.mainloop()