from tkinter import ttk, messagebox

import Refresher


def add_course(cnx, cursor, courseID, name, courseID_entry, name_entry):
    query = "INSERT INTO course (courseID, name) VALUES (%s, %s)"
    cursor.execute(query, (courseID, name))
    cnx.commit()
    messagebox.showinfo("Success", "Course added successfully!")
    courseID_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    Refresher.refresh_all(cursor)


def setup_frame(frame_courses, cnx, cursor):
    # Define the fields and buttons for the Courses frame
    courseID_label = ttk.Label(frame_courses, text="Course ID:")
    courseID_label.pack()

    courseID_entry = ttk.Entry(frame_courses)
    courseID_entry.pack()

    name_label = ttk.Label(frame_courses, text="Course Name:")
    name_label.pack()

    name_entry = ttk.Entry(frame_courses)
    name_entry.pack()

    add_button = ttk.Button(frame_courses, text="Add Course",
                            command=lambda: add_course(cnx, cursor, courseID_entry.get(), name_entry.get(),
                                                       courseID_entry, name_entry))
    add_button.pack()
