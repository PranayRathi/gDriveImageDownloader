import os
import glob
from variable import modified_image_sheet
#checkForGoogleLink 
def checkForGoogleLink(s2):
    s1 = "drive.google.com" 
    if (len(s2) > 0 and s2.count(s1)>0):
        image_id = s2[s2.index("id=")+3:]    
        return image_id 
    else: 
        return False

#Check if sheet exists
def sheet_exists(wb):
    if modified_image_sheet in wb.sheetnames:
        return True
    return False

path = "./data/*"
def remove_content():
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def check_directory():
    # You should change 'test' to your preferred folder.
    MYDIR = ("data")
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)

    else:
        print(MYDIR, "folder already exists.")
        remove_content()




