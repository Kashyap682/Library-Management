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

delbookvar = tk.StringVar()

def delbook():

        main = tk.Toplevel(root)

        delbook = delbookvar.get()
        delbook1 = str(delbook) + "\n"

        k = open(file_paths_list[4] + "/quantity.txt",'r+')
        l = k.readlines()
        j = open(file_paths_list[1] + "/bookname.txt",'r+')
        p = j.readlines()

        k.close()
        j.close()

        try:
                p.remove(delbook1)
                del l[l.index(delbook1) + 1]
                l.remove(delbook1)
                

                print(delbook)
                print(p)
                print(l)

                k1 = open(file_paths_list[4] + "/quantity.txt",'w+')
                k1.writelines(l)
                j1 = open(file_paths_list[1] + "/bookname.txt",'w+')
                j1.writelines(p)

                k1.flush()
                k1.close()
                j1.flush()
                j1.close()

                os.remove(file_paths_list[1] + "/" + str(delbook) + ".txt")
                
                msgvar = tk.Label(main, text = "Book Deleted Successfully.")
                msgvar.pack()

                main.attributes('-topmost',True)
                main.mainloop()

        except:
                msg1var = tk.Label(main, text = "No such book found.")
                msg1var.pack()

                main.attributes('-topmost',True)
                main.mainloop()


delbook_label = tk.Label(root, text = 'Name of Book', font = ('calibre', 10, 'bold'))
delbook_entry = tk.Entry(root, textvariable = delbookvar, font = ('calibre', 10, 'normal'))

del_btn = tk.Button(root, text = 'Delete', command = delbook)

delbook_label.grid(row=0,column=0)
delbook_entry.grid(row=0,column=1)

del_btn.grid(row=1,column=1)

root.attributes('-topmost',True)
root.mainloop()
