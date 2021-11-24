"""
7. For a user-defined integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Use the cascade if-elif-else for it.
"""

print("-1 means that your integer is negative, 1 if it is positive, and 0 if it is equal to zero ")

XInteger = int(input("Enter and integer to determine wether is zero, positive or negative . "))
if XInteger < 0:
  print ("-1")
elif XInteger > 0:
  print ("1")
else:
  print ("0")
#decides in which category the inputed number falls on