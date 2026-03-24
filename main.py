##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv


from datetime import datetime
import pandas as pd
import smtplib
import random 
import os

# 2. Check if today matches a birthday in the birthdays.csv
date_file = pd.read_csv(filepath_or_buffer="/Users/manasapola/PycharmProjects/Basicsofpython/Birthdaywisher_project/birthday-wisher-extrahard-start/birthdays.csv")
date_table = pd.DataFrame(date_file)
date_file_day = (date_file.day).to_list()
date_file_month = (date_file.month).to_list()
present_day = datetime.now().day
present_month = datetime.now().month
letter_file_path = "/Users/manasapola/PycharmProjects/Basicsofpython/Birthdaywisher_project/birthday-wisher-extrahard-start/letter_templates/"
letters = ("letter_1","letter_2","letter_3")
random_letter = random.choice(letters)

email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if present_day in date_file_day and present_month in date_file_month:
    name = date_file[date_file.day == present_day].name.iloc[0]
    reciever_email = date_file[date_file.day == present_day].email.iloc[0]
    with open(f"{letter_file_path}/{random_letter}.txt",mode = "r+") as letter:
        content = letter.read()
        content = content.replace("Angela","Manasa")
        new_name = content.replace("[NAME]", name)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email, password  = password)
        connection.sendmail(
            from_addr = email,
            to_addrs = reciever_email, 
            msg = f"Subject:Birthday Wishes\n\n {new_name}"
            )
    connection.close()


    
    









