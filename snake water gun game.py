import random

'''1 = snake
   0 = water
  -1 = gun'''

for i in range(1,10):
    youstr = input("snake, water or gun (type exit to quit):").lower()
    
    if youstr == "exit":
        print("Game exited")
        break

    if youstr not in ["snake","water","gun"]:
        print("Enter a valid input")
        continue

    computer = random.choice([1,0,-1])

    youdict = {"snake":1,
              "water":0,
              "gun":-1}
    reversedict = {1:"snake",
                 0:"water",
                 -1:"gun"}

    you = youdict[youstr]

    print(f"you choose {reversedict[you]}")
    print(f"computer choose {reversedict[computer]}")

    if computer == you:
        print("it's a draw!")
    elif computer == 1 and you == 0:
        print("you lose!")    
    elif computer == 1 and you == -1:
        print("you win!")
    elif computer == 0 and you == 1:
        print("you win!")
    elif computer == 0 and you == -1:
        print("you lose!")
    elif computer == -1 and you == 0:
        print("you win!")
    elif computer == -1 and you == 1:
        print("you lose!")      