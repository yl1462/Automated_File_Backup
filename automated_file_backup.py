import os
import shutil
import datetime
import schedule
import time

source_dir = "F:/2024_Infosys_Bench_Projects/Automated_File_Backup/screenshots"
destination_dir = "F:/2024_Infosys_Bench_Projects/Automated_File_Backup/back_up"

def copy_folder_to_directory(source, dest):
    #getting today's date
    today = datetime.date.today()
    #combine the file directory with today's date
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

#make sure the time is entered in HH:MM(:SS) format        
schedule.every().day.at("17:34").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    #once program start running, it will stay running, keeps on checking if there is any pending fuction waiting to be ran, and checks at a 60 seconds interval
    schedule.run_pending()
    time.sleep(60)
        

    