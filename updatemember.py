import tkinter as tk

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

root = tk.Tk()

root.geometry("600x400")

namevar = tk.StringVar()
datavar = tk.StringVar()
newdatavar = tk.StringVar()

def updateb():

    main = tk.Toplevel(root)

    name = namevar.get()
    data = datavar.get()
    newdata = newdatavar.get()

    data2 = str(data) + " : "

    l = file_paths_list[0] + "/" + str(name) + ".txt"

    try:
        f = open(l,'r+')
        x = f.readlines()
        f.close()

        i = len(x)

        for a in range(0,i):
                if x[a].find(str(data2)) != -1:
                        x[a] = str(data) + " : " + str(newdata) + "\n"
                        f2 = open(l,'w+')
                        f2.writelines(x)
                        f2.flush()
                        f2.close()

                        msgvar = tk.Label(main, text = "Data updated Successfully.")
                        msgvar.pack()

                        main.attributes('-topmost',True)
                        main.mainloop()

        else:
                msg3var = tk.Label(main, text = "No such attribute found.")
                msg3var.pack()

                main.attributes('-topmost',True)
                main.mainloop()


    except:

        msg1var = tk.Label(main, text = "No such member found.")
        msg1var.pack()

        main.attributes('-topmost',True)
        main.mainloop()

book_label = tk.Label(root, text = 'Name', font = ('calibre', 10, 'bold'))
book_entry = tk.Entry(root, textvariable = namevar, font = ('calibre',10, 'normal'))

data_label = tk.Label(root, text = 'Data to be updated', font = ('calibre', 10, 'bold'))
data_entry = tk.Entry(root, textvariable = datavar, font = ('calibre',10, 'normal'))

newdata_label = tk.Label(root, text = 'New Data', font = ('calibre', 10, 'bold'))
newdata_entry = tk.Entry(root, textvariable = newdatavar, font = ('calibre',10, 'normal'))

up_btn = tk.Button(root, text = 'Update', command = updateb)

book_label.grid(row=0,column=0)
book_entry.grid(row=0,column=1)

data_label.grid(row=1,column=0)
data_entry.grid(row=1,column=1)

newdata_label.grid(row=2,column=0)
newdata_entry.grid(row=2,column=1)

up_btn.grid(row=3,column=1)

root.attributes('-topmost',True)
root.mainloop()
