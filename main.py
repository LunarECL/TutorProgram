import os
import tkinter as tk
from tkinter import ttk

import mysql.connector
from dotenv import load_dotenv

import ledger
import model.attendance as attendance
import model.courses as courses
import model.payments as payments
import model.students as students
from Refresher import refresh_all

load_dotenv()

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Initialize the root window
root = tk.Tk()
root.title("Tutor Management System")

# Create the notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create the frames for each section
frame_students = ttk.Frame(notebook)
frame_courses = ttk.Frame(notebook)
frame_attendance = ttk.Frame(notebook)
frame_payments = ttk.Frame(notebook)

# Add the frames to the notebook
notebook.add(frame_students, text='Students')
notebook.add(frame_courses, text='Courses')
notebook.add(frame_attendance, text='Attendance')
notebook.add(frame_payments, text='Payments')

# Import the modules and set up the frames

students.setup_frame(frame_students, cnx, cursor)

courses.setup_frame(frame_courses, cnx, cursor)

attendance.setup_frame(frame_attendance, cnx, cursor)

payments.setup_frame(frame_payments, cnx, cursor)

frame_ledger = ttk.Frame(notebook)

notebook.add(frame_ledger, text='Ledger')

ledger.setup_frame(frame_ledger, cursor)

root.bind("<F5>", refresh_all(cursor))

root.mainloop()
