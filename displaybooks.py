import tkinter as tk

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

g=open(file_paths_list[1] + "/bookname.txt",'r')
h=g.read()

main = tk.Tk()
ourMessage = ''.join(h)
messageVar = tk.Message(main, text = ourMessage)
messageVar.pack()
main.mainloop()
