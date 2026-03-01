from tkinter import *
from tkinter import ttk ,messagebox
from PIL import Image , ImageTk
import pymysql



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        #+++++++++++++++++++++variables++++++++++++++++++++++++++++++++++++++

        self.var_fn=StringVar()
        self.var_ln=StringVar()
        self.var_un=StringVar()
        self.var_cnt=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()







        #+++++++++++++++++background+++++++++++++++++++++++++++++++++++++++++++++
        
        reg_bg=Image.open(r"V:\File\Documents\db images\reg bg.jpg")
        reg_bg=reg_bg.resize((1550,800),Image.LANCZOS)
        self.phimg=ImageTk.PhotoImage(reg_bg)

        regimg=Label(self.root,image=self.phimg,relief=RIDGE)
        regimg.place(x=0,y=0,width=1550,height=800)


        


        #++++++++++++++++++++++++++++frm image+++++++++++++++++++++++++++++++++++++
        reg_1=Image.open(r"V:\File\Documents\db images\reg 2.jpeg")
        reg_1=reg_1.resize((900,300),Image.LANCZOS)
        self.phimg1=ImageTk.PhotoImage(reg_1)

        regimg=Label(self.root,image=self.phimg1,relief=RIDGE)
        regimg.place(x=650,y=250,width=900,height=300)

        #++++++++++++++++++++++++++++frame++++++++++++++++++++++++++++++++++++++++++
        frm=Frame(self.root,bg="Black")
        frm.place(x=650,y=450,width=900,height=350)


        #labels++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++========

        #first name
        firstname=lbl=Label(frm,text="First name:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        firstname.place(x=50,y=20)

        self.ent_fn=ttk.Entry(frm,textvariable=self.var_fn,font=("times new roman",15,"bold"))
        self.ent_fn.place(x=50,y=50,width=270)


        #Last name
        lastname=lbl=Label(frm,text="Last name:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        lastname.place(x=500,y=20)

        self.ent_ln=ttk.Entry(frm,textvariable=self.var_ln,font=("times new roman",15,"bold"))
        self.ent_ln.place(x=500,y=50,width=270)
      
        #Username
        username=lbl=Label(frm,text="User name:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        username.place(x=50,y=90)

        self.ent_un=ttk.Entry(frm,textvariable=self.var_un,font=("times new roman",15,"bold"))
        self.ent_un.place(x=50,y=120,width=270)

        #Contact
        cnt=lbl=Label(frm,text="Contact:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        cnt.place(x=500,y=90)

        self.ent_cnt=ttk.Entry(frm,textvariable=self.var_cnt,font=("times new roman",15,"bold"))
        self.ent_cnt.place(x=500,y=120,width=270)

        #Password
        psw=lbl=Label(frm,text="Password:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        psw.place(x=50,y=160)

        self.ent_psw=ttk.Entry(frm,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.ent_psw.place(x=50,y=190,width=270)

        #confirm Password
        cfm_pass=lbl=Label(frm,text="Confirm Password:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        cfm_pass.place(x=500,y=160)

        self.ent_cfm=ttk.Entry(frm,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        self.ent_cfm.place(x=500,y=190,width=270)

        #Select sec qtn
        sec_que=Label(frm,text="Security question:",font=("lucida calligraphy",15,"bold"),fg="white",bg="black")
        sec_que.place(x=50,y=230)

        cmb_sec_que=ttk.Combobox(frm,textvariable=self.var_secQ,font=("times new roman",15,"bold"),width=20,state="readonly")
        cmb_sec_que["value"]=("*","Birth place","Girl friend","Pet name")
        cmb_sec_que.current(0)
        cmb_sec_que.place(x=50,y=260,width=270)

        #Security ans
        sec_ans=lbl=Label(frm,text="security answer:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        sec_ans.place(x=500,y=230)

        self.ent_sec_ans=ttk.Entry(frm,textvariable=self.var_secA,font=("times new roman",15,"bold"))
        self.ent_sec_ans.place(x=500,y=260,width=270)



        btn_img1=Image.open(r"V:\File\Documents\db images\reg btn.jpg")
        btn_img1=btn_img1.resize((200,50),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(btn_img1)
        b1=Button(frm,image=self.phimg2,command=self.reg_data,borderwidth=0,cursor="hand2")
        b1.place(x=250,y=300,width=200)


        btn_img2=Image.open(r"V:\File\Documents\db images\login btn.jpg")
        btn_img2=btn_img2.resize((200,50),Image.LANCZOS)
        self.phimg3=ImageTk.PhotoImage(btn_img2)
        b2=Button(frm,image=self.phimg3,command=self.log,borderwidth=0,cursor="hand2")
        b2.place(x=550,y=300,width=200)



    #+++++++++++++++++++++++++++++++++register data++++++++++++++++++++++++++++++++++++
    def reg_data(self):
        if self.var_fn.get()=="" or self.var_un.get()=="" or self.var_secQ.get()=="*":
            messagebox.showerror("Error","All Entries fills are required",parent=self.root)
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Passwords entered must be same",parent=self.root)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
            my_cur=conn.cursor()
            query=("SELECT * FROM register where username=%s")
            value=(self.var_un.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists try another name",parent=self.root)
            else:
                my_cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fn.get(),
                    self.var_ln.get(),
                    self.var_un.get(),
                    self.var_cnt.get(),
                    self.var_pass.get(),
                    self.var_secQ.get(),
                    self.var_secA.get()
                ))
            
                conn.commit()
                messagebox.showinfo("Success","Registration successfull",parent=self.root)
            conn.close()





    def log(self):
        self.root.destroy()









if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()