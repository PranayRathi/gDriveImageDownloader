import dropbox
from variable import auth_token, filename
from datetime import datetime

dbx = dropbox.Dropbox(auth_token)
acc_details = dbx.users_get_current_account()

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = str(now.strftime('%d_%m_%Y_%H_%M_%S'))

print ('linked account: ', acc_details.name)
print ("Time === ", dt_string)
def upload_image(file_path):
    file_path_dropbox = "/" + filename[:-5] + "/" + dt_string +  file_path[5:]
    # print("======== file_path[1:]", file_path_dropbox)
    with open(file_path, 'rb') as f:
        response = dbx.files_upload(f.read(), file_path_dropbox)
        # print ('uploaded: ', response)

    # Generate the link which is downloadable 
    # result = dbx.files_get_temporary_link(file_path[1:])
    # print(result)
    # return result.link
    
    # Generate sharable link which open in browser
    res = dbx.sharing_create_shared_link_with_settings(file_path_dropbox)
    # print(res.url)    
    return res.url
