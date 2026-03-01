from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox
import random

class InboxModule:
    def __init__(self, parent):
        self.parent = parent
        

        
        

        rec_ = LabelFrame(self.parent, bd=2, relief=RIDGE, text="Receipt", font=("arial", 12, "bold"))
        rec_.place(x=870, y=50, width=400, height=420)

        canvas = Canvas(rec_, bd=0, highlightthickness=0,bg="black")
        canvas.place(x=0, y=0, width=380, height=390)

        # Scrollbar
        srl2_y = Scrollbar(rec_, orient=VERTICAL, command=canvas.yview)
        srl2_y.place(x=380, y=0, height=390)

        # Configure canvas scrolling
        canvas.configure(yscrollcommand=srl2_y.set)

        # Create scrollable inner frame
        self.rec_frm = Frame(canvas,bg="black")
        self.rec_frm.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.rec_frm, anchor="nw")




        self.var_msg_id = StringVar(value=self.generate_random_id())

        self.var_bill = StringVar()
        self.var_cust = StringVar()
        self.var_conn = StringVar()

        lb_title = Label(self.parent, text="Inbox", font=("lucida calligraphy", 20, "bold"), bg="black", fg="yellow", bd=4, relief=RIDGE)
        lb_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open("V:/File/Documents/db images/lg.jpg")
        img2 = img2.resize((50, 50), Image.LANCZOS)
        self.phimg2 = ImageTk.PhotoImage(img2)
        lbimg = Label(self.parent, image=self.phimg2, relief=RIDGE)
        lbimg.place(x=0, y=0, width=50, height=50)

        lbl_frm = LabelFrame(self.parent, bd=2, relief=RIDGE, text="Message Details", font=("times new roman", 12, "bold"),bg="black",fg="white", padx=2)
        lbl_frm.place(x=5, y=50, height=420, width=400)

        Label(lbl_frm, text="Receipt ID:", bg="black",fg="white",font=("times new roman", 12, "bold")).grid(row=0, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_msg_id, width=22).grid(row=0, column=1)

        Label(lbl_frm, text="Bill id:", bg="black",fg="white",font=("times new roman", 12, "bold")).grid(row=1, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_bill, width=22).grid(row=1, column=1)

        Label(lbl_frm, text="Customer Id:",bg="black",fg="white", font=("times new roman", 12, "bold")).grid(row=2, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_cust, width=22).grid(row=2, column=1)

        Label(lbl_frm, text="Connection Id:", bg="black",fg="white",font=("times new roman", 12, "bold")).grid(row=3, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_conn, width=22).grid(row=3, column=1)

        btn_frm = Frame(lbl_frm, bg="black",bd=2, relief=RIDGE)
        btn_frm.place(x=50, y=300, width=275, height=38)
        Button(btn_frm, text="Get Receipt", font=("arial", 12, "bold"), bg="grey", fg="white", width=12, command=self.display_receipt_details).grid(row=0, column=0, padx=2)
        Button(btn_frm, text="Save Receipt", font=("arial", 12, "bold"), bg="grey", fg="white", width=12,command=self.save_receipt).grid(row=0, column=1, padx=2)



     #=========================Show table============================


        tbl_frm = LabelFrame(self.parent, bd=2, relief=RIDGE, text="View Details", font=("arial", 12, "bold"))
        tbl_frm.place(x=420, y=50, width=450, height=420)


        det_tbl=Frame(tbl_frm,bd=2,relief=RIDGE)
        det_tbl.place(x=5,y=10,width=430,height=380)


        srl_x=Scrollbar(det_tbl,orient=HORIZONTAL)
        srl_y=Scrollbar(det_tbl,orient=VERTICAL)


        self.cust_tbl=ttk.Treeview(det_tbl,column=("Receipt Id","Bill id","Customer id","Connection id","Customer Name","Connection Type","Units","Charge per unit","Amount"),xscrollcommand=srl_x.set,yscrollcommand=srl_y.set)

        srl_x.pack(side=BOTTOM,fill=X)
        srl_y.pack(side=RIGHT,fill=Y)

        srl_x.config(command=self.cust_tbl.xview)
        srl_y.config(command=self.cust_tbl.yview)\
        
        self.cust_tbl.heading("Receipt Id",text="Receipt Id")
        self.cust_tbl.heading("Bill id",text="Bill id")
        self.cust_tbl.heading("Customer id",text="Customer id")
        self.cust_tbl.heading("Connection id",text="Connection id")
        self.cust_tbl.heading("Customer Name",text="Customer Name")
        self.cust_tbl.heading("Connection Type",text="Connection Type")
        self.cust_tbl.heading("Units",text="Units")
        self.cust_tbl.heading("Charge per unit",text="Charge per unit")
        self.cust_tbl.heading("Amount",text="Amount")
        

        self.cust_tbl["show"]="headings"
        self.cust_tbl.pack(fill=BOTH,expand=1)
        self.cust_tbl.bind("<ButtonRelease-1>",self.get_cur)
        self.fetch_data()



        




    def display_receipt_details(self):
        if self.var_msg_id.get() == "":
            messagebox.showerror("Error", "Please select a receipt", parent=self.parent)
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()

            # Fetch from receipt
            my_cur.execute("SELECT receipt_id, bills_id, customers_id, connections_id, charge_pu FROM receipt WHERE receipt_id = %s", (self.var_msg_id.get(),))
            receipt_data = my_cur.fetchone()
            if not receipt_data:
                messagebox.showerror("Error", "Receipt not found", parent=self.parent)
                conn.close()
                return

            receipt_id, bill_id, cust_id, conn_id, charge_pu = receipt_data

            # Fetch from customers
            my_cur.execute("SELECT name, mobile, id FROM customers WHERE id = %s", (cust_id,))
            cust_data = my_cur.fetchone()
            name, mobile, cid = cust_data if cust_data else ("-", "-", "-")

            # Fetch from new_connection
            my_cur.execute("SELECT connection_id, connection_type, load_required, address, application_date FROM new_connection WHERE connection_id = %s", (conn_id,))
            conn_data = my_cur.fetchone()
            conn_id, conn_type, load_req, address, app_date = conn_data if conn_data else ("-", "-", "-", "-", "-")

            # Fetch from bills
            my_cur.execute("SELECT bill_id, status, amount FROM bills WHERE bill_id = %s", (bill_id,))
            bill_data = my_cur.fetchone()
            bill_id, status, amount = bill_data if bill_data else ("-", "-", "-")

            conn.close()

            # Display in rec_frm
            for widget in self.rec_frm.winfo_children():
                widget.destroy()

            Label(self.rec_frm, fg="white",bg="black",text="Customer Info", font=("arial", 12, "bold")).pack(anchor=W, padx=10, pady=(5, 0))
            Label(self.rec_frm, fg="white",bg="black",text=f"Name: {name}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Mobile: {mobile}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Customer ID: {cid}", font=("arial", 11)).pack(anchor=W, padx=20)

            Label(self.rec_frm, fg="white",bg="black",text="Connection Info", font=("arial", 12, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
            Label(self.rec_frm, fg="white",bg="black",text=f"Connection ID: {conn_id}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Type: {conn_type}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Load: {load_req} Units", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Address: {address}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Applied On: {app_date}", font=("arial", 11)).pack(anchor=W, padx=20)

            Label(self.rec_frm, fg="white",bg="black",text="Bill Info", font=("arial", 12, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
            Label(self.rec_frm, fg="white",bg="black",text=f"Bill ID: {bill_id}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Status: {status}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Amount: ₹{amount}", font=("arial", 11)).pack(anchor=W, padx=20)

            Label(self.rec_frm, fg="white",bg="black",text="Receipt Info", font=("arial", 12, "bold")).pack(anchor=W, padx=10, pady=(10, 0))
            Label(self.rec_frm, fg="white",bg="black",text=f"Receipt ID: {receipt_id}", font=("arial", 11)).pack(anchor=W, padx=20)
            Label(self.rec_frm, fg="white",bg="black",text=f"Charge/Unit: ₹{charge_pu}", font=("arial", 11)).pack(anchor=W, padx=20)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.parent)









    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
        my_cur=conn.cursor()

        my_cur.execute("Select * from receipt")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.cust_tbl.delete(*self.cust_tbl.get_children())
            for i in rows:
                self.cust_tbl.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cur(self, event=""):
        cur_row = self.cust_tbl.focus()
        content = self.cust_tbl.item(cur_row)
        row = content["values"]

        if len(row) >= 9:
            self.var_msg_id.set(row[0])     
            self.var_bill.set(row[1])       
            self.var_cust.set(row[2])       
            self.var_conn.set(row[3])       
            
        else:
            messagebox.showwarning("Warning", "Incomplete row data", parent=self.parent)







    def generate_random_id(self):
        return f"RCP{random.randint(1000, 9999)}"
    


    
        



    def save_receipt(self):
        if self.var_msg_id.get() == "" or self.var_bill.get() == "" or self.var_cust.get() == "" or self.var_conn.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.parent)
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()

            # Fetch customer name
            my_cur.execute("SELECT name FROM customers WHERE id = %s", (self.var_cust.get(),))
            customer = my_cur.fetchone()
            if not customer:
                messagebox.showerror("Error", "Customer not found", parent=self.parent)
                conn.close()
                return
            cust_name = customer[0]

            # Fetch connection details
            my_cur.execute("SELECT connection_type, load_required FROM new_connection WHERE connection_id = %s AND customer_id = %s",
                        (self.var_conn.get(), self.var_cust.get()))
            connection = my_cur.fetchone()
            if not connection:
                messagebox.showerror("Error", "Connection not found", parent=self.parent)
                conn.close()
                return

            conn_type, units = connection
            units = int(units)

            # Define base residential slab rates
            slab_rates = [
                (200, 3.00),
                (400, 5.00),
                (800, 6.50),
                (1200, 7.00),
                (float('inf'), 8.00)
            ]

            # Adjust slab rates by connection type
            conn_type_lower = conn_type.lower()
            if conn_type_lower == "commercial":
                slab_rates = [(limit, rate + 1.00) for limit, rate in slab_rates]
            elif conn_type_lower == "industrial":
                slab_rates = [(limit, rate + 2.00) for limit, rate in slab_rates]
            elif conn_type_lower != "residential":
                messagebox.showerror("Error", f"Unknown connection type: {conn_type}", parent=self.parent)
                conn.close()
                return

            # Calculate amount based on slabs
            remaining_units = units
            previous_limit = 0
            amount = 0.0
            for limit, rate in slab_rates:
                if remaining_units <= 0:
                    break
                applicable_units = min(remaining_units, limit - previous_limit)
                amount += applicable_units * rate
                remaining_units -= applicable_units
                previous_limit = limit

            # Use the last rate applied as charge per unit for the receipt display
            charge_pu = slab_rates[-1][1] if units > 1200 else next(rate for limit, rate in slab_rates if units <= limit)

            # Save receipt to database
            my_cur.execute("""
                INSERT INTO receipt (receipt_id, bills_id, customers_id, connections_id, cust_name, conn_type, units, charge_pu, amount)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                self.var_msg_id.get(),
                self.var_bill.get(),
                self.var_cust.get(),
                self.var_conn.get(),
                cust_name,
                conn_type,
                str(units),
                f"{charge_pu:.2f}",
                f"{amount:.2f}"
            ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Receipt saved successfully", parent=self.parent)

        except Exception as e:
            messagebox.showerror("Error", f"Error while saving receipt: {str(e)}", parent=self.parent)






 

if __name__ == "__main__":
    root = Tk()
    obj = InboxModule(root)
    root.mainloop()
