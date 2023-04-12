from tkinter import ttk, messagebox
from tkinter import *
import json
from PIL import ImageTk, Image
import pandas as pd
import random
import csv
import re
import datetime
import matplotlib.pyplot as plt
from tkcalendar import Calendar
from validate_email import validate_email

lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i', 'q', 'w', 'k', 'l', 'm', 'n', 'y', 'u', 'o', 'r', 'z', 's',
        'p', 't', 'v']
lst3 = ''
cal = None
but = None
top = None
c = None
n = None
d = None
v11 = None
m = None
b = None
v22 = None
data = {
    "Username": "admin",
    "Password": "123"
}
jsonString = json.dumps(data)
with open('User and Pass.json', 'w') as a:
    a.write(jsonString)
    a.close()

# todo Tạo cửa sổ đăng nhập
window = Tk()
window.title("LOGIN")
window.geometry("750x200")
window.attributes('-topmost', True)
window.resizable(False, False)
img = ImageTk.PhotoImage(Image.open("D:\\22DKHA1\\lập trình 2\\đồ án\\gui9.jpg").resize((1000, 500)))
img1 = ImageTk.PhotoImage(Image.open("D:\\22DKHA1\\lập trình 2\\đồ án\\điềukhoản.png").resize((1200, 750)))


# !########## name
def validate_text(text):
    if text.isalpha() or text == "":
        return True
    else:
        return False


validation = window.register(validate_text)


# todo login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    with open('User and Pass.json', 'r') as s:
        data1 = json.loads(s.read())
        user = data1['Username']
        passs = data1['Password']
        s.close()

    userr = str(user)
    passss = str(passs)

    if username == userr and password == passss:
        result_text.set("Successful login!")
        open_main_window()
    else:
        result_text.set("Login failed! Please double-check your username and password.")


def open_main_window():
    # todo Tạo cửa sổ chính
    main_window = Toplevel()
    main_window.title("Human Resource Management Software")
    main_window.geometry("1000x500")
    main_window.attributes('-topmost', True)
    main_window.resizable(False, False)
    menu = Menu(main_window)
    main_window.config(menu=menu)
    # Thêm thanh menu vào cửa sổ chính
    menubar = Menu(main_window)

    def thaydoimatkhau():
        master = Toplevel()
        master.title('Change password')
        master.geometry('300x150')

        main_window.withdraw()
        master.iconify()
        master.deiconify()

        password = entry_password.get()
        ee = StringVar(master)
        e11 = StringVar(master)
        e22 = StringVar(master)

        Label(master, text='Old password:').place(x=20, y=0)
        e = Entry(master, width=17, textvariable=ee, show='*')
        e.place(x=140, y=0)
        Label(master, text='Enter a new password:').place(x=0, y=30)
        e1 = Entry(master, width=17, textvariable=e11, show='*')
        e1.place(x=140, y=30)
        Label(master, text='Confirm new password:').place(x=0, y=60)
        e3 = Entry(master, width=17, textvariable=e22, show='*')
        e3.place(x=140, y=60)

        def xacnhan():
            passw = e11.get()

            if e.get() == password and passw != e.get() and passw == e22.get():
                e1 = str(passw)
                jsonFile = open("User and Pass.json", "r")
                data = json.load(jsonFile)
                jsonFile.close()

                # Working with buffered content
                tmp = data["Password"]
                data["Password"] = e1
                # Save our changes to JSON file
                jsonFile = open("User and Pass.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()
                messagebox.showinfo('NOTIFICATION', 'Password changed successfully')

                master.withdraw()
                window.iconify()
                window.deiconify()
            else:
                messagebox.showinfo('ERROR', 'Please try again')

        Button(master, text='Confirm', command=xacnhan).place(x=160, y=90)

    def dagxuat():
        main_window.destroy()
        window.iconify()
        window.deiconify()
        window.mainloop()

    def dieukhoan():
        master = Toplevel()
        master.title('Terms and legality')
        master.geometry('1200x750')
        master.attributes('-topmost', True)
        master.resizable(False, False)
        Menu1 = Menu(master)
        master.config(menu=Menu1)

        main_window.withdraw()
        master.iconify()
        master.deiconify()

        a = Label(master, image=img1)
        a.pack()

        def returnn():
            master.destroy()
            main_window.iconify()
            main_window.deiconify()

        Menu1.add_command(label='Back', command=returnn)

    def dsnv():
        master = Toplevel()
        master.title('List of employees')
        master.geometry('800x500')

        main_window.withdraw()
        master.iconify()
        master.deiconify()
        tree = ttk.Treeview(master)

        tree["columns"] = ('Employee ID', "Full name", "Date of birth", "Gender", "email", "Place of birth", "Position")

        def loc(column, descending=False):
            data = [(tree.set(child, column), child) for child in tree.get_children('')]
            data.sort(reverse=descending)
            for i, item in enumerate(data):
                tree.move(item[1], '', i)
            tree.heading(column, command=lambda: loc(column, not descending))

        tree.column("#0", width=0, minwidth=0)
        tree.column("Employee ID", width=50, minwidth=25)
        tree.column("Full name", width=50, minwidth=25)
        tree.column("Date of birth", width=50, minwidth=25)
        tree.column("Gender", width=50, minwidth=25)
        tree.column("email", width=50, minwidth=25)
        tree.column("Place of birth", width=50, minwidth=25)
        tree.column("Position", width=50, minwidth=25)
        tree.heading("Employee ID", text="Employee ID", anchor=W, command=lambda: loc('Employee ID', False))
        tree.heading("Full name", text="Full name", anchor=W, command=lambda: loc('Full name', False))
        tree.heading("Date of birth", text="Date of birth", anchor=W, command=lambda: loc('Date of birth', False))
        tree.heading("Gender", text="Gender", anchor=W, command=lambda: loc('Gender', False))
        tree.heading("email", text="Email", anchor=W, command=lambda: loc('email', False))
        tree.heading("Place of birth", text="Place of birth", anchor=W, command=lambda: loc('Place of birth', False))
        tree.heading("Position", text="Position", anchor=W, command=lambda: loc('Position', False))
        tree.pack(side=LEFT, fill=BOTH, expand=1)

        def add_employee_window():
            # Create a new window for adding a new employee
            window = Toplevel()
            window.title("Add Employee")
            window.geometry("400x400")
            window.attributes("-topmost", True)
            master.withdraw()
            window.iconify()
            window.deiconify()

            value1 = ['Male', 'Female']
            value2 = ['Part time', 'Full time', 'Resign']
            v1 = StringVar(master)
            v2 = StringVar(master)

            def returrn():
                window.destroy()
                master.iconify()
                master.deiconify()

            def get_date():
                global cal  # use the global cal variable
                date = cal.get_date()
                dob_entry.delete(0, END)
                dob_entry.insert(0, date)
                if but:
                    top.withdraw()

            def create_calendar():
                global top
                global cal  # use the global cal variable
                global but
                top = Toplevel()
                cal = Calendar(top, selectmode='day', year=2023, month=4, day=9)
                cal.pack()
                but = Button(top, text="Select", command=get_date)
                but.pack()

            # Create labels and entry fields for the new employee's information
            code_label = Label(window, text="Employee ID:")
            code_entry = Entry(window)
            name_label = Label(window, text="Full name:")
            name_entry = Entry(window, validate="key", validatecommand=(validation, "%S"))
            dob_label = Label(window, text="Date of birth:")
            dob_entry = Entry(window)
            aa = Button(window, text='Select date', command=create_calendar)
            gender_label = Label(window, text="Gender:")
            gender_entry = ttk.Combobox(window, values=value1, textvariable=v1, state='readonly')
            gender_entry.set('Select Gender')
            Mail_label = Label(window, text="email:")
            Mail_entry = Entry(window)
            Birth_label = Label(window, text="Place of birth:")
            Birth_entry = Entry(window)
            Position_label = Label(window, text="Position:")
            Position_entry = ttk.Combobox(window, values=value2, textvariable=v2, state='readonly')
            Position_entry.set('Choose your position')

            # Add a "Generate Code" button to randomly generate an employee code
            def generate_code():
                code_entry.delete(0, END)
                code_entry.insert(0, random.randint(1000, 9999))
                code_entry.config(state='readonly')
                code_button.config(state='disabled')

            code_button = Button(window, text="Generate Code", command=generate_code)

            def add_employee():
                global c
                global n
                global d
                global v11
                global m
                global b
                global v22

                c = code_entry.get()
                n = name_entry.get()
                d = dob_entry.get()
                v11 = v1.get()
                m = Mail_entry.get()
                b = Birth_entry.get()
                v22 = v2.get()
                data = {
                    ""
                    "Employee ID": c,
                    "Full name": n,
                    "Date of birth": d,
                    "Gender": v11,
                    "email": m,
                    "Place of birth": b,
                    "Position": v22

                }
                with open('Info.json', 'w') as f:
                    json_object = json.dumps(data, indent=4)
                    f.write(json_object)

                def checkerror():
                    try:
                        for e in lst:
                            for i in n:
                                for s in b:
                                    if i == e or e == s or not validate_email(m):
                                        messagebox.showerror('Error', 'Invalid syntax')
                                        return top
                                    elif i == e or e == s or validate_email(m):
                                        for line in tree.get_children():
                                            for value in tree.item(line)['values']:
                                                if m == value:
                                                    messagebox.showerror('Error', 'email existed')
                                                    return top
                    finally:
                        pass

                if not checkerror():
                    tree.insert("", END, values=(c, n, d, v11, m, b, v22))
                    messagebox.showinfo('NOTICE', 'Add Success')
                    window.withdraw()
                    master.iconify()
                    master.deiconify()
                else:
                    pass

            cancel_button = Button(window, text='Cancel', command=returrn)
            add_button = Button(window, text="Add", command=add_employee)

            code_label.pack()
            code_entry.pack()
            code_button.pack()
            name_label.pack()
            name_entry.pack()
            dob_label.pack()
            dob_entry.pack()
            aa.pack()
            gender_label.pack()
            gender_entry.pack()
            Mail_label.pack()
            Mail_entry.pack()
            Birth_label.pack()
            Birth_entry.pack()
            Position_label.pack()
            Position_entry.pack()
            add_button.pack()
            cancel_button.pack()
            name_entry.focus()

        def sua():
            suawindow = Toplevel()
            suawindow.title("Edit Employee")
            suawindow.geometry("400x400")
            suawindow.attributes("-topmost", True)
            master.withdraw()
            suawindow.iconify()
            suawindow.deiconify()

            def get_date():
                global cal  # use the global cal variable
                date = cal.get_date()
                dob_entry1.delete(0, END)
                dob_entry1.insert(0, date)
                if but:
                    top.withdraw()

            def create_calendar():
                global top
                global cal  # use the global cal variable
                global but
                top = Toplevel()

                cal = Calendar(top, selectmode='day', year=2023, month=4, day=9)
                cal.pack()
                but = Button(top, text="Select", command=get_date)
                but.pack()

            value1 = ['Male', 'Female']
            value2 = ['Part time', 'Full time', 'Resign']
            v12 = StringVar(master)
            v23 = StringVar(master)
            # Create labels and entry fields for the new employee's information
            name_label1 = Label(suawindow, text="Full name:")
            name_entry1 = Entry(suawindow)
            dob_label1 = Label(suawindow, text="Date of birth:")
            dob_entry1 = Entry(suawindow)
            ab = Button(suawindow, text='Select date', command=create_calendar)
            gender_label1 = Label(suawindow, text="Gender:")
            gender_entry1 = ttk.Combobox(suawindow, values=value1, textvariable=v12, state='readonly')
            gender_entry1.set('Chọn Gender')
            Origin_label1 = Label(suawindow, text="email:")
            Origin_entry1 = Entry(suawindow)
            Birth_label1 = Label(suawindow, text="Place of birth:")
            Birth_entry1 = Entry(suawindow)
            Position_label1 = Label(suawindow, text="Position:")
            Position_entry1 = ttk.Combobox(suawindow, values=value2, textvariable=v23, state='readonly')
            Position_entry1.set('Choose your position')

            def edit_employee():
                n1 = name_entry1.get()
                d1 = dob_entry1.get()
                v111 = v12.get()
                o1 = Origin_entry1.get()
                b1 = Birth_entry1.get()
                v222 = v23.get()
                tree.item(tree.selection(), values=(c, n1, d1, v111, o1, b1, v222))

                def error():
                    try:
                        for e in lst:
                            for i in n1:
                                for s in o1:
                                    if i == e or e == s or not validate_email(b1):
                                        messagebox.showerror('Error', 'Invalid syntax')
                                        return top
                    finally:
                        pass

                if error():
                    messagebox.showinfo('NOTIFICATION', 'Corrected successfully')
                    window.withdraw()
                    master.iconify()
                    master.deiconify()

            def withdraw():
                suawindow.withdraw()
                master.iconify()
                master.deiconify()

            save_button = Button(suawindow, text="Save", command=edit_employee)
            cancel_button = Button(suawindow, text="Cancel", command=withdraw)

            name_label1.pack()
            name_entry1.pack()
            dob_label1.pack()
            dob_entry1.pack()
            ab.pack()
            gender_label1.pack()
            gender_entry1.pack()
            Origin_label1.pack()
            Origin_entry1.pack()
            Birth_label1.pack()
            Birth_entry1.pack()
            Position_label1.pack()
            Position_entry1.pack()
            save_button.pack()
            cancel_button.pack()
            name_entry1.focus()

        def Thoat():
            global cc
            global ccx
            global ccxx
            col = int(tree.identify_column(8).replace('#', '')) - 1
            listofentriesintreeview = tree.get_children()
            cc = 0
            ccx = 0
            ccxx = 0
            master.withdraw()
            main_window.iconify()
            main_window.deiconify()
            for i in listofentriesintreeview:
                if tree.item(i)['values'][col] == 'Full time':
                    cc += 1
                elif tree.item(i)['values'][col] == 'Part time':
                    ccx += 1
                else:
                    ccxx += 1

            with open("new.csv", "w", newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')

                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    csvwriter.writerow(row)

        def load_csv():
            with open("new.csv") as myfile:
                csvread = csv.reader(myfile, delimiter=',')

                for row in csvread:
                    tree.insert("", 'end', values=row)

        def xoa():
            try:
                selected_item = tree.selection()[0]  ## get selected item
                tree.delete(selected_item)
            except:
                messagebox.showerror('ERROR', 'PLEASE SELECT AGAIN')

        Button(master, text='Add', command=add_employee_window, width=10).pack(anchor=S, pady=3)
        Button(master, text='Edit', command=sua, width=10).pack(anchor=S, pady=3)
        Button(master, text='load', command=load_csv, width=10).pack(anchor=S, pady=3)
        Button(master, text='Delete', command=xoa, width=10).pack(anchor=S, pady=3)
        Button(master, text='Exit', command=Thoat, width=10).pack(anchor=S, pady=3)

    def report():
        master = Toplevel()
        master.title('Report table')
        master.geometry('400x400')
        Menu1 = Menu(master)
        master.config(menu=Menu1)

        def addlabels(x, y):
            for i in range(len(x)):
                plt.text(i, y[i], y[i], ha='center')

        def returnn():
            master.destroy()
            main_window.iconify()
            main_window.deiconify()

        Menu1.add_command(label='Back', command=returnn)
        x = ["Full time", 'Part time', 'Resign']
        y = [cc, ccx, ccxx]
        plt.bar(x, y)
        addlabels(x, y)
        plt.xlabel('Amount')
        plt.ylabel('Position')
        plt.title('Total personnel')
        plt.show()

    # Thêm mục File và các lệnh con New, Open, Save và Exit
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Home", menu=file_menu)

    file_menu1 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Employee", menu=file_menu1)
    file_menu1.add_command(label="Employee list", command=dsnv)
    file_menu1.add_command(label="Report", command=report)

    file_menu3 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="System", menu=file_menu3)
    file_menu3.add_command(label="Terms and Policy", command=dieukhoan)
    file_menu3.add_command(label="Exit", command=main_window.destroy)

    file_menu4 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Account", menu=file_menu4)
    file_menu4.add_command(label="password change", command=thaydoimatkhau)
    file_menu4.add_command(label="logout", command=dagxuat)
    main_window.config(menu=menubar)
    a1 = Label(main_window, image=img)
    a1.pack()

    window.withdraw()

    # todo Đợi cửa sổ chính hiển thị trước khi đóng cửa sổ đăng nhập
    window.wait_window(main_window)

    # todo Đóng cửa sổ đăng nhập
    window.destroy()


error_label = Label(window)
# todo Tạo tiêu đề và đường phân cách
label_title = Label(text="Login please", font=("Arial", 14))
label_title.pack(pady=10)
separator = Frame(height=2, bd=1, relief="sunken")
separator.pack(fill="x", padx=20, pady=5)
# todo Tạo các trường nhập
frame_entry = Frame(window)
frame_entry.pack(padx=20, pady=10)
label_username = Label(frame_entry, text="Username: ", font=("Arial", 12))
label_username.pack(side="left")
entry_username = Entry(frame_entry, font=("Arial", 12))
entry_username.pack(side="left")
label_password = Label(frame_entry, text="Password: ", font=("Arial", 12))
label_password.pack(side="left", padx=(20, 0))
entry_password = Entry(frame_entry, show="*", font=("Arial", 12))
entry_password.pack(side="left")
# todo Tạo nút đăng nhập
btn_login = Button(window, text="Login", font=("Arial", 12), bg='red', command=validate_login)
btn_login.pack(pady=10)
# todo Tạo khu vực hiển thị kết quả
result_text = StringVar()
result_text.set("")
label_result = Label(window, textvariable=result_text, font=("Arial", 12))
label_result.pack()

# todo Chạy cửa sổ đăng nhập
window.mainloop()
