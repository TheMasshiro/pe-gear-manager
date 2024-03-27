import customtkinter
import tkinter as tk

from tkinter import ttk
from ..fonts import title_font, button_font


class History(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        label = customtkinter.CTkLabel(self, text="History", font=title_font)
        label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        history_button = customtkinter.CTkButton(
            self, text="Check History", font=button_font
        )
        history_button.grid(row=2, column=0, padx=30, pady=20, sticky="s")

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

        tree = ttk.Treeview(self, height=23)

        tree["columns"] = ("Student ID", "Name", "Course", "Sign Out Time")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Student ID", anchor=tk.CENTER, width=200)
        tree.column("Name", anchor=tk.CENTER, width=200)
        tree.column("Course", anchor=tk.CENTER, width=200)
        tree.column("Sign Out Time", anchor=tk.CENTER, width=200)

        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Sign Out Time", text="Sign Out Time")

        tree.grid(row=1, column=0, padx=30, sticky="nswe")
