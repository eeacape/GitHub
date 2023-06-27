#Name: prep-csv-for-dataloader.py
#Ref: A way to automate the curating of the CSV file to be used by dataloader
#     was required.  This script enables this to be done.
#Copyright (c) 2023. CPEREIRA. All Rights Reserved.
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

def get_input_process():
    
    cname = input("Customer Name: ")
    accid = input("Account Id (Salesforce format): ")
    contid = input("Contact Id (Salesforce format): ")
    descr = input("Description: ")
    oppor = input("Opportunity (Salesforce format): ")
    proid = input("Product Id (Salesforce format): ")
    pdate = input("Purchase date (YYYY-MM-DD): ")
    quant = input("Quantity: ")
    status = input("Status: ")
    yoinit = input("Your initials: ")
    snfile = input("File name with serial numbers: ")

    csv_column_headers = get_column_headers()
    b_file_name = get_fname_format()
    serial_numbers = read_excel_file(snfile)

    serial_count = len(serial_numbers)

    print("{} serial numbers retrieved from {}".format(serial_count, snfile))

    mydate = datetime.date.today().strftime('%d%m%Y')

    final_file_name = cname + '_' + mydate + "_" + yoinit + "-" + b_file_name

    if os.path.exists(final_file_name):
        os.rename(final_file_name, str(datetime.datetime.now().strftime("[%H%M%S]-") + final_file_name))
    
    try:
        with open(final_file_name, 'w') as file:
            file.write("{}\n".format(csv_column_headers))
            for serialnumber in serial_numbers:
                file.write("{},{},{},{},{},{},{},{},{},{}\n".format(accid,contid,descr,serialnumber[0],oppor,proid,pdate,quant,serialnumber[0],status))
        file.close()
    except FileNotFoundError:
        print("Error: {} is not accessible.  Exiting".format(final_file_name))
        sys.exit()

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
        print("Error: {} does not exist in current directory.  Exiting".format(snfile))
        sys.exit()
    return data

def main():
    get_input_process()

if __name__ == '__main__':
    main()