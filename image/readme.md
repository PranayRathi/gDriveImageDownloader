
// Installation cmd

 pip install xlrd==1.2.0
 pip install openpyxl
 pip install googledrivedownloader
 pip install dropbox
 pip install gdown

This project will work as follows:

1. read the excel file sheet name "provided_image_sheet" where the google drive link is available.

(1 image at a Time)
2. First download the image and store it data directory.
3. Upload the same image file in the dropbox (create Apps in dropbox to get access token which should be provided in variable.py file)



