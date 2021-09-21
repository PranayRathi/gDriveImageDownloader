import os
import glob
from variable import modified_image_sheet
#checkForGoogleLink 
MAX_SIZE = 2097152
from PIL import Image
def checkForGoogleLink(s2):
    s1 = "drive.google.com" 
    if (len(s2) > 0 and s2.count(s1)>0):
        if s2.count("id=")>0:
            image_id = s2[s2.index("id=")+3:]   
            return image_id
        elif (s2.index("/d/")):
            split_link = s2.split("/")
            return split_link[5]
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

def file_exist(path):
    try:
        os.path.exists(path)
        return True
        # Do something with the file
    except IOError:
        print("File not exist")
        return False
    finally:
        f.close()


#### Look up data
lookup_table = {}
def lookupForImageId(file_id, current_row, current_col):
    if not( file_id in lookup_table):
        lookup_table[file_id] = {"row" : current_row, "col" : current_col}
        return []
        
    print("Found the dublicate link in sheet at row" + str(current_row) + "and coloum " + str(current_col))

    found_row = lookup_table[file_id]["row"]
    found_col = lookup_table[file_id]["col"]

    print("Previous Location : row = " + str(found_row) + "col = " + str(found_col))

    if(found_row == current_row):
        return False
    
    return [found_row, found_col]
# import math
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
# # check_file_size 
# path = 'data/img_86.png' 
def check_file_size(path):
    file_size = os.path.getsize(path)
    print("File Size is :", file_size, "bytes")
    
    if(MAX_SIZE > file_size):
        print("File size has crossed the max limit")
        return True

    return True
# temp = 1
# def compress(path):
#     og_path = path
#     new_path = path[0:-4] + 'og.png'
#     os.rename(og_path, new_path)

#     # while(os.path.getsize(new_path) > MAX_SIZE):
#     #     print("Image compression inside while loop ")
#     #     # new_path1 = path[0:-4] + (temp + 1) + 'og.png'
#     #     # os.rename(new_path, new_path)
#     #     picture = Image.open(new_path)
#     #     new_path1 = path[0:-4] + 'og2.png'
#     #     picture.save(new_path1 , optimize = True, quality = 30)
#     #     print("====== " + str(os.path.getsize(new_path1)))
#     print("File Size is og:",  os.path.getsize(new_path), MAX_SIZE)
#     while(os.path.getsize(new_path) > MAX_SIZE):
#         print("@@@@@File Size is og:",  os.path.getsize(new_path), MAX_SIZE)
#         foo = Image.open(new_path)
#         x, y = foo.size
#         x2, y2 = math.floor(x-50), math.floor(y-20)
#         # foo = foo.resize((x2,y2),Image.ANTIALIAS)
#         foo.save(new_path,optimize = True, quality=30)
#         print("====File Size is compressed:",  os.path.getsize(new_path), MAX_SIZE)
#     os.rename(new_path, og_path)
#     print("Image compressed")

# print("Image compressed")
# check_file_size(path)
