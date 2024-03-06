import random

def myfunction():
  x = random.randint(0,50)
  z=0
  print("In this game you will have 10 attempts to guess the random number between 0 & 50.")
  for i in range(0,10):
    y= input("Give me a number between 0 and 50 :\n")
    if x == int(y):
       print("✅ Yaay you won")
       return
    elif x>int(y):
      print("❌ Your number is less than the right number.")
    else:
      print("❌ Your number is greater than the right number.")
    z+=1
    print("You have",10-i,"attempts left.")
  print("You lost.")

myfunction()
