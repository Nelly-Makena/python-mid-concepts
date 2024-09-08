import pandas
import random
import datetime as dt
now= dt.datetime.now()
import smtplib

MY_EMAIL = "nellysolomonmakena3@gmail.com"
MY_PASSWORD = "tcvm nhcx kiio fsre"


today =now.month,now.day

today_month=now.month
today_day=now.day
today_tuple = (today_month,today_day)

data =pandas.read_csv("birthdays.csv")
df =pandas.DataFrame(data)

birthday_dict =df.to_dict()

new_birthdays_dict = {
    (row['month'], row['day']): row
    for index, row in df.iterrows()

}

if today_tuple  in new_birthdays_dict:
    birthday_person =new_birthdays_dict[today_tuple]
    file_path =f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open (file_path) as letters:
        contents=letters.read()
        new_letter=contents.replace("[NAME]", birthday_person["name"])

    print(new_letter)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Happy Birthday \n\n{new_letter}"
    )





