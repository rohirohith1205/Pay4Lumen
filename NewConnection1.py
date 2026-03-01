from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import random
from datetime import datetime

class NewConnection:
    def __init__(self, parent):
        self.parent = parent
        

        # ========================== Variables ==============================
        self.var_conn_id = StringVar()
        x = random.randint(10000, 99999)
        self.var_conn_id.set(str(x))

        self.var_cust_id = StringVar()
        self.var_conn_type = StringVar()
        self.var_load = StringVar()
        self.var_address = StringVar()
        self.var_date = StringVar(value=datetime.now().strftime("%Y-%m-%d"))

        # ========================== Title ==============================
        title_lbl = Label(self.parent, text="New Connection", font=("lucida calligraphy", 20, "bold"), bg="black", fg="yellow", bd=4, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1295, height=50)


        #================Logo=========================

        img2=Image.open(r"V:\File\Documents\db images\lg.jpg")
        img2=img2.resize((50,50),Image.LANCZOS)
        self.phimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.parent,image=self.phimg2,relief=RIDGE)
        lbimg.place(x=0,y=0,width=50,height=50)

        # ========================== Form Frame ==============================
        frm = LabelFrame(self.parent, text="Connection Details", font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        frm.place(x=5, y=50, width=400, height=420)

        # Labels and Entries
        Label(frm, text="Connection ID:", font=("times new roman", 12, "bold")).grid(row=0, column=0, sticky=W, padx=2, pady=6)
        Entry(frm, textvariable=self.var_conn_id, font=("times new roman", 12), state="readonly").grid(row=0, column=1)

        Label(frm, text="Customer ID:", font=("times new roman", 12, "bold")).grid(row=1, column=0, sticky=W, padx=2, pady=6)
        Entry(frm, textvariable=self.var_cust_id, font=("times new roman", 12)).grid(row=1, column=1)

        Label(frm, text="Type:", font=("times new roman", 12, "bold")).grid(row=2, column=0, sticky=W, padx=2, pady=6)
        combo_type = ttk.Combobox(frm, textvariable=self.var_conn_type, font=("times new roman", 12), state="readonly")
        combo_type["values"] = ("*", "Residential", "Commercial", "Industrial")
        combo_type.current(0)
        combo_type.grid(row=2, column=1)

        Label(frm, text="Load (kW):", font=("times new roman", 12, "bold")).grid(row=3, column=0, sticky=W, padx=2, pady=6)
        Entry(frm, textvariable=self.var_load, font=("times new roman", 12)).grid(row=3, column=1)

        

        Label(frm, text="Address:", font=("times new roman", 12, "bold")).grid(row=4, column=0, sticky=W, padx=2, pady=6)
        Entry(frm, textvariable=self.var_address, font=("times new roman", 12)).grid(row=4, column=1)

        Label(frm, text="Date:", font=("times new roman", 12, "bold")).grid(row=5, column=0, sticky=W, padx=2, pady=6)
        Entry(frm, textvariable=self.var_date, font=("times new roman", 12)).grid(row=5, column=1)

        # ========================== Buttons ==============================
        btn_frame = Frame(frm, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=380, height=38)

        Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="grey", fg="white", width=8).grid(row=0, column=0, padx=2)
        Button(btn_frame, text="Update", command=self.update_data, font=("arial", 12, "bold"), bg="grey", fg="white", width=8).grid(row=0, column=1, padx=2)
        Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), bg="grey", fg="white", width=8).grid(row=0, column=2, padx=2)
        Button(btn_frame, text="Reset", command=self.reset_fields, font=("arial", 12, "bold"), bg="grey", fg="white", width=8).grid(row=0, column=3, padx=2)

        # ========================== Table Frame ==============================
        table_frame = LabelFrame(self.parent, bd=2, relief=RIDGE, text="View Connections", font=("arial", 12, "bold"))
        table_frame.place(x=420, y=50, width=850, height=420)


        srl_x=Scrollbar(table_frame,orient=HORIZONTAL)
        srl_y=Scrollbar(table_frame,orient=VERTICAL)

        self.conn_table = ttk.Treeview(table_frame, columns=("id", "cust_id", "type", "load", "address", "date"), show="headings",xscrollcommand=srl_x.set,yscrollcommand=srl_y.set)
        srl_x.pack(side=BOTTOM,fill=X)
        srl_y.pack(side=RIGHT,fill=Y)

        srl_x.config(command=self.conn_table.xview)
        srl_y.config(command=self.conn_table.yview)


        for col in self.conn_table["columns"]:
            self.conn_table.heading(col, text=col.replace("_", " ").title())
            self.conn_table.column(col, width=100)

        self.conn_table.pack(fill=BOTH, expand=1)
        self.conn_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ========================== DB Functions ==============================

    def add_data(self):
        if self.var_cust_id.get() == "" or self.var_conn_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
                my_cur = conn.cursor()

                my_cur.execute("SELECT * FROM customers WHERE ID=%s", (self.var_cust_id.get(),))
                result = my_cur.fetchone()

                if result is None:
                    messagebox.showerror("Error", "Customer is not registered.", parent=self.parent)
                    conn.close()
                    return


                my_cur.execute("INSERT INTO new_connection VALUES (%s,%s,%s,%s,%s,%s)", (
                    self.var_conn_id.get(),
                    self.var_cust_id.get(),
                    self.var_conn_type.get(),
                    self.var_load.get(),
                    self.var_address.get(),
                    self.var_date.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "New connection added",parent=self.parent)
            except Exception as e:
                messagebox.showwarning("Error", f"Something went wrong: {e}",parent=self.parent)

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
        my_cur = conn.cursor()
        my_cur.execute("SELECT * FROM new_connection")
        rows = my_cur.fetchall()
        if rows:
            self.conn_table.delete(*self.conn_table.get_children())
            for row in rows:
                self.conn_table.insert("", END, values=row)
        conn.close()

    def get_cursor(self, event=""):
        selected = self.conn_table.focus()
        values = self.conn_table.item(selected, "values")
        if values:
            self.var_conn_id.set(values[0])
            self.var_cust_id.set(values[1])
            self.var_conn_type.set(values[2])
            self.var_load.set(values[3])
            self.var_address.set(values[4])
            self.var_date.set(values[5])

    def update_data(self):
        if self.var_conn_id.get() == "":
            messagebox.showerror("Error", "Select a record to update",parent=self.parent)
        else:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()
            my_cur.execute("""
                UPDATE new_connection SET
                customer_id=%s, connection_type=%s, load_required=%s, address=%s, application_date=%s
                WHERE connection_id=%s
            """, (
                self.var_cust_id.get(),
                self.var_conn_type.get(),
                self.var_load.get(),
                self.var_address.get(),
                self.var_date.get(),
                self.var_conn_id.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Updated", "Record updated successfully",parent=self.parent)

    def delete_data(self):
        confirm = messagebox.askyesno("Delete", "Do you really want to delete?",parent=self.parent)
        if confirm:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()
            my_cur.execute("DELETE FROM new_connection WHERE connection_id=%s", (self.var_conn_id.get(),))
            conn.commit()
            conn.close()
            self.fetch_data()

    def reset_fields(self):
        self.var_cust_id.set("")
        self.var_conn_type.set("*")
        self.var_load.set("")
        self.var_address.set("")
        self.var_date.set(datetime.now().strftime("%Y-%m-%d"))
        self.var_conn_id.set(str(random.randint(10000, 99999)))


# =========================== Run App ===========================
if __name__ == "__main__":
    root = Tk()
    obj = NewConnection(root)
    root.mainloop()
