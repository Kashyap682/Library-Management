import tkinter as tk
from tkinter.ttk import *
import os

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

###################################################################

def addbookgui():
        os.system("python addbook.py")

def displaybooksgui():
        g=open(file_paths_list[1] + "/bookname.txt",'r')
        h=g.read()

        main = tk.Tk()
        ourMessage = ''.join(h)
        messageVar = tk.Message(main, text = ourMessage)
        messageVar.pack()
        main.attributes('-topmost',True)
        main.mainloop()

def displayabookgui():
        os.system("python displayabook.py")

def deletebookgui():
        os.system("python delbook.py")
        
def updatebookgui():
        os.system("python updatebook.py")

def searchbyauthorgui():
        os.system("python searchauthor.py")

def searchbygenregui():
        os.system("python searchgenre.py")

def issuedbooksgui():
        k=open(file_paths_list[4] + "/issued.txt",'r')
        i=k.read()

        main = tk.Tk()
        ourMessage = ''.join(i)
        messageVar = tk.Message(main, text = ourMessage)
        messageVar.pack()
        main.attributes('-topmost',True)
        main.mainloop()

def bookmanagementgui():
	
	newWindow = tk.Toplevel(master)
	
	newWindow.title("Book Managemant")

	newWindow.geometry("500x500")

	Label(newWindow, text ="Book Management").pack()

	btn11 = Button(newWindow, text = "Add Book Record", command = addbookgui)
	btn11.pack(pady = 10)

	btn12 = Button(newWindow, text = "Display Book Records", command = displaybooksgui)
	btn12.pack(pady = 10)

	btn13 = Button(newWindow, text = "Display a Book", command = displayabookgui)
	btn13.pack(pady = 10)

	btn14 = Button(newWindow, text = "Delete a Book", command = deletebookgui)
	btn14.pack(pady = 10)

	btn15 = Button(newWindow, text = "Update Book Record", command = updatebookgui)
	btn15.pack(pady = 10)

	btn16 = Button(newWindow, text = "Search by Author", command = searchbyauthorgui)
	btn16.pack(pady = 10)

	btn17 = Button(newWindow, text = "Search by Genre", command = searchbygenregui)
	btn17.pack(pady = 10)

	btn18 = Button(newWindow, text = "Issued Books", command = issuedbooksgui)
	btn18.pack(pady = 10)

	btn19 = Button(newWindow, text = "Return to main menu", command = newWindow.destroy)
	btn19.pack(pady = 10)

###################################################################

def addmembergui():
        os.system("python addmember.py")

def displaymembersgui():
        g=open(file_paths_list[0] + "/membername.txt",'r')
        h=g.read()

        main = tk.Tk()
        ourMessage = ''.join(h)
        messageVar = tk.Message(main, text = ourMessage)
        messageVar.pack()
        main.attributes('-topmost',True)
        main.mainloop()

def displayamembergui():
        os.system("python displayamember.py")
        
def deletemembergui():
        os.system("python delmember.py")

def updatemembergui():
        os.system("python updatemember.py")


def membermanagementgui():
	
	newWindow = tk.Toplevel(master)
	
	newWindow.title("Member Managemant")

	newWindow.geometry("500x500")

	Label(newWindow, text ="Member Management").pack()

	btn11 = Button(newWindow, text = "Add New Member", command = addmembergui)
	btn11.pack(pady = 10)

	btn12 = Button(newWindow, text = "Display All Members", command = displaymembersgui)
	btn12.pack(pady = 10)

	btn13 = Button(newWindow, text = "Display a Member", command = displayamembergui)
	btn13.pack(pady = 10)

	btn14 = Button(newWindow, text = "Remove Current Member", command = deletemembergui)
	btn14.pack(pady = 10)

	btn15 = Button(newWindow, text = "Update Member Record", command = updatemembergui)
	btn15.pack(pady = 10)

	btn16 = Button(newWindow, text = "Return to main menu", command = newWindow.destroy)
	btn16.pack(pady = 10)


###################################################################

def issuebookgui():
        os.system("python issuebook.py")

def returnbookgui():
        os.system("python returnbook.py")

def issuereturngui():

	newWindow = tk.Toplevel(master)
	
	newWindow.title("Issue/Return")

	newWindow.geometry("500x500")

	Label(newWindow, text ="Issue/Return").pack()

	btn11 = Button(newWindow, text = "Issue a Book", command = issuebookgui)
	btn11.pack(pady = 10)

	btn12 = Button(newWindow, text = "Return a Book", command = returnbookgui)
	btn12.pack(pady = 10)
        
	btn13 = Button(newWindow, text = "Return to main menu", command = newWindow.destroy)
	btn13.pack(pady = 10)

        
        
        


###################################################################

master = tk.Tk()

master.geometry("500x500")

label = Label(master, text ="Main Menu")

label.pack(pady = 10)

btn1 = Button(master, text ="Book Management", command = bookmanagementgui)
btn1.pack(pady = 10)
btn2 = Button(master, text ="Member Management", command = membermanagementgui)
btn2.pack(pady = 10)
btn3 = Button(master, text ="Issue/Return", command = issuereturngui)
btn3.pack(pady = 10)
btn4 = Button(master, text ="Exit", command = master.destroy)
btn4.pack(pady = 10)

tk.mainloop()
