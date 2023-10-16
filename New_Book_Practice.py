# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:52:35 2023

@author: user
"""

#firstname = input("Enter your first name: ")
#print("hello", firstname.capitalize())
#surname = input("Enter your surname: ")
#print("Hello", firstname, surname, "nice to meet you")

#print("What do you call a bear with no teeth\nA grummy bear")

#print("Please enter two numbers!")
#num1 = int(input("Number1: "))
#num2 = int(input("Number2: "))
#answer = num1 + num2
#print("Total answer is ", answer)

#num1 = int(input("Enter your first number: "))
#num2 = int(input("Enter your second number: "))
#num3 = int(input("Enter your third number: "))
#answer = (num1 + num2)*num3
#rint("The answer is ", answer)

#slice1 = int(input("How many slices of pizza did you start with: "))
#slice2 = int(input("How many slices have you eaten: "))
#left = slice1 - slice2
#rint("you have left ", left, "slices of pizza")

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#new_age = age + 1
#print(name.capitalize(), "next birthday you will be", new_age, "years old")

#totalBill = int(input("Enter total bill: "))
#numDiners = int(input("Enter the number of diners: "))
#eachPay = totalBill/numDiners
#print("Each person will pay ", eachPay)

#days = int(input("Write the number of days that you want to count: "))
#hours = days*24
#minutes = hours*60
#seconds = minutes*60
#rint("there are ", hours, "hours", minutes, "minutes", seconds, "seconds in", days, "days")

#print("This is the programm for converting kilograms to pounds!")
#kilo = int(input("Enter the weight in kilograms: "))
#convert = kilo*2.204
#print(f"There are {convert} pounds in {kilo} kilo")

#num = int(input("Enter a number over 100: "))
#num1 = int(input("Enter a number under 10: "))
#difference = num//num1
#print(f"{num} is bigger for {difference} times than {num1} ")


# if statement challenges


#num1 = int(input("Please enter first number: "))
#num2 = int(input("Please enter the second number: "))
#if num1 > num2:
#   print(f"the order will be: {num1}, {num2}")
#elif num1 < num2:
#   print(f"the order will be: {num2}, {num1}")

#num = int(input("Enter a number under 20: "))
#if num >= 20:
#    print("Too high")
#else:
#   print("Thank you")

#number = int(input("Enter a number between 10 and 20: "))
#if number >= 10  and number <= 20:
#        print("Thank you")
#else:
#    print("Incorrect answer!")    

#color = input("Enter your favourite color: ")
#if color.lower() == "red":
#    print("I like red too")
#else:
#    print(f"I don't like {color}, I prefer red.")

#rain = input("Is it raining right now outside? ")
#if rain.lower() == "yes":
 #   wind = input("Is it windy? ")
 #   if wind.lower() == "yes":
#        print("It is too windy for an umbrella")
#    else:
#        print("Take an umbrella!")
#else:
#    print("Enjoy your day!")

#age = int(input("Enter your age: "))
#if age >= 18:
#    print("You can vote")
#elif age == 17:
#    print("You can learn to drive")
#elif age == 16:
#    print("You can buy a lottery ticket")
#elif age < 16:
#    print("You can go Trick-or-Treating")

#num = int(input("Enter a number: "))
#if num < 10:
#    print("Too low")
#elif num >10 and num <20:
#    print("Correct")
#else:
#    print("Too high")

#num = int(input("Enter 1, 2 or 3: "))
#if num == 1:
#   print("Thank you")
#elif num == 2:
#   print('Well done')
#lif num == 3:
#   print("Correct")
#else:
#   print("Error message")


#Strings

#name = input("Enter your name: ")
#print(len(name))

#name = input('Enter your first name: ')
#surname = input("Enter your surname: ")
#add = name + " " + surname
#print("Your full name is", add, "that consists of", len(add), "words")

#name = input("Enter your name in lower case: ")
#surname = input("Enter your surname in lower case: ")
#name = name.title()
#surname = surname.title()
#add = name + " " + surname
#print(add)

#name = input("Please, enter your first name: ")
#length = len(name)
#if length < 5:
#    ask = input("Enter your surname: ")
#    join = name + " " + ask
#    join = join.upper()
#    print(join)
#elif length >= 5:
#    print(name.lower())

#word = input("Enter any word that we will convert it to Pig Latin: ")
#first = word[0]
#length = len(word)
#rest = word[1:length]
#if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
#    newword = rest + first + "ay"
#lse:
#    newword = word + "way"
#print(newword.lower())

#MATHS


#num = float(input('Enter a number with lots of decimal places: '))
#answer = num*2
#print(answer)
#print(round(answer, 2))

#import math
#number = int(input("Enter a number over 500: "))
#if number> 500:
#    calculation =math.sqrt(number)
#    print(round(calculation, 2))
#else:
#    print("Enter a number over than 500")

#import math
#radius = float(input("Enter a radius of a circle: "))
#area = math.pi*radius**2
#print(area)

#import math
#print(round(math.pi, 5))

#import math
#radius = float(input("Enter the radius of cyclender: "))
#h = float(input("Enter the height of cyclender: "))
#volume = math.pi*radius**2*h
#print("The volume of cyclender equals to ", round(volume,3))

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#devision = num1//num2
#remainder = num1%num2
#print(f"{num1} divided by {num2} is {devision} with {remainder} remaining")

#import math
#print("1) Square")
#print("2) triangle")
#num = input("Enter a number: ")
#  num == "1":
#    side1 = int(input("Enter one side of square: "))
#   area1 = side1**2
#   print(area1)
#elif num == "2":
#   base = int(input("Enter the base of triangle: "))
#   height = int(input("Enter the height of triangle: "))
#   area2 = base*height//2
#   print(area2)
#else:
#   print("Error message")


#For Loop

#for i in range(1, 10):
#    print(i)

#word = "dilshod"
#for i in word:
#   print(i.title())

#name = input("Enter your name: ")
#for i in range(0, 3):
#    print(name)

#name = input("Enter your name: ")
#num = int(input("Enter a number: "))
#for i in range(0, num):
#   print(name)

#num = int(input("Enter a number: "))
#name = input("ENter your name: ")
#or x in range(0, num):
#    for i in name:
#        print(i)

#number = int(input("Enter a number between 1 and 12: "))
#for i in range(0, 13):
#    answer = i*number
#    print(i, "x", number, "=", answer)

#number = int(input("Enter a number below 50: "))
#for i in range(50, number-1, -1):
#    print(i)

#name = input("Enter your name: ")
#num = int(input("ENter a number: "))
#f num < 10:
#    for i in range(0, num):
#        print(name)
#else:
#    message = "Too high"
#    for i in range(0, 3):
#        print(message)

#print("Total to zero")
#total = 0
#for i in range(0, 5):
#    num = int(input("Enter a number: "))
#    ans = input("Do you want to add this number? (y/n) ")
#    if ans == "yes":
#       total = total + num
#print(total)

#direction = input("Do you want to count from up or down: ")
#if direction == "up":
#    top = int(input("Enter the top number: "))
#    for i in range(1, top+1):
#        print(i)
#elif direction == "down":
#    down = int(input("Enter a number below 20: "))
#    for i in range(20, down-1, -1):
#        print(i)
#else:
#    print("I don't understant")

#num = int(input("How many people do you want invite to the party: "))
#if num <10:
#    for i in range(0, num):
#        name = input("Enter their name: ").capitalize()
#        print(f"{name} has been invited")
#elif num >=10:
#    print("Too many people")


#WHILE LOOP

#total = 0
#while total <=50:
#    num = int(input("Enter a number: "))
#    total = total + num
#   print("The total is ", total)

#number = 0
#while number <= 5:
#    number = int(input("Enter a number: "))
#print("The last number you entered was a ", number)
    
#num1 = int(input("Enter a number: "))
#total = num1
#answer = "y"
#while answer == "y":
#    num2 = int(input('Enter another number: '))
#    total = total + num2
#    answer = input("Do you want to add another number? (y/s)")
#print("The total is equal to ", total)

#count = 0
#again = "yes"
#while again == "yes":
#    name = input("Enter a name that you want to invite to the party: ")
#    print(name.capitalize(), "have now been invited!")
#    again = input("Do you want to add another person to the party? (yes/no): ")
#    count +=1
#print("The total number of guests are ", count)

#compnum = 50
#num = int(input("Enter a compnum number: "))
#attemp = 1
#while num != compnum:
#    if num>50:
#        print("It is too high")
#    elif num<5:
#        print("It is too low")
#    attemp += 1 
#    num = int(input("Have another number? "))
#print("Well done!, you took", attemp, "attempts")
        
#number = int(input("Enter a number between 10 and 20: "))
#while number<10 or number>20:
#    if number <10:
#        print("Too low")
#    else:
#        print("Too high")
#    number = int(input("Try again: "))
#print("Thank you!")

#num = 10
#while num>0:
#    print("There are ", num, "green bottles hanging on the wall.")
#    print( num, "green bottles hanging on the wall.")
#    print("And if 1 green bottle should accidentally fall,")
#    num = num - 1
#    answer = int(input("How many green bottles left on the bottle? "))
#   if answer == num:
#        print("There will be, ", num, "green bottles on the wall.")
#    else:
#        while answer !=num:
#            answer = int(input("No try again: "))
#print("There are no more green bottles hanging on the wall.")


#RANDOM

#import random
#integer = random.randint(0, 100)
#print(integer)

#import random
#fruits = random.choice(["banana", "chery", "apple", "melon", "watermelon"])
#print(fruits)

#import random
#win = random.choice(["t", "h"])
#choice = input("Choose tail(t) or head(h): ")
#f choice == win:
#   print("You win")
#lse:
#    print("Bad luck")
#f win == "h":
#   print("It was tails")
#lse:
#    print("It was heads")

#import random
#num = random.randint(1, 5)
#guess = (input("Enter a number between 1 to 5: "))
#if guess == num:
#    print("Well done")
#elif guess>num:
#    print("Too high")
#    guess = int(input("Guess again: "))
#    if guess == num:
#        print("Correct")
#    else:
#        print("You lose")
#elif guess < num:
#    print("Too low")
#    guess = int(input("Guess again: "))
#    if guess == num:
#        print("Correct")
#    else:
#        print("You lose")

#import random
#number = random.randint(1, 10)
#correct = False
#while correct == False:
#    num = int(input("Enter a number: "))
#    if num == number:
#        correct = True

#import random
#number = random.randint(1, 10)
#correct = False
#while correct == False:
#   num = int(input("Enter a number: "))
#   if num > number:
#        print("Too high")
#   elif num < number:
#        print("Too low")
#  else:
#        print("You are right")
#        correct = True

#import random
#print("Welcome to math quiz")
#score = 0
#for i in range(1, 6):
#    num1 = random.randint(1, 50)
#    num2 = random.randint(1, 50)
#    correct = num1 + num2
#    print(num1, "+", num2, "= ")
#    answer = int(input("Enter your answer: "))
#   print()
#    if answer == correct:
#        score += 1
#print("You scored", score, "out of 5")

#import random
#colors = random.choice(["blue", "red", "yellow", "green", "white"])
#tryagain = True
#while tryagain == True:
#    choice = input("Pick one of these colors: blue, red, yellow, green, white: ")
#    choice = choice.lower()
#    if colors == choice:
#        print("Well done!")
#        tryagain = False
#    else:
#        if colors == "red":
#           print("I bet you are seeing RED right now!")
#        elif colors == "blue":
#            print("Don't feel BLUE")
#        elif colors == "yellow":
#            print("I don't recommend you YELLOW color")
#        elif colors == "green":
#            print("You began to think just like frog, because it has GREEN color")
#        elif colors == "white":
#           print("Are you WHITE as a sheet, as you didn't guess correctly")
    
#TURTLE

#import turtle
#turtle.shape("turtle")
#for i in range(0, 5):
#    turtle.forward(100)
#   turtle.right(72)
#turtle.exitonclick()

#import turtle
#for i in range(10):
#    turtle.right(36)
#    for i in range(0, 5):
#        turtle.forward(100)
#        turtle.right(72)
#turtle.exitonclick()

#import turtle
#for i in range(0, 4):
#    turtle.forward(100)
#    turtle.right(90)
#    turtle.hideturtle()
#turtle.exitonclick()

#import turtle
#for i in range(0,3):
#    turtle.forward(100)
#    turtle.right(120)
#turtle.exitonclick()

#import turtle
#for i in range(0, 360):
#    turtle.forward(1)
#    turtle.right(1)
#turtle.exitonclick()



#import turtle
#turtle.color("black", "red")
#turtle.begin_fill()
#for i in range(0, 4):
#    turtle.forward(70)
#    turtle.right(90)
#turtle.penup()
#turtle.end_fill()
#turtle.forward(100)

#turtle.pendown()
#turtle.color("black", "blue")
#turtle.begin_fill()
#for i in range(0, 4):
#    turtle.forward(70)
#    turtle.right(90)
#turtle.penup()
#turtle.end_fill()
#turtle.forward(100)
#
#turtle.pendown()
#turtle.color("black", "green")
#turtle.begin_fill()
#for i in range(0, 4):
#    turtle.forward(70)
#    turtle.right(90)
#turtle.end_fill()
#turtle.exitonclick()


#import turtle
#for i in range(0 ,5):
#    turtle.forward(100)
#   turtle.right(144)
#turtle.exitonclick()

#import turtle
#turtle.left(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.penup()
#turtle.forward(50)

#turtle.pendown()
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.penup()
#turtle.forward(50)

#turtle.pendown()
#turtle.forward(75)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(45)
#turtle.left(180)
#turtle.forward(45)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(75)

#turtle.hideturtle()
#turtle.exitonclick()


#import turtle
#import random

#turtle.pensize(3)

#for i in range(0, 8):
#    turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
#    turtle.forward(50)
#    turtle.right(45)
    
#turtle.exitonclick()


#import turtle
#import random

#for x in range(0, 10):
#    for i in range(0, 8):
#        turtle.forward(50)
#        turtle.right(45)
#    turtle.right(36)
    
#turtle.hideturtle()
#turtle.exitonclick()


#import turtle
#import random

#lines = random.randint(5, 20)

#for x in range(0, lines):
#    length = random.randint(25, 100)
#    rotate = random.randint(1, 365)
#    turtle.forward(length)
#    turtle.right(rotate)
    
#turtle.exitonclick()




























