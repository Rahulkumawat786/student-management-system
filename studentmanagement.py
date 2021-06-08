# importing required modulus
from DataBase import MySql
from tkinter import *
from tkinter import Toplevel, messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas as pd
import time

# functions to perform operations on data----------------------------------------------------------------------------------------
connected = False
def addStudent():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    nameval = StringVar()
    fnameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    #function for register
    def register():
        name = nameval.get()
        fname = fnameval.get()
        dob = dobval.get()
        mobile = mobileval.get()
        email = emailval.get()
        gender = genderval.get()
        currdate = time.strftime("%d/%m/%Y")
        currtime = time.strftime("%H:%M:%S")
        category = categoryval.get()
        addStroot.destroy()
        if name=='' or fname=='' or dob=='':
            messagebox.showerror('Notification','Name/fathers name/Date of birth are required field!')
            return None
        try:
            db.insert(name=name, fname=fname, dob=dob, mobile=mobile, email=email, gender=gender, category=category,
                  date=currdate, time=currtime)
            studenttable.delete(*studenttable.get_children())
            records = db.showdata()
            for record in records:
                v = [record[k] for k in range(10)]
                studenttable.insert('', END, values=v)
        except:
            messagebox.showerror('Notification','Connect to the database')

    #new window for registration-------------------
    addStroot = Toplevel()
    addStroot.grab_set()
    addStroot.geometry('500x500+650+150')
    addStroot.iconbitmap('sms.ico')
    addStroot.resizable(False, False)
    addStroot.config(bg='gray90')
    #  fields and labels
    # ---------------------------------------------------------------------------- Name
    name = Label(addStroot, text='Name: ', font=('Helvetica', 15), bg='gray90')
    name.place(x=20, y=10)
    namefield = Entry(addStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=nameval)
    namefield.place(x=210, y=10, width=270)

    #-----------------------------------------------------------------------------Father name
    Fathersname = Label(addStroot, text='Father\'s Name: ', font=('Helvetica', 15), bg='gray90')
    Fathersname.place(x=20, y=70)
    fnamefield = Entry(addStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=fnameval)
    fnamefield.place(x=210, y=70, width=270)

    #----------------------------------------------------------------------------Date of bearth
    dob = Label(addStroot, text='DOB. : ', font=('Helvetica', 15), bg='gray90')
    dob.place(x=20, y=130)
    dobfield = Entry(addStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=dobval)
    dobfield.place(x=210, y=130, width=270)

    #--------------------------------------------------------------------------mobile number
    mobile = Label(addStroot, text='Mobile No. : ', font=('Helvetica', 15), bg='gray90')
    mobile.place(x=20, y=190)
    mobilefield = Entry(addStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=mobileval)
    mobilefield.place(x=210, y=190, width=270)

    #-------------------------------------------------------------------------Email id
    email_id = Label(addStroot, text='Email id: ', font=('Helvetica', 15), bg='gray90')
    email_id.place(x=20, y=250)
    emailfield = Entry(addStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=emailval)
    emailfield.place(x=210, y=250, width=270)

    #---------------------------------------------------------------------------Gender
    gender = Label(addStroot, text='Gender: ', font=('Helvetica', 15), bg='gray90')
    gender.place(x=20, y=310)
    genderfield1 = Radiobutton(addStroot, text='Female', variable=genderval, value='Female', font=('Helvetica', 15),
                               bg='gray90')
    genderfield1.select()
    genderfield1.place(x=210, y=310)
    genderfield2 = Radiobutton(addStroot, text='Male', variable=genderval, value='Male', font=('Helvetica', 15),
                               bg='gray90')
    genderfield2.deselect()
    genderfield2.place(x=350, y=310)

    #---------------------------------------------------------------------------category
    category = Label(addStroot, text='Category: ', font=('Helvetica', 15), bg='gray90')
    category.place(x=20, y=370)
    categoryval = ttk.Combobox(addStroot, font=('Helvetica', 15), state='readonly')
    categoryval['values'] = ('General','OBC','SC/ST')
    categoryval.place(x=210,y=370,width=270)

    #---------------------------------------------------------------------------submit button
    submit = Button(addStroot, text="Submit", bg='gray65', relief=RIDGE, borderwidth=3, font=('Helvetica', 15),
                    activebackground='gray55', command=register)
    submit.place(x=150, y=430, width=200)

    addStroot.mainloop()

def searchStudent():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    search_by = combosearch.get()
    val = searchfield.get()
    if search_by=='':
        messagebox.showerror('Notification','Select one parameter!')
    else:
        dict = {"Id":"Id", "Name" : "name", "Father\'s Name" : "Father_name", "Email id" : "Email_id", "Mobile No": "mobile", "DOB" : "DOB",
                         "Date of registration" : "date", "gender":"gender", "category":"category"}
        search_by = dict[search_by]
        try:
            records = db.search(search_by, val)
            if len(records)==0:
                messagebox.showerror('Notification','Data not found!')
            else:
                studenttable.delete(*studenttable.get_children())
                for record in records:
                    v = [record[k] for k in range(10)]
                    #print(v)
                    studenttable.insert('', END, values=v)
        except:
            messagebox.showerror('Notification','connect to the database')

def deleteStudent():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    if studenttable.focus()=='':
        messagebox.showerror('Notification','select a record to update')
        return None
    key = studenttable.focus()
    if key!='':
        content = studenttable.item(key)
        id = content['values'][0]
        try:
            db.delete(id)
            studenttable.delete(*studenttable.get_children())
            records = db.showdata()
            for record in records:
                v = [record[k] for k in range(10)]
                studenttable.insert('', END, values=v)
        except:
            messagebox.showerror('Notification','Connect to the database!')



def updateStudent():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    if studenttable.focus()=='':
        messagebox.showerror('Notification','select a record to update')
        return None
    #  required variables
    nameval = StringVar()
    fnameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    idvar = StringVar()

    def updateData():
        id = idvar.get()
        name = nameval.get()
        fname = fnameval.get()
        dob = dobval.get()
        mobile = mobileval.get()
        email = emailval.get()
        gender = genderval.get()
        category = categoryval.get()
        try:
            updated = db.update(id=id,name=name,fname=fname,mobile=mobile,email=email,gender=gender,dob=dob,category=category)
            if(updated):
                studenttable.delete(*studenttable.get_children())
                records = db.showdata()
                for record in records:
                    v = [record[k] for k in range(10)]
                    studenttable.insert('', END, values=v)

        except:
            messagebox.showerror('Notification','connect to database!')

        updateStroot.destroy()

    #  new window for updating
    updateStroot = Toplevel()
    updateStroot.grab_set()
    updateStroot.geometry('500x560+650+150')
    updateStroot.iconbitmap('sms.ico')
    updateStroot.resizable(False, False)
    updateStroot.config(bg='gray90')

    #  field and labels
    # ---------------------------------------------------------------------------------- id
    id = Label(updateStroot, text='Id : ', font=('Helvetica', 15), bg='gray90')
    id.place(x=20, y=10)
    idfield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=idvar,state=DISABLED)
    idfield.place(x=210, y=10, width=270)

    #---------------------------------------------------------------------------------  name
    name = Label(updateStroot, text='Name: ', font=('Helvetica', 15), bg='gray90')
    name.place(x=20, y=70)
    namefield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=nameval)
    namefield.place(x=210, y=70, width=270)

    #-------------------------------------------------------------------------------  Father's name
    Fathersname = Label(updateStroot, text='Father\'s Name: ', font=('Helvetica', 15), bg='gray90')
    Fathersname.place(x=20, y=130)
    fnamefield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=fnameval)
    fnamefield.place(x=210, y=130, width=270)

    #----------------------------------------------------------------------------- Date of birth
    dob = Label(updateStroot, text='DOB. : ', font=('Helvetica', 15), bg='gray90')
    dob.place(x=20, y=190)
    dobfield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=dobval)
    dobfield.place(x=210, y=190, width=270)

    #---------------------------------------------------------------------------- mobile number
    mobile = Label(updateStroot, text='Mobile No. : ', font=('Helvetica', 15), bg='gray90')
    mobile.place(x=20, y=250)
    mobilefield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=mobileval)
    mobilefield.place(x=210, y=250, width=270)

    #---------------------------------------------------------------------------- Emain id
    email_id = Label(updateStroot, text='Email id: ', font=('Helvetica', 15), bg='gray90')
    email_id.place(x=20, y=310)
    emailfield = Entry(updateStroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=emailval)
    emailfield.place(x=210, y=310, width=270)

    #---------------------------------------------------------------------------  gender
    gender = Label(updateStroot, text='Gender: ', font=('Helvetica', 15), bg='gray90')
    gender.place(x=20, y=370)
    genderfield1 = Radiobutton(updateStroot, text='Female', variable=genderval, value='Female', font=('Helvetica', 15),
                               bg='gray90')
    genderfield1.select()
    genderfield1.place(x=210, y=370)
    genderfield2 = Radiobutton(updateStroot, text='Male', variable=genderval, value='Male', font=('Helvetica', 15),
                               bg='gray90')
    genderfield2.deselect()
    genderfield2.place(x=350, y=370)

    #---------------------------------------------------------------------------  Category
    category = Label(updateStroot, text='Category: ', font=('Helvetica', 15), bg='gray90')
    category.place(x=20, y=430)
    categoryval = ttk.Combobox(updateStroot, font=('Helvetica', 15), state='readonly')
    categoryval['values'] = ('General', 'OBC', 'SC/ST')
    categoryval.place(x=210, y=430, width=270)

    #------------------------------------------------------------------------------ update button
    submit = Button(updateStroot, text="Update", bg='gray65', relief=RIDGE, borderwidth=3, font=('Helvetica', 15),
                    activebackground='gray55',command=updateData)
    submit.place(x=150, y=490, width=200)

    key = studenttable.focus()
    content = studenttable.item(key)
    val = content['values']
    if len(val)!=0:
        idvar.set(val[0])
        nameval.set(val[1])
        fnameval.set(val[2])
        dobval.set(val[3])
        mobileval.set(val[4])
        emailval.set(val[5])
        genderval.set(val[6])
        categoryval.set(val[7])
    updateStroot.mainloop()


def showAll():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    try:
        studenttable.delete(*studenttable.get_children())
        records = db.showdata()
        for record in records:
            v = [record[k] for k in range(10)]
            studenttable.insert('', END, values=v)
    except:
        messagebox.showerror('Notification','connect to the database')

def exportData():
    if not connected:
        messagebox.showerror('Notification','Connect to the data base')
        return None
    path = filedialog.asksaveasfilename()
    records = studenttable.get_children()
    id,name,fname,dob,mobile,email,gender,category,added_time,added_date = [],[],[],[],[],[],[],[],[],[]
    for key in records:
        content = studenttable.item(key)
        record = content['values']
        id.append(record[0]),name.append(record[1]),fname.append(record[2]),dob.append(record[3]),mobile.append(record[4]),email.append(record[5]),gender.append(record[6]),category.append(record[7]),added_time.append(record[8]),added_date.append(record[9])

    headings = ['Id','Name','Father\'s Name','D.O.B.','Mobile Number','Email id','Gender','Category','Added Time','Added Date']
    df = pd.DataFrame(list(zip(id,name,fname,dob,mobile,email,gender,category,added_time,added_date)),columns=headings)
    save = r'{}.csv'.format(path)
    df.to_csv(save,index=False)
    messagebox.showinfo('Notification','Data successfully saved!')


def exitSystem():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if res:
        root.destroy()


def ConnectToDb():
    # required variables
    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()
    #-----function to connect to mysql
    def connect():
        host = hostval.get()
        user = userval.get()
        passward = passval.get()
        dbroot.destroy()
        global db
        global connected
        db = MySql(host=host, user=user, passward=passward)
        if db.connect:
            connected = True

    # new window
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x260+800+230')
    dbroot.iconbitmap('sms.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='gray90')

    #labels and fields
    # ----------------------------------------------------------- host value
    hostlabel = Label(dbroot, text="Enter Host: ", font=('Helvetica', 15), bg='gray90')
    hostlabel.place(x=20, y=10)
    hostfield = Entry(dbroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=hostval)
    hostfield.place(x=230, y=10, width=220)

    #----------------------------------------------------------- user name
    userlabel = Label(dbroot, text="Enter UserName: ", font=('Helvetica', 15), bg='gray90')
    userlabel.place(x=20, y=70)
    userfield = Entry(dbroot, font=('Helvetica', 15), bg='white', bd=5, textvariable=userval)
    userfield.place(x=230, y=70, width=220)

    #---------------------------------------------------------- passward
    passlabel = Label(dbroot, text="Enter Passward: ", font=('Helvetica', 15), bg='gray90')
    passlabel.place(x=20, y=130)
    passfield = Entry(dbroot, show='*', font=('Helvetica', 15), bg='white', bd=5, textvariable=passval)
    passfield.place(x=230, y=130, width=220)

    # ----------------------------------------- Connect button
    submit = Button(dbroot, text="Connect", bg='gray65', relief=RIDGE, borderwidth=3, font=('Helvetica', 15),
                    activebackground='gray55', command=connect)
    submit.place(x=135, y=200, width=200)
    #---------------------------------------------------------------------------
    dbroot.mainloop()


def timer():
    time_str = time.strftime("%H:%M:%S")
    date_str = time.strftime(("%d/%m/%Y"))
    clock.config(text="Date: " + date_str + "\nTime: " + time_str)
    clock.after(200, timer)


def IntroLabel():
    global count, text
    if (count >= len(ss)):
        count = -1;
        text = ''
    else:
        text = text + ss[count]
        welLabel.config(text=text)
    count += 1
    welLabel.after(150, IntroLabel)


#----------------------------------------MAIN WINDOW-----------------------------------------------------------------------------
root = Tk()
root.geometry("1152x700+200+50")
root.title('Student management system')
root.iconbitmap('sms.ico')
root['bg'] = 'gray72'
root.resizable(False, False)


#-------------------------------------------------------------------------------------------- TOP Frames starts
#----------------left clock
clock = Label(root, bg='gray80', relief=RIDGE, borderwidth=3, font=('Helvetica', 13))
clock.place(x=30, y=10, width=200, height=50)
timer()
#---------------- middle slider
count = 0
text = ''
ss = 'Student Management System'
welLabel = Label(root, bg='gray80', text=ss, relief=RIDGE, borderwidth=3, font=('Helvetica', 15, 'italic bold'))
welLabel.place(x=300, y=10, width=552, height=50)
IntroLabel()
#----------------- right connect to Database
connectdb = Button(root, text="Connect to Database", bg='gray80', relief=RIDGE, borderwidth=3, font=('Helvetica', 13),
                   activebackground='gray60', command=ConnectToDb)
connectdb.place(x=922, y=10, width=200, height=50)
#--------------------------------------------------------------------------------------------- Top Frame Ends

#--------------------------------------------------------------------------------------------- Left Frame Start
operationsFrame = Frame(root, bg='gray60', relief=GROOVE, borderwidth=5)
operationsFrame.place(x=30, y=80, width=500, height=550)
########-----------------Adding fields and labels
addStudent = Button(operationsFrame, text='Add Student', bg='gray80', relief=GROOVE, borderwidth=3,
                    font=('Helvetica', 15),
                    activebackground='gray55', command=addStudent)
addStudent.place(x=100, y=80, width=300, height=45)
#----------------------------------------------------
deleteStudent = Button(operationsFrame, text='Delete Student', bg='gray80', relief=GROOVE, borderwidth=3,
                       font=('Helvetica', 15),
                       activebackground='gray55', command=deleteStudent)
deleteStudent.place(x=100, y=149, width=300, height=45)
#------------------------------------------------------
updateStudent = Button(operationsFrame, text='Update Student', bg='gray80', relief=GROOVE, borderwidth=3,
                       font=('Helvetica', 15),
                       activebackground='gray55', command=updateStudent)
updateStudent.place(x=100, y=218, width=300, height=45)
#---------------------------------------------------------
showall = Button(operationsFrame, text='Show All', bg='gray80', relief=GROOVE, borderwidth=3, font=('Helvetica', 15),
                 activebackground='gray55', command=showAll)
showall.place(x=100, y=287, width=300, height=45)
#----------------------------------------------------------
exportdata = Button(operationsFrame, text='Export Data', bg='gray80', relief=GROOVE, borderwidth=3,
                    font=('Helvetica', 15),
                    activebackground='gray55', command=exportData)
exportdata.place(x=100, y=356, width=300, height=45)
#---------------------------------------------------------------
exit = Button(operationsFrame, text='Exit', bg='gray80', relief=GROOVE, borderwidth=3, font=('Helvetica', 15),
              activebackground='gray55', command=exitSystem)
exit.place(x=100, y=425, width=300, height=45)
#---------------------------------------------------------------------------------------------- Left Frame End

#----------------------------------------------------------------------------------------------- Right Frame Start
####-------------Search Frame start
searchFrame = Frame(root, bg='gray72', relief=RIDGE, borderwidth=3)
searchFrame.place(x=560, y=80, width=562, height=50)
##---------------------------------------------------------------------
searchLabel = Label(searchFrame, text='Search By', font=('Helvetica', 13, 'italic'), bg='gray72')
searchLabel.place(x=10, y=10, height=30)
##----------------------------------------------------------------
combosearch = ttk.Combobox(searchFrame, font=('Helvetica', 10), state='readonly')
combosearch['values'] = ("Id", "Name", "Father\'s Name", "Email id", "Mobile No", "DOB",
                         "Date of registration", "gender", "category")
combosearch.place(x=110, y=10, width=150, height=30)
##-------------------------------------------------------------------
searchfield = Entry(searchFrame, font=('Helvetica', 10), bg='white', bd=5)
searchfield.place(x=280, y=10, width=170, height=30)
##--------------------------------------------------------------------
searchbtn = Button(searchFrame, text='Search', bg='gray80', relief=GROOVE, borderwidth=3, font=('Helvetica', 10),
                   activebackground='gray55',command=searchStudent)
searchbtn.place(x=472, y=10, width=70, height=30)
####------------- Search Frame Ends
####----------------------------------------- Data Frame start
DataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataFrame.place(x=560, y=130, width=562, height=500)
#----------------------------------
style = ttk.Style()
style.configure('Treeview.Heading', font=('Helvetica', 13))
style.configure('Treeview', font=('Helvetica', 13))
#---------------------------------------
scroll_x = Scrollbar(DataFrame, orient=HORIZONTAL)
scroll_Y = Scrollbar(DataFrame, orient=VERTICAL)
#-----------------------------------------
studenttable = Treeview(DataFrame, columns=(
'Id', 'Name', 'Father\'s Name', 'DOB', 'Mobile No.', 'Email id', 'Gender', 'Category', 'Time', 'Date'),
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_Y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_Y.config(command=studenttable.yview)
#-------------------------------------------
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Father\'s Name', text='Father\'s Name')
studenttable.heading('Mobile No.', text='Mobile No.')
studenttable.heading('Email id', text='Email id')
studenttable.heading('Gender', text='Gender')
studenttable.heading('Category', text='Category')
studenttable.heading('DOB', text='DOB')
studenttable.heading('Time', text='Added Time')
studenttable.heading('Date', text='Added Date')
studenttable['show'] = 'headings'
#--------------------------------------------
studenttable.column('Id', width=100)
studenttable.column('Name', width=130)
studenttable.column('Father\'s Name', width=130)
studenttable.column('DOB', width=130)
studenttable.column('Mobile No.', width=150)
studenttable.column('Email id', width=200)
studenttable.column('Gender', width=100)
studenttable.column('Category', width=100)
studenttable.column('Time', width=150)
studenttable.column('Date', width=150)
studenttable.pack(fill=BOTH, expand=1)
####----------------------------------------- Data Frame Ends
#-------------------------------------------------------------------------------------------------- Right Frame end
root.mainloop()
