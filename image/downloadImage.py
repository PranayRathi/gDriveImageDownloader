import requests

import gdown

url = 'https://drive.google.com/uc?id='

# url2 = "https://drive.google.com/drive/u/0/folders/1lfqsx0OZhjV2Dp3FfC0Lh23MlyzLG0AW"

# id2 = "1lfqsx0OZhjV2Dp3FfC0Lh23MlyzLG0AW"

# destination = "./data/zip/12.ext"
def download_file_from_google_drive(id, destination):

    gdown.download(url+id, destination, quiet=False) 

# def download_file_from_google_drive(id, destination):
#     URL = "https://docs.google.com/uc?export=download"

#     session = requests.Session()

#     response = session.get(URL, params = { 'id' : id }, stream = True)
#     token = get_confirm_token(response)

#     if token:
#         params = { 'id' : id, 'confirm' : token }
#         response = session.get(URL, params = params, stream = True)

#     save_response_content(response, destination)    

# def get_confirm_token(response):
#     for key, value in response.cookies.items():
#         if key.startswith('download_warning'):
#             return value

#     return None

# def save_response_content(response, destination):
#     CHUNK_SIZE = 32768

#     with open(destination, "wb") as f:
#         for chunk in response.iter_content(CHUNK_SIZE):
#             if chunk: # filter out keep-alive new chunks
#                 f.write(chunk)

# download_file_from_google_drive(id2, destination)

