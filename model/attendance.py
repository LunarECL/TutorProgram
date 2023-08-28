from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

import Refresher

student_name_entry = None
course_id_entry = None


def record_attendance(cnx, cursor, student_name, course_id, hours_attended, hours_attended_entry):
    date = datetime.now().date()
    firstname, lastname = student_name.split(' ')
    cursor.execute("SELECT id FROM student WHERE firstname = %s AND lastname = %s", (firstname, lastname))
    student_id = cursor.fetchone()[0]
    query = "INSERT INTO attendance (student_id, course_id, date, hours_attended) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (student_id, course_id, date, hours_attended))
    cnx.commit()
    messagebox.showinfo("Success", "Attendance recorded successfully!")
    hours_attended_entry.delete(0, 'end')
    Refresher.refresh_all(cursor)


def refresh_dropdowns(cursor):
    # Query the database for all student names
    cursor.execute("SELECT firstname, lastname FROM student")
    student_names = [' '.join(row) for row in cursor.fetchall()]
    student_name_entry['values'] = student_names

    # Query the database for all course IDs
    cursor.execute("SELECT courseID FROM course")
    course_ids = [row[0] for row in cursor.fetchall()]
    course_id_entry['values'] = course_ids


def setup_frame(frame_attendance, cnx, cursor):
    global student_name_entry, course_id_entry

    # Define the fields and buttons for the Attendance frame
    student_name_label = ttk.Label(frame_attendance, text="Student Name:")
    student_name_label.pack()

    student_name_entry = ttk.Combobox(frame_attendance)
    student_name_entry.pack()

    course_id_label = ttk.Label(frame_attendance, text="Course ID:")
    course_id_label.pack()

    course_id_entry = ttk.Combobox(frame_attendance)
    course_id_entry.pack()

    hours_attended_label = ttk.Label(frame_attendance, text="Hours Attended:")
    hours_attended_label.pack()

    hours_attended_entry = ttk.Entry(frame_attendance)
    hours_attended_entry.pack()

    add_button = ttk.Button(frame_attendance, text="Record Attendance",
                            command=lambda: record_attendance(cnx, cursor, student_name_entry.get(),
                                                              course_id_entry.get(), hours_attended_entry.get(),
                                                              hours_attended_entry))
    add_button.pack()

    refresh_dropdowns(cursor)
