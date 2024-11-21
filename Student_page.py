import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#Googlesheet Access initialization
#use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('attendance.json', scope)
client = gspread.authorize(creds)
sh2 = client.open("Student_Management").worksheet('Sheet2')
list_of_hashes = sh2.get_all_records()
ll=0
sb=0


# Creating the universal font variables
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Creating the functions
# def add_record():
#     global name_strvar, email_strvar, contact_strvar, gender_strvar,Dob_strvar, stream_strvar
#     name = name_strvar.get()
#     email = email_strvar.get()
#     contact = contact_strvar.get()
#     gender = gender_strvar.get()
#     DOB = Dob_strvar.get()
#     stream = stream_strvar.get()
#     list_of_hashes = sheet.get_all_records()
#     IDD=list_of_hashes[-1]['ID']+1 
#     r=len(list_of_hashes)
#     row=[IDD,name,contact,email,gender,str(DOB),stream]
#     sheet.insert_row(row,r+2)
#     display_records()
#     reset_fields()
def display_records(data,sb):
    mark=data[2:7]
    sub=sb[2:7]
    tm=0
    st="Name:{}\nRoll No:{}\n".format(data[1],data[0])
    st+="-----------------------------------------------------------------\n"
    st+="Sr.No     Subject         Marks          Percentage \n"
    st+="-----------------------------------------------------------------\n"
    for k in range(0,len(mark)):
        st+="{}      {}            {}                     -  \n".format(k+1,sub[k],mark[k])
        tm+=int(mark[k])
    st+="-----------------------------------------------------------------\n"
    st+="          Total Marks=    {}                   {}%           ".format(tm,data[7])

    Tbox.insert(END,st)
def Read_result(Nm):
    for i in list_of_hashes:
        if(i['Name']==Nm):
            ll=list(i.values())
            sb=list(i.keys())
            break
    return [ll,sb]
# def view_record():
#     global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

#     current_item = tree.focus()
#     values = tree.item(current_item)
#     selection = values["values"]

    

#     name_strvar.set(selection[1]); email_strvar.set(selection[3])
#     contact_strvar.set(selection[2]); gender_strvar.set(selection[4])
#     Dob_strvar.set(selection[5]); stream_strvar.set(selection[6])
# def reset_fields():
#     global name_strvar, email_strvar, contact_strvar, gender_strvar,Dob_strvar, stream_strvar

#     for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar','Dob_strvar', 'stream_strvar']:
#         exec(f"{i}.set('')")
# def delete_record():  
#     current_item = tree.focus()
#     values = tree.item(current_item)
#     selection = values["values"]
#     idd=selection[0] 
#     print(idd)  
#     list_of_hashes = sheet.get_all_records()
#     for i in range (0,len(list_of_hashes)):
#         if(list_of_hashes[i]['ID']==idd):
#             sheet.delete_row(i+2)
#             break

    
#     display_records()


# Initializing the GUI window
main = Tk()
main.title('School Management System')
main.geometry('700x600')
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
Label(main, text="Result Display", font=headlabelfont, bg='DarkOliveGreen1').pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

# center_frame = Frame(main, bg=cf_bg)
# center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.8)

Tbox=Text(right_frame, height=100, width=200)
Tbox.pack()
# display_records()
def run_app(nn):
    main.update()
    data=Read_result(nn)
    display_records(data[0],data[1])
    main.mainloop()

if __name__ == '__main__':
    run_app('pp')