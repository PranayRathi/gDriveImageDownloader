#Imports

import xlrd
import openpyxl

#Function imports
from helperFunction import *
from downloadImage import download_file_from_google_drive

from uploadImage import *
from variable import *
from google_drive_downloader import GoogleDriveDownloader as gdd
import time

# provided_image_sheet = "provided_image_sheet"
# modified_image_sheet = "modified_image_sheet"

#open workbook
wb = openpyxl.load_workbook(filename = filename)

ws_read = wb[provided_image_sheet]
ws_write =  wb[modified_image_sheet] if sheet_exists(wb) else wb.create_sheet(modified_image_sheet)

read_sheet_row_size = ws_read.max_row
read_sheet_col_size = ws_read.max_column

# Creating new sheet and writing header ["Image1, Image2", ...]

for i in range(1, read_sheet_col_size+1):
    ws_write.cell(1, i).value = ws_read.cell(1, i).value
wb.save(filename)

# Remove files from data directory
check_directory()
# print("==== " ,acc_details)
# # def checkForGoogleLink(s2):
# #     s1 = "drive.google.com" 
# #     if (s2.count(s1)>0):     
# #         print("YES") 
# #     else: 
# #         print("NO") 
product_successful_count = 0
image_modified_count = 0
unsuccessful_image_count = 0

# Entire sheet
for row in range(2, read_sheet_row_size +1):
    
# For the required range of rows 
# for row in range(2, 10):
    for col in range(1, read_sheet_col_size+1):
        image_link = str(ws_read.cell(row, col).value)
        file_id = checkForGoogleLink(image_link)
        if(file_id):
            print(file_id)
            destination = './data/img_'+ file_id + ".png"
            download_file_from_google_drive(file_id, destination)

            dropbox_link_data = upload_image(destination)
            ws_write.cell(row, col).value = dropbox_link_data
            
            image_modified_count +=1
            print(dropbox_link_data)
        
        else:
            ws_write.cell(row, col).value = image_link
            unsuccessful_image_count +=1
    
    product_successful_count += 1
    wb.save(filename)
    print(row , "Completed \n")

print("===============Report========================")
print("Product_successful_count = ", product_successful_count)
print("image_modified_count = ", image_modified_count)
print("unsuccessful_image_count = ", unsuccessful_image_count)


