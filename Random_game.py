import random
target=random.randint(1,100)
while True:
    user_num=(input("Guess the target or Quit(Q) :"))
    if(user_num=="Quit"):
        break
    user_num= int(user_num)
    if(user_num==target):
        print("Guess Successfully",)
        break
    elif(user_num<target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")
    

print("------GAME OVER-----")