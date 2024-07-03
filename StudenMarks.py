marks1 = int(input("Please Enter Your Physics Marks :"))

marks2 = int(input("Please Enter Your Maths Marks :"))

marks3 = int(input("Please Enter Your Urdu Marks :"))

marks4 = int(input("Please Enter Your English Marks :"))

marks5 = int(input("Please Enter Your Computer Marks :"))

marks6 = int(input("Please Enter Your Tarjama Quran Marks :"))

marks7 = int(input("Please Enter Your Islamiat Marks :"))

# Calculating Percentage

total_percentage = (marks1 + marks2 + marks3 + marks4 + marks5 + marks6 + marks7)/570*100

if total_percentage<40:
    print("You Are Failed! You didn't reach the required Percentage.")

else:
    print("You Are Passed! You reached the required Percentage.")
    print("You Got 5th Position! Congrats.", total_percentage)