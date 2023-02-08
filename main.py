from flatmates_bill import Bill, Flatmate
from report import PdfReport

while True:
    try:
        bill = float(input("Please enter the bill value: "))
        break
    except ValueError:
        print("Please enter a number")

period = input("Please enter the period - E.g. December 2020: ")
user = input("Please enter your name: ")

while True:
    try:
        days_in_house = int(input(f"Please enter the days {user} stayed in the house during the bill period: "))
        break
    except ValueError:
        print("Please enter a number")

user2 = input("Please enter the name of your flatmate: ")

while True:
    try:
        days_in_house2 = int(input(f"Please enter the days your {user2} stayed in the house during the bill period: "))
        break
    except ValueError:
        print("Please enter a number")

my_bill = Bill(bill, period)
flatmate_1 = Flatmate(user, days_in_house)
flatmate_2 = Flatmate(user2, days_in_house2)

pdf_report = PdfReport(filename=f"{period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, my_bill)
