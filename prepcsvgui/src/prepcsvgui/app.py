"""
Script to automate the prepping of the CSV file for SF dataloader application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, CENTER, BOLD, NORMAL
from toga.colors import BLUE, RED
import datetime
import sys
import os
import openpyxl


class PrepCSVGUI(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        box2 = toga.Box()

        
        name_label = toga.Label(
            "Customer Name: ",
            style=Pack(font_weight=NORMAL)
        )
        self.name_input = toga.TextInput(style=Pack(flex=1, padding_left=69))

        account_label = toga.Label (
            "Account Id (SF format):",
            style=Pack(font_weight=NORMAL)
        )
        self.account_input = toga.TextInput(style=Pack(flex=1, padding_left=41))

        contactid_label = toga.Label (
            "Contact Id (SF format):",
            style=Pack(font_weight=NORMAL, padding_left=3)
         )
        self.contactid_input = toga.TextInput(style=Pack(flex=1, padding_left=41))

        description_label = toga.Label (
            "Description:",
            style=Pack(font_weight=NORMAL)
         )
        self.description_input = toga.TextInput(style=Pack(flex=1, padding_left=93))

        opportunity_label = toga.Label (
            "Opportunity (SF format):",
            style=Pack(font_weight=NORMAL)
         )
        self.opportunity_input = toga.TextInput(style=Pack(flex=1, padding_left=38))

        productid_label = toga.Label (
            "Product Id (SF format):",
            style=Pack(font_weight=NORMAL, padding_left=5)
         )
        self.productid_input = toga.TextInput(style=Pack(flex=1, padding_left=38))

        purchasedate_label = toga.Label (
            "Purchase Date (YYYY-MM-DD):",
            style=Pack(font_weight=NORMAL)
         )
        self.purchasedate_input = toga.TextInput(style=Pack(flex=1))

        quantity_label = toga.Label (
            "Quantity:",
            style=Pack(font_weight=NORMAL, padding_right=109)
         )
        self.quantity_input = toga.TextInput(style=Pack(flex=1))

        status_label = toga.Label (
            "Status:",
            style=Pack(font_weight=NORMAL, padding_right=118)
         )
        self.status_input = toga.TextInput(style=Pack(flex=1))

        initials_label = toga.Label (
            "Your Initials:",
            style=Pack(font_weight=NORMAL, padding_right=95)
         )
        self.initials_input = toga.TextInput(style=Pack(flex=1))

        filename_label = toga.Label (
            "File Name with S/N's (xlsx):",
            style=Pack(font_weight=NORMAL)
         )
        self.filename_input = toga.TextInput(style=Pack(flex=1, padding_left=24))


        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        account_box = toga.Box(style=Pack(direction=ROW, padding=5))
        account_box.add(account_label)
        account_box.add(self.account_input)
        contactid_box = toga.Box(style=Pack(direction=ROW, padding=5))
        contactid_box.add(contactid_label)
        contactid_box.add(self.contactid_input)
        description_box = toga.Box(style=Pack(direction=ROW, padding=5))
        description_box.add(description_label)
        description_box.add(self.description_input)
        opportunity_box = toga.Box(style=Pack(direction=ROW, padding=5))
        opportunity_box.add(opportunity_label)
        opportunity_box.add(self.opportunity_input)
        productid_box = toga.Box(style=Pack(direction=ROW, padding=5))
        productid_box.add(productid_label)
        productid_box.add(self.productid_input)
        purchasedate_box = toga.Box(style=Pack(direction=ROW, padding=5))
        purchasedate_box.add(purchasedate_label)
        purchasedate_box.add(self.purchasedate_input)
        quantity_box = toga.Box(style=Pack(direction=ROW, padding=5))
        quantity_box.add(quantity_label)
        quantity_box.add(self.quantity_input)
        status_box = toga.Box(style=Pack(direction=ROW, padding=5))
        status_box.add(status_label)
        status_box.add(self.status_input)
        initials_box = toga.Box(style=Pack(direction=ROW, padding=5))
        initials_box.add(initials_label)
        initials_box.add(self.initials_input)
        filename_box = toga.Box(style=Pack(direction=ROW, padding=5))
        filename_box.add(filename_label)
        filename_box.add(self.filename_input)

        button = toga.Button(
            "Close",
            on_press=self.exit_app,
            style=Pack(padding=20,width=90,padding_left=165,color=BLUE, font_weight="bold")
        )

        cf_button = toga.Button(
            "Create File",
            on_press=self.get_input_process,
            style=Pack(padding=20,width=90,padding_left=165,color=BLUE, font_weight="bold")
        )

        main_box.add(name_box)
        main_box.add(account_box)
        main_box.add(contactid_box)
        main_box.add(description_box)
        main_box.add(opportunity_box)
        main_box.add(productid_box)
        main_box.add(purchasedate_box)
        main_box.add(quantity_box)
        main_box.add(status_box)
        main_box.add(initials_box)
        main_box.add(filename_box)
        
        # Setting the Close and Create File button to Box2 at bottom of screen.
        box2.add(button)
        box2.add(cf_button)

        main_box.add(box2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_input_process(self,widget):

        count = 0
        no_values_input = list()
        for field in [self.name_input,\
                        self.account_input,\
                        self.contactid_input,\
                        self.description_input,\
                        self.opportunity_input,\
                        self.productid_input,\
                        self.purchasedate_input,\
                        self.quantity_input,\
                        self.status_input,\
                        self.initials_input,\
                        self.filename_input]:            
            if field.value == '':
                count = count + 1
        if count > 0:
            self.main_window.info_dialog("Prep CSV GUI Info", \
                                             f"Ensure all fields are completed.\n\n"
                                             f"Currently {count} fields are missing values.\n\n"                                             
                )
            return
        
        if 'xlsx' not in self.filename_input.value:
            self.main_window.info_dialog("Prep CSV GUI Info", \
                                         f"Please ensure an Excel file (xlsx) is used for the serial numbers."
                )
            return
        
        ##csv_column_headers = get_column_headers()
        # The Column name needed for the ingesting of data by dataloader.
        col_names = ('ACCOUNTID','CONTACTID','DESCRIPTION','NAME','OPPORTUNITY__C','PRODUCT2ID','PURCHASEDATE','QUANTITY','SERIALNUMBER','STATUS')

        column_headers = col_names[0] + "," + col_names[1] + "," + col_names[2] + "," + \
            col_names[3] + "," + col_names[4] + "," + col_names[5] + "," + col_names[6] +\
                  "," + col_names[7] + "," + col_names[8] + "," + col_names[9]
        
        csv_column_headers = str(column_headers)

        # The base file name will be taken and changed to reflect the customer,date and initials.
        # See example below.
        # Example might be "TAB_15052023_SN-AOPEN-ANZ-Salesforce-Assets-PRODUCTION-Insert.csv" 
        b_file_name = 'AOPEN-ANZ-Salesforce-Assets-PRODUCTION-Insert.csv'
        
        try:
            wb = openpyxl.load_workbook(self.filename_input.value)
            sheet = wb.active
            data = []
            for row in sheet.rows:
                data_row = []
                for cell in row:
                    if cell.value:
                        data_row.append(cell.value)
                        data.append(data_row)
        except FileNotFoundError:
            #print(f"{os.listdir()}")
            self.main_window.info_dialog("Error", "Excel file does not exist in the directory of the program.  Please check and try again.")
            return
        
        #print(f"csv file contents: {data}")
        serial_numbers = data
        serial_count = len(serial_numbers)
        #print(serial_count)

        mydate = datetime.date.today().strftime('%d%m%Y')
        final_file_name = str(self.name_input.value) + '_' + mydate + "_" + str(self.initials_input.value) + \
            "-" + b_file_name
        
        if os.path.exists(final_file_name):
            os.rename(final_file_name, str(datetime.datetime.now().strftime("[%H%M%S]-") + final_file_name))
        try:
            with open(final_file_name, 'w') as file:
                file.write("{}\n".format(csv_column_headers))
                for serialnumber in serial_numbers:
                    file.write("{},{},{},{},{},{},{},{},{},{}\n".format(self.account_input.value,self.contactid_input.value,\
                                                                        self.description_input.value,serialnumber[0],\
                                                                            self.opportunity_input.value,self.productid_input.value,\
                                                                                self.purchasedate_input.value,\
                                                                                    self.quantity_input.value,\
                                                                                        serialnumber[0],\
                                                                                            self.status_input.value))
            file.close()
            self.main_window.info_dialog("Info", f"CSV file created.\n{serial_count} S/N processed.\nFile Name: {final_file_name}")
        except FileNotFoundError:
            self.main_window.info_dialog("Error", "CSV file is not accessible.  Please try again.")
            return

    def exit_app(self, widget): 
        self.main_window.close()   
        


def main():
    return PrepCSVGUI()
