from datetime import date

name = input("What is your name? ")
age = int(input("How old are you? "))

todays_date = date.today()

print(name + ", you will turn 100 in " + str(todays_date.year-age+100))
