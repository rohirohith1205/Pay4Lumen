from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql
from tkinter import messagebox
import random

class BillModule:
    def __init__(self, parent):
        self.parent = parent


        self.var_bill_id = StringVar()
        self.var_cust_id = StringVar()
        self.var_conn_id = StringVar()
        self.var_units = StringVar()
        self.var_amount = StringVar()
        self.var_status = StringVar()
        self.var_bill_id.set(str(random.randint(1000, 9999)))

        lb_title = Label(self.parent, text="Bill Details", font=("lucida calligraphy", 20, "bold"), bg="black", fg="yellow", bd=4, relief=RIDGE)
        lb_title.place(x=0, y=0, width=1295, height=50)

        img2 = Image.open("V:/File/Documents/db images/lg.jpg")
        img2 = img2.resize((50, 50), Image.LANCZOS)
        self.phimg2 = ImageTk.PhotoImage(img2)
        lbimg = Label(self.parent, image=self.phimg2, relief=RIDGE)
        lbimg.place(x=0, y=0, width=50, height=50)

        lbl_frm = LabelFrame(self.parent, bd=2, relief=RIDGE, text="Bill Details", font=("times new roman", 12, "bold"), padx=2)
        lbl_frm.place(x=5, y=50, height=420, width=400)

        Label(lbl_frm, text="Bill ID:", font=("times new roman", 12, "bold")).grid(row=0, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_bill_id, state="readonly", width=22).grid(row=0, column=1)

        Label(lbl_frm, text="Customer ID:", font=("times new roman", 12, "bold")).grid(row=1, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_cust_id, width=22).grid(row=1, column=1)

        Label(lbl_frm, text="Connection ID:", font=("times new roman", 12, "bold")).grid(row=2, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_conn_id, width=22).grid(row=2, column=1)

        Label(lbl_frm, text="Units:", font=("times new roman", 12, "bold")).grid(row=3, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_units, width=22, state="readonly").grid(row=3, column=1)

        Label(lbl_frm, text="Amount:", font=("times new roman", 12, "bold")).grid(row=4, column=0, sticky=W)
        ttk.Entry(lbl_frm, textvariable=self.var_amount, width=22, state="readonly").grid(row=4, column=1)

        Label(lbl_frm, text="Status:", font=("times new roman", 12, "bold")).grid(row=5, column=0, sticky=W)
        cmb_status = ttk.Combobox(lbl_frm, textvariable=self.var_status, state="readonly", width=20)
        cmb_status["value"] = ("unpaid", "Paid")
        cmb_status.current(0)
        cmb_status.grid(row=5, column=1)

        # Buttons
        btn_frm = Frame(lbl_frm, bd=2, relief=RIDGE)
        btn_frm.place(x=0, y=300, width=380, height=38)
        Button(btn_frm, text="Save Bill", font=("arial", 12, "bold"), bg="grey", fg="white", width=8, command=self.add_data).grid(row=0, column=0, padx=2)
        Button(btn_frm, text="Get Units", font=("arial", 12, "bold"), bg="grey", fg="white", width=8, command=self.get_units).grid(row=0, column=1, padx=2)
        Button(btn_frm, text="Get Amount", font=("arial", 12, "bold"), bg="grey", fg="white", width=8, command=self.get_amount).grid(row=0, column=2, padx=2)
        Button(btn_frm, text="Pay", font=("arial", 12, "bold"), bg="grey", fg="white", width=8, command=self.show_bill_summary).grid(row=0, column=3, padx=2)





        # Table Frame===============================================================================================================



        tbl_frm = LabelFrame(self.parent, bd=2, relief=RIDGE, text="View Details", font=("arial", 12, "bold"))
        tbl_frm.place(x=420, y=50, width=850, height=420)



        #=========================Show table============================



        det_tbl=Frame(tbl_frm,bd=2,relief=RIDGE)
        det_tbl.place(x=5,y=10,width=830,height=380)


        srl_x=Scrollbar(det_tbl,orient=HORIZONTAL)
        srl_y=Scrollbar(det_tbl,orient=VERTICAL)


        self.cust_tbl=ttk.Treeview(det_tbl,column=("Bill id","Customer id","Connection id","Units","Amount","Status"),xscrollcommand=srl_x.set,yscrollcommand=srl_y.set)

        srl_x.pack(side=BOTTOM,fill=X)
        srl_y.pack(side=RIGHT,fill=Y)

        srl_x.config(command=self.cust_tbl.xview)
        srl_y.config(command=self.cust_tbl.yview)

        self.cust_tbl.heading("Bill id",text="Bill id")
        self.cust_tbl.heading("Customer id",text="Customer id")
        self.cust_tbl.heading("Connection id",text="Connection id")
        self.cust_tbl.heading("Units",text="Units")
        self.cust_tbl.heading("Amount",text="Amount")
        self.cust_tbl.heading("Status",text="Status")

        self.cust_tbl["show"]="headings"
        self.cust_tbl.pack(fill=BOTH,expand=1)
        self.cust_tbl.bind("<ButtonRelease-1>",self.get_cur)
        self.fetch_data()



    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="MysqlRoot",database="dbms_customers")
        my_cur=conn.cursor()

        my_cur.execute("Select * from bills")
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

        self.var_bill_id.set(row[0]),
        self.var_cust_id.set(row[1]),
        self.var_conn_id.set(row[2]),
        self.var_units.set(row[3]),
        self.var_amount.set(row[4]),
        self.var_status.set(row[5])



        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def get_units(self):
        if self.var_cust_id.get() == "" or self.var_conn_id.get() == "":
            messagebox.showerror("Error", "Customer ID and Connection ID are required")
            return
        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()
            my_cur.execute("SELECT load_required FROM new_connection WHERE connection_id = %s AND customer_id = %s", 
                           (self.var_conn_id.get(), self.var_cust_id.get()))
            result = my_cur.fetchone()
            conn.close()
            if result:
                self.var_units.set(str(result[0]))
            else:
                messagebox.showerror("Error", "Connection not found or mismatch with customer ID",parent=self.parent)
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}",parent=self.parent)






    def get_amount(self):
        if self.var_units.get() == "":
            messagebox.showerror("Error", "Please get units first", parent=self.parent)
            return
        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()
            my_cur.execute("SELECT connection_type FROM new_connection WHERE connection_id = %s AND customer_id = %s", 
                        (self.var_conn_id.get(), self.var_cust_id.get()))
            result = my_cur.fetchone()
            conn.close()
            if result:
                conn_type = result[0].lower()
                units = int(self.var_units.get())

                # Define base residential slab
                slabs = [
                    (200, 3.00),
                    (400, 5.00),
                    (800, 6.50),
                    (1200, 7.00),
                    (float('inf'), 8.00)
                ]

                # Adjust rate based on connection type
                if conn_type == "residential":
                    modifier = 0
                elif conn_type == "commercial":
                    modifier = 1
                elif conn_type == "industrial":
                    modifier = 2
                else:
                    messagebox.showerror("Error", f"Unknown connection type: {conn_type}", parent=self.parent)
                    return

                # Calculate amount based on slab
                amount = 0
                remaining_units = units
                previous_limit = 0
                for limit, rate in slabs:
                    slab_units = min(remaining_units, limit - previous_limit)
                    amount += slab_units * (rate + modifier)
                    remaining_units -= slab_units
                    previous_limit = limit
                    if remaining_units <= 0:
                        break

                self.var_amount.set(str(round(amount, 2)))
            else:
                messagebox.showerror("Error", "Connection type not found", parent=self.parent)
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.parent)






    def add_data(self):
        if self.var_cust_id.get() == "" or self.var_conn_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.parent)
            return
        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()

            # Verify customer exists
            my_cur.execute("SELECT * FROM customers WHERE id = %s", (self.var_cust_id.get(),))
            customer = my_cur.fetchone()
            if customer is None:
                messagebox.showerror("Error", "Customer ID is not registered", parent=self.parent)
                conn.close()
                return

            # Get load and connection type
            my_cur.execute("SELECT load_required, connection_type FROM new_connection WHERE connection_id = %s AND customer_id = %s", 
                        (self.var_conn_id.get(), self.var_cust_id.get()))
            connection = my_cur.fetchone()
            if connection is None:
                messagebox.showerror("Error", "Invalid Connection ID for this Customer", parent=self.parent)
                conn.close()
                return

            load_required = int(connection[0])
            conn_type = connection[1].lower()

            # Define slab structure
            slabs = [
                (200, 3.00),
                (400, 5.00),
                (800, 6.50),
                (1200, 7.00),
                (float('inf'), 8.00)
            ]

            # Set slab modifier
            if conn_type == "residential":
                modifier = 0
            elif conn_type == "commercial":
                modifier = 1
            elif conn_type == "industrial":
                modifier = 2
            else:
                messagebox.showerror("Error", f"Unknown connection type: {conn_type}", parent=self.parent)
                conn.close()
                return

            # Slab-based calculation
            amount = 0
            remaining_units = load_required
            previous_limit = 0
            for limit, rate in slabs:
                slab_units = min(remaining_units, limit - previous_limit)
                amount += slab_units * (rate + modifier)
                remaining_units -= slab_units
                previous_limit = limit
                if remaining_units <= 0:
                    break

            total_amount = round(amount, 2)

            # Set units and amount variables for display
            self.var_units.set(str(load_required))
            self.var_amount.set(str(total_amount))

            # Insert bill into database
            my_cur.execute("INSERT INTO bills (bill_id, customer_id, conn_id, units, amount, status) VALUES (%s, %s, %s, %s, %s, %s)", (
                self.var_bill_id.get(),
                self.var_cust_id.get(),
                self.var_conn_id.get(),
                self.var_units.get(),
                self.var_amount.get(),
                self.var_status.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Bill Added Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.parent)








    def show_bill_summary(self):
        if self.var_cust_id.get() == "" or self.var_conn_id.get() == "":
            messagebox.showerror("Error", "Customer ID and Connection ID required", parent=self.parent)
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="MysqlRoot", database="dbms_customers")
            my_cur = conn.cursor()

            my_cur.execute("SELECT * FROM customers WHERE id = %s", (self.var_cust_id.get(),))
            customer = my_cur.fetchone()
            if customer is None:
                messagebox.showerror("Error", "Customer ID is not registered", parent=self.parent)
                conn.close()
                return

            my_cur.execute("SELECT load_required, connection_type FROM new_connection WHERE connection_id = %s AND customer_id = %s",
                        (self.var_conn_id.get(), self.var_cust_id.get()))
            connection = my_cur.fetchone()
            if connection is None:
                messagebox.showerror("Error", "Invalid Connection ID for this Customer", parent=self.parent)
                conn.close()
                return

            units = int(connection[0])
            conn_type = connection[1].lower()

            # Slab definitions
            slabs = [
                (200, 3.00),
                (400, 5.00),
                (800, 6.50),
                (1200, 7.00),
                (float('inf'), 8.00)
            ]

            # Modifier for connection type
            if conn_type == "residential":
                modifier = 0
            elif conn_type == "commercial":
                modifier = 1
            elif conn_type == "industrial":
                modifier = 2
            else:
                messagebox.showerror("Error", f"Unknown connection type: {conn_type}", parent=self.parent)
                conn.close()
                return

            # Calculate slab-based amount
            amount = 0
            remaining_units = units
            previous_limit = 0
            last_rate = 0
            for limit, rate in slabs:
                slab_units = min(remaining_units, limit - previous_limit)
                final_rate = rate + modifier
                amount += slab_units * final_rate
                remaining_units -= slab_units
                previous_limit = limit
                last_rate = final_rate
                if remaining_units <= 0:
                    break

            total_amount = round(amount, 2)

            # Update fields
            self.var_units.set(str(units))
            self.var_amount.set(str(total_amount))
            self.var_status.set("Paid")

            # Display summary in new window
            top = Toplevel(self.parent)
            top.title("Bill Summary")
            top.geometry("300x220+600+400")
            top.resizable(False, False)

            Label(top, text=f"Connection Type: {conn_type.capitalize()}", font=("arial", 12)).pack(pady=10)
            Label(top, text=f"Units Used: {units}", font=("arial", 12)).pack(pady=5)
            Label(top, text=f"Rate per Unit (last slab): ₹{last_rate}", font=("arial", 12)).pack(pady=5)
            Label(top, text=f"Total Amount: ₹{total_amount}", font=("arial", 12, "bold")).pack(pady=10)
            Label(top, text="Payment successful", font=("arial", 12, "bold")).pack(pady=10)

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.parent)







if __name__ == "__main__":
    root = Tk()
    obj = BillModule(root)
    root.mainloop()
