#!/usr/bin/python

answer = input("What is the greatest NFL team on planet earth?: ")
counter = 1
while (counter == 1):
    if answer.lower() in ("buffalo", "bills", "buffalo bills", "buffalobills", "billsbuffalo", "bills buffalo"):
        print("Correct! Go Bills!")
        counter = 0
    else:
        print("Wrong! Try again.")
        answer = input("What is the greatest NFL team on planet earth?: ")
        counter = 1
