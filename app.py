import tkinter as tk
from  tkinter import filedialog, Text
import os


root = tk.Tk()
apps=[]

def Addfile():
    filename = filedialog.askopenfilename(initialdir= "/", title="Select File", filetypes=(("Zip Files","*.zip"),("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    import zipfile
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('C:\ML_Projects')
    print(filename)
    pass;

def Runfile():
    os.chdir("C:\\ML_Projects\\telecom-churn-project")
    lis=os.listdir("C:\\ML_Projects\\telecom-churn-project")
    print(lis)
    for i in lis:
        if i == "requirements.txt":
            os.mkdir("staged")
            import shutil
            shutil.copyfile(i, 'staged\REQUIREMENTS.TXT')
            
    for app in apps:
        os.startfile(app)
    print(apps)
    pass;

frame = tk.Frame(root, bg="white")

frame.place(relwidth =0.8, relheight=0.8)
openFile = tk.Button(frame, text="Open File", padx=10,pady=5,fg="white",bg="grey", command= Addfile)
CreateTar = tk.Button(frame, text="Create Tarfile", padx=10,pady=5,fg="white",bg="grey", command = Runfile)
openFile.pack()
CreateTar.pack()
root.mainloop()