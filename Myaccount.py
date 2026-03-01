from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import random
from tkinter import messagebox



class MyAcc:
    def __init__(self,parent):
        self.parent=parent
        



        #============================variables===============================
        self.var_id=StringVar()
        x=random.randint(1000,9999)
        self.var_id.set(str(x))

        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_addre=StringVar()
        self.var_mob=StringVar()
        self.var_gdr=StringVar()




        #================Title=========================

        lb_title=Label(self.parent,text="Customer Details",width=20,font=("lucida calligraphy",20,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        lb_title.place(x=0,y=0,width=1295,height=50)


        #================Logo=========================

        img2=Image.open(r"V:\File\Documents\db images\lg.jpg")
        img2=img2.resize((50,50),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.parent,image=self.phimg2,relief=RIDGE)
        lbimg.place(x=0,y=0,width=50,height=50)



#=================================================================================================================================================




        #====================label frame ========================

        lbl_frm=LabelFrame(self.parent,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        lbl_frm.place(x=5,y=50,height=420,width=400)



        #==================== label and entry ====================
        #Name
        cust_name=Label(lbl_frm,text="Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_name.grid(row=0,column=0,sticky=W)

        ent_name=ttk.Entry(lbl_frm,textvariable=self.var_name,width=22,font=("times new roman",12,"bold"))
        ent_name.grid(row=0,column=1)


        #Age
        cust_age=Label(lbl_frm,text="Age:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_age.grid(row=2,column=0,sticky=W)

        ent_age=ttk.Entry(lbl_frm,textvariable=self.var_age,width=22,font=("times new roman",12,"bold"))
        ent_age.grid(row=2,column=1)

        #Gender 
        cust_gdr=Label(lbl_frm,text="Gender:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_gdr.grid(row=5,column=0,sticky=W)

        cmb_gdr=ttk.Combobox(lbl_frm,font=("times new roman",12,"bold"),textvariable=self.var_gdr,width=20,state="readonly")
        cmb_gdr["value"]=("*","Male","Female")
        cmb_gdr.current(0)
        cmb_gdr.grid(row=5,column=1)



        #contact
        cust_cnt=Label(lbl_frm,text="Phone number:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_cnt.grid(row=3,column=0,sticky=W)

        ent_cnt=ttk.Entry(lbl_frm,textvariable=self.var_mob,width=22,font=("times new roman",12,"bold"))
        ent_cnt.grid(row=3,column=1)


        #Address
        cust_ads=Label(lbl_frm,text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_ads.grid(row=4,column=0,sticky=W)

        ent_ads=ttk.Entry(lbl_frm,textvariable=self.var_addre,width=22,font=("times new roman",12,"bold"))
        ent_ads.grid(row=4,column=1)



        #ID
        cust_id=Label(lbl_frm,text="User Id:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cust_id.grid(row=1,column=0,sticky=W)

        ent_id=ttk.Entry(lbl_frm,textvariable=self.var_id,width=22,font=("times new roman",12,"bold"),state="readonly")
        ent_id.grid(row=1,column=1)



#=================================================================================================================================================




        #=====================buttons=============================
        btn_frm=Frame(lbl_frm,bd=2,relief=RIDGE)
        btn_frm.place(x=0,y=300,width=380,height=38)

        #add
        btnAdd=Button(btn_frm,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="grey",fg="white",width=8,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=2)

        #Update
        btnUP=Button(btn_frm,text="Update",command=self.update,font=("arial",12,"bold"),bg="grey",fg="white",width=8,cursor="hand2")
        btnUP.grid(row=0,column=1,padx=2)

        #Delete
        btnDlt=Button(btn_frm,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="grey",fg="white",width=8,cursor="hand2")
        btnDlt.grid(row=0,column=2,padx=2)

        #Reset
        btnRst=Button(btn_frm,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="grey",fg="white",width=8,cursor="hand2")
        btnRst.grid(row=0,column=3,padx=2)



#=================================================================================================================================================



        #==================Table Frame======================
        tbl_frm=LabelFrame(self.parent,bd=2,relief=RIDGE,text="View Details",font=("arial",12,"bold"))
        tbl_frm.place(x=420,y=50,width=850,height=420)


        lblSearch=Label(tbl_frm,font=("arial",12,"bold"),text="Search:",bg="black",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W,padx=2)

        self.var_srh=StringVar()
        cmb_srh=ttk.Combobox(tbl_frm,textvariable=self.var_srh,font=("arial",12,"bold"),width=24,state="readonly")
        cmb_srh["value"]=("*","Name","ID")
        cmb_srh.current(0)
        cmb_srh.grid(row=0,column=1,padx=2)


        self.var_txtsrh=StringVar()
        txt_srh=ttk.Entry(tbl_frm,textvariable=self.var_txtsrh,font=("arial",12,"bold"),width=24)
        txt_srh.grid(row=0,column=2,padx=2)

        btn_srh=Button(tbl_frm,text="Search",command=self.search,font=("arial",12,"bold"),bg="red",fg="white",width=10)
        btn_srh.grid(row=0,column=3,padx=1)

        btn_showall=Button(tbl_frm,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="red",fg="white",width=10)
        btn_showall.grid(row=0,column=4,padx=1)

        #=========================Show table============================



        det_tbl=Frame(tbl_frm,bd=2,relief=RIDGE)
        det_tbl.place(x=5,y=50,width=830,height=340)


        srl_x=Scrollbar(det_tbl,orient=HORIZONTAL)
        srl_y=Scrollbar(det_tbl,orient=VERTICAL)


        self.cust_tbl=ttk.Treeview(det_tbl,column=("Name","ID","Age","Mobile","Address","Gender"),xscrollcommand=srl_x.set,yscrollcommand=srl_y.set)

        srl_x.pack(side=BOTTOM,fill=X)
        srl_y.pack(side=RIGHT,fill=Y)

        srl_x.config(command=self.cust_tbl.xview)
        srl_y.config(command=self.cust_tbl.yview)

        self.cust_tbl.heading("Name",text="Name")
        self.cust_tbl.heading("ID",text="ID")
        self.cust_tbl.heading("Age",text="Age")
        self.cust_tbl.heading("Mobile",text="Mobile")
        self.cust_tbl.heading("Address",text="Address")
        self.cust_tbl.heading("Gender",text="Gender")

        self.cust_tbl["show"]="headings"
        self.cust_tbl.pack(fill=BOTH,expand=1)
        self.cust_tbl.bind("<ButtonRelease-1>",self.get_cur)
        self.fetch_data()



#=================================================================================================================================================

    def add_data(self):
        if self.var_mob.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.parent)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
                my_cur=conn.cursor()
                my_cur.execute("INSERT INTO customers (name,id, age, mobile, address, gender) VALUES (%s, %s, %s, %s, %s, %s)", (

                        self.var_name.get(),
                        self.var_id.get(),
                        self.var_age.get(),
                        self.var_mob.get(),
                        self.var_addre.get(),
                        self.var_gdr.get()
                
                ))
                messagebox.showinfo("Success","Customer details added",parent=self.parent)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.parent)
            
    


    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
        my_cur=conn.cursor()

        my_cur.execute("Select * from customers")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.cust_tbl.delete(*self.cust_tbl.get_children())
            for i in rows:
                self.cust_tbl.insert("",END,values=i)
            conn.commit()
            conn.close()





    def get_cur(self,event=""):
        cur_row=self.cust_tbl.focus()
        content=self.cust_tbl.item(cur_row)
        row=content["values"]

        self.var_name.set(row[0]),
        self.var_id.set(row[1]),
        self.var_age.set(row[2]),
        self.var_mob.set(row[3]),
        self.var_addre.set(row[4]),
        self.var_gdr.set(row[5])




    def update(self):
        if self.var_mob.get()=="":
            messagebox.showerror("Error","PLease enter mobile number",parent=self.parent)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
            my_cur=conn.cursor()
            my_cur.execute("UPDATE customers SET Name=%s, Age=%s, Mobile=%s, Address=%s, Gender=%s WHERE ID=%s",(
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_mob.get(),
                        self.var_addre.get(),
                        self.var_gdr.get(),
                        self.var_id.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Customer details has been updated",parent=self.parent)




    def delete(self):
        delete=messagebox.askyesno("Electricity bill payment","Do you want to delete this customer",parent=self.parent)
        if delete>0:
            conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
            my_cur=conn.cursor()
            query="delete from customers where ID=%s"
            value=(self.var_id.get(),)
            my_cur.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()




    def reset(self):
        self.var_name.set(""),
        self.var_age.set(""),
        self.var_mob.set(""),
        self.var_addre.set(""),
        self.var_gdr.set("")
        x=random.randint(1000,9999)
        self.var_id.set(str(x))



    def search(self):
        conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
        my_cur=conn.cursor()
        query = f"SELECT * FROM customers WHERE {self.var_srh.get()} LIKE %s"
        value = f"%{self.var_txtsrh.get()}%"
        my_cur.execute(query, (value,))

        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.cust_tbl.delete(*self.cust_tbl.get_children())
            for i in rows:
                self.cust_tbl.insert("",END,values=i)
            conn.commit()
        conn.close()




#================================================================================================================================================

if __name__=="__main__":
    root=Tk()
    obj=MyAcc(root)
    root.mainloop()