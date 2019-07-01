import os
import zipfile

dir_path = os.path.dirname(os.path.abspath(__file__))

local_zip = dir_path+'/cats_and_dogs_filtered.zip'

zip_ref = zipfile.ZipFile(local_zip, 'r')

zip_ref.extractall(dir_path)
zip_ref.close()