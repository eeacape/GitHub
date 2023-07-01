#Name: prep-csv-for-dataloader-gui.py
#Ref: A way to automate the curating of the CSV file to be used by dataloader
#     was required.  This script enables this to be done.
#Copyright (c) July 2023. CPEREIRA. All Rights Reserved.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#this list of conditions and the following disclaimer in the documentation and/or
#other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its contributors
#may be used to endorse or promote products derived from this software without
#specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
####

import datetime
import sys
import os
import openpyxl
import tkinter as tk
import tkinter.messagebox as msgbox

# Create the main window
root = tk.Tk()
root.title("Prep CSV Dataloader File")

# Define the function to create the file
def get_input_process():
    # Check if the file name exists
    if not file_name.get():
        msgbox.showinfo("Info", "Please enter file name of spreadsheet")
        return

    # Check if all the other fields are not empty
    for field in [customer_name, account_id, contact_id, description, opportunity, product_id, purchase_date, quantity, status, your_initials]:
        if not field.get():
            msgbox.showinfo("Info", "Ensure all fields are completed.")
            return
    if 'xlsx' not in file_name.get():
        msgbox.showwarning("Warning", "Excel (xlsx) format supported only")
        return

        
    csv_column_headers = get_column_headers()
    b_file_name = get_fname_format()
    serial_numbers = read_excel_file(file_name.get())

    serial_count = len(serial_numbers)

    mydate = datetime.date.today().strftime('%d%m%Y')

    final_file_name = str(customer_name.get()) + '_' + mydate + "_" + str(your_initials.get()) + "-" + b_file_name


    if os.path.exists(final_file_name):
        os.rename(final_file_name, str(datetime.datetime.now().strftime("[%H%M%S]-") + final_file_name))
    try:
        with open(final_file_name, 'w') as file:
            file.write("{}\n".format(csv_column_headers))
            for serialnumber in serial_numbers:
                file.write("{},{},{},{},{},{},{},{},{},{}\n".format(account_id.get(),contact_id.get(),description.get(),serialnumber[0],opportunity.get(),product_id.get(),purchase_date.get(),quantity.get(),serialnumber[0],status.get()))
        file.close()
        msgbox.showinfo("Info", "CSV file created. {} S/N processed\nFile Name: {} ".format(serial_count, final_file_name))
    except FileNotFoundError:
        msgbox.showerror("Error", "CSV file is not accessible.  Please try again.")
        return
    
    return(final_file_name)

def get_column_headers():

    # The Column name needed for the ingesting of data by dataloader.
    col_names = ('ACCOUNTID','CONTACTID','DESCRIPTION','NAME','OPPORTUNITY__C','PRODUCT2ID','PURCHASEDATE','QUANTITY','SERIALNUMBER','STATUS')

    column_headers = col_names[0] + "," + col_names[1] + "," + col_names[2] + "," + col_names[3] + "," + col_names[4] + "," + col_names[5] + "," + col_names[6] + "," + col_names[7] + "," + col_names[8] + "," + col_names[9]

    return str(column_headers)

def get_fname_format():

    # The base file name will be taken and changed to reflect the customer,date and initials.
    # See example below.
    # Example might be "TAB_15052023_SN-AOPEN-ANZ-Salesforce-Assets-PRODUCTION-Insert.csv" 
    base_file_name = 'AOPEN-ANZ-Salesforce-Assets-PRODUCTION-Insert.csv'

    return str(base_file_name)

def read_excel_file(snfile):
    try:
        wb = openpyxl.load_workbook(snfile)
        sheet = wb.active
        data = []
        for row in sheet.rows:
            data_row = []
            for cell in row:
                if cell.value:
                    data_row.append(cell.value)
            data.append(data_row)
    except FileNotFoundError:
        msgbox.showerror("Error", "Excel file does not exist.  Please check and try again.")
        return

    return data


# Create the input fields
customer_name = tk.Entry(root)
account_id = tk.Entry(root)
contact_id = tk.Entry(root)
description = tk.Entry(root)
opportunity = tk.Entry(root)
product_id = tk.Entry(root)
purchase_date = tk.Entry(root)
quantity = tk.Entry(root)
status = tk.Entry(root)
your_initials = tk.Entry(root)
file_name = tk.Entry(root)

# Create the labels for the input fields
customer_name_label = tk.Label(root, text="Customer Name:")
account_id_label = tk.Label(root, text="Account Id (Salesforce format):")
contact_id_label = tk.Label(root, text="Contact Id (Salesforce format):")
description_label = tk.Label(root, text="Description:")
opportunity_label = tk.Label(root, text="Opportunity (Salesforce format):")
product_id_label = tk.Label(root, text="Product Id (Salesforce format):")
purchase_date_label = tk.Label(root, text="Purchase Date (YYYY-MM-DD):")
quantity_label = tk.Label(root, text="Quantity:")
status_label = tk.Label(root, text="Status:")
your_initials_label = tk.Label(root, text="Your Initials:")
file_name_label = tk.Label(root, text="File Name with Serial Numbers (xlsx):")

# Place the labels and input fields
customer_name_label.grid(row=0, column=0)
customer_name.grid(row=0, column=1)
account_id_label.grid(row=1, column=0)
account_id.grid(row=1, column=1)
contact_id_label.grid(row=2, column=0)
contact_id.grid(row=2, column=1)
description_label.grid(row=3, column=0)
description.grid(row=3, column=1)
opportunity_label.grid(row=4, column=0)
opportunity.grid(row=4, column=1)
product_id_label.grid(row=5, column=0)
product_id.grid(row=5, column=1)
purchase_date_label.grid(row=6, column=0)
purchase_date.grid(row=6, column=1)
quantity_label.grid(row=7, column=0)
quantity.grid(row=7, column=1)
status_label.grid(row=8, column=0)
status.grid(row=8, column=1)
your_initials_label.grid(row=9, column=0)
your_initials.grid(row=9, column=1)
file_name_label.grid(row=10, column=0)
file_name.grid(row=10, column=1)

# Create the buttons
cancel_button = tk.Button(root, text="Close", command=root.destroy)
create_file_button = tk.Button(root, text="Create File", command=get_input_process)

# Place the buttons
cancel_button.grid(row=11, column=0)
create_file_button.grid(row=11, column=1)

# Start the mainloop
root.mainloop()