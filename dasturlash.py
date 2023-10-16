#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#if num1 > num2:
#    print(num2, num1)
#else:
#    print(num1, num2)

#num = int(input("Enter a number under 20: "))
#if num >= 20:
#    print("Too high")
#else:
#    print("Thank you!")

#number = int(input("Enter a number between 10 and 20:  "))
#if number>10 and number<20:
#    print("Thank you")
#else:
#    print("Incorrect answer!")

#color = input("Enter your favourite color:  ")
#if color == "RED" or color == "red" or color =="Red":
#    print("I like red too")
#else:
#    print(f"I do not like {color}, I prefer red")

#answer = input("It is raining?:  ")
#answer = answer.lower()
#if answer == "yes":
#    windy = input("It is windy?:  ")
#    windy = windy.lower()
#    if windy == "yes":
#        print("It is too windy for an umbrella")
#    else:
#        print("Take an umbrella")
#else:
#    print("Enjoy your day")

#age = int(input("Enter your age:  "))
#if age>=18:
#    print("You can vote!")
#elif age==17:
#    print("You can learn to drive")
#if age==16:
#    print("You can buy a lottery ticket")
#if age<16:
#    print("You can go trick-or-treating")

#STRINGS EXERCISES
#name = input("Enter your name: ")
#surname = input("Enter your surname: ")
#fullname = name + " " + surname
#print(fullname.title(),  len(fullname))

#question = input("Enter your nursery rhyme: ")
#length = len(question)
#print(length)
#start = int(input("Enter a starting number: "))
#nd = int(input("Enter an ending number: "))
#part = question[start:end]
#print(part)

#word = input("Enter a word: ")
#first = word[0]
#length = len(word)
#rest = word[1: length]
#if first != "a" and first != "e" and first != "o" and first != "u" and first != "i":
#    newword = rest + first + "ay"
#else:
#    newword = word + "way"
#print(newword)

#MATH
import math
#num = float(input("Enter a number with lots of decimal places: "))
#multiplication = num * 2
#print(multiplication)
#print(round(multiplication, 2))

#number = int(input("Enter an integer over 500: "))
#root = math.sqrt(number)
#print(round(root, 2))

#PI = math.pi
#print(round(PI, 5))

#radius = int(input("Enter the radius of the cylinder: "))
#depth = int(input("Depth: "))
#PI = math.pi
#area = PI * (radius**2)
#volume = area * depth
#print(volume)

#num1 = int(input("Enter a devider: "))
#num2 = int(input("Enter a devident: "))
#partition = round(num1/num2)
#remainder = num1%num2
#print(f"{num1} diveded by {num2} is {partition} with remaining {remainder}")

#print("1) Square")
#print("2) Triangle")
#print()
#chose = int(input("Enter a number (1 or 2): "))
#if chose == 1:
#    side = int(input("Enter the one side of the square: "))
#    area = side * 4
#    print(f"The area of the square {area}")
#elif chose ==2:
#    base = int(input("Enter the base of the triangle: "))
#    height = int(input("Enter the height of the triangle: "))
#    area = (base * height)/2
#    print(f"The area of triangle is {area}")
#else:
#    print("Error message")

#LOOP

#name = input("Enter your name: ")
#number = int(input("Enter number of times: "))
#for i in range(number+1):
#    print(name)

#name = input("NAme: ")
#num = int(input("NUmber: "))
#for i in range(num):
#    for j in name:
#        print(j)

#import calendar
#month = 12
#year = 2004
#for i in range(1, month+1):
#    x = calendar.month(year, i)
#    print(x)

#num = int(input("Enter a number between 1 and 12: "))
#for i in range(1, 13):
#    answer = i *num
#    print(i, "x", num, "=", answer)

