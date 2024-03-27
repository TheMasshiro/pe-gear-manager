import customtkinter
import tkinter as tk

from tkinter import ttk
from ..fonts import title_font, button_font


class Logout(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        label = customtkinter.CTkLabel(self, text="Student Logout", font=title_font)
        label.grid(row=0, column=0, pady=20, sticky="n")

        logout_button = customtkinter.CTkButton(
            self, text="Logout", font=button_font
        )
        logout_button.grid(row=3, column=0, pady=(10,20), sticky="s")

        status_button = customtkinter.CTkButton(
            self, text="Check Status", font=button_font
        )
        status_button.grid(row=2, column=0, pady=(20,10), sticky="s")


        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            font=("Inter", 11),
            background="#eeeeee",
            foreground="black",
            lrowheight=25,
            fieldbackground="#eeeeee",
            bordercolor="eeeeee",
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

        self.users_tree = ttk.Treeview(self, height=23)

        self.users_tree["columns"] = ("Student ID", "Name", "Course", "Sign In Time")

        self.users_tree.column("#0", width=0, stretch=tk.NO)
        self.users_tree.column("Student ID", anchor=tk.CENTER, width=200)
        self.users_tree.column("Name", anchor=tk.CENTER, width=200)
        self.users_tree.column("Course", anchor=tk.CENTER, width=200)
        self.users_tree.column("Sign In Time", anchor=tk.CENTER, width=200)

        self.users_tree.heading("Student ID", text="Student ID")
        self.users_tree.heading("Name", text="Name")
        self.users_tree.heading("Course", text="Course")
        self.users_tree.heading("Sign In Time", text="Sign In Time")

        self.users_tree.grid(row=1, column=0, padx=30, sticky="we")
