year = (int(input("Which year do u want to know?\n")))

if year % 4 == 0 and year % 100 > 0:
     print(f"Your Year is {year} & Its A Leap Year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
     print(f"Your Year is {year} & Its A Leap Year")
else:
      print("Your Year Is Not a leap year.")

