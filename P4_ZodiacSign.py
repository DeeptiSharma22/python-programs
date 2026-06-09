'''
Project 4
Problem Statement:
Given the birthdate and name of the person, you want to create a Python program to determine the corresponding Zodiac sign based on the date.

Question:
How can you write a Python program that takes name and birthdate as input and outputs the corresponding Zodiac sign and store it in a file using Pandas?
'''

from datetime import datetime
import pandas as pd

#Function to get the Zodiac sign
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

#Getting details from User
str_birthdate = input("Enter you Date Of Birth (YYYY-MM-DD) format:")
name = input("Enter you name: ")

birthdate = datetime.strptime(str_birthdate, "%Y-%m-%d")

birth_day = birthdate.day
birth_month = birthdate.month
print(f"User birth day and month : {birth_day} {birth_month}")
# Get zodiac sign
zodiac_sign = get_zodiac_sign(birth_day, birth_month)

print(f"Name: {name} with DOB: {str_birthdate}, Zodiac sign is: {zodiac_sign}")

# --- Store in a file using Pandas ---
data = {
    "Name": [name],
    "Birthdate": [birthdate],
    "Zodiac Sign": [zodiac_sign]
}

df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("p4_user_details.csv", index=False)
print("Data saved successfully to p4_user_details.csv")