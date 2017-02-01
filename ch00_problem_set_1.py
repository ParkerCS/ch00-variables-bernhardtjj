# SECTION 1 - MATH OPERATORS AND VARIABLES (20PTS TOTAL)
from math import *

# PROBLEM 1 (From Math Class to Code - 2pts)
x = 12.83
# Print the answer to the math question:
your_answer = 3 * (60 * x ** 2 + 3 * x / 9) + 2 * x - 4 / 3 * (x) - sqrt(x)
# where x = 12.83

# your_answer = "Enter the equation"
print(your_answer)

# PROBLEM 2 (Set your alarm - 3pts)

# You look at the clock and see that it is currently 1:00PM.
# You set an alarm to go off 728 hours later.
# At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator.

time = 13.00
time += 728.00
newtime = (time % 24)
if newtime > 12.00:
    print("{:0.2f}".format(newtime - 12.00), "pm")
else:
    print("{:0.2f}".format(newtime), "am")

# Lee - Very nice.  Using the formatting techniques.

# PROBLEM 3 (Wholesale Books - 3pts)
# The cover price of a book is $27.95, but bookstores get a 50 percent discount.
# Shipping costs $4 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 68 copies to the nearest penny.
cover_price = 27.95
discount = 0.5
copies = 68
shipping = 0.75 * copies + 4
print("${:0.2f}".format(cover_price * copies * discount + shipping))

# PROBLEM 4 (Dining Room Chairs - 3pts)
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny
chair_price = 189.99
tax_percent = 0.095
units = 8

print(round(units * chair_price * tax_percent, 2))
# LEE - This is only the tax, not the total. (-1)


# PROBLEM 5 (Area of Circle - 3pts)
# Write code that can compute the area of circle.
# Create variables for radius and pi (3.14159)
# The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows:
# “The surface area of a circle with radius ... is ...”
radius = 3
print("The surface area of a circle with radius", radius, "is", pi * radius ** 2)

# PROBLEM 6 (Coin counter - 4pts)
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.

count = 63.34
print("dollars:", count // 1.00)
print("quartars:", count % 1.00 // 0.25)
print("dimes:", (count % 1.00) % 0.25 // 0.10)
print("nickels:", ((count % 1.00) % 0.25) % 0.10 // 0.05)
print("pennies:", (((count % 1.00) % 0.25) % 0.10) % 0.05 // 0.01)
# I found a float precision error in python! make count 17.65 and print (count % 1.00) % 0.25) % 0.10) % 0.05 and you will see what I mean! it isn't 0.05...



# PROBLEM 7 (Variable Swap - 2pts)
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.

a = 17
b = 23
print("a =", a, "and b =", b)
a = a + b  # this is the first line to help you out
b = a - b
a = a - b
# add two more lines of code here to cause swapping of a and b
print("a =", a, "and b =", b)

print("calculating the definite integral")
print("using a left hand riemann sum")


def f(x): return x ** 2


start_val = 0
end_val = 5
rectangles = 10000

dist = end_val - start_val
xstep = dist / rectangles
ans = 0
print("from", start_val, "to", end_val)
for rect in range(rectangles):
    ans += xstep * f(xstep * rect)
print("Answer is", ans)
# It is about 41.6 ish.
## Now graph rectangles versus ans! when I learn how to matplot I can do that..

# Lee - NICE WORK on some iterated calculus!
