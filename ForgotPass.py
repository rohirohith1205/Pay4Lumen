from tkinter import *
from tkinter import ttk ,messagebox
import pymysql

class Fg_pass:
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot password")
        self.root.geometry("500x500")


        #variables
        self.var_un=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()


    #+++++++++++++++++++++++++++frame++++++++++++++++++++++++++++++++++++++
        frm=Frame(self.root,bg="black")
        frm.place(x=0,y=0,width=500,height=500)

        title_str=Label(frm,text="Change Password",font=("lucida calligraphy",20,"bold"),fg="red",bg="black")
        title_str.place(x=65,y=10)
        
        #username
        username=lbl=Label(frm,text="User name:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        username.place(x=30,y=50)

        self.ent_un=ttk.Entry(frm,textvariable=self.var_un,font=("times new roman",15,"bold"))
        self.ent_un.place(x=30,y=80,width=270)


        #Security q
        sec_que=Label(frm,text="Security question:",font=("lucida calligraphy",15,"bold"),fg="white",bg="black")
        sec_que.place(x=30,y=120)

        cmb_sec_que=ttk.Combobox(frm,textvariable=self.var_secQ,font=("times new roman",15,"bold"),width=20,state="readonly")
        cmb_sec_que["value"]=("*","Birth place","Girl friend","Pet name")
        cmb_sec_que.current(0)
        cmb_sec_que.place(x=30,y=150,width=270)

        #Security ans
        sec_ans=lbl=Label(frm,text="security answer:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        sec_ans.place(x=30,y=190)

        self.ent_sec_ans=ttk.Entry(frm,textvariable=self.var_secA,font=("times new roman",15,"bold"))
        self.ent_sec_ans.place(x=30,y=220,width=270)


        #Password
        psw=lbl=Label(frm,text="New Password:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        psw.place(x=30,y=260)

        self.ent_psw=ttk.Entry(frm,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.ent_psw.place(x=30,y=290,width=270)

        #confirm Password
        cfm_pass=lbl=Label(frm,text="Confirm Password:",font=("lucida calligraphy",15,"bold"),fg="White",bg="black")
        cfm_pass.place(x=30,y=330)

        self.ent_cfm=ttk.Entry(frm,textvariable=self.var_cpass,font=("times new roman",15,"bold"))
        self.ent_cfm.place(x=30,y=360,width=270)

        #reset button
        btn_reset = Button(frm, text="Reset Password", font=("Arial", 12, "bold"),
                           bg="blue", fg="white", command=self.for_pass)
        btn_reset.place(x=150, y=420, width=200)



    def for_pass(self):
        if (self.var_un.get() == "" or
            self.var_secQ.get() == "*" or
            self.var_secA.get() == "" or
            self.var_pass.get() == "" or
            self.var_cpass.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        if self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            cur = conn.cursor()
            cur.execute("SELECT * FROM register WHERE username=%s AND SecurityQ=%s AND SecurityA=%s",
                        (self.var_un.get(), self.var_secQ.get(), self.var_secA.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Incorrect security details", parent=self.root)
            else:
                cur.execute("UPDATE register SET password=%s WHERE username=%s",
                            (self.var_pass.get(), self.var_un.get()))
                conn.commit()
                messagebox.showinfo("Success", "Password reset successfully", parent=self.root)
                self.root.destroy()

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)




if __name__=="__main__":
    root=Tk()
    app=Fg_pass(root)
    root.mainloop()

