import smtplib
import datetime as dt
import random

MY_EMAIL = "nellysolomonmakena3@gmail.com"
MY_PASSWORD = "tcvm nhcx kiio fsre"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    try:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Hello Beautiful, here is your Monday Motivation\n\n{quote}"
            )
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Today is not Monday.")
