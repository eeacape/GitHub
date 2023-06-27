import openpyxl

def read_excel_file(file_name):
    """
    Read data from an Excel file with the extension of XLSX and only read the cells that contain data.

    Args:
        file_name (str): The name of the Excel file.

    Returns:
        list: A list of lists containing the data from the Excel file.
    """

    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    data = []
    for row in sheet.rows:
        data_row = []
        for cell in row:
            if cell.value:
                data_row.append(cell.value)
        data.append(data_row)
    return data

def write_data_to_file(data, file_name):
    """
    Write data to a file with a comma separate values.

    Args:
        data (list): The data to be written to the file.
        file_name (str): The name of the file.
    """

    with open(file_name, "w") as f:
        for row in data:
            f.write(", ".join(row) + "\n")

if __name__ == "__main__":
    data = read_excel_file("SN for PO2402.xlsx")
    write_data_to_file(data, "data.csv")