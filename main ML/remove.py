import openpyxl

# Load the Excel file
wb = openpyxl.load_workbook('outputin xl.xlsx')
ws = wb.active

# Get the data from the second column
data = ws['B']

# Process the data
for cell in data:
    # Remove opening and closing brackets
    cell.value = cell.value.replace('[', '').replace(']', '')

    # Remove spaces after commas
    cell.value = cell.value.replace(', ', ',')

# Save the file as XLSX
wb.save('processed_data.xlsx')
