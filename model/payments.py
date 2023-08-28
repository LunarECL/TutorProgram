from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

import Refresher

student_name_entry = None


def make_payment(cnx, cursor, student_name, amount, amount_entry):
    date = datetime.now().date()
    firstname, lastname = student_name.split(' ')
    cursor.execute("SELECT id FROM student WHERE firstname = %s AND lastname = %s", (firstname, lastname))
    student_id = cursor.fetchone()[0]
    query = "INSERT INTO payment (student_id, date, amount) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, date, amount))
    cnx.commit()
    messagebox.showinfo("Success", "Payment made successfully!")
    amount_entry.delete(0, 'end')
    Refresher.refresh_all(cursor)


def refresh_dropdowns(cursor):
    # Query the database for all student names
    cursor.execute("SELECT firstname, lastname FROM student")
    student_names = [' '.join(row) for row in cursor.fetchall()]
    student_name_entry['values'] = student_names


def setup_frame(frame_payments, cnx, cursor):
    global student_name_entry

    # Define the fields and buttons for the Payments frame
    student_name_label = ttk.Label(frame_payments, text="Student Name:")
    student_name_label.pack()

    student_name_entry = ttk.Combobox(frame_payments)
    student_name_entry.pack()

    amount_label = ttk.Label(frame_payments, text="Amount:")
    amount_label.pack()

    amount_entry = ttk.Entry(frame_payments)
    amount_entry.pack()

    add_button = ttk.Button(frame_payments, text="Mke Payment",
                            command=lambda: make_payment(cnx, cursor, student_name_entry.get(), amount_entry.get(),
                                                         amount_entry))
    add_button.pack()

    refresh_dropdowns(cursor)
