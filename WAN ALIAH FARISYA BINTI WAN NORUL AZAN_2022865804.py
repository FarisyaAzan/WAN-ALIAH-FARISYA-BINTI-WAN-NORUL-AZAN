import tkinter
from tkinter import ttk
import mysql.connector
from datetime import datetime

def create_table ():
    db_connection= mysql.connector.connect(
        host= "localhost",
        user="root",
        password= "",
        database= "restaurant_table_reservation"

    )
    cursor = db_connection.cursor ()

    cursor.execute ('''
                   
        CREATE TABLE IF NOT EXISTS reservation_info (
            customer_name VARCHAR (255),
            phone_number VARCHAR (15),
            party_size INT,
            deposit_amount_rm DECIMAL (10,2),
            reservation_datetime DATETIME
            ) 
            ''')
    
    cursor.close()
    db_connection.close()
    


# Connect to MySQL database
def connect_to_database():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",
        database="restaurant_table_reservation"
    )
    return db_connection

def calculate_deposit():
    cust_party = int(cust_party_spinbox.get())
    deposit_amount_rm = cust_party * 5.0 
    deposit_amount_entry.delete(0, tkinter.END)
    deposit_amount_entry.insert(0, "{:.2f}".format(deposit_amount_rm))

def insert_data():
    full_name = full_name_entry.get()
    cust_phone = cust_phone_entry.get()
    cust_party = int(cust_party_spinbox.get())

    # Calculate the deposit 
    deposit_amount_rm = cust_party * 5.0

    
    # Specific datetime
    specific_datetime=datetime (2024, 3, 3, 21,00)

    #Format datetime

    formatted_datetime = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    conn = connect_to_database()

    print("Full Name:", full_name)
    print("Phone Number:", cust_phone)
    print("Number of Party:", cust_party)
    print("Deposit Amount (RM): {:.2f}".format(deposit_amount_rm))
    print("Reservation Date and Time:", specific_datetime)

    cursor = conn.cursor()

    try:

        # Assuming you have a 'reservations' table with appropriate columns
        sql = "INSERT INTO reservation_info (customer_name, phone_number, party_size, deposit_amount_rm, reservation_datetime) VALUES (%s, %s, %s, %s, %s)"
        val = (full_name, cust_phone, cust_party, deposit_amount_rm, specific_datetime)
        cursor.execute(sql, val)

        print("Data inserted successfully!")

        # Commit changes
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Tkinter GUI
root = tkinter.Tk()
root.title("RESTAURANT TABLE RESERVATION")
root.geometry("600x600")
root.configure (bg= "Pink")

frame = tkinter.Frame(root)
frame.pack()

# Saving Customer Info
reservation_info_frame = tkinter.LabelFrame(frame, text=("Reservation Information"), bg= "Pink")
reservation_info_frame.grid(row=0, column=0, padx=40, pady=40)

full_name_label = tkinter.Label(reservation_info_frame, text=("Customer Name"), bg= ("White"))
full_name_label.grid(row=0, column=0)

full_name_entry = tkinter.Entry(reservation_info_frame)
full_name_entry.grid(row=1, column=0)

cust_phone_label = tkinter.Label(reservation_info_frame, text=("Phone Number"), bg= "White")
cust_phone_label.grid(row=0, column=1)

cust_phone_entry = tkinter.Entry(reservation_info_frame)
cust_phone_entry.grid(row=1, column=1)

cust_party_label = tkinter.Label(reservation_info_frame, text=("Number of Party"), bg= "White")
cust_party_spinbox = tkinter.Spinbox(reservation_info_frame, from_=2, to=10, command=calculate_deposit)
cust_party_label.grid(row=2, column=0)
cust_party_spinbox.grid(row=3, column=0)

deposit_amount_label = tkinter.Label(reservation_info_frame, text=("Deposit Amount"), bg= "White")
deposit_amount_label.grid(row=2, column=1)

deposit_amount_entry = tkinter.Entry(reservation_info_frame)
deposit_amount_entry.grid(row=3, column=1)

reservation_datetime_label = tkinter.Label(reservation_info_frame, text= ("Reservation Date and Time"), bg= "White")
reservation_datetime_label.grid(row=6, column=0)

reservation_datetime_entry = tkinter.Entry(reservation_info_frame)
reservation_datetime_entry.grid(row=7, column=0)


for widget in reservation_info_frame.winfo_children():
    widget.grid_configure(padx=20, pady=10)

insert_button = tkinter.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

root.mainloop()


