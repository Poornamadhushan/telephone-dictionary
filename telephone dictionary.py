from tkinter import *
from tkinter import messagebox


def search():
    name = entrysearch.get()
    if name == '':
        txtdisplay_tel.delete(0.0, END)
        tel = "Enter a Name"
    else:
        name = name.lower()
        txtdisplay_tel.delete(0.0, END)
        try:
            tel = mydic[name]
        except:
            tel = "Can't find this name"
        txtdisplay_tel.insert(END, tel)


def addcontact():
    telNo = entryaddtel.get()
    cname = addentry.get()
    cname = cname.lower()

    if cname != '' and telNo != '':
        mydic.update({cname: telNo})
        messagebox.showinfo('Add Contact', 'Successfully Added')
       
        addentry.delete(0, END)
        entryaddtel.delete(0, END)
    else:
        messagebox.showinfo('Oops', 'Please input data correctly')

#delete contact
def delete():
    try:
        ans = messagebox.askquestion("Delete Contact Warning", "Are You Sure you want to delete this contact...")
        if ans == 'yes':
            name = entrysearch.get()
            name = name.lower()
            messagebox.showinfo('Confirm Delete Contact', 'The Record Deleted Successfully')
            del mydic[name]
            entrysearch.delete(0, END)
            txtdisplay_tel.delete(0.0, END)
    except:
        messagebox.showinfo('Oops...', 'This contact not available')

#create window
win = Tk()
win.geometry('500x300+200+200')
win.resizable(False, False)
win.title('My Telephone Dictionary')
win.configure(bg='black')

Label(win, text='Search Contact', font='none 14 bold', bg='black', fg='white').place(x=175, y=1)

#search Section
#create a label and entry box for search
lblsearch = Label(win, text='Enter Name', font='none 12 bold', bg='black', fg='white')
entrysearch = Entry(win, width=20, bg='white', font='none 12')
#create a button to search
btnsearch = Button(win, text='Search', width=12, fg='blue', command=search, bg='green')
#create label and text box to display result
lbltel = Label(win, text='Tel. Number', font='none 12 bold', bg='black', fg='white')
txtdisplay_tel = Text(win, width=15, height=1, font='none 12')

#add contacts
Label(win, text='Add Contacts', font='none 14 bold', bg='black', fg='white').place(x=175, y=120)
lbladdname = Label(win, text='Enter Name', font='none 12 bold', bg='black', fg='white')
addentry = Entry(win, width=20, font='none 12')
lbladdtel = Label(win, text='Enter Tel No', font='none 12 bold', bg='black', fg='white')
entryaddtel = Entry(win, width=15, bg='white', font='none 12')
btnadd = Button(win, text='Add contact', width=12, fg='blue', command=addcontact, bg='green')
#delete contacts
btndel = Button(win, text='Delete', width=12, fg='red', command=delete, bg='yellow')
#placed controls
#place search controls
lblsearch.place(x=1, y=30)
entrysearch.place(x=100, y=30)
btnsearch.place(x=350, y=30)
lbltel.place(x=1, y=60)
txtdisplay_tel.place(x=100, y=60)
#place add control
lbladdname.place(x=1, y=150)
addentry.place(x=100, y=150)
lbladdtel.place(x=1, y=180)
entryaddtel.place(x=100, y=180)
btnadd.place(x=350, y=180)
btndel.place(x=350, y=60)

#create a dictionary to add names and numbers
mydic = {'anton': '0714466533'}

win.mainloop()
