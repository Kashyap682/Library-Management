import tkinter as tk

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

root = tk.Tk()
root.geometry("300x300")

namevar = tk.StringVar()
bookvar = tk.StringVar()

def issueb():


    main = tk.Toplevel(root)
    
    name = namevar.get()
    book = bookvar.get()

    name2 = str(name) + "\n"
    book2 = str(book) + "\n"
    
    f1 = open(file_paths_list[0] + "/membername.txt",'r+')
    p1 = f1.read()
    f1.close()

    if name2 in p1:
        f2 = open(file_paths_list[4] + "/quantity.txt",'r+')
        p2 = f2.readlines()
        i1 = p2.index(book2)
        i2 = int(p2[i1+1])

        if i2 > 0:
            f3 = open(file_paths_list[4] + "/quantity.txt",'r+')
            p3 = f3.read()
            f3.close()

            newdata = p3.replace(str(i2),str(i2-1))

            f4 = open(file_paths_list[4] + "/quantity.txt",'w+')
            f4.write(newdata)
            f4.flush()
            f4.close()

            f5 = open(file_paths_list[4] + "/issued.txt",'a+')
            f5.write(str(name) + "-" + str(book) + "\n")
            f5.flush()
            f5.close()
            
            msg = str(book) + " issued successfully."
            msgvar = tk.Label(main, text = msg)
            msgvar.pack()

            main.attributes('-topmost',True)
            main.mainloop()

        else:
            msg2var = tk.Labal(main, text = "Book not available.")
            msg2var.pack()

            main.attributes('-topmost',True)
            main.mainloop()
    else:
        msg3var = tk.Label(main, text = "You are not a member.")
        msg3var.pack()

        main.attributes('-topmost', True)
        main.mainloop()

name_label = tk.Label(root, text = "Name", font = ('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable = namevar, font = ('calibre', 10, 'normal'))

book_label = tk.Label(root, text = "Book", font = ('calibre', 10, 'bold'))
book_entry = tk.Entry(root, textvariable = bookvar, font = ('calibre', 10, 'normal'))

i_btn = tk.Button(root, text = "issue", command = issueb)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
book_label.grid(row=1,column=0)
book_entry.grid(row=1,column=1)

i_btn.grid(row=3,column=1)

root.attributes('-topmost',True)
root.mainloop()
