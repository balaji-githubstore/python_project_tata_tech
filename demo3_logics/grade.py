# mark=float(input("Enter mark: "))

percentage = 89.5

if percentage >= 90:
    print("Grade A & Percentage is " + str(percentage))
elif 80 <= percentage <= 89:
    print("Grade B & Percentage is " + str(percentage))
elif percentage >= 60 and percentage <= 79:
    print("Grade C & Percentage is " + str(percentage))
elif percentage >= 45 and percentage <= 59:
    print("Grade D & Percentage is " + str(percentage))
else:
    print("Grade F & Percentage is " + str(percentage))
