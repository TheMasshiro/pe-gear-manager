import os
import tkinter as tk
import webbrowser
from tkinter import ttk

import customtkinter
import src.controller.validation as validation
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

path = os.getcwd()


class MenuFrame(customtkinter.CTkFrame):
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
            Image.open(os.path.join(path, "src/view/assets/school_logo.png")),
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
        self.active_users.grid_remove()

        self.sign_in.grid_remove()
        self.sign_out.grid_remove()

        self.add_equipment.grid_remove()
        self.inventory_buttons.grid_remove()
        self.inventory_search.grid_remove()

        self.history.grid_remove()

        if value == "Active Users":
            self.active_users.grid(row=0, column=0, padx=(200, 20), pady=30, sticky="n")
            self.separator.grid(row=0, column=0, padx=(0, 960), pady=0, sticky="n")
        elif value == "Sign In/Out":
            self.sign_in.grid(row=0, column=0, padx=(225, 10), pady=30, sticky="n")
            self.sign_out.grid(row=0, column=1, padx=(10, 70), pady=30, sticky="n")
            self.separator.grid(row=0, column=0, padx=(0, 290), pady=0, sticky="n")
        elif value == "Add Equipments":
            self.add_equipment.grid(
                row=0, column=0, padx=(235, 10), pady=30, sticky="n"
            )
            self.inventory_buttons.grid(
                row=0, column=1, padx=(30, 200), pady=(70, 100), sticky="s"
            )
            self.inventory_search.grid(
                row=0, column=1, padx=(30, 200), pady=(30, 100), sticky="n"
            )
            self.separator.grid(row=0, column=0, padx=(0, 370), pady=0, sticky="n")
        elif value == "Return History":
            self.history.grid(row=0, column=0, padx=(200, 20), pady=30, sticky="n")
            self.separator.grid(row=0, column=0, padx=(0, 960), pady=0, sticky="n")
        else:
            raise Exception("Not in the menu")

    def show_about(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = AboutApplicationWindow(self)
        else:
            self.about_window.focus_force()


class ActiveUserFrame(customtkinter.CTkFrame):
    def __init__(self, master):
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

        tree["columns"] = ("Student ID", "Name", "Course", "Sign In Time")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Student ID", anchor=tk.CENTER, width=200)
        tree.column("Name", anchor=tk.CENTER, width=200)
        tree.column("Course", anchor=tk.CENTER, width=200)
        tree.column("Sign In Time", anchor=tk.CENTER, width=200)

        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Sign In Time", text="Sign In Time")

        tree.grid(row=1, column=0, padx=20, pady=20, sticky="n")


class SignInFrame(customtkinter.CTkFrame):
    def __init__(self, master):
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
        self.id_number = customtkinter.CTkEntry(self, width=110)
        self.id_number.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        name_label = customtkinter.CTkLabel(
            self, text="Student Name", font=("Inter", 14, "bold")
        )
        name_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.student_name = customtkinter.CTkEntry(self, width=170)
        self.student_name.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        number_label = customtkinter.CTkLabel(
            self, text="Phone Number", font=("Inter", 14, "bold")
        )
        number_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.student_number = customtkinter.CTkEntry(self, width=120)
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
            self, values=["1st-Year", "2nd-Year", "3rd-Year", "4th-Year"], width=110
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
            self, text="Sign In", font=("Inter", 15, "bold"), command=self.get_equipment
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

    def sign_in_popup(self):
        pass

    def sign_up_popup(self):
        if validation.validate_id(
            self.id_number.get()
        ) and validation.validate_phone_number(self.student_number.get()):
            CTkMessagebox(
                title="Sign Up",
                message="Successfuly Registered",
                icon="check",
                option_1="OK",
                justify="center",
                corner_radius=10,
            )
        else:
            CTkMessagebox(
                title="Sign Up Error",
                message="Please properly fill in the fields.",
                icon="cancel",
                option_1="OK",
                justify="center",
                corner_radius=10,
            )

    def get_equipment(self):
        if (
            self.get_equipment_window is None
            or not self.get_equipment_window.winfo_exists()
        ):
            self.get_equipment_window = GetEquipmentWindow(self)
        else:
            self.get_equipment_window.focus_force()


class SignOutFrame(customtkinter.CTkFrame):
    def __init__(self, master):
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

        tree = ttk.Treeview(self, height=21)

        tree["columns"] = ("Student ID", "Name", "Course", "Sign In Time")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Student ID", anchor=tk.CENTER, width=130)
        tree.column("Name", anchor=tk.CENTER, width=170)
        tree.column("Course", anchor=tk.CENTER, width=100)
        tree.column("Sign In Time", anchor=tk.CENTER, width=150)

        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Sign In Time", text="Sign In Time")

        tree.grid(row=1, column=0, padx=20, pady=20, sticky="n")

        sign_out_button = customtkinter.CTkButton(
            self, text="Sign Out", font=("Inter", 15, "bold")
        )
        sign_out_button.grid(
            row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ns"
        )


class AddEquipmentFrame(customtkinter.CTkFrame):
    def __init__(self, master):
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
    def __init__(self, master):
        super().__init__(master)

        self._border_color = "black"
        self._border_width = 1

        inventory_icon = customtkinter.CTkImage(
            Image.open(os.path.join(path, "src/view/assets/inventory_image.png")),
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
    def __init__(self, master):
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
    def __init__(self, master):
        super().__init__(master)

        line = customtkinter.CTkFrame(
            self,
            width=2,
            height=self.winfo_screenheight(),
            border_width=1,
            border_color="black",
        )
        line.grid(row=0, column=0, sticky="w")


class AboutApplicationWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
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
            Image.open(os.path.join(path, "src/view/assets/facebook_icon.png")),
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
            lambda e: self.open_link("https://www.facebook.com/Inchan.Vi/"),
        )

        self.github_mark = customtkinter.CTkImage(
            Image.open(os.path.join(path, "src/view/assets/github_mark.png")),
            size=(80, 80),
        )
        self.github_link = customtkinter.CTkLabel(
            self, text="", image=self.github_mark, cursor="hand2"
        )
        self.github_link.grid(row=2, column=2, padx=(0, 70), pady=(10, 10), sticky="ne")
        self.github_link.bind(
            "<Button-1>", lambda e: self.open_link("https://github.com/TheMasshiro")
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
    def __init__(self, master):
        super().__init__(master)
        self.title("Get Equipments")
        self.geometry("600x400")
        self.resizable(False, False)
        self.grab_set()

        # TODO
        # ask the user for input in text box


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PE Borrow Buddy")
        self.iconpath = ImageTk.PhotoImage(
            file=os.path.join(path, "src/view/assets/icon.png")
        )
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
