import tkinter
from tkinter import filedialog
import customtkinter as ctk
from CTkMenuBar import *
from customtkinter import CTkInputDialog
from CTkMessagebox import CTkMessagebox
from Generate_Cards import generate_card_number
from MC_Scheme import copyipmfile,copytolocal,uat_filesend,local_decrypt,uat_copy
import webbrowser
import cx_Oracle
import time
#from Generate_Cards import generate_card_number
import tkinter as tk
import ctypes

from PIL import ImageTk,Image

#Modes:system(default),light,dark

ctk.set_appearance_mode("dark")
#Themes:blue(default),dark-blue,green
ctk.set_default_color_theme("green")

class App(ctk.CTk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("QA Utility")
        # App.iconphoto(True, tk.PhotoImage(
        #      file=r"C:\Users\F2CSJHQ\Desktop\OneDrive - Fiserv Corp\Maniraj\Automation\QA_Utilities_Rewrite\CustomTkinter\fiserv_logo2.png"))
        # ctypes.windll.user32.SetClassLongA(App.winfo_id(self),-20,0x0000A8FF)
        self.geometry("500x440")
        self.env=["EMEA","APAC"]
        self.APACInst=["00000021","00000029","00000047","00000062","00000066","00000078","00000081","00000093"]
        self.EMEAInst=["00000002","00000003","00000004","00000008","00000009","00000011","00000012","00000013","00000014","00000016","00000017","00000018","00000019","00000020","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000030","00000031","00000033","00000034","00000035","00000039","00000040","00000041","00000043","00000044","00000045","00000046","00000048","00000049","00000050","00000051","00000052","00000053","00000054","00000055","00000057","00000058","00000063","00000064","00000065","00000068","00000069","00000070","00000071","00000073","00000074","00000076","00000077","00000079","00000080","00000082","00000083","00000087","00000088","00000089","00000090","00000091","00000092","00000094","00000099"]

        self.Inst = {"EMEA" : ["00000002","00000003","00000004","00000008","00000009","00000011","00000012","00000013","00000014","00000016","00000017","00000018","00000019","00000020","00000022","00000023","00000024","00000025","00000026","00000027","00000028","00000030","00000031","00000033","00000034","00000035","00000039","00000040","00000041","00000043","00000044","00000045","00000046","00000048","00000049","00000050","00000051","00000052","00000053","00000054","00000055","00000057","00000058","00000063","00000064","00000065","00000068","00000069","00000070","00000071","00000073","00000074","00000076","00000077","00000079","00000080","00000082","00000083","00000087","00000088","00000089","00000090","00000091","00000092","00000094","00000099"],
        "APAC" : ["00000021","00000029","00000047","00000062","00000066","00000078","00000081","00000093"]
                     }

        #self.iconify()
        #icon = s(file="fiserv_logo.png")


        # self.minsize(500,300)
        # self.grid_rowconfigure(0, weight=1)
        # self.textbox = ctk.CTkTextbox(master=self)
        # self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")


        #self.grid_columnconfigure((0, 1), weight=1)

        self.menu=CTkMenuBar(self)

        button1=self.menu.add_cascade("RAM")
        button2 = self.menu.add_cascade("Batch")
        button3 = self.menu.add_cascade("Scheme")
        button4 = self.menu.add_cascade("JIRA")


        dropdown1 = CustomDropdownMenu(widget=button1)
        dropdown1.add_option(option="Reset RAM Password ", command=self.reset_ram_pwd)

        dropdown1.add_separator()

        dropdown2 = CustomDropdownMenu(widget=button2)
        dropdown2.add_option(option="Generate Cards",command=self.generatecard)
        dropdown2.add_option(option="Update 80Byte Batch", command=lambda: print("InProgress"))
        #dropdown2.add_option(option="MC Scheme Test", command=lambda: print("InProgress"))
        dropdown2.add_separator()

        dropdown3 = CustomDropdownMenu(widget=button3)
        dropdown3.add_option(option="MC Scheme Test", command=self.mc_schemetest)
        dropdown3.add_separator()

        # dropdown4 = CustomDropdownMenu(widget=button4)
        # dropdown4.add_option(option="TestCase Upload", command=lambda: print("InProgress"))
        # dropdown4.add_separator()

        self.nameLabel = ctk.CTkLabel(self,text="Batch -> Generate Cards",font=("Arial",25))
        self.nameLabel.place(relx=0.5,rely=0.12,anchor='center')

        self.nameLabel2 = ctk.CTkLabel(self,text="Card BIN   ",font=("Arial",20))
        self.nameLabel2.place(relx=0.2,rely=0.2)#,anchor='w'


        # customization=dict(relx=0.5,rely=0.5,anchor='center')
        # self.error_label = ctk.CTkLabel(self, text="Enter the CardBin", font=("Arial", 10),text_color="red")
        #   # ,anchor='w'
        # self.error_label.place(**customization)
        # self.error_label.pack_forget()

        #
        self.nameEntry1 = ctk.CTkEntry(self,
                                      placeholder_text="Enter Bin Value")
        self.nameEntry1.place(relx=0.5,rely=0.2)

        self.nameLabel3 = ctk.CTkLabel(self, text="Card Length",font=("Arial",20))
        self.nameLabel3.place(relx=0.2,rely=0.3)
        #
        self.CardLengthOptionMenu = ctk.CTkOptionMenu(self,
                                                      values=["16",
                                                              "19"])
        self.CardLengthOptionMenu.place(relx=0.5,rely=0.3)
        #
        self.nameLabel4 = ctk.CTkLabel(self, text="No of Cards",font=("Arial",20))
        self.nameLabel4.place(relx=0.2,rely=0.4)
        #
        self.nameEntry2 = ctk.CTkEntry(self,
                                      placeholder_text="No of Card Required")
        self.nameEntry2.place(relx=0.5,rely=0.4)

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
                                       placeholder_text="Enter DB Password",show="*")
        self.nameEntry4.place(relx=0.5, rely=0.7)

        self.nameLabel8 = ctk.CTkLabel(self, text="DB Name", font=("Arial", 20))
        self.nameLabel8.place(relx=0.2, rely=0.8)
        self.nameEntry5 = ctk.CTkEntry(self,
                                       placeholder_text="Example: BWQ9")
        self.nameEntry5.place(relx=0.5, rely=0.8)

        self.button1=ctk.CTkButton(self,text="Help",command=self.help_generatecard)
        self.button1.place(relx=0.2,rely=0.9)
        self.button2 = ctk.CTkButton(self, text="Generate Cards",bg_color="Red",fg_color="Red",hover_color="Red",command=self.button_Generate_Cards)
        self.button2.place(relx=0.5, rely=0.9)
        self.default_values()

    def default_values(self):
        print("Default values called")
        self.nameEntry1.insert(0,"62945152940")
        self.nameEntry2.insert(0,"5")
        self.nameEntry3.insert(0,"bw3")
        self.nameEntry4.insert(0,"carlow")
        self.nameEntry5.insert(0,"BWQ9")

    def generate_card_output(self,clearcard,encryptedcard):
        self.geometry("500x440")
        #import cutom_tkinter
        print(len(clearcard))
        # clearcard.sort()
        # encryptedcard.sort()
        # print("j value is :",j)
        # if j == 0:
        textbox_window = ctk.CTkToplevel(app)
        textbox_window.title("Output")
        textbox_window.geometry("500x250")
        textbox = ctk.CTkTextbox(textbox_window,height=500,width=500)
        #carddetails = clearcard+"\t\t\t"+encryptedcard
        i="1.0"
        textbox.insert(i, "ClearCard\t\t\tEncryptedCard\n")
        for k in range(len(clearcard)):
            print("k value is :",k)
            l=k+2
            l=int(l)
            l=float(l)
            print("k value is:",l)
            ClearCard=clearcard[k]
            EncryptedCard=encryptedcard[k]
            print(ClearCard)
            print(EncryptedCard)
            carddetails = ClearCard + "\t\t\t" + EncryptedCard+"\n"
            textbox.insert(l, carddetails)



        #textbox.insert("2",carddetails)
        textbox.pack()
        # else:
        #     carddetails = cardnumber_generated + "\t\t\t" + encrypted
        #     textbox.insert(j+2, carddetails)
        app.mainloop()

    def db_connection(self):
        username = "bw3"
        pwd = "carlow"
        env = "BWQ91"
        try:
            con = cx_Oracle.connect(user=username, password=pwd, dsn=env)
        except Exception as e:
            print("Oracle Connection Failed, please try connecting the DB Manually & then try again:", e)
            exit()
        cursor = con.cursor()
        return cursor

    def button_Generate_Cards(self):
        binvalue=self.nameEntry1.get()

        NoOfCards=self.nameEntry2.get()
        DBUserName=self.nameEntry3.get()
        DBPassword=self.nameEntry4.get()
        DBEnv = self.nameEntry5.get()
        CardLen =  self.CardLengthOptionMenu.get()
        if binvalue == "":
            CTkMessagebox(title="Error", message="Card Bin Should be Valid!", icon="cancel",width=150,height=50,justify='center',sound='true')
        elif NoOfCards == "":
            CTkMessagebox(title="Error", message="No Of Cards Should be Valid!", icon="cancel",width=150,height=50,justify='center',sound='true')
        elif DBUserName == "":
            CTkMessagebox(title="Error", message="DB UserName Should be Present", icon="cancel", width=150, height=50,
                          justify='center', sound='true')
        elif DBPassword == "":
            CTkMessagebox(title="Error", message="DB Password Should be Present", icon="cancel", width=150, height=50,
                          justify='center', sound='true')
        elif DBEnv == "":
            CTkMessagebox(title="Error", message="DB Name Should be Present", icon="cancel", width=150, height=50,
                          justify='center', sound='true')
        # print("Function Called inside:",binvalue)
        # print("CardLength:",CardLen)
        clearcard=[]
        encryptedcard=[]
        encrypted_card = []
        try:
            cursor = self.db_connection()
            #print(type(NoOfCards))
            #print("NoOfCards is:",NoOfCards)
            NoOfCards = int(NoOfCards)
            print(type(NoOfCards))
            print("NoOfCards is:", NoOfCards)
            for j in range(0,NoOfCards):
                print("j value in for loop:",j)
                #cardnumber_generated, encrypted = generate_card_number(binvalue, int(CardLen))

                cardnumber_generated = generate_card_number(binvalue, int(CardLen))
                if cardnumber_generated in clearcard:
                    print("Duplicate card:",cardnumber_generated)
                    while cardnumber_generated in clearcard:#loop if duplicate card is present
                        cardnumber_generated = generate_card_number(binvalue, int(CardLen))
                        print("Alternatecard:",cardnumber_generated)
                clearcard.append(cardnumber_generated)
                encrypted_query = "SELECT vlt_api.vlt_api_wrapper.encrypt(" + cardnumber_generated + ", 'CARD-eFPE') from dual"
                # print(encrypted_query)
                cursor.execute(encrypted_query)
                rows_encrypt = cursor.fetchmany(1)
                if len(rows_encrypt) == 0:
                    print("Issue in Encryption")
                    print(encrypted_query)
                    encrypted_card.append("InvalidData")
                    # TestData_Updated.at[i, 'clearcard'] = 'No Data Available'
                    # df_db.at[k, 'Card Number'] = 'InvalidData'
                else:
                    encrypted = rows_encrypt[0]
                    print(encrypted)
                    print(type(encrypted))
                    encrypted = ','.join(encrypted)
                    print(encrypted)
                    print(type(encrypted))
                    encrypted_card.append(encrypted)
                    # df_db.at[k, 'clearcard'] = card_number
                    # df_db.at[k, 'Card Number'] = encrypted_bin
                    print("Encrypted card is :", encrypted)
                    #return encrypted
                #clearcard.append(cardnumber_generated)
                # if cardnumber_generated in clearcard:

                encryptedcard.append(encrypted)
                print("card number inside main:", cardnumber_generated)
                print("encrypted card number inside main:", encrypted)
                #self.generate_card_output(encrypted, cardnumber_generated,j)
                # if j == 0:
                #     self.generate_card_output(encrypted, cardnumber_generated)
                # else:
                #     self.generate_insert_output(encrypted, cardnumber_generated)



        except Exception as e:
            print(e)
            print("Inside Exception")
            CTkMessagebox(title="Error", message="No Of Cards Should be Numeric", icon="cancel", width=150, height=50,
                          justify='center', sound='true')
            for i in range(2):
                if i == 1:
                 break
        #cardnumber_generated,encrypted = generate_card_number(binvalue, int(CardLen))
        #cardnumber_generated=generate_card_number()
        print(clearcard)
        print(encryptedcard)
        print("card number inside main:",cardnumber_generated)
        print("encrypted card number inside main:", encrypted)
        self.generate_card_output(clearcard,encryptedcard)


    def help_generatecard(self):
        Help_CardNumber = 'https://enterprise-confluence.onefiserv.net/display/OQ/Generate+Card+-+Macro'
        webbrowser.open(Help_CardNumber)
    def mcscheme(self):

        inst_no = self.nameEntry1Scheme.get()
        if len(inst_no) < 8:
            inst_no = inst_no.zfill(8)
        local_file = self.nameEntry2Scheme.get()
        print("local file is :",local_file)
        UATServer=self.UATOptionMenu.get()
        print("UAT Server:",UATServer)
        uat_host=UATServer+".1dc.com"
        print("host is:",uat_host)
        username = self.nameEntry3Scheme.get()
        #print("UATUserName:", UATUserName)
        password=self.nameEntry4Scheme.get()
        #print("UATPwd:", UATPwd)
        EnvTested = self.nameEntry5Scheme.get()
        print("EnvTested:", EnvTested)
        host = 'a5dvap1017.1dc.com'  # BWQ84 hardcoded as default QA Server for decryption
        copyipm = copyipmfile(host, username, password, local_file)





























        # host = 'A5CCVA8000.1dc.com'
        # username = 'f2csjhq'
        # password = 'Mobile@2026'
        # #inst_no = '00000019'





















        remote_file_name = inst_no + 'gcms_r111_outgoing.out'
        print(remote_file_name)
        copyipm = copyipmfile(host, username, password,local_file)
        time.sleep(10)
        print("waiting for 10 seconds")
        ldecrypt = local_decrypt()
        copyipmtolocal = copytolocal(host, username, password)
        ucopy=uat_copy()
        #copyipm = copyipmfile()

    def selectipm(self):
        ipmpath = filedialog.askopenfilename(filetypes=[("IPM File","*.out")])
        if ipmpath:
            self.nameEntry2Scheme.delete(0,ctk.END)
            self.nameEntry2Scheme.insert(ctk.END,ipmpath)
        else:
            self.nameEntry2Scheme.delete(0, ctk.END)
            self.nameEntry2Scheme.insert(ctk.END, "Please Select IPM File")

    def mc_schemetest(self):
        try:
            for widget in App.winfo_children(self):
                if isinstance(widget,ctk.CTkLabel):
                    widget.destroy()
                elif isinstance(widget,ctk.CTkEntry):
                    widget.destroy()
                elif isinstance(widget, ctk.CTkOptionMenu):
                    widget.destroy()
                elif isinstance(widget,ctk.CTkButton):
                    widget.destroy()
        except Exception as e:
            print("Error Message:",e)
            pass
        self.geometry("500x440")
        self.nameLabelScheme = ctk.CTkLabel(self, text="Scheme -> MC Scheme Test", font=("Arial", 25))
        self.nameLabelScheme.place(relx=0.5, rely=0.12, anchor='center')

        self.nameLabel2Scheme = ctk.CTkLabel(self, text="Institution", font=("Arial", 20))
        self.nameLabel2Scheme.place(relx=0.2, rely=0.2)  # ,anchor='w'

        # customization=dict(relx=0.5,rely=0.5,anchor='center')
        # self.error_label = ctk.CTkLabel(self, text="Enter the CardBin", font=("Arial", 10),text_color="red")
        #   # ,anchor='w'
        # self.error_label.place(**customization)
        # self.error_label.pack_forget()

        #
        self.nameEntry1Scheme = ctk.CTkEntry(self,
                                       placeholder_text="Enter the Inst")
        self.nameEntry1Scheme.place(relx=0.5, rely=0.2)

        self.nameLabel3Scheme = ctk.CTkLabel(self, text="Environment", font=("Arial", 20))
        self.nameLabel3Scheme.place(relx=0.2, rely=0.3)
        #
        self.SchemeEnvOptionMenu = ctk.CTkOptionMenu(self,
                                                      values=["EMEA",
                                                              "APAC"])
        self.SchemeEnvOptionMenu.place(relx=0.5, rely=0.3)
        #
        self.nameLabel4Scheme = ctk.CTkLabel(self, text="IPM Path     ", font=("Arial", 20))
        self.nameLabel4Scheme.place(relx=0.2, rely=0.4)
        #
        self.nameEntry2Scheme = ctk.CTkEntry(self,
                                       placeholder_text="IPM Path  ")

        self.nameEntry2Scheme.place(relx=0.5, rely=0.4)

        self.browse_button = ctk.CTkButton(self,text="Browse",command=self.selectipm,width=15)#,width=13,height=7)
        self.browse_button.place(relx=0.8,rely=0.4)
        # Need to start here
        # self.nameEntry2Scheme = filedialog.askopenfilename(App,title="Select a IPM.OUT FILE",filetypes=[("All Files","*.*")]).rstrip()
        # self.nameEntry2Scheme.place(relx=0.5, rely=0.4)



        self.nameLabel5Scheme = ctk.CTkLabel(self, text="UAT Server", font=("Arial", 20))
        self.nameLabel5Scheme.place(relx=0.2, rely=0.5)
        self.UATOptionMenu = ctk.CTkOptionMenu(self,
                                                   values=["A5CCVA8000",
                                                           "A5CVAP1015"])
        self.UATOptionMenu.place(relx=0.5, rely=0.5)

        self.nameLabel6Scheme = ctk.CTkLabel(self, text="UAT UserName", font=("Arial", 20))
        self.nameLabel6Scheme.place(relx=0.2, rely=0.6)
        self.nameEntry3Scheme = ctk.CTkEntry(self,
                                       placeholder_text="UAT UserName")
        self.nameEntry3Scheme.place(relx=0.5, rely=0.6)

        self.nameLabel7Scheme = ctk.CTkLabel(self, text="UAT Password", font=("Arial", 20))
        self.nameLabel7Scheme.place(relx=0.2, rely=0.7)
        self.nameEntry4Scheme = ctk.CTkEntry(self,
                                       placeholder_text="UAT Password", show="*")
        self.nameEntry4Scheme.place(relx=0.5, rely=0.7)

        self.nameLabel8Scheme = ctk.CTkLabel(self, text="Testing Env", font=("Arial", 20))
        self.nameLabel8Scheme.place(relx=0.2, rely=0.8)
        self.nameEntry5Scheme = ctk.CTkEntry(self,
                                       placeholder_text="Example: BWQ9")
        self.nameEntry5Scheme.place(relx=0.5, rely=0.8)

        self.button1Scheme = ctk.CTkButton(self, text="Help", command=self.help_generatecard)
        self.button1Scheme.place(relx=0.2, rely=0.9)
        self.button2Scheme = ctk.CTkButton(self, text="StageToMasterCard", bg_color="Red", fg_color="Red", hover_color="Red",
                                     command=self.mcscheme)
        self.button2Scheme.place(relx=0.5, rely=0.9)

    def generatecard(self):

        #To remove the ealier loaded frame
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
        self.geometry("500x440")
            # if self.nameLabelScheme.destroy:
            #     self.nameLabelScheme.destroy()
            # self.nameLabel2Scheme.destroy()
            # self.nameEntry1Scheme.destroy()
            # self.nameLabel3Scheme.destroy()
            # self.nameLabel4Scheme.destroy()
            # self.nameEntry2Scheme.destroy()
            # self.nameLabel5Scheme.destroy()
            # self.UATOptionMenu.destroy()
            # self.nameLabel6Scheme.destroy()
            # self.nameEntry3Scheme.destroy()
            # self.nameLabel7Scheme.destroy()
            # self.nameEntry4Scheme.destroy()
            # self.nameLabel8Scheme.destroy()
            # self.nameEntry5Scheme.destroy()
            # self.button1Scheme.destroy()
            # self.button2Scheme.destroy()
        # except Exception as e:
        #     print("Error Message:",e)
        #     pass


        self.nameLabel = ctk.CTkLabel(self, text="Batch -> Generate Cards", font=("Arial", 25))
        self.nameLabel.place(relx=0.5, rely=0.12, anchor='center')

        self.nameLabel2 = ctk.CTkLabel(self, text="Card BIN   ", font=("Arial", 20))
        self.nameLabel2.place(relx=0.2, rely=0.2)  # ,anchor='w'

        # customization=dict(relx=0.5,rely=0.5,anchor='center')
        # self.error_label = ctk.CTkLabel(self, text="Enter the CardBin", font=("Arial", 10),text_color="red")
        #   # ,anchor='w'
        # self.error_label.place(**customization)
        # self.error_label.pack_forget()

        #
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

        self.button1 = ctk.CTkButton(self, text="Help", command=self.help_generatecard)
        self.button1.place(relx=0.2, rely=0.9)
        self.button2 = ctk.CTkButton(self, text="Generate Cards", bg_color="Red", fg_color="Red", hover_color="Red",
                                     command=self.button_Generate_Cards)
        self.button2.place(relx=0.5, rely=0.9)

    def reset_dropdown(self,*args):
        self.InstOptionMenu.deletecommand()

    def reset_ram_pwd(self):
        try:
            for widget in App.winfo_children(self):
                if isinstance(widget,ctk.CTkLabel):
                    widget.destroy()
                elif isinstance(widget,ctk.CTkEntry):
                    widget.destroy()
                elif isinstance(widget, ctk.CTkOptionMenu):
                    widget.destroy()
                elif isinstance(widget,ctk.CTkButton):
                    widget.destroy()
        except Exception as e:
            print("Error Message:",e)
            pass
        self.geometry("300x300")
        self.nameLabelScheme = ctk.CTkLabel(self, text="RAM -> Reset RAM Password", font=("Arial", 16))
        self.nameLabelScheme.place(relx=0.5, rely=0.15, anchor='center')

        self.nameLabel3Scheme = ctk.CTkLabel(self, text="Environment", font=("Arial", 14))
        self.nameLabel3Scheme.place(relx=0.2, rely=0.25)

        self.SchemeEnvOptionMenu = ctk.CTkOptionMenu(self,values=self.env,width=100,height=7,font=("Arial", 11))
        self.SchemeEnvOptionMenu.place(relx=0.5, rely=0.25)

        self.nameLabel2Scheme = ctk.CTkLabel(self, text="Institution", font=("Arial", 14))
        self.nameLabel2Scheme.place(relx=0.2, rely=0.35)  # ,anchor='w'

        # customization=dict(relx=0.5,rely=0.5,anchor='center')
        # self.error_label = ctk.CTkLabel(self, text="Enter the CardBin", font=("Arial", 10),text_color="red")
        #   # ,anchor='w'
        # self.error_label.place(**customization)
        # self.error_label.pack_forget()

        #
        # self.nameEntry1Scheme = ctk.CTkEntry(self,
        #                                placeholder_text="Enter the Inst",width=100,height=7,font=("Arial", 11))
        # self.nameEntry1Scheme.place(relx=0.5, rely=0.35)
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



        # self.nameLabel3Scheme = ctk.CTkLabel(self, text="Environment", font=("Arial", 20))
        # self.nameLabel3Scheme.place(relx=0.2, rely=0.3)
        # #
        # self.SchemeEnvOptionMenu = ctk.CTkOptionMenu(self,
        #                                               values=["EMEA",
        #                                                       "APAC"])
        # self.SchemeEnvOptionMenu.place(relx=0.5, rely=0.3)
        #
        self.nameLabel4Scheme = ctk.CTkLabel(self, text="Database     ", font=("Arial", 14))
        self.nameLabel4Scheme.place(relx=0.2, rely=0.45)
        #
        self.nameEntry2Scheme = ctk.CTkEntry(self,
                                       placeholder_text="Enter the Database ",width=100,height=7,font=("Arial", 11))
        self.nameEntry2Scheme.place(relx=0.5, rely=0.45)

        # self.nameLabel5Scheme = ctk.CTkLabel(self, text="UAT Server", font=("Arial", 20))
        # self.nameLabel5Scheme.place(relx=0.2, rely=0.5)
        # self.UATOptionMenu = ctk.CTkOptionMenu(self,
        #                                            values=["A5CCVA8000",
        #                                                    "A5CVAP1015"])
        # self.UATOptionMenu.place(relx=0.5, rely=0.5)

        self.nameLabel6Scheme = ctk.CTkLabel(self, text="UserName", font=("Arial", 14))
        self.nameLabel6Scheme.place(relx=0.2, rely=0.55)
        self.nameEntry3Scheme = ctk.CTkEntry(self,
                                       placeholder_text="Enter the UserName",width=100,height=7,font=("Arial", 11))
        self.nameEntry3Scheme.place(relx=0.5, rely=0.55)

        self.nameLabel7Scheme = ctk.CTkLabel(self, text="Password", font=("Arial", 14))
        self.nameLabel7Scheme.place(relx=0.2, rely=0.65)
        self.nameEntry4Scheme = ctk.CTkEntry(self,
                                       placeholder_text="Password To Reset", show="*",width=100,height=7,font=("Arial", 11))
        self.nameEntry4Scheme.place(relx=0.5, rely=0.65)

        # self.nameLabel8Scheme = ctk.CTkLabel(self, text="Testing Env", font=("Arial", 20))
        # self.nameLabel8Scheme.place(relx=0.2, rely=0.8)
        # self.nameEntry5Scheme = ctk.CTkEntry(self,
        #                                placeholder_text="Example: BWQ9")
        # self.nameEntry5Scheme.place(relx=0.5, rely=0.8)

        self.button1Scheme = ctk.CTkButton(self, text="Help", command=self.help_generatecard,width=100,height=7,font=("Arial", 14))
        self.button1Scheme.place(relx=0.1, rely=0.85)
        self.button2Scheme = ctk.CTkButton(self, text="Reset Password", bg_color="Red", fg_color="Red", hover_color="Red",
                                     command=self.button_Generate_Cards,width=100,height=7,font=("Arial", 14))
        self.button2Scheme.place(relx=0.5, rely=0.85)






if __name__=="__main__":
    app = App()
    app.mainloop()