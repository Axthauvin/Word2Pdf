from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from docx2pdf import convert
import os


def Closewin():
    root.quit()

def Choosefile():
    filename = askopenfilename(title="Choisir un fichier à convertir")
    
    if filename != "":
        filepdf = filename.replace("docx", "pdf")
        splited = filename.split("/")

        nameend = splited[len(splited) - 1]
    
        path = filename.replace(nameend, '')
        print(path)
        path = os.path.realpath(path)
    
        convert(filename, filepdf)

    
    
        Closewin()


def Choosefile2():
    filename = askdirectory(title="Choisir un dossier")
    if filename != "":
        
        
    
        path = filename
        print(path)
        path = os.path.realpath(path)
    
        convert(path, path)

    
    
        Closewin()


root = Tk()
root.title("Convertir DOCX en PDF")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

root.overrideredirect(1)

L = Label(root, text="Convertir DOCX en PDF", font=("Raleway", 15, 'bold'))
L.pack()

Choose = Button(root, text="Choisir un fichier", command=Choosefile)
Choose.pack()

Choose2 = Button(root, text="Choisir un dossier", command=Choosefile2)
Choose2.pack()

Close = Button(root, text="Fermer", command=Closewin)
Close.pack()



root.mainloop()