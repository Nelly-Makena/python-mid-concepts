import smtplib
my_email = "nellysolomonmakena3@gmail.com"
my_password= "tcvm nhcx kiio fsre"

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()

    connection.login(user=my_email, password=my_password)

    connection.sendmail(from_addr=my_email, to_addrs="nellymakenakarithi@gmail.com", msg="Subject:Hello\n\n This is a dream come true ")


