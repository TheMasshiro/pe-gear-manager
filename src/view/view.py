import customtkinter

from .frames.login import Login
from .frames.logout import Logout
from .frames.manage_equipments import Equipments
from .frames.history import History
from src.controller import generate_frames
from .fonts import menu_font
from pathlib import Path
from PIL import ImageTk, Image


asset_dir = Path(__file__).parent.absolute()


class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, main_frame):
        super().__init__(master)

        self.main_frame = main_frame
        self.menus = []
        self.values=[
                "Student Login",
                "Student Logout",
                "Manage Equipments",
                "Manage Students",
                "Return History",
            ]

        self.grid_rowconfigure(9, weight=1)

        university_icon = customtkinter.CTkImage(
            Image.open(asset_dir / "assets" / "school_logo.png"),
            size=(90, 90),
        )
        university_logo = customtkinter.CTkLabel(self, text="", image=university_icon)
        university_logo.grid(row=0, column=0, padx=30, pady=30, sticky="nwe")

        for i, value in enumerate(self.values):
            self.menu = customtkinter.CTkButton(
                self,
                text=value,
                font=menu_font,
                border_spacing=10,
                corner_radius = 0,
                fg_color="transparent",
                height=50,
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                anchor="w",
                command=lambda value=value: self.get_value(value),
            )
            self.menu.grid(row=i + 1, column=0, sticky="we")
            self.menus.append(self.menu)

        about_button = customtkinter.CTkButton(self, text="About")
        about_button.grid(row=9, column=0, padx=15, pady=(15, 0), sticky="s")

        exit_button = customtkinter.CTkButton(self, text="Exit")
        exit_button.grid(row=10, column=0, padx=15, pady=15, sticky="s")

        self.menus[0].configure(fg_color=("gray75", "gray25"))

    def get_value(self, value):
        self.selected_menu(value)
        self.main_frame.show_frame(value)

    def selected_menu(self, value):
        self.menus[0].configure(fg_color=("gray75", "gray25") if value == "Student Login" else "transparent")
        self.menus[1].configure(fg_color=("gray75", "gray25") if value == "Student Logout" else "transparent")
        self.menus[2].configure(fg_color=("gray75", "gray25") if value == "Manage Equipments" else "transparent")
        self.menus[3].configure(fg_color=("gray75", "gray25") if value == "Manage Students" else "transparent")
        self.menus[4].configure(fg_color=("gray75", "gray25") if value == "Return History" else "transparent")



class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.login = Login(self)
        self.logout = Logout(self)
        self.equipments = Equipments(self)
        self.history = History(self)

    def show_frame(self, value):
        generate_frames(
            self.login, self.logout, self.equipments, self.history, value
        )

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PE Gear Manager")
        self.iconpath = ImageTk.PhotoImage(file=asset_dir / "assets" / "app_icon.png")
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)
        customtkinter.set_default_color_theme("theme.json")
        customtkinter.set_appearance_mode("light")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nswe")
        self.main_frame.show_frame("Student Login")

        self.main_menu = MenuFrame(self, self.main_frame)
        self.main_menu.grid(row=0, column=0, sticky="nsw")
