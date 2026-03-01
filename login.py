from tkinter import *
from tkinter import ttk ,messagebox
from PIL import Image , ImageTk
import pymysql
from ElectricityBill import ElectricbillManagementSystem
from Register import Register
from ForgotPass import Fg_pass


class login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1545x810+0+0")


        #++++++++++++++++++++++++++++varible+++++++++++++++++++++++++
        self.var_un=StringVar()
        self.var_pass=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()


       


        #=======================background======================================
        lg_bg=Image.open(r"V:\File\Documents\db images\login bg.jpg")
        lg_bg=lg_bg.resize((1550,800),Image.LANCZOS)
        self.phimg=ImageTk.PhotoImage(lg_bg)

        lbimg=Label(self.root,image=self.phimg,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1550,height=800)

        #++++++++++++++++++++++++++++logo++++++++++++++++++++++++++++++++++++
        logo=Image.open(r"V:\File\Documents\db images\lg.jpg")
        logo=logo.resize((140,140),Image.LANCZOS)
        self.phimg_logo=ImageTk.PhotoImage(logo)
        lb_logo=Label(self.root,image=self.phimg_logo,relief=RIDGE)
        lb_logo.place(x=500,y=100,width=140,height=140)

        #++++++++++++++++++++++++frame+++++++++++++++++++++++++++++++++++++++++++
        frm=Frame(self.root,bg="black")
        frm.place(x=940,y=320,width=340,height=450)



        #+++++++++++++++++++++++logo+++++++++++++++++++++++++++++++++++++++++
        img1=Image.open(r"V:\File\Documents\db images\login lg.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.phimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.phimg1,bd=0,relief=RIDGE)
        lbimg.place(x=1060,y=325,width=100,height=100)


        get_str=Label(frm,text="Get Started",font=("lucida calligraphy",20,"bold"),fg="red",bg="black")
        get_str.place(x=95,y=100)


        username=lbl=Label(frm,text="User Name:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        username.place(x=75,y=155)

        self.ent_usr=ttk.Entry(frm,font=("times new roman",15,"bold"))
        self.ent_usr.place(x=40,y=180,width=270)


        password=lbl=Label(frm,text="Password:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        password.place(x=75,y=225)


        self.ent_pass=ttk.Entry(frm,show="🤔",font=("Segoe UI Emoji", 15))
        self.ent_pass.place(x=40,y=250,width=270)

        #icons+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        img2=Image.open(r"V:\File\Documents\db images\login lg.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(img2)

        lbimg2=Label(self.root,image=self.phimg2,bd=0,relief=RIDGE)
        lbimg2.place(x=990,y=473,width=25,height=25)


        img3=Image.open(r"V:\File\Documents\db images\icon2.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.phimg3=ImageTk.PhotoImage(img3)

        lbimg3=Label(self.root,image=self.phimg3,bd=0,relief=RIDGE)
        lbimg3.place(x=990,y=540,width=25,height=25)

        #login btn ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        login_btn=Button(frm,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,fg="white",bg="blue",relief=RIDGE,activebackground="blue",activeforeground="white",cursor="hand2")
        login_btn.place(x=110,y=300,width=120,height=35)

        #Register btn +++++++++++++++++++++++++++++++++++++++++++++++++++++

        reg_btn=Button(frm,text="Register",command=self.reg,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
        reg_btn.place(x=20,y=350,width=160)

        #forgot password ++++++++++++++++++++++++++++++++++++++++++++++++++
        fgpass_btn=Button(frm,text="Forgot password",command=self.fg,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white",cursor="hand2")
        fgpass_btn.place(x=20,y=370,width=160)





    def login(self):
        # Check if input fields are empty
        if self.ent_usr.get() == "" or self.ent_pass.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        
        # Hardcoded admin login
        elif self.ent_usr.get() == "abcd" and self.ent_pass.get() == "1234":
            messagebox.showinfo("Success", "Login Successful",parent=self.root)
        
        else:
            try:
                # Connect to MySQL
                conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
                my_cur = conn.cursor()

                # Use the actual entry values

                
                my_cur.execute("SELECT * FROM register WHERE username=%s AND password=%s", (
                    self.ent_usr.get(),
                    self.ent_pass.get()
                ))

                row = my_cur.fetchone()  # fetchone is better here since you're checking login

                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password",parent=self.root)
                else:
                    
                    self.root.destroy()
                    new_root = Tk()
                    self.app1 = ElectricbillManagementSystem(new_root)
                    new_root.mainloop()

                conn.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}",parent=self.root)

                
                

    def reg(self):
        self.new_win1=Toplevel(self.root)
        self.app2=Register(self.new_win1)


    def fg(self):
        self.new_win2=Toplevel(self.root)
        self.app3=Fg_pass(self.new_win2)



    def des_log(self):
        self.root.destroy()








if __name__=="__main__":
    root=Tk()
    app=login_win(root)
    root.mainloop()


