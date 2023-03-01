# declaring all file paths
file_paths = open("your_path/name.txt","r")
file_paths_list1 = file_paths.readlines()
file_paths_list = []

for i in file_paths_list1:
	j = i.strip("\n")
	print(j)
	file_paths_list.append(j)

# function to search
def search(a,b):
	x = "adba"
	y = "abba"
	c = 0

	for i in range(0,len(x)):
		if x[i] == y[i]:
			c = c + 1
		else:
			c = c
	return c



# function defined to display the main menu of the programme
def mainmenu():
    print('Main Menu')
    print()
    print('''1. Book Management
2. Members Management
3. Issue/Return Book
4. Exit''')

# function defined to display menu for the management of the books in the programme
def bookmanagement():
    print('Book Management')
    print()
    print('''1. Add Book Record
2. Display Book Records
3. Disply a Book
4. Delete Book Record
5. Update Book Record
6. Display Books of an Author
7. Display Books by Genre
8. Display Issued Books
9. Retuen to Main Menu''')

# function defined to display menu for the management of the members of library
def membermanagement():
    print('Members Management')
    print()
    print('''1. Add New Member
2. Remove Current Member
3. Update Current Member's Data
4. Display All Members
5. Display Particular Member
6. Return to Main Menu''')

# function defined to display menu for the issuing of returning of book 
def issuereturn():
    print('Issue or Return a Book')
    print()
    print('''1. Issue a Book
2. Return a Book
3. Return to Main Menu''')

def exit1():
    print('Thank You')

# function defined to add record of a new book in the library
def addbookrecord():
    print('Add Book Record')
    print()
    b = '.txt'
    d = file_paths_list[1] + "/"
    dd = file_paths_list[3] + "/"
    ddd = file_paths_list[2] + "/"
    bookname = input('Enter name of the book:')
    author = input('Enter name of the author:')
    price = input('Enter price of the book:')
    genre = input('Enter genre/subject of the book:')
    pub = input('Enter name of the publisher:')
    qty = input('Enter quantity purchased:')
    dt = input('Enter date of purchase:')
    c = d + bookname + b
    cc = dd + genre + b
    ccc = ddd + author + b
    a = open(c,'a+')
    e=open(file_paths_list[1] + "/bookname.txt","a+")
    ee=open(file_paths_list[4] + "/quantity.txt","a+")
    eee=open(cc,'a+')
    eeee=open(ccc,'a+')
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
    a.write(pub)
    a.write('\n')
    a.write('Genre : ')
    a.write(genre)
    a.write('\n')
    a.write('Quantity purchased : ')
    a.write(qty)
    a.write('\n')
    a.write('Date of purchase : ')
    a.write(dt)
    a.write('\n')
    e.write(bookname)
    e.write('\n')
    ee.write(bookname)
    ee.write('\n')
    ee.write(qty)
    ee.write('\n')
    eee.write(bookname)
    eee.write('\n')
    eeee.write(bookname)
    eeee.write('\n')
    print('Record Added')
    a.flush()
    a.close()
    e.flush()
    e.close()
    ee.flush()
    ee.close()
    eee.flush()
    eee.close()
    eeee.flush()
    eeee.close()

# function defined to display list of books in the library
def displaybookrecord():
    print('Book Record')
    print()
    g=open(file_paths_list[1] + "/bookname.txt",'r')
    h=g.read()
    print(h)
    g.close()

# function defined to display a book from library data
def displaybook():
    dd='.txt'
    hh=file_paths_list[1] + "/"
    ff=input('Enter name of the book:')
    print()
    gg=hh+ff+dd
    try:
        pp=open(gg,'r')
        xx=pp.read()
        print(xx)
        pp.close()
    except:
        print('No such book found.')

# function defined to delete a book from the data
def deletebookrecord():
    print('Delete a book record')
    print()
    w=input('Enter name of the book to be deleted:')
    j=(file_paths_list[1] + "/bookname.txt",'r+')
    p=j.readlines()
    i=0
    while i<len(p) and p[i]!=w:
        i+=1
    if i<len(p):
        del p[i]
    else:
        print('No book found.')
    j.writelines(p)
    j.close()

# function defined to update book details
def updatebookrecord():
    print('Update a book record')
    print()
    o=input('Enter name of book:')
    r=input('Enter what data is to be updated:')
    print('''Enter the below data in the form :'''
,r,''' : Data''')
    t=input('Enter current Data:')
    y=input('Enter new Data:')
    m='.txt'
    n=file_paths_list[1] + "/"
    l=n+o+m
    try:
        v=open(l,'r')
        filedata = v.read()
        v.close()
        newdata = filedata.replace(t,y)
        f = open(l,'w')
        f.write(newdata)
        f.close()
        print('Data Updated.')
    except:
        print('No such book found.')
#function defined to display books by an author
def displaybyauthor():
    print('''Authors:
J.K Rowlings
E.L James
Lee Child
Todd Ritter
Robin Kirkpatrick
Dante Alighieri
Sumita Arora''')
    try:
        a=input('Enter name of the author:')
        b=file_paths_list[2] + "/"
        c='.txt' 
        d=b+a+c
        e=open(d,'r')
        f=e.read()
        print(f)
    except:
        print('No such author found.')

#function defined to display books by genre/topic
def displaybygenre():
    try:
        a=input('Enter topic or genre:')
        b=file_paths_list[3] + "/"
        c='.txt'
        d=b+a+c
        e=open(d,'r')
        f=e.read()
        print(f)
    except:
        print('No such Genre or Topic found.')

#function defined to display issued books
def issuedbooks():
    a=open(file_paths_list[4] + "/issue.txt",'r')
    a.read()
    try:
        print(a)
    except:
        print('No books issued.')

# function defined to add a new member in the library
def addmember():
    print('Add a member')
    print()
    b='.txt'
    d=file_paths_list[0] + "/"
    membername=input('Enter your name:')
    rollno=input('Enter rollno:')
    dob=input('Enter your Date of Birth:')
    age=input('Enter your age:')
    addrs=input('Enter your permanent address:')
    cn=input('Enter your contact number:')
    intr=input('Enter your interest of books:')
    c=d+membername+b
    a=open(c,'a+')
    e=open(file_paths_list[0] + "/membername.txt",'a+')
    a.write('Name : ')
    a.write(membername)
    a.write('\n')
    a.write('Roll no. : ')
    a.write('\n')
    a.write('Date of Birth : ')
    a.write(dob)
    a.write('\n')
    a.write('Age : ')
    a.write(age)
    a.write('\n')
    a.write('Address : ')
    a.write(addrs)
    a.write('\n')
    a.write('Contact No. : ')
    a.write(cn)
    a.write('\n')
    a.write('Topic of interest : ')
    a.write(intr)
    a.write('\n')
    e.write(membername)
    e.write('\n')
    print('Record Added')
    a.flush()
    a.close()
    e.flush()
    e.close()

# fuction defined to remove a member from library
def removemember():
    print('Remove a member')
    print()
    w=input('Enter name of the book to be deleted:')
    j=(file_paths_list[0] + "/membername.txt",'w+')
    p=j.readlines()
    i=0
    while i<len(p) and p[i]!=w:
        i+=1
    if i<len(p):
        del p[i]
    else:
        print('No such member found')
    j.writelines(p)
    j.close()

# function defined to update a member's details
def updatemember():
    print('Update information')
    print()
    o=input('Enter name of member:')
    r=input('Enter what data is to be updated(Name cannot be updated):')
    print('Enter the below data in form : ',r,' : Data')
    t=input('Enter current ',r)
    y=input('Enter new ',r)
    m='.txt'
    n=file_paths_list[1] + "/"
    l=n+o+m
    try:
        v=open(l,'r')
        filedata = v.read()
        v.close()
        newdata = filedata.replace(t,y)
        f = open(l,'w')
        f.write(newdata)
        f.close()
        print('Data Updated.')
    except:
        print('No such member found.')

# function defined to display all the members of the library
def displayallmembers():
    print('List of all members')
    print()
    g=open(file_paths_list[0] + "/membername.txt",'r')
    h=g.read()
    print(h)
    g.close()

# function defined to display details of a particular member of the library
def displaymember():
    i=input('Enter name of the member:')
    print()
    u=file_paths_list[0] + "/"
    a='.txt'
    y1=u+i+a
    try:
        h=open(y1,'r')
        h1=h.read()
        print(h1)
        h.close()
    except:
        print('No such member found.')

# function defined to issue a book
def issuebook():
    s=input('Enter name of the book:')
    ff='\n'
    ss=s+ff
    dp=input('Enter your name:')
    o=open(file_paths_list[0] + "/membername.txt",'r')
    p=o.read()
    if dp in p:
        aa=open(file_paths_list[4] + "/quantity.txt",'r')
        bb=aa.readlines()
        cc=bb.index(ss)
        dd=int(bb[cc+1])
        if dd>0:
            f = open(file_paths_list[4] + "/quantity.txt",'r')
            filedata = f.read()
            f.close()
            newdata = filedata.replace(str(dd),str(dd-1))
            f = open(file_paths_list[4] + "/quantity.txt",'w')
            f.write(newdata)
            f.close()
            print('Book ',s,' issued successfully.')
            print('You have issued this book on date ')
            aa.close()
        else:
            print('Book not available.')
            aa.close()
    else:
        print('You are not member of this library.')

# function defined to return a book
def returnbook():
    w=input('Enter your name:')
    i=input('Enter the book to be returned:')
    ii=i+'\n'
    ss=open(file_paths_list[4] + "/quantity.txt",'r')
    bb=ss.readlines()
    cc=bb.index(ii)
    dd=int(bb[cc+1])
    f = open(file_paths_list[4] + "/quantity.txt",'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(str(dd),str(dd+1))
    f = open(file_paths_list[4] + "/quantity.txt",'w')
    f.write(newdata)
    f.close()
    print('Book ',i,'returned successfully by ',w)

x=True
while x==True:
    mainmenu()
    c=int(input('Enter your choice:'))
    while c in [1,2,3,4,5]:
        if c==1:
            bookmanagement()
            c11=int(input('Enter your choice:'))
            print('+---------------------------------------------+')
            if c11==1:
                addbookrecord()
                print('+---------------------------------------------+')
            elif c11==2:
                displaybookrecord()
                print('+---------------------------------------------+')
            elif c11==3:
                displaybook()
                print('+---------------------------------------------+')
            elif c11==4:
                deletebookrecord()
                print('+---------------------------------------------+')
            elif c11==5:
                updatebookrecord()
                print('+---------------------------------------------+')
            elif c11==6:
                displaybyauthor()
                print('+---------------------------------------------+')
            elif c11==7:
                displaybygenre()
            elif c11==8:
                issuedbooks()
            elif c11==9:
                x=True
                break
            else:
                c1=int(input('Enter 7 for main menu or any other key to exit:'))
                if c1==7:
                    x=True
                    break
                else:
                    x=False
                    break
        elif c==2:
            membermanagement()
            c22=int(input('Enter your choice:'))
            print('+---------------------------------------------+')
            if c22==1:
                addmember()
                print('+---------------------------------------------+')
            elif c22==2:
                removemember()
                print('+---------------------------------------------+')
            elif c22==3:
                updatemember()
                print('+---------------------------------------------+')
            elif c22==4:
                displayallmembers()
                print('+---------------------------------------------+')
            elif c22==5:
                displaymember()
                print('+---------------------------------------------+')
            elif c22==6:
                x=True
                break
            else:
                c1=int(input('Enter 7 for main menu or any other key to exit:'))
                if c1==7:
                    x=True
                    break
                else:
                    x=False
                    break
        elif c==3:
            issuereturn()
            c33=int(input('Enter your choice:'))
            print('+---------------------------------------------+')
            if c33==1:
                issuebook()
                print('+---------------------------------------------+')
            elif c33==2:
                returnbook()
                print('+---------------------------------------------+')
            elif c33==3:
                x=True
                break
            else:
                c1=int(input('Enter 5 for main menu or any other key to exit:'))
                if c1==5:
                    x=True
                    break
                else:
                    x=False
                    break
        else:
            exit1()
            x=False
            break
    else:
        print('Invalid choice.')
        c2=int(input('Enter 5 for main menu or any key to exit:'))
        print()
        if c2==5:
            True
        else:
            print('Thank You.')
            False
            break
