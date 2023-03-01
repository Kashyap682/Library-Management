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

root.geometry("300x300")

delmembvar = tk.StringVar()

def delbook():

        main = tk.Toplevel(root)

        delmemb = delmembvar.get()
        delmemb1 = str(delmemb) + "\n"

        j = open(file_paths_list[0] + "/membername.txt",'r+')
        p = j.readlines()

        j.close()

        try:
                p.remove(delmemb1)
                j1 = open(file_paths_list[0] + "/membername.txt",'w+')
                j1.writelines(p)

                j1.flush()
                j1.close()

                os.remove(file_paths_list[0] + "/" + str(delmemb) + ".txt")
                
                msgvar = tk.Label(main, text = "Member Deleted Successfully.")
                msgvar.pack()

                main.attributes('-topmost',True)
                main.mainloop()

        except:
                msg1var = tk.Label(main, text = "No such member found.")
                msg1var.pack()

                main.attributes('-topmost',True)
                main.mainloop()


delmemb_label = tk.Label(root, text = 'Name ', font = ('calibre', 10, 'bold'))
delmemb_entry = tk.Entry(root, textvariable = delmembvar, font = ('calibre', 10, 'normal'))

del_btn = tk.Button(root, text = 'Delete', command = delbook)

delmemb_label.grid(row=0,column=0)
delmemb_entry.grid(row=0,column=1)

del_btn.grid(row=1,column=1)

root.attributes('-topmost',True)
root.mainloop()
