from tkinter import *
from tkinter import messagebox
import gspread

from oauth2client.service_account import ServiceAccountCredentials
#Googlesheet Access initialization
#use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds'
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('attendance.json"', scope)
client = gspread.authorize(creds)
sh2 = client.open("Student_Management").worksheet('Sheet2')
sh3 = client.open("Student_Management").worksheet('Sheet3')
list_of_hashes = sh2.get_all_records()
col_data=sh2.col_values(2)
dip_val=sh2.col_values(9)
# print(col_data)
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Managment System")
        self.root.geometry("1350x700+0+0")
        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=450,y=150 ,height=500)

        self.user=StringVar()
        self.password=StringVar()

        title=Label(F1,text="   Login Ststem",font=("times new roman",30,"bold")).grid(row=0,columnspan=2,pady=20)

        lblusername=Label(F1,text="UserName",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=10)
        txtuser=Entry(F1,bd=7,relief=GROOVE,textvariable=self.user,width=25,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)


        lblpass=Label(F1,text="Password",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=10)
        txtpass=Entry(F1,bd=7,relief=GROOVE,show="*",textvariable=self.password,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnlog=Button(F1,text="Admin Login",font="arial 15 bold",bd=7,width=10,command=self.logfun).place(x=10,y=250)
        btnreset=Button(F1,text="Student Login",font="arial 15 bold",bd=7,width=12,command=self.logfun1).place(x=170,y=250)
        # btnexit=Button(F1,text="Exit",font="arial 15 bold",bd=7,command=self.exit_fun,width=10,).place(x=320,y=250)
        note_l=Label(F1,text="Notification:",font=("times new roman",20,"bold")).grid(row=5,columnspan=1,pady=100)
        self.Mbox=Text(F1, height=5, width=30)
        self.Mbox.place(x=10,y=370)
      
        

    def logfun(self):
        if self.user.get()=="admin" and self.password.get()=="admin":
            self.root.destroy()
            import Main_page
            Main_page.run_app()
                   
        else:
            messagebox.showerror("Error","Invalid username or password")
    def logfun1(self):
        User=self.user.get()
        # if User=="pp" and self.password.get()=="1234":
        if User in col_data:
            self.root.destroy()
            import Student_page
            Student_page.run_app(User)
                   
        else:
            messagebox.showerror("Error","Invalid username or password")        
    def reset(self):
        self.user.set("")
        self.password.set("")


    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you really want to Exit ?")
        if option>0:
            self.root.destroy()
        else:
            return

    def Note(self):
          cd=sh3.col_values(1)
          sti='' 
          for j in cd:
            sti+="{}\n".format(j)  
          self.Mbox.delete("1.0", "end")    
          self.Mbox.insert(END,sti)

root=Tk()
ob=Login(root)
ob.Note()
root.mainloop()

