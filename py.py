import customtkinter as ctk
from CTkMenuBar import *
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("QA Utility")
        self.geometry("500x440")
        self.env = ["EMEA", "APAC"]
        self.APACInst = ["00000021", "00000029", "00000047", "00000062", "00000066", "00000078", "00000081", "00000093"]
        self.EMEAInst = ["00000002", "00000003", "00000004", "00000008", "00000009", "00000011", "00000012", "00000013",
                         "00000014", "00000016", "00000017", "00000018", "00000019", "00000020", "00000022", "00000023",
                         "00000024", "00000025", "00000026", "00000027", "00000028", "00000030", "00000031", "00000033",
                         "00000034", "00000035", "00000039", "00000040", "00000041", "00000043", "00000044", "00000045",
                         "00000046", "00000048", "00000049", "00000050", "00000051", "00000052", "00000053", "00000054",
                         "00000055", "00000057", "00000058", "00000063", "00000064", "00000065", "00000068", "00000069",
                         "00000070", "00000071", "00000073", "00000074", "00000076", "00000077", "00000079", "00000080",
                         "00000082", "00000083", "00000087", "00000088", "00000089", "00000090", "00000091", "00000092",
                         "00000094", "00000099"]

        self.Inst = {
            "EMEA": ["00000002", "00000003", "00000004", "00000008", "00000009", "00000011", "00000012", "00000013",
                     "00000014", "00000016", "00000017", "00000018", "00000019", "00000020", "00000022", "00000023",
                     "00000024", "00000025", "00000026", "00000027", "00000028", "00000030", "00000031", "00000033",
                     "00000034", "00000035", "00000039", "00000040", "00000041", "00000043", "00000044", "00000045",
                     "00000046", "00000048", "00000049", "00000050", "00000051", "00000052", "00000053", "00000054",
                     "00000055", "00000057", "00000058", "00000063", "00000064", "00000065", "00000068", "00000069",
                     "00000070", "00000071", "00000073", "00000074", "00000076", "00000077", "00000079", "00000080",
                     "00000082", "00000083", "00000087", "00000088", "00000089", "00000090", "00000091", "00000092",
                     "00000094", "00000099"],
            "APAC": ["00000021", "00000029", "00000047", "00000062", "00000066", "00000078", "00000081", "00000093"]
            }
        self.menu = CTkMenuBar(self)

        button1 = self.menu.add_cascade("RAM")
        button2 = self.menu.add_cascade("Batch")
        button3 = self.menu.add_cascade("Scheme")
        button4 = self.menu.add_cascade("JIRA")

        dropdown1 = CustomDropdownMenu(widget=button1)
        dropdown1.add_option(option="Reset RAM Password ", command=self.reset_ram_pwd)


        self.nameLabel = ctk.CTkLabel(self, text="Batch -> Generate Cards", font=("Arial", 25))
        self.nameLabel.place(relx=0.5, rely=0.12, anchor='center')

        self.nameLabel2 = ctk.CTkLabel(self, text="Card BIN   ", font=("Arial", 20))
        self.nameLabel2.place(relx=0.2, rely=0.2)  # ,anchor='w'
        self.nameEntry1 = ctk.CTkEntry(self,
                                       placeholder_text="Enter Bin Value")
        self.nameEntry1.place(relx=0.5, rely=0.2)

        self.nameLabel3 = ctk.CTkLabel(self, text="Card Length", font=("Arial", 20))
        self.nameLabel3.place(relx=0.2, rely=0.3)
        #
        self.CardLengthOptionMenu = ctk.CTkOptionMenu(self,
                                                      values=["16",
                                                              "19"])
        self.CardLengthOptionMenu.place(relx=0.5, rely=0.3)
        #
        self.nameLabel4 = ctk.CTkLabel(self, text="No of Cards", font=("Arial", 20))
        self.nameLabel4.place(relx=0.2, rely=0.4)
        #
        self.nameEntry2 = ctk.CTkEntry(self,
                                       placeholder_text="No of Card Required")
        self.nameEntry2.place(relx=0.5, rely=0.4)

        self.nameLabel5 = ctk.CTkLabel(self, text="Voltage", font=("Arial", 20))
        self.nameLabel5.place(relx=0.2, rely=0.5)
        self.VoltageOptionMenu = ctk.CTkOptionMenu(self,
                                                   values=["Yes",
                                                           "No"])
        self.VoltageOptionMenu.place(relx=0.5, rely=0.5)

        self.nameLabel6 = ctk.CTkLabel(self, text="DB UserName", font=("Arial", 20))
        self.nameLabel6.place(relx=0.2, rely=0.6)
        self.nameEntry3 = ctk.CTkEntry(self,
                                       placeholder_text="Enter DB UserName")
        self.nameEntry3.place(relx=0.5, rely=0.6)

        self.nameLabel7 = ctk.CTkLabel(self, text="DB Password", font=("Arial", 20))
        self.nameLabel7.place(relx=0.2, rely=0.7)
        self.nameEntry4 = ctk.CTkEntry(self,
                                       placeholder_text="Enter DB Password", show="*")
        self.nameEntry4.place(relx=0.5, rely=0.7)

        self.nameLabel8 = ctk.CTkLabel(self, text="DB Name", font=("Arial", 20))
        self.nameLabel8.place(relx=0.2, rely=0.8)
        self.nameEntry5 = ctk.CTkEntry(self,
                                       placeholder_text="Example: BWQ9")
        self.nameEntry5.place(relx=0.5, rely=0.8)

        self.button1 = ctk.CTkButton(self, text="Help")
        self.button1.place(relx=0.2, rely=0.9)
        self.button2 = ctk.CTkButton(self, text="Generate Cards", bg_color="Red", fg_color="Red", hover_color="Red")
        self.button2.place(relx=0.5, rely=0.9)
        self.default_values()
    def default_values(self):
        print("Default values called")
        self.nameEntry1.insert(0, "62945152940")
        self.nameEntry2.insert(0, "5")
        self.nameEntry3.insert(0, "bw3")
        self.nameEntry4.insert(0, "carlow")
        self.nameEntry5.insert(0, "BWQ9")
    def reset_dropdown(self, *args):
        self.InstOptionMenu.deletecommand()
    def reset_ram_pwd(self):
        try:
            for widget in App.winfo_children(self):
                if isinstance(widget, ctk.CTkLabel):
                    widget.destroy()
                elif isinstance(widget, ctk.CTkEntry):
                    widget.destroy()
                elif isinstance(widget, ctk.CTkOptionMenu):
                    widget.destroy()
                elif isinstance(widget, ctk.CTkButton):
                    widget.destroy()
        except Exception as e:
            print("Error Message:", e)
            pass
        self.geometry("300x300")
        self.nameLabelScheme = ctk.CTkLabel(self, text="RAM -> Reset RAM Password", font=("Arial", 16))
        self.nameLabelScheme.place(relx=0.5, rely=0.15, anchor='center')

        self.nameLabel3Scheme = ctk.CTkLabel(self, text="Environment", font=("Arial", 14))
        self.nameLabel3Scheme.place(relx=0.2, rely=0.25)

        self.SchemeEnvOptionMenu = ctk.CTkOptionMenu(self, values=self.env, width=100, height=7, font=("Arial", 11))
        self.SchemeEnvOptionMenu.place(relx=0.5, rely=0.25)

        self.nameLabel2Scheme = ctk.CTkLabel(self, text="Institution", font=("Arial", 14))
        self.nameLabel2Scheme.place(relx=0.2, rely=0.35)  # ,anchor='w'
        self.InstOptionMenu = ctk.CTkOptionMenu(self, values=self.APACInst, width=100, height=7, font=("Arial", 11))
        self.InstOptionMenu.place(relx=0.5, rely=0.35)
        self.selected_Env = self.SchemeEnvOptionMenu.get()
        if self.selected_Env == "APAC":
            print("Inside APAC")
            self.InstOptionMenu = ctk.CTkOptionMenu(self, values=self.APACInst, width=100, height=7, font=("Arial", 11))
            self.InstOptionMenu.place(relx=0.5, rely=0.35)
        elif self.selected_Env == "EMEA":
            print("Inside EMEA")
            self.InstOptionMenu = ctk.CTkOptionMenu(self, values=self.EMEAInst, width=100, height=7, font=("Arial", 11))
            self.InstOptionMenu.place(relx=0.5, rely=0.35)
        self.nameLabel4Scheme = ctk.CTkLabel(self, text="Database     ", font=("Arial", 14))
        self.nameLabel4Scheme.place(relx=0.2, rely=0.45)
        #
        self.nameEntry2Scheme = ctk.CTkEntry(self,
                                             placeholder_text="Enter the Database ", width=100, height=7,
                                             font=("Arial", 11))
        self.nameEntry2Scheme.place(relx=0.5, rely=0.45)

        self.nameLabel6Scheme = ctk.CTkLabel(self, text="UserName", font=("Arial", 14))
        self.nameLabel6Scheme.place(relx=0.2, rely=0.55)
        self.nameEntry3Scheme = ctk.CTkEntry(self,
                                             placeholder_text="Enter the UserName", width=100, height=7,
                                             font=("Arial", 11))
        self.nameEntry3Scheme.place(relx=0.5, rely=0.55)

        self.nameLabel7Scheme = ctk.CTkLabel(self, text="Password", font=("Arial", 14))
        self.nameLabel7Scheme.place(relx=0.2, rely=0.65)
        self.nameEntry4Scheme = ctk.CTkEntry(self,
                                             placeholder_text="Password To Reset", show="*", width=100, height=7,
                                             font=("Arial", 11))
        self.nameEntry4Scheme.place(relx=0.5, rely=0.65)

        # self.nameLabel8Scheme = ctk.CTkLabel(self, text="Testing Env", font=("Arial", 20))
        # self.nameLabel8Scheme.place(relx=0.2, rely=0.8)
        # self.nameEntry5Scheme = ctk.CTkEntry(self,
        #                                placeholder_text="Example: BWQ9")
        # self.nameEntry5Scheme.place(relx=0.5, rely=0.8)

        self.button1Scheme = ctk.CTkButton(self, text="Help", width=100, height=7,
                                           font=("Arial", 14))
        self.button1Scheme.place(relx=0.1, rely=0.85)

        self.button2Scheme = ctk.CTkButton(self, text="Reset Password", bg_color="Red", fg_color="Red",
                                           hover_color="Red",command=self.print_ram_inputs,
                                         width=100, height=7, font=("Arial", 14))
        self.button2Scheme.place(relx=0.5, rely=0.85)

    def print_ram_inputs(self):
        # Get and print inputs from the reset RAM password section
        selected_env = self.SchemeEnvOptionMenu.get()
        selected_institution = self.InstOptionMenu.get()
        db_name = self.nameEntry2Scheme.get()
        username = self.nameEntry3Scheme.get()
        password = self.nameEntry4Scheme.get()

        print("Environment:", selected_env)
        print("Institution:", selected_institution)
        print("Database:", db_name)
        print("Username:", username)
        print("Password:", password)


if __name__ == "__main__":
    app = App()
    app.mainloop()
