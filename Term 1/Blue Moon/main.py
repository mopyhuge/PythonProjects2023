# Dylan Cowley

bluemoon = input("Is there a blue moon tonight (Yes / No)?")
weekday = input("What is the day of the week (Monday - Sunday)?")
day = input("What is the day of the month (1 - 31)?")

if bluemoon == "Yes":
    print("Play song 'Once in a Blue Moon'")
elif bluemoon == "No":
    if weekday == "Monday":
        print ("Manic Monday")
    elif weekday == "Tuesday":
        print ("Tuesday's Gone")
    elif weekday == "Wednesday":
        print ("Just Wednesday")
    elif weekday == "Thursday":
        print ("Sweet Thursday")
    elif weekday == "Friday":
        print ("Friday I'm in Love")
    elif weekday == "Saturday":
        print ("Saturday in the Park")
    elif weekday == "Sunday":
        print ("Lazing on a Sunday Afternoon")
    else:
        print("Days of the Week")
else:
    print("Day Dream Believer")