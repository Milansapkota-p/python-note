import os
import shutil
import datetime

source="C:\\Users\\D E L L\\Documents\\git\\python-note\\06_Student Management System\\records"
destination="C:\\Users\\D E L L\\Documents\\git\\python-note\\06_Student Management System\\backup"
def copy_file_to_dist(src,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(destination,str(today))
    print(dest_dir)
    try:
        shutil.copytree(src,dest_dir)
        print(f"file is copy to {dest_dir}")
    except FileExistsError:
        print(f"file already exist in: {dest}")
def back_up():
    copy_file_to_dist(source,destination)
back_up()