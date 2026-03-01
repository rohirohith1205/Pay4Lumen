from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk


class New_con:
    def __init__(self,root):
        self.root=root
        self.root.title("New Connection")
        self.root.geometry("1285x470+244+312")



        #================Title=========================

        lb_title=Label(self.root,text="New Connection",width=20,font=("lucida calligraphy",20,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        lb_title.place(x=0,y=0,width=1295,height=50)


        #================Logo=========================

        img2=Image.open(r"V:\File\Documents\db images\lg.jpg")
        img2=img2.resize((50,50),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.phimg2,relief=RIDGE)
        lbimg.place(x=0,y=0,width=50,height=50)



        #====================label frame ========================

        lbl_frm=LabelFrame(self.root,bd=2,relief=RIDGE,text="Connection Details",font=("times new roman",12,"bold"),padx=2)
        lbl_frm.place(x=5,y=50,height=420,width=400)



        #======================== label and entry ========================  

        #Connection id 
        conn_id=Label(lbl_frm,text="Connection ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        conn_id.grid(row=0,column=0,sticky=W)

        ent_id=ttk.Entry(lbl_frm,width=22,font=("times new roman",12,"bold"))
        ent_id.grid(row=0,column=1)

        #User id
        conn_uid=Label(lbl_frm,text="User ID:",font=("times new roman",12,"bold"),padx=2,pady=6)
        conn_uid.grid(row=1,column=0,sticky=W)

        ent_uid=ttk.Entry(lbl_frm,width=22,font=("times new roman",12,"bold"))
        ent_uid.grid(row=1,column=1)


        #connection type 
        conn_tp=Label(lbl_frm,text="Connection Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        conn_tp.grid(row=2,column=0,sticky=W)

        cmb_tp=ttk.Combobox(lbl_frm,font=("times new roman",12,"bold"),width=20,state="readonly")
        cmb_tp["value"]=("*","Commercial","Residential")
        cmb_tp.current(0)
        cmb_tp.grid(row=2,column=1)

        #Load 
        conn_load=Label(lbl_frm,text="Load Required(in KW):",font=("times new roman",12,"bold"),padx=2,pady=6)
        conn_load.grid(row=3,column=0,sticky=W)

        ent_load=ttk.Entry(lbl_frm,width=22,font=("times new roman",12,"bold"))
        ent_load.grid(row=3,column=1)

        #House address
        conn_addre=Label(lbl_frm,text="Load Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        conn_addre.grid(row=4,column=0,sticky=W)

        ent_addre=ttk.Entry(lbl_frm,width=22,font=("times new roman",12,"bold"))
        ent_addre.grid(row=4,column=1)
























if __name__=="__main__":
    root=Tk()
    obj=New_con(root)
    root.mainloop()