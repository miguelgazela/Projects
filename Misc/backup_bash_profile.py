import shutil

bash_file_path = '/Users/migueloliveira/.bash_profile'
dest_file_path = '/Users/migueloliveira/Dropbox/Stuff/.bash_profile_backup'

shutil.copyfile(bash_file_path, dest_file_path)