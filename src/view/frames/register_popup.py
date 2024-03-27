import customtkinter

from ..fonts import title_font, label_font, button_font


class RegisterPopup(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Student Register")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grab_set()

        reigster_label = customtkinter.CTkLabel(self, text="Register", font=title_font)
        reigster_label.grid(row=0, column=0, columnspan=2, padx=30, pady=30, sticky="n")

        student_id_label = customtkinter.CTkLabel(self, text="ID Number:", font=label_font)
        student_id_label.grid(row=1, column=0, padx=30, pady=20, sticky="e")
        id_number = customtkinter.CTkEntry(self)
        id_number.grid(row=1, column=1, padx=30, pady=20, sticky="w")

        student_name_label = customtkinter.CTkLabel(self, text="Name:", font=label_font)
        student_name_label.grid(row=2, column=0, padx=30, pady=20, sticky="e")
        name = customtkinter.CTkEntry(self, width=190)
        name.grid(row=2, column=1, padx=30, pady=20, sticky="w")

        student_number_label = customtkinter.CTkLabel(self, text="Phone Number:", font=label_font)
        student_number_label.grid(row=3, column=0, padx=30, pady=20, sticky="e")
        number = customtkinter.CTkEntry(self)
        number.grid(row=3, column=1, padx=30, pady=20, sticky="w")

        student_course_label = customtkinter.CTkLabel(self, text="Course:", font=label_font)
        student_course_label.grid(row=4, column=0, padx=30, pady=20, sticky="e")
        course = customtkinter.CTkEntry(self, width=90)
        course.grid(row=4, column=1, padx=30, pady=20, sticky="w")

        student_year_label = customtkinter.CTkLabel(self, text="Year Level:", font=label_font)
        student_year_label.grid(row=5, column=0, padx=30, pady=20, sticky="e")
        year =  customtkinter.CTkOptionMenu(
            self, values=["1", "2", "3", "4"], width=70
        )
        year.grid(row=5, column=1, padx=30, pady=20, sticky="w")


        student_section_label = customtkinter.CTkLabel(self, text="Section:", font=label_font)
        student_section_label.grid(row=6, column=0, padx=30, pady=20, sticky="e")
        section = customtkinter.CTkEntry(self, width=60, justify="center")
        section.grid(row=6, column=1, padx=30, pady=20, sticky="w")

        register_button = customtkinter.CTkButton(self, text="Register", font=button_font)
        register_button.grid(row=7, column=0, columnspan=2, padx=30, pady=30, sticky="s")

