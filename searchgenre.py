import tkinter as tk
import os

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

root = tk.Tk()
root.geometry("600x400")

genrevar = tk.StringVar()

def genres():

    genre = genrevar.get()

    main = tk.Tk()
    main.geometry("300x300")

    al = ""

    d = file_paths_list[1] + "/"
    ent = os.scandir(d)

    for e in ent:

        f1 = open(file_paths_list[1] + "/" + str(e.name),'r+')
        r1 = f1.read()

        if r1.find("Genre : " + str(genre)) != -1:
            al = al + str(e.name).strip(".txt") + "\n"

    if al != "":

        msg = al
        msgvar = tk.Message(main, text = msg)
        msgvar.pack()
            
        main.attributes('-topmost',True)
        main.mainloop()

    else:

        msg2var = tk.Message(main, text = "No book found.")
        msg2var.pack()
        main.attributes('-topmost',True)
        main.mainloop()


author_label = tk.Label(root, text = "Genre", font = ('calibre', 10, 'bold'))
author_entry = tk.Entry(root, textvariable = genrevar, font = ('calibre', 10, 'normal'))

srch_btn = tk.Button(root, text = "Search", command = genres)

author_label.grid(row=0,column=0)
author_entry.grid(row=0,column=1)

srch_btn.grid(row=1,column=1)

root.attributes('-topmost',True)
root.mainloop()
