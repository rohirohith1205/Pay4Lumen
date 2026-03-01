from tkinter import*
from PIL import Image,ImageTk
from Myaccount import MyAcc
from NewConnection1 import NewConnection
from Billing import BillModule
from Inbox import InboxModule

class ElectricbillManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Electricity Bill Management System")
        self.root.geometry("1550x800+0+0")




        self.main_frame = Frame(root, bg="white")
        self.main_frame.place(x=0, y=50, width=1285, height=620)


        #================Image=========================

        img1=Image.open(r"V:\File\Documents\db images\img.jpg")
        img1=img1.resize((1550,200),Image.LANCZOS)
        self.phimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.phimg1,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1550,height=200)

        #================Logo=========================

        img2=Image.open(r"V:\File\Documents\db images\lg.jpg")
        img2=img2.resize((140,140),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.phimg2,bd=0,relief=RIDGE)
        lbimg.place(x=50,y=25,width=140,height=140)



        #================Title=========================

        lb_title=Label(self.root,text="Electricity bill System",width=20,font=("lucida calligraphy",40,"bold"),bg="lime",fg="black",bd=4,relief=RIDGE)
        lb_title.place(x=0,y=205,width=1550,height=80)


        #================Main frame=========================
        self.m_frm=Frame(self.root,bg="peru",bd=4,relief=RIDGE)
        self.m_frm.place(x=0,y=285,width=1550,height=515)


        self.open_frm=Frame(self.root,bd=4,relief=RIDGE)
        self.open_frm.place(x=245,y=290,width=1300,height=515)

        img3=Image.open(r"V:\File\Documents\db images\main img.jpg")
        img3=img3.resize((1310,515),Image.LANCZOS)
        self.phimg3=ImageTk.PhotoImage(img3)

        lbimg=Label(self.open_frm,image=self.phimg3,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1300,height=515)

        #================Menu=========================
        lb_menu=Label(self.m_frm,text="MENU",width=20,font=("times new roman",20,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
        lb_menu.place(x=0,y=0,width=240)

        #================Button frame=========================
        btn_frm=Frame(self.m_frm,bd=4,relief=RIDGE)
        btn_frm.place(x=0,y=35,width=240,height=321)

        home_btn=Button(btn_frm,text="Home",command=self.home_page,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        home_btn.grid(row=0,column=0,pady=1)

        info_btn=Button(btn_frm,text="Slab info",command=self.SlabInfo,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        info_btn.grid(row=1,column=0,pady=1)

        myacc_btn=Button(btn_frm,text="Customer",command=self.acc_details,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        myacc_btn.grid(row=2,column=0,pady=1)

        conn_btn=Button(btn_frm,text="New Connection",command=self.new_connection,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        conn_btn.grid(row=3,column=0,pady=1)


        bill_btn=Button(btn_frm,text="Bill",command=self.load_billing,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        bill_btn.grid(row=4,column=0,pady=1)


        inbox_btn=Button(btn_frm,text="Inbox",command=self.inbox,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        inbox_btn.grid(row=5,column=0,pady=1)

        log_btn=Button(btn_frm,text="Logout",command=self.logout,width=20,font=("times new roman",14,"bold"),bg="grey",fg="white",bd=4,relief= RIDGE,activebackground="grey",activeforeground="white",cursor="hand2")
        log_btn.grid(row=6,column=0,pady=1)



        #============================thunderbolt============================
        img_side=Image.open(r"V:\File\Documents\db images\side.jpg")
        img_side=img_side.resize((240,185),Image.LANCZOS)
        self.phimg_side=ImageTk.PhotoImage(img_side)

        lbside=Label(self.m_frm,image=self.phimg_side,bd=0,relief=RIDGE)
        lbside.place(x=0,y=357,width=240,height=185)




    def home_page(self):
        for widget in self.open_frm.winfo_children():
            widget.destroy()
        img3=Image.open(r"V:\File\Documents\db images\main img.jpg")
        img3=img3.resize((1310,515),Image.LANCZOS)
        self.phimg3=ImageTk.PhotoImage(img3)

        lbimg=Label(self.open_frm,image=self.phimg3,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1300,height=515)

        



    def acc_details(self):
        for widget in self.open_frm.winfo_children():
            widget.destroy()
        MyAcc(self.open_frm)




    def new_connection(self):
        for widget in self.open_frm.winfo_children():
            widget.destroy()
        NewConnection(self.open_frm)



    def load_billing(self):
        for widget in self.open_frm.winfo_children():
            widget.destroy()
        BillModule(self.open_frm)



    def inbox(self):
        for widget in self.open_frm.winfo_children():
            widget.destroy()
        InboxModule(self.open_frm)


    def logout(self):
        self.root.destroy()





    def SlabInfo(self):

        for widget in self.open_frm.winfo_children():
            widget.destroy()

        #=================================================================================================
        self.frm1=Frame(self.open_frm,bg="black",bd=4,relief=RIDGE)
        self.frm1.place(x=0,y=0,width=433,height=515)

        resi_title=Label(self.frm1,text="Residential",width=20,font=("lucida calligraphy",20,"bold"),bg="blue",fg="yellow",bd=4,relief=RIDGE)
        resi_title.pack(fill=X, pady=(0, 10))

        self.frm2=Frame(self.open_frm,bg="black",bd=4,relief=RIDGE)
        self.frm2.place(x=433,y=0,width=434,height=515)

        commercial_title=Label(self.frm2,text="Commercial",width=20,font=("lucida calligraphy",20,"bold"),bg="blue",fg="yellow",bd=4,relief=RIDGE)
        commercial_title.pack(fill=X, pady=(0, 10))

        self.frm3=Frame(self.open_frm,bg="black",bd=4,relief=RIDGE)
        self.frm3.place(x=867,y=0,width=433,height=515)

        Indus_title=Label(self.frm3,text="Industrial",width=20,font=("lucida calligraphy",20,"bold"),bg="blue",fg="yellow",bd=4,relief=RIDGE)
        Indus_title.pack(fill=X, pady=(0, 10))


        #===============================================================================

        Label(self.frm1, fg="red", bg="black", text="Slab Rates", font=("arial", 18, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
        Label(self.frm1, fg="deepskyblue", bg="black", text="0–200 units: ₹3.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm1, fg="deepskyblue", bg="black", text="201–400 units: ₹5.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm1, fg="deepskyblue", bg="black", text="401–800 units: ₹6.50/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm1, fg="deepskyblue", bg="black", text="801–1200 units: ₹7.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm1, fg="deepskyblue", bg="black", text="Above 1200 units: ₹8.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)



        #==============================================================================
        Label(self.frm2, fg="red", bg="black", text="Slab Rates", font=("arial", 18, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
        Label(self.frm2, fg="deepskyblue", bg="black", text="0–200 units: ₹4.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm2, fg="deepskyblue", bg="black", text="201–400 units: ₹6.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm2, fg="deepskyblue", bg="black", text="401–800 units: ₹7.50/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm2, fg="deepskyblue", bg="black", text="801–1200 units: ₹8.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm2, fg="deepskyblue", bg="black", text="Above 1200 units: ₹9.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)


        #==============================================================================
        Label(self.frm3, fg="red", bg="black", text="Slab Rates", font=("arial", 18, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
        Label(self.frm3, fg="deepskyblue", bg="black", text="0–200 units: ₹5.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm3, fg="deepskyblue", bg="black", text="201–400 units: ₹7.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm3, fg="deepskyblue", bg="black", text="401–800 units: ₹8.50/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm3, fg="deepskyblue", bg="black", text="801–1200 units: ₹9.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)
        Label(self.frm3, fg="deepskyblue", bg="black", text="Above 1200 units: ₹10.00/unit", font=("arial", 14)).pack(anchor=W, padx=20)





#================================================================================================================================================

if __name__=="__main__":
    root=Tk()
    obj=ElectricbillManagementSystem(root)
    root.mainloop()