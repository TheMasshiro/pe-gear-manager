"""

Module : view.py

This module is used to
create the user interface.
It is responsible for creating
diffrent tabs like check-in
while also sending data to
backend for computation and storage

"""

import tkinter as tk
import webbrowser
import customtkinter

from tkinter import ttk
from pathlib import Path
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from src.controller import (
    generate_frames,
    validate_id,
    validate_name,
    validate_phone_number,
    validate_course,
    validate_section,
    student_id_record,
    student_name_record,
    autofill_helper_fill,
    autofill_helper_clear,
    sign_up_insert_data,
    student_tree_helper,
)

# Get the current working dictionary
asset_dir = Path(__file__).parent.absolute()


class MenuFrame(customtkinter.CTkFrame):
    # Class to represent main menu frame
    def __init__(
        self,
        master,
        values,
        active_users,
        sign_in,
        sign_out,
        add_equipment,
        inventory_buttons,
        inventory_search,
        history,
        separator,
    ):
        """Initialize and create MenuFrame Interface"""
        super().__init__(master)

        self.values = values
        self.active_users = active_users
        self.sign_in = sign_in
        self.sign_out = sign_out
        self.add_equipment = add_equipment
        self.inventory_buttons = inventory_buttons
        self.inventory_search = inventory_search
        self.history = history
        self.separator = separator

        self.menus = []

        university_icon = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "school_logo.png"),
            size=(80, 80),
        )
        university_logo = customtkinter.CTkLabel(self, text="", image=university_icon)
        university_logo.grid(row=0, column=0, padx=20, pady=(20, 110), sticky="n")

        for i, value in enumerate(self.values):
            menu = customtkinter.CTkButton(
                self,
                text=value,
                font=("Inter", 14, "bold"),
                command=lambda value=value: self.show_frame(value),
            )
            menu.grid(row=i + 1, column=0, padx=10, pady=20, sticky="w")
            self.menus.append(menu)

        about_button = customtkinter.CTkButton(
            self,
            text="About",
            font=("Inter", 14, "bold"),
            fg_color="transparent",
            hover_color="gray90",
            text_color="black",
            command=self.show_about,
        )
        about_button.grid(row=5, column=0, padx=10, pady=(160, 20), sticky="w")
        self.about_window = None

        self.active_users.grid_remove()

        self.sign_in.grid_remove()
        self.sign_out.grid_remove()

        self.add_equipment.grid_remove()
        self.inventory_buttons.grid_remove()
        self.inventory_search.grid_remove()

        self.history.grid_remove()

        self.separator.grid_remove()

        self.show_frame(self.values[1])


    def show_frame(self, value):
        """Function to place the tabs on the screen"""
        generate_frames(
            self.active_users,
            self.sign_in,
            self.sign_out,
            self.add_equipment,
            self.inventory_buttons,
            self.inventory_search,
            self.history,
            self.separator,
            value,
        )

    def show_about(self):
        """Display information related to signing out a user"""
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = AboutApplicationWindow(self)
        else:
            self.about_window.focus_force()


class ActiveUserFrame(customtkinter.CTkFrame):
    """Represents the frame for displaying active users"""

    def __init__(self, master):
        """Initialize and Displays the ACtiveUserFrame widgets"""
        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        label = customtkinter.CTkLabel(
            self, text="Current Users", font=("Inter", 25, "bold")
        )
        label.grid(row=0, column=0, padx=100, pady=20, sticky="s")

        status_button = customtkinter.CTkButton(
            self, text="Check Status", font=("Inter", 14, "bold")
        )
        status_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="n")

        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            font=("Inter", 11),
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

        self.tree = ttk.Treeview(self, height=23)

        self.tree["columns"] = ("Student ID", "Name", "Course", "Sign In Time")

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Student ID", anchor=tk.CENTER, width=200)
        self.tree.column("Name", anchor=tk.CENTER, width=200)
        self.tree.column("Course", anchor=tk.CENTER, width=200)
        self.tree.column("Sign In Time", anchor=tk.CENTER, width=200)

        self.tree.heading("Student ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Sign In Time", text="Sign In Time")

        self.tree.grid(row=1, column=0, padx=20, pady=20, sticky="n")

    def add_active_students(self):
        student_tree_helper(self.tree)


class SignInFrame(customtkinter.CTkFrame):
    """Represents the users sign in frame"""

    def __init__(self, master):
        """Initializes the SignInFrame and sets up the interface for signing in users"""

        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1
        self.get_equipment_window = None

        label = customtkinter.CTkLabel(self, text="Sign In", font=("Inter", 25, "bold"))
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="ns")

        id_label = customtkinter.CTkLabel(
            self, text="ID Number", font=("Inter", 14, "bold")
        )
        id_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.id_number = customtkinter.CTkEntry(self, width=120)
        self.id_number.bind("<Return>", self.autofill_entries)
        self.id_number.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        name_label = customtkinter.CTkLabel(
            self, text="Student Name", font=("Inter", 14, "bold")
        )
        name_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.student_name = customtkinter.CTkEntry(self, width=190)
        self.student_name = customtkinter.CTkEntry(self, width=185)
        self.student_name.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        number_label = customtkinter.CTkLabel(
            self, text="Phone Number", font=("Inter", 14, "bold")
        )
        number_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.student_number = customtkinter.CTkEntry(self, width=140)
        self.student_number.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        course_label = customtkinter.CTkLabel(
            self, text="Course", font=("Inter", 14, "bold")
        )
        course_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.student_course = customtkinter.CTkEntry(self, width=80)
        self.student_course.grid(row=4, column=1, padx=20, pady=20, sticky="w")

        year_label = customtkinter.CTkLabel(
            self, text="Year Level", font=("Inter", 14, "bold")
        )
        year_label.grid(row=5, column=0, padx=20, pady=20, sticky="w")
        self.student_year = customtkinter.CTkOptionMenu(
            self, values=["1", "2", "3", "4"], width=60
        )
        self.student_year.grid(row=5, column=1, padx=20, pady=20, sticky="w")

        section_label = customtkinter.CTkLabel(
            self, text="Section", font=("Inter", 14, "bold")
        )
        section_label.grid(row=6, column=0, padx=20, pady=20, sticky="w")
        self.student_section = customtkinter.CTkEntry(self, justify="center", width=40)
        self.student_section.grid(row=6, column=1, padx=20, pady=20, sticky="w")

        blank_label = customtkinter.CTkLabel(self, text="")
        blank_label.grid(row=7, column=0, padx=20, pady=20, sticky="w")

        sign_in_button = customtkinter.CTkButton(
            self, text="Sign In", font=("Inter", 15, "bold"), command=self.sign_in_popup
        )
        sign_in_button.grid(
            row=8, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ns"
        )

        sign_up_button = customtkinter.CTkButton(
            self,
            text="Sign Up",
            font=("Inter", 15, "bold"),
            fg_color="#0496ff",
            hover_color="#006ba6",
            command=self.sign_up_popup,
        )
        sign_up_button.grid(
            row=9, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ns"
        )

    def autofill_entries(self, event):
        """Autofill the entry fields in the sign up frame"""
        if event.widget:
            if student_id_record(self.id_number.get()):
                autofill_helper_fill(
                    self.id_number,
                    self.student_name,
                    self.student_number,
                    self.student_course,
                    self.student_year,
                    self.student_section,
                    tk,
                )
            else:
                autofill_helper_clear(
                    self.id_number,
                    self.student_name,
                    self.student_number,
                    self.student_course,
                    self.student_year,
                    self.student_section,
                    tk,
                )
                CTkMessagebox(
                    title="No Student Found",
                    message="No student found in record, please sign up first.",
                    icon="cancel",
                    option_1="OK",
                    justify="center",
                    corner_radius=10,
                )

    def sign_in_popup(self):
        if student_id_record(self.id_number.get()) and student_name_record(
            self.student_name.get()
        ):
            print("Hello, World")
            ActiveUserFrame(self).add_active_students()
            SignOutFrame(self).add_to_sign_out()
            autofill_helper_clear(
                self.id_number,
                self.student_name,
                self.student_number,
                self.student_course,
                self.student_year,
                self.student_section,
                tk,
            )
        else:
            print("No hello received")

    def sign_up_popup(self):
        """Opens a popup window for signing up new users"""

        if not (
            validate_id(self.id_number.get())
            and validate_name(self.student_name.get())
            and validate_phone_number(self.student_number.get())
            and validate_course(self.student_course.get())
            and self.student_year.get()
            and validate_section(self.student_section.get())
        ):
            CTkMessagebox(
                title="Sign Up Error",
                message="Please properly fill in the fields.",
                icon="cancel",
                option_1="OK",
                justify="center",
                corner_radius=10,
            )
        elif student_id_record(self.id_number.get()) or student_name_record(
            self.student_name.get()
        ):
            CTkMessagebox(
                title="Sign Up Error",
                message="Student ID or Name Already Exists.",
                icon="cancel",
                option_1="OK",
                justify="center",
                corner_radius=10,
            )
        else:
            sign_up_insert_data(
                self.id_number,
                self.student_name,
                self.student_number,
                self.student_course,
                self.student_year,
                self.student_section,
            )
            CTkMessagebox(
                title="Sign Up",
                message="Successfuly Registered",
                icon="check",
                option_1="OK",
                justify="center",
                corner_radius=10,
            )
            autofill_helper_clear(
                self.id_number,
                self.student_name,
                self.student_number,
                self.student_course,
                self.student_year,
                self.student_section,
                tk,
            )

    def get_equipment(self):
        """Opens a window for getting equipment after signing in"""

        if (
            self.get_equipment_window is None
            or not self.get_equipment_window.winfo_exists()
        ):
            self.get_equipment_window = GetEquipmentWindow(self)
        else:
            self.get_equipment_window.focus_force()


class SignOutFrame(customtkinter.CTkFrame):
    """Represents the frame for signing out users"""

    def __init__(self, master):
        """Initializes the SignOutFrame and sets up the interface for signing out users"""

        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        label = customtkinter.CTkLabel(
            self, text="Sign Out", font=("Inter", 25, "bold")
        )
        label.grid(row=0, column=0, padx=10, pady=20, sticky="n")

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

        self.sign_out_tree = ttk.Treeview(self, height=21)

        self.sign_out_tree["columns"] = ("Student ID", "Name", "Course", "Sign In Time")

        self.sign_out_tree.column("#0", width=0, stretch=tk.NO)
        self.sign_out_tree.column("Student ID", anchor=tk.CENTER, width=130)
        self.sign_out_tree.column("Name", anchor=tk.CENTER, width=170)
        self.sign_out_tree.column("Course", anchor=tk.CENTER, width=100)
        self.sign_out_tree.column("Sign In Time", anchor=tk.CENTER, width=150)

        self.sign_out_tree.heading("Student ID", text="Student ID")
        self.sign_out_tree.heading("Name", text="Name")
        self.sign_out_tree.heading("Course", text="Course")
        self.sign_out_tree.heading("Sign In Time", text="Sign In Time")

        self.sign_out_tree.grid(row=1, column=0, padx=20, pady=20, sticky="n")

        sign_out_button = customtkinter.CTkButton(
            self, text="Sign Out", font=("Inter", 15, "bold")
        )
        sign_out_button.grid(
            row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ns"
        )

    def add_to_sign_out(self):
        print("Hello from signout")
        student_tree_helper(self.sign_out_tree)


class AddEquipmentFrame(customtkinter.CTkFrame):
    """Represents the frame for managing equipment inventory."""

    def __init__(self, master):
        """Initializes the InventoryButtonsFrame and sets up the interface for managing inventory buttons."""

        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        label = customtkinter.CTkLabel(
            self, text="Equipments Inventory", font=("Inter", 25, "bold")
        )
        label.grid(row=0, column=0, padx=10, pady=20, sticky="n")

        sort_label = customtkinter.CTkLabel(
            self, text="Sort By", font=("Inter", 14, "bold")
        )
        sort_label.grid(row=1, column=0, padx=(40, 5), pady=(20, 0), sticky="w")
        sort_option = customtkinter.CTkSegmentedButton(
            self, values=["ID", "Name", "Quantity"]
        )
        sort_option.grid(row=1, column=0, padx=(10, 165), pady=(20, 0), sticky="e")

        sort_label_2 = customtkinter.CTkLabel(
            self, text="Order", font=("Inter", 14, "bold")
        )
        sort_label_2.grid(row=2, column=0, padx=(40, 5), pady=5, sticky="w")
        sort_option_2 = customtkinter.CTkSegmentedButton(self, values=["↑", "↓"])
        sort_option_2.grid(row=2, column=0, padx=(10, 270), pady=5, sticky="e")

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

        tree = ttk.Treeview(self, height=20)

        tree["columns"] = ("Equipment ID", "Name", "Quantity")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Equipment ID", anchor=tk.CENTER, width=130)
        tree.column("Name", anchor=tk.CENTER, width=170)
        tree.column("Quantity", anchor=tk.CENTER, width=100)

        tree.heading("Equipment ID", text="Equipment ID")
        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")

        tree.grid(row=3, column=0, padx=20, pady=20, sticky="n")


class InventoryButtonsFrame(customtkinter.CTkFrame):
    """Represents the frame for searching equipment in the inventory"""

    def __init__(self, master):
        """Initializes the InventorySearchFrame and sets up the interface for searching equipment"""
        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        inventory_icon = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "inventory_image.png"),
            size=(80, 80),
        )
        inventory_label = customtkinter.CTkLabel(self, text="", image=inventory_icon)
        inventory_label.grid(
            row=0, column=0, columnspan=2, padx=20, pady=20, sticky="n"
        )

        equipment_name_label = customtkinter.CTkLabel(
            self, text="Equipment Name", font=("Inter", 14, "bold")
        )
        equipment_name_label.grid(row=1, column=0, padx=(20, 10), pady=20, sticky="w")
        equipment_entry = customtkinter.CTkEntry(self, width=150)
        equipment_entry.grid(row=1, column=1, padx=(0, 20), pady=20, sticky="w")

        equipment_quantity_label = customtkinter.CTkLabel(
            self, text="Quantity", font=("Inter", 14, "bold")
        )
        equipment_quantity_label.grid(
            row=2, column=0, padx=(20, 10), pady=20, sticky="w"
        )
        quantity_entry = customtkinter.CTkEntry(self, width=100)
        quantity_entry.grid(row=2, column=1, padx=(0, 20), pady=20, sticky="w")

        add_button = customtkinter.CTkButton(
            self, text="Add", font=("Inter", 15, "bold")
        )
        add_button.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        update_button = customtkinter.CTkButton(
            self, text="Update", font=("Inter", 15, "bold")
        )
        update_button.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        delete_button = customtkinter.CTkButton(
            self,
            text="Delete",
            fg_color="#ef476f",
            hover_color="#c1121f",
            font=("Inter", 15, "bold"),
        )
        delete_button.grid(row=4, column=1, padx=20, pady=20, sticky="w")

        clear_button = customtkinter.CTkButton(
            self, text="Clear", font=("Inter", 15, "bold")
        )
        clear_button.grid(row=4, column=0, padx=20, pady=20, sticky="w")


class InventorySearchFrame(customtkinter.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        search_label = customtkinter.CTkLabel(
            self, text="Search Equipment", font=("Inter", 16, "bold")
        )
        search_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="n")

        name_label = customtkinter.CTkLabel(
            self, text="Name", font=("Inter", 14, "bold")
        )
        name_label.grid(row=1, column=0, padx=(20, 5), pady=(10, 10), sticky="n")

        search_entry = customtkinter.CTkEntry(self, width=120)
        search_entry.grid(
            row=1, column=1, columnspan=2, padx=(5, 20), pady=(10, 10), sticky="n"
        )

        search_button = customtkinter.CTkButton(
            self, text="Search", font=("Inter", 15, "bold")
        )
        search_button.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="n")


class HistoryFrame(customtkinter.CTkFrame):
    """Represents the frame for displaying sign-in and sign-out history"""

    def __init__(self, master):
        """Initializes the HistoryFrame and sets up the interface for displaying history"""

        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        label = customtkinter.CTkLabel(self, text="History", font=("Inter", 25, "bold"))
        label.grid(row=0, column=0, padx=100, pady=20, sticky="s")

        status_button = customtkinter.CTkButton(
            self, text="Check History", font=("Inter", 14, "bold")
        )
        status_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="n")

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

        tree.grid(row=1, column=0, padx=20, pady=20, sticky="n")


class Separator(customtkinter.CTkFrame):
    """Represents a separator between different sections of the user interface"""

    def __init__(self, master):
        """Initializes the Separator with the provided master widget and sets up the separator line"""

        super().__init__(master)

        line = customtkinter.CTkFrame(
            self,
            width=2,
            height=self.winfo_screenheight(),
            border_width=1,
            border_color="black",
        )
        line.grid(row=0, column=0, sticky="nsew")


class AboutApplicationWindow(customtkinter.CTkToplevel):
    """Represents the window for displaying information about the application"""

    def __init__(self, master):
        """Initializes the AboutApplicationWindow and sets up the interface for displaying application information"""

        super().__init__(master)
        self.title("About Application")
        self.geometry("500x400")
        self.resizable(False, False)
        self.grab_set()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.columnconfigure(3, minsize=50)

        self.any_bugs = customtkinter.CTkLabel(
            self, text="Found Any Bugs?", font=("Inter", 15, "bold")
        )
        self.any_bugs.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="n")

        self.contact_label = customtkinter.CTkLabel(
            self, text="Contact Me At", font=("Inter", 15, "bold")
        )
        self.contact_label.grid(
            row=1, column=0, columnspan=4, padx=20, pady=20, sticky="n"
        )

        self.facebook_icon = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "facebook_icon.png"),
            size=(80, 80),
        )
        self.facebook_link = customtkinter.CTkLabel(
            self, text="", image=self.facebook_icon, cursor="hand2"
        )
        self.facebook_link.grid(
            row=2, column=0, padx=(125, 0), pady=(10, 20), sticky="nw"
        )
        self.facebook_link.bind(
            "<Button-1>",
            lambda _: self.open_link("https://www.facebook.com/Inchan.Vi/"),
        )

        self.github_mark = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "github_mark.png"),
            size=(80, 80),
        )
        self.github_link = customtkinter.CTkLabel(
            self, text="", image=self.github_mark, cursor="hand2"
        )
        self.github_link.grid(row=2, column=2, padx=(0, 70), pady=(10, 10), sticky="ne")
        self.github_link.bind(
            "<Button-1>", lambda _: self.open_link("https://github.com/TheMasshiro")
        )

        self.facebook_label = customtkinter.CTkLabel(
            self, text="Facebook", font=("Inter", 13, "bold")
        )
        self.facebook_label.grid(
            row=3, column=0, padx=(0, 40), pady=(0, 20), sticky="e"
        )

        self.github_label = customtkinter.CTkLabel(
            self, text="Github", font=("Inter", 13, "bold")
        )
        self.github_label.grid(row=3, column=2, padx=(50, 0), pady=(0, 20), sticky="w")

        self.made_label = customtkinter.CTkLabel(
            self, text="Made By John Christian Vicente", font=("Inter", 14, "bold")
        )
        self.made_label.grid(
            row=4, column=0, columnspan=4, padx=20, pady=10, sticky="s"
        )

        self.button = customtkinter.CTkButton(
            self, text="Close", font=("Inter", 14, "bold")
        )
        self.button.grid(
            row=5, column=0, columnspan=4, padx=20, pady=(10, 20), sticky="s"
        )
        self.button.configure(command=self.destroy)

    def open_link(self, url):
        webbrowser.open_new(url)


class GetEquipmentWindow(customtkinter.CTkToplevel):
    """Represents the window for getting equipment after signing in"""

    def __init__(self, master):
        """Initializes the GetEquipmentWindow and sets up the interface for getting equipment"""
        super().__init__(master)
        self.title("Get Equipments")
        self.geometry("600x400")
        self.resizable(False, False)
        self.grab_set()

        # TODO
        # ask the user for input in text box


class App(customtkinter.CTk):
    """Represents the main applicationRepresents the main application"""

    def __init__(self):
        """Initializes the App and sets up the main user interface by creating instances of various frames and widgets"""

        super().__init__()
        self.title("PE Gear Manager")
        self.iconpath = ImageTk.PhotoImage(file=asset_dir / "assets" / "icon.png")
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("theme.json")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.active_users = ActiveUserFrame(self)

        self.sign_in = SignInFrame(self)
        self.sign_out = SignOutFrame(self)

        self.add_equipment = AddEquipmentFrame(self)
        self.inventory_buttons = InventoryButtonsFrame(self)
        self.inventory_search = InventorySearchFrame(self)

        self.history = HistoryFrame(self)

        self.separator = Separator(self)

        self.menu_frame = MenuFrame(
            self,
            values=["Active Users", "Sign In/Out", "Add Equipments", "Return History"],
            active_users=self.active_users,
            sign_in=self.sign_in,
            sign_out=self.sign_out,
            add_equipment=self.add_equipment,
            inventory_buttons=self.inventory_buttons,
            inventory_search=self.inventory_search,
            history=self.history,
            separator=self.separator,
        )
        self.menu_frame.grid(row=0, column=0, padx=20, pady=30, sticky="nw")
