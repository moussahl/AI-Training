import random


def myfunction():
  x = random.randint(0,50)
  z=0
  print("In this game you will have 10 attempts to guess the random number between 0 & 50.")
  while(z<10):
    y= input("t  number between 0 and 50 :\n")
    if x == int(y):
       print("✅ Yaay you won")
       break
    elif x>int(y):
      print("❌ Your number is less than the right number.")
    else:
      print("❌ Your number is greater than the right number.")
    z+=1
    print("You have",10-z,"attempts left.")


myfunction()