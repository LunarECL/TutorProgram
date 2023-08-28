from tkinter import ttk, messagebox

import Refresher


def add_student(cnx, cursor, firstname, lastname, firstname_entry, lastname_entry):
    query = "INSERT INTO student (firstname, lastname) VALUES (%s, %s)"
    cursor.execute(query, (firstname, lastname))
    cnx.commit()
    messagebox.showinfo("Success", "Student added successfully!")
    firstname_entry.delete(0, 'end')
    lastname_entry.delete(0, 'end')
    Refresher.refresh_all(cursor)


def setup_frame(frame_students, cnx, cursor):
    # Define the fields and buttons for the Students frame
    firstname_label = ttk.Label(frame_students, text="First Name:")
    firstname_label.pack()

    firstname_entry = ttk.Entry(frame_students)
    firstname_entry.pack()

    lastname_label = ttk.Label(frame_students, text="Last Name:")
    lastname_label.pack()

    lastname_entry = ttk.Entry(frame_students)
    lastname_entry.pack()

    add_button = ttk.Button(frame_students, text="Add Student",
                            command=lambda: add_student(cnx, cursor, firstname_entry.get(), lastname_entry.get(),
                                                        firstname_entry, lastname_entry))
    add_button.pack()
