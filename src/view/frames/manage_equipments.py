import customtkinter
import tkinter as tk

from tkinter import ttk
from ..fonts import title_font, button_font, label_font


class Equipments(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        equipment_tree = customtkinter.CTkFrame(self, fg_color="transparent")
        equipment_tree.grid_columnconfigure((0, 1, 2, 3), weight=1)
        equipment_tree.grid_rowconfigure((0, 1, 2), weight=1)
        equipment_tree.grid(row=0, column=0, rowspan=2, sticky="nswe")

        tree_label = customtkinter.CTkLabel(
            equipment_tree, text="Manage Equipments", font=title_font
        )
        tree_label.grid(row=0, column=0, columnspan=4, padx=20, pady=33, sticky="n")

        sort_label = customtkinter.CTkLabel(
            equipment_tree, text="Sort:", font=label_font
        )
        sort_label.grid(row=1, column=0, padx=5, pady=(20, 0), sticky="e")
        sort_option = customtkinter.CTkSegmentedButton(
            equipment_tree, values=["ID", "Name", "Quantity"]
        )
        sort_option.set("Name")
        sort_option.grid(row=1, column=1, padx=5, pady=(20, 0), sticky="w")

        order_label = customtkinter.CTkLabel(
            equipment_tree, text="Order:", font=label_font
        )
        order_label.grid(row=1, column=2, padx=5, pady=(20, 0), sticky="e")
        order_option = customtkinter.CTkSegmentedButton(
            equipment_tree, values=["↑", "↓"]
        )
        order_option.set("↓")
        order_option.grid(row=1, column=3, padx=5, pady=(20, 0), sticky="w")

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

        tree = ttk.Treeview(equipment_tree, height=20)

        tree["columns"] = ("Equipment ID", "Name", "Quantity", "Date Updated")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Equipment ID", anchor=tk.CENTER, width=130)
        tree.column("Name", anchor=tk.CENTER, width=170)
        tree.column("Quantity", anchor=tk.CENTER, width=100)
        tree.column("Date Updated", anchor=tk.CENTER, width=150)

        tree.heading("Equipment ID", text="Equipment ID")
        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Date Updated", text="Date Updated")

        tree.grid(row=2, column=0, columnspan=4, padx=20, pady=(20, 35), sticky="nswe")

        add_equipment = customtkinter.CTkFrame(self)
        add_equipment.grid_columnconfigure((0, 1), weight=1)
        add_equipment.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        add_equipment.grid(row=1, column=1, sticky="nswe")

        search_label = customtkinter.CTkLabel(
            add_equipment, text="Search Equipment", font=label_font
        )
        search_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="n")

        search_entry = customtkinter.CTkEntry(
            add_equipment, placeholder_text="Equipment Name", font=label_font
        )
        search_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="n")

        search_button = customtkinter.CTkButton(
            add_equipment, text="Search", font=button_font
        )
        search_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="n")

        add_equipment_label = customtkinter.CTkLabel(
            add_equipment, text="Add Equipment", font=label_font
        )
        add_equipment_label.grid(
            row=3, column=0, columnspan=2, padx=20, pady=10, sticky="n"
        )

        equipment_name_label = customtkinter.CTkLabel(
            add_equipment, text="Equipment Name", font=label_font
        )
        equipment_name_label.grid(row=4, column=0, padx=20, pady=20, sticky="e")

        equipment_entry = customtkinter.CTkEntry(add_equipment, width=150)
        equipment_entry.grid(row=4, column=1, padx=20, pady=20, sticky="w")

        quantity_label = customtkinter.CTkLabel(
            add_equipment, text="Quantity", font=label_font
        )
        quantity_label.grid(row=5, column=0, padx=20, pady=20, sticky="e")

        quantity_entry = customtkinter.CTkEntry(add_equipment, width=150)
        quantity_entry.grid(row=5, column=1, padx=20, pady=20, sticky="w")

        add_button = customtkinter.CTkButton(
            add_equipment, text="Add", font=button_font
        )
        add_button.grid(row=6, column=0, padx=20, pady=20, sticky="e")

        update_button = customtkinter.CTkButton(
            add_equipment, text="Update", font=button_font
        )
        update_button.grid(row=6, column=1, padx=20, pady=20, sticky="w")

        clear_button = customtkinter.CTkButton(
            add_equipment, text="Clear", font=button_font
        )
        clear_button.grid(row=7, column=0, padx=20, pady=(20, 35), sticky="e")

        delete_button = customtkinter.CTkButton(
            add_equipment,
            text="Delete",
            fg_color="#ef476f",
            hover_color="#c1121f",
            font=button_font,
        )
        delete_button.grid(row=7, column=1, padx=20, pady=(20, 35), sticky="w")