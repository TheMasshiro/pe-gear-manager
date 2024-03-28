import customtkinter
import tkinter as tk

from tkinter import ttk
from ..fonts import title_font, label_font, button_font


class Students(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        student_tree = customtkinter.CTkFrame(self)
        student_tree.grid_columnconfigure((0, 1, 2, 3), weight=1)
        student_tree.grid_rowconfigure((0, 1, 2), weight=1)
        student_tree.grid(row=0, column=0, sticky="nswe")

        student_label = customtkinter.CTkLabel(
            student_tree, text="Manage Students", font=title_font
        )
        student_label.grid(
            row=0, column=0, columnspan=4, padx=30, pady=(30, 50), sticky="n"
        )

        sort_label = customtkinter.CTkLabel(student_tree, text="Sort:", font=label_font)
        sort_label.grid(row=1, column=0, padx=5, pady=(20, 0), sticky="e")

        self.sort_text = ["Name", "Course", "Date"]
        self.sort_index = 0
        self.sort_button = customtkinter.CTkButton(
            student_tree,
            text=self.sort_text[self.sort_index],
            font=button_font,
            width=80,
            command=self.sort_command,
        )
        self.sort_button.grid(row=1, column=1, padx=(5, 0), pady=(20, 0), sticky="w")

        self.order_text = ["↑", "↓"]
        self.order_index = 0
        self.order_button = customtkinter.CTkButton(
            student_tree,
            text=self.order_text[self.order_index],
            font=button_font,
            width=30,
            command=self.order_command,
        )
        self.order_button.grid(row=1, column=1, padx=(90, 0), pady=(20, 0), sticky="w")

        search_label = customtkinter.CTkLabel(
            student_tree, text="Search:", font=label_font
        )
        search_label.grid(row=1, column=2, padx=5, pady=(20, 0), sticky="e")
        search_entry = customtkinter.CTkEntry(
            student_tree, placeholder_text="Student ID"
        )
        search_entry.grid(row=1, column=3, padx=5, pady=(20, 0), sticky="w")

        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            font=("Inter", 10),
            background="#eeeeee",
            foreground="black",
            lrowheight=25,
            fieldbackground="#eeeeee",
            bordercolor="#eeeeee",
            borderwidth=0,
        )
        style.map("Treeview", background=[("selected", "#cccccc")])
        style.configure(
            "Treeview.Heading",
            font=("Inter", 11, "bold"),
            background="#dddddd",
            foreground="black",
            relief="flat",
        )
        style.map("Treeview.Heading", background=[("active", "#cccccc")])

        tree = ttk.Treeview(student_tree, height=20)

        tree["columns"] = (
            "Student ID",
            "Name",
            "Course",
            "Phone Number",
            "Date Created",
        )

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Student ID", anchor=tk.CENTER, width=120)
        tree.column("Name", anchor=tk.CENTER, width=170)
        tree.column("Course", anchor=tk.CENTER, width=100)
        tree.column("Phone Number", anchor=tk.CENTER, width=150)
        tree.column("Date Created", anchor=tk.CENTER, width=130)

        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Phone Number", text="Phone Number")
        tree.heading("Date Created", text="Date Created")

        tree.grid(row=2, column=0, columnspan=4, padx=30, pady=(20, 35), sticky="nswe")

        students_command = customtkinter.CTkFrame(self)
        students_command.grid_columnconfigure(0, weight=1)
        students_command.grid_rowconfigure((0, 1, 2, 3), weight=1)
        students_command.grid(row=0, column=1, sticky="we")

        view_button = customtkinter.CTkButton(students_command, text="View Details")
        view_button.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        edit_button = customtkinter.CTkButton(students_command, text="Edit")
        edit_button.grid(row=1, column=0, padx=20, pady=20, sticky="ns")

        export_button = customtkinter.CTkButton(
            students_command, text="Export to Excel"
        )
        export_button.grid(row=2, column=0, padx=20, pady=20, sticky="ns")

        delete_button = customtkinter.CTkButton(students_command, text="Delete")
        delete_button.grid(row=3, column=0, padx=20, pady=20, sticky="ns")

        self.print_current_sort()
        self.print_current_order()

    def sort_command(self):
        self.sort_index = (self.sort_index + 1) % len(self.sort_text)
        self.sort_button.configure(text=self.sort_text[self.sort_index])
        self.print_current_sort()

    def order_command(self):
        self.order_index = (self.order_index + 1) % len(self.order_text)
        self.order_button.configure(text=self.order_text[self.order_index])
        self.print_current_order()

    def print_current_sort(self):
        print(f"Current button text: {self.sort_button.cget('text')}")

    def print_current_order(self):
        print(f"Current button text: {self.order_button.cget('text')}")
