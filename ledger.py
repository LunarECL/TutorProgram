from tkinter import ttk

ledger_table = None


def refresh_ledger(cursor):
    # Clear the table
    for row in ledger_table.get_children():
        ledger_table.delete(row)

    # Execute the query
    query = """
    SELECT 
        s.id, 
        s.firstname, 
        s.lastname,
        IFNULL((SELECT SUM(p.amount) FROM payment p WHERE p.student_id = s.id), 0) AS total_payment,
        IFNULL((SELECT SUM(a.hours_attended) FROM attendance a WHERE a.student_id = s.id), 0) AS total_hours,
        IFNULL((SELECT SUM(p.amount) FROM payment p WHERE p.student_id = s.id), 0) - 
        IFNULL((SELECT SUM(a.hours_attended) FROM attendance a WHERE a.student_id = s.id), 0) * 30 AS balance
    FROM 
        student s;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Insert the results into the table
    for row in results:
        ledger_table.insert("", "end", values=row)


def setup_frame(frame_ledger, cursor):
    global ledger_table
    # Define the table for the Ledger frame
    ledger_table = ttk.Treeview(frame_ledger,
                                columns=("id", "firstname", "lastname", "total_payment", "total_hours", "balance"),
                                show="headings")
    ledger_table.pack()

    # Define the column headings
    ledger_table.heading("id", text="ID")
    ledger_table.heading("firstname", text="First Name")
    ledger_table.heading("lastname", text="Last Name")
    ledger_table.heading("total_payment", text="Total Payment")
    ledger_table.heading("total_hours", text="Total Hours")
    ledger_table.heading("balance", text="Balance")

    refresh_ledger(cursor)
