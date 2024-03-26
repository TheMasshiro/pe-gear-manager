import customtkinter

from ..fonts import title_font, button_font, label_font
from .register_popup import RegisterPopup

class Login(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.register_window = None

        sign_in_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        sign_in_frame.grid_columnconfigure(1, weight=1)
        sign_in_frame.grid_rowconfigure(3, weight=1)
        sign_in_frame.grid(row=0, column=0, sticky="n")

        sign_in_label = customtkinter.CTkLabel(
            sign_in_frame, text="Student Login", font=title_font
        )
        sign_in_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(30, 50), sticky="n")

        id_label = customtkinter.CTkLabel(
            sign_in_frame, text="ID Number", font=label_font
        )
        id_label.grid(row=1, column=0, padx=30, pady=30, sticky="we")
        self.id_number = customtkinter.CTkEntry(sign_in_frame, justify="center", width=120)
        # TODO add the enter button function
        self.id_number.grid(row=1, column=1, padx=30, pady=30, sticky="we")

        log_in_button = customtkinter.CTkButton(
            sign_in_frame, text="Login", font=button_font
        )
        log_in_button.grid(row=3, column=0, columnspan=2, padx=30, pady=(20, 15), sticky="s")

        register_button = customtkinter.CTkButton(
            sign_in_frame, text="Register", font=button_font, command=self.show_register
        )
        register_button.grid(row=4, column=0, columnspan=2, padx=30, pady=(15, 20), sticky="s")

        student_info_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        student_info_frame.grid_columnconfigure((0,1), weight=1)
        student_info_frame.grid_rowconfigure(7, weight=1)
        student_info_frame.grid(row=0, column=1, sticky="ns")

        student_info_label = customtkinter.CTkLabel(
            student_info_frame, text="Student Information", font=title_font
        )
        student_info_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(30, 50), sticky="n")

        student_id_label = customtkinter.CTkLabel(student_info_frame, text="ID Number:", font=label_font)
        student_id_label.grid(row=1, column=0, padx=20, pady=20, sticky="we")
        student_id = customtkinter.CTkLabel(student_info_frame, text="")
        student_id.grid(row=1, column=1, padx=20, pady=20, sticky="we")

        student_name_label = customtkinter.CTkLabel(student_info_frame, text="Student Name:", font=label_font)
        student_name_label.grid(row=2, column=0, padx=20, pady=20, sticky="we")
        student_name = customtkinter.CTkLabel(student_info_frame, text="")
        student_name.grid(row=2, column=1, padx=20, pady=20, sticky="we")

        student_number_label = customtkinter.CTkLabel(student_info_frame, text="Phone Number:", font=label_font)
        student_number_label.grid(row=3, column=0, padx=20, pady=20, sticky="we")
        student_number = customtkinter.CTkLabel(student_info_frame, text="")
        student_number.grid(row=3, column=1, padx=20, pady=20, sticky="we")

        student_course_label = customtkinter.CTkLabel(student_info_frame, text="Course:", font=label_font)
        student_course_label.grid(row=4, column=0, padx=20, pady=20, sticky="we")
        student_course = customtkinter.CTkLabel(student_info_frame, text="")
        student_course.grid(row=4, column=1, padx=20, pady=20, sticky="we")

        student_year_label = customtkinter.CTkLabel(student_info_frame, text="Year:", font=label_font)
        student_year_label.grid(row=5, column=0, padx=20, pady=20, sticky="we")
        student_year = customtkinter.CTkLabel(student_info_frame, text="")
        student_year.grid(row=5, column=1, padx=20, pady=20, sticky="we")

        student_section_label = customtkinter.CTkLabel(student_info_frame, text="Section:", font=label_font)
        student_section_label.grid(row=6, column=0, padx=20, pady=20, sticky="we")
        student_section = customtkinter.CTkLabel(student_info_frame, text="")
        student_section.grid(row=6, column=1, padx=20, pady=20, sticky="we")


    def show_register(self):
        if self.register_window is None or not self.register_window.winfo_exists():
            self.register_window = RegisterPopup(self)  # create window if its None or destroyed
        else:
            self.register_window.focus()
