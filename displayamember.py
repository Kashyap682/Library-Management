import tkinter as tk

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
    j = i.strip("\n")
    print(j)
    file_paths_list.append(j)


root1 = tk.Tk()

root1.geometry("400x400")

displaymembvar = tk.StringVar()

def displayb():

    dd='.txt'
    hh=file_paths_list[0] + "/"
    
    displaymemb = displaymembvar.get()
    
    gg=hh+displaymemb+dd

    main1 = tk.Tk()
    
    try:
        pp=open(gg,'r')
        xx=pp.read()
        pp.close()
        msg = xx
        msgvar = tk.Message(main1, text = msg)
        msgvar.pack()
        main1.attributes('-topmost',True)
        main1.mainloop()

    except:
        msg2 = "No such book found."
        msg2var = tk.Label(main1, text = msg2)
        msg2var.pack()
        main1.attributes('-topmost',True)
        main1.mainloop()

        
membsearch_label = tk.Label(root1, text = 'Name', font = ('calibre', 10, 'bold'))
membsearch_entry = tk.Entry(root1, textvariable = displaymembvar, font = ('calibre', 10, 'normal'))

srch_btn = tk.Button(root1, text = "Search", command = displayb)

membsearch_label.grid(row=0,column=0)
membsearch_entry.grid(row=0,column=1)

srch_btn.grid(row=1,column=1)

root1.attributes('-topmost',True)
root1.mainloop()
