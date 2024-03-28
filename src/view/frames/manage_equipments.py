import customtkinter
import tkinter as tk

from tkinter import ttk
from ..fonts import title_font, button_font, label_font
from pathlib import Path
from PIL import Image

asset_dir = Path(__file__).parent.absolute()


class Equipments(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        equipment_tree = customtkinter.CTkFrame(self)
        equipment_tree.grid_columnconfigure((0, 1, 2, 3), weight=1)
        equipment_tree.grid_rowconfigure((0, 1, 2), weight=1)
        equipment_tree.grid(row=0, column=0, sticky="nswe")

        tree_label = customtkinter.CTkLabel(
            equipment_tree, text="Manage Equipments", font=title_font
        )
        tree_label.grid(
            row=0, column=0, columnspan=4, padx=30, pady=(30, 50), sticky="n"
        )

        sort_label = customtkinter.CTkLabel(
            equipment_tree, text="Sort:", font=label_font
        )
        sort_label.grid(row=1, column=0, padx=5, pady=(20, 0), sticky="e")

        self.sort_text = ["Name", "Quantity", "Date"]
        self.sort_index = 0
        self.sort_button = customtkinter.CTkButton(
            equipment_tree,
            text=self.sort_text[self.sort_index],
            font=button_font,
            width=80,
            command=self.sort_command,
        )
        self.sort_button.grid(row=1, column=1, padx=(5, 0), pady=(20, 0), sticky="w")

        self.order_text = ["↑", "↓"]
        self.order_index = 0
        self.order_button = customtkinter.CTkButton(
            equipment_tree,
            text=self.order_text[self.order_index],
            font=button_font,
            width=30,
            command=self.order_command,
        )
        self.order_button.grid(row=1, column=1, padx=(90, 0), pady=(20, 0), sticky="w")

        search_label = customtkinter.CTkLabel(
            equipment_tree, text="Search:", font=label_font
        )
        search_label.grid(row=1, column=2, padx=5, pady=(20, 0), sticky="e")
        search_entry = customtkinter.CTkEntry(equipment_tree, placeholder_text="Name")
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

        tree = ttk.Treeview(equipment_tree, height=20)

        tree["columns"] = ("Name", "Quantity", "Date Updated")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Name", anchor=tk.CENTER, width=170)
        tree.column("Quantity", anchor=tk.CENTER, width=100)
        tree.column("Date Updated", anchor=tk.CENTER, width=150)

        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Date Updated", text="Date Updated")

        tree.grid(row=2, column=0, columnspan=4, padx=30, pady=(20, 35), sticky="nswe")

        add_equipment = customtkinter.CTkFrame(self)
        add_equipment.grid_columnconfigure((0, 1), weight=1)
        add_equipment.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        add_equipment.grid(row=0, column=1, sticky="we")

        add_equipment_image = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "inventory_image.png"), size=(90, 90)
        )
        equipment_image = customtkinter.CTkLabel(
            add_equipment, text="", image=add_equipment_image
        )
        equipment_image.grid(row=0, column=0, columnspan=2, sticky="we")

        add_equipment_label = customtkinter.CTkLabel(
            add_equipment, text="Add Equipment", font=label_font
        )
        add_equipment_label.grid(
            row=1, column=0, columnspan=2, padx=20, pady=10, sticky="n"
        )

        equipment_name_label = customtkinter.CTkLabel(
            add_equipment, text="Equipment Name", font=label_font
        )
        equipment_name_label.grid(row=2, column=0, padx=20, pady=20, sticky="e")

        equipment_entry = customtkinter.CTkEntry(add_equipment, width=150)
        equipment_entry.grid(row=2, column=1, padx=(20, 30), pady=20, sticky="w")

        quantity_label = customtkinter.CTkLabel(
            add_equipment, text="Quantity", font=label_font
        )
        quantity_label.grid(row=3, column=0, padx=20, pady=20, sticky="e")

        quantity_entry = customtkinter.CTkEntry(
            add_equipment, justify="center", width=80
        )
        quantity_entry.grid(row=3, column=1, padx=(20, 30), pady=20, sticky="w")

        add_button = customtkinter.CTkButton(
            add_equipment, text="Add", font=button_font
        )
        add_button.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="e")

        update_button = customtkinter.CTkButton(
            add_equipment, text="Update", font=button_font
        )
        update_button.grid(row=4, column=1, padx=20, pady=(20, 10), sticky="w")

        clear_button = customtkinter.CTkButton(
            add_equipment, text="Clear", font=button_font
        )
        clear_button.grid(row=5, column=0, padx=(30, 20), pady=(10, 35), sticky="e")

        delete_button = customtkinter.CTkButton(
            add_equipment,
            text="Delete",
            fg_color="#ef476f",
            hover_color="#c1121f",
            font=button_font,
        )
        delete_button.grid(row=5, column=1, padx=(20, 30), pady=(10, 35), sticky="w")

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
