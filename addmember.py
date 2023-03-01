import tkinter as tk

file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)


root=tk.Tk()

root.geometry("600x400")

membernamevar = tk.StringVar()
rollnovar = tk.StringVar()
dobvar = tk.StringVar()
cnvar = tk.StringVar()
intrstvar = tk.StringVar()

def submit():

	membername = membernamevar.get()
	rollno = rollnovar.get()
	dob = dobvar.get()
	cn = cnvar.get()
	intrst = intrstvar.get()

	b = '.txt'
	d = file_paths_list[0] + "/"

	c = d + str(membername) + b

	a = open(c,'a+')
	e=open(file_paths_list[0] + "/membername.txt","a+")

	a.write('Name : ')
	a.write(membername)
	a.write('\n')
	a.write('Roll no. : ')
	a.write(rollno)
	a.write('\n')
	a.write('Date of Birth : ')
	a.write(dob)
	a.write('\n')
	a.write('Contact no. : ')
	a.write(cn)
	a.write('\n')
	a.write('Genre of interest : ')
	a.write(intrst)
	a.write('\n')
	e.write(membername)
	e.write('\n')

	print('Record Added')

	a.flush()
	a.close()
	e.flush()
	e.close()

	membernamevar.set("")
	rollnovar.set("")
	dobvar.set("")
	cnvar.set("")
	intrstvar.set("")

name_label = tk.Label(root, text = 'Name', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = membernamevar, font=('calibre',10,'normal'))

rollno_label = tk.Label(root, text = 'Roll no.', font = ('calibre',10,'bold'))
rollno_entry=tk.Entry(root, textvariable = rollnovar, font = ('calibre',10,'normal'))

dob_label = tk.Label(root, text = 'Date of Birth', font=('calibre',10, 'bold'))
dob_entry = tk.Entry(root,textvariable = dobvar, font=('calibre',10,'normal'))

cn_label = tk.Label(root, text = 'Contact no.', font=('calibre',10, 'bold'))
cn_entry = tk.Entry(root,textvariable = cnvar, font=('calibre',10,'normal'))

goi_label = tk.Label(root, text = 'Genre of Interest', font=('calibre',10, 'bold'))
goi_entry = tk.Entry(root,textvariable = intrstvar, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

rollno_label.grid(row=1,column=0)
rollno_entry.grid(row=1,column=1)

dob_label.grid(row=2,column=0)
dob_entry.grid(row=2,column=1)

cn_label.grid(row=3,column=0)
cn_entry.grid(row=3,column=1)

goi_label.grid(row=4,column=0)
goi_entry.grid(row=4,column=1)


sub_btn.grid(row=5,column=1)

root.attributes('-topmost',True)
root.mainloop()
