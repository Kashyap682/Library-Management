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

booknamevar = tk.StringVar()
authorvar = tk.StringVar()
pricevar = tk.StringVar()
genrevar = tk.StringVar()
publishervar = tk.StringVar()
quantityvar = tk.StringVar()
dopvar = tk.StringVar()

def submit():

	bookname = booknamevar.get()
	author = authorvar.get()
	price = pricevar.get()
	genre = genrevar.get()
	publisher = publishervar.get()
	quantity = quantityvar.get()
	dop = dopvar.get()

	b = '.txt'
	d = file_paths_list[1] + "/"

	c = d + bookname + b

	a = open(c,'a+')
	e=open(file_paths_list[1] + "/bookname.txt","a+")
	ee=open(file_paths_list[4] + "/quantity.txt","a+")

	a.write('Book name : ')
	a.write(bookname)
	a.write('\n')
	a.write('Author : ')
	a.write(author)
	a.write('\n')
	a.write('Price : ')
	a.write(price)
	a.write('\n')
	a.write('Publication : ')
	a.write(publisher)
	a.write('\n')
	a.write('Genre : ')
	a.write(genre)
	a.write('\n')
	a.write('Quantity purchased : ')
	a.write(quantity)
	a.write('\n')
	a.write('Date of purchase : ')
	a.write(dop)
	a.write('\n')
	e.write(bookname)
	e.write('\n')
	ee.write(bookname)
	ee.write('\n')
	ee.write(quantity)
	ee.write('\n')

	print('Record Added')

	a.flush()
	a.close()
	e.flush()
	e.close()
	ee.flush()
	ee.close()
	
	booknamevar.set("")
	authorvar.set("")
	pricevar.set("")
	genrevar.set("")
	publishervar.set("")
	quantityvar.set("")
	dopvar.set("")
	
name_label = tk.Label(root, text = 'Name of Book', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = booknamevar, font=('calibre',10,'normal'))

author_label = tk.Label(root, text = 'Author', font = ('calibre',10,'bold'))
author_entry=tk.Entry(root, textvariable = authorvar, font = ('calibre',10,'normal'))

price_label = tk.Label(root, text = 'Price', font=('calibre',10, 'bold'))
price_entry = tk.Entry(root,textvariable = pricevar, font=('calibre',10,'normal'))

genre_label = tk.Label(root, text = 'Genre', font=('calibre',10, 'bold'))
genre_entry = tk.Entry(root,textvariable = genrevar, font=('calibre',10,'normal'))

pub_label = tk.Label(root, text = 'Publisher', font=('calibre',10, 'bold'))
pub_entry = tk.Entry(root,textvariable = publishervar, font=('calibre',10,'normal'))

qty_label = tk.Label(root, text = 'Quantity', font=('calibre',10, 'bold'))
qty_entry = tk.Entry(root,textvariable = quantityvar, font=('calibre',10,'normal'))

dop_label = tk.Label(root, text = 'Date of Purchase', font=('calibre',10, 'bold'))
dop_entry = tk.Entry(root,textvariable = dopvar, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

author_label.grid(row=1,column=0)
author_entry.grid(row=1,column=1)

price_label.grid(row=2,column=0)
price_entry.grid(row=2,column=1)

genre_label.grid(row=3,column=0)
genre_entry.grid(row=3,column=1)

pub_label.grid(row=4,column=0)
pub_entry.grid(row=4,column=1)

qty_label.grid(row=5,column=0)
qty_entry.grid(row=5,column=1)

dop_label.grid(row=6,column=0)
dop_entry.grid(row=6,column=1)

sub_btn.grid(row=7,column=1)

root.attributes('-topmost',True)
root.mainloop()
