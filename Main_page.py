import datetime
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#Googlesheet Access initialization
#use creds to create a client to interact with the Google Drive API
scope = ['https://docs.google.com/spreadsheets/d/1kjy22HkvdweK9V_Wa6L2BATzauyYjtOjz14-SEJ-LBg/edit?usp=drive_link',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('attendance.json', scope)
client = gspread.authorize(creds)
# sheet = client.open("Student_Management").sheet1
sheet = client.open("Student_Management").worksheet('Sheet1')
sh2 = client.open("Student_Management").worksheet('Sheet2')
sh3 = client.open("Student_Management").worksheet('Sheet3')
# Creating the universal font variables
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Creating the functions
def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar,Dob_strvar, stream_strvar
    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    DOB = Dob_strvar.get()
    stream = stream_strvar.get()
    list_of_hashes = sheet.get_all_records()
    IDD=list_of_hashes[-1]['ID']+1 
    r=len(list_of_hashes)
    row=[IDD,name,contact,email,gender,str(DOB),stream]
    sheet.insert_row(row,r+2)
    display_records()
    reset_fields()
def display_records():
    tree.delete(*tree.get_children())
    list_of_hashes = sheet.get_all_records()
    # print(len(list_of_hashes))
    # r=len(list_of_hashes)
    for i in list_of_hashes:
        records=list(i.values())
        tree.insert('', END, values=records)
    col_data=sh3.col_values(1)
    # print(col_data) 
    sti='' 
    for j in col_data:
        sti+="{}\n".format(j)  
    Tbox.delete("1.0", "end")    
    Tbox.insert(END,sti)
def view_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    

    name_strvar.set(selection[1]); email_strvar.set(selection[3])
    contact_strvar.set(selection[2]); gender_strvar.set(selection[4])
    Dob_strvar.set(selection[5]); stream_strvar.set(selection[6])
def reset_fields():
    global name_strvar, email_strvar, contact_strvar, gender_strvar,Dob_strvar, stream_strvar

    for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar','Dob_strvar', 'stream_strvar']:
        exec(f"{i}.set('')")
def delete_record():  
    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]
    idd=selection[0] 
    print(idd)  
    list_of_hashes = sheet.get_all_records()
    for i in range (0,len(list_of_hashes)):
        if(list_of_hashes[i]['ID']==idd):
            sheet.delete_row(i+2)
            break

    
    display_records()
def upload_result():
    
    f = tkinter.filedialog.askopenfilename(
        parent=main, initialdir='',
        title='Choose file',
        filetypes=[('Text file','.txt')]
        )
    list_of_hashes = sh2.get_all_records()
    r=len(list_of_hashes)
    ff=open(f,'r')
    ld=[]
    for i in ff:
        sh2.append_row(i.split())
def upload_note():
    dd=Tbox.get(1.0, "end-1c")
    print(dd)
    sh3.append_row([dd])
def clear_note():
    sh3.clear()

# Initializing the GUI window
main = Tk()
main.title('School Management System')
main.geometry('1000x600')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = 'DarkSlateGray1' # bg color for the left_frame
cf_bg = 'DarkSlateBlue' # bg color for the center_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
Dob_strvar=StringVar()
stream_strvar = StringVar()

# Placing the components in the main window
Label(main, text="SCHOOL MANAGEMENT SYSTEM", font=headlabelfont, bg='DarkOliveGreen1').pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.44)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)
Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.7)

Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.36)
Entry(left_frame, width=19, textvariable=Dob_strvar, font=entryfont).place(x=20, rely=0.62)
Entry(left_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=20, rely=0.75)

OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.49, relwidth=0.5)

# dob = DateEntry(left_frame, font=("Arial", 12), width=15)
# dob.place(x=20, rely=0.62)

Button(left_frame, text='Submit and Add Record', font=labelfont,command=add_record, width=18).place(relx=0.025, rely=0.85)

# Placing components in the center frame
Button(center_frame, text='Delete Record', font=labelfont,command=delete_record, width=15).place(relx=0.1, rely=0.25)
Button(center_frame, text='View Record', font=labelfont,command=view_record , width=15).place(relx=0.1, rely=0.35)
Button(center_frame, text='Reset Fields', font=labelfont,command=reset_fields,  width=15).place(relx=0.1, rely=0.45)
Button(center_frame, text='Upload Result', font=labelfont,command=upload_result, width=15).place(relx=0.1, rely=0.55)
Button(center_frame, text='Upload Notification', font=labelfont,command=upload_note, width=15).place(relx=0.1, rely=0.65)
Button(center_frame, text='Clear Notification', font=labelfont,command=clear_note, width=15).place(relx=0.1, rely=0.75)
Tbox=Text(center_frame, height=8, width=20)
Tbox.place(x=20,y=10)
# Placing components in the right frame
Label(right_frame, text='Students Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)

tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=("ID","Name","Contact Number", "Email Address",  "Gender", "Date of Birth", "Stream"))

X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=80, stretch=NO)
tree.column('#4', width=200, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)


tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

display_records()
def run_app():
    main.update()
    main.mainloop()

if __name__ == '__main__':
    run_app()