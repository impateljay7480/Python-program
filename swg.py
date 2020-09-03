import random

print("Welcome To Snake-Water-Gun Game:>\n\nRules: You Have only 5 Try after Your Game Is Over.\n")

list= ("S - Snake", "W - Water", "G - Gun")
for l in list:
    print(l)

i=1


while i <= 5:

    def draw():
        print("Your Match Is Draw. Try Again.")
        print(f"Your Attempt {i}.\n")

    def lose():
        print("You Are Lose. Try Again.")
        print(f"Your Attempt {i}.\n ")

    def won():
        print("Congratulation , You Won")
        print(f"you Won In {i} Try.\n")

    s = input("Enter Your Choise:")

    cpu = random.choice(list)
    print("Cpu Selected:",cpu)
    print("\n")
    if s  is int():
        print("Please Choose The Proper Letter (W-S-G)")
    elif s == "W" and cpu == "W - Water":
        draw()
        i = i+1
    elif s == "W" and cpu == "S - Snake":
        lose()
        i = i+1
    elif s == "W" and cpu == "G - Gun":
        won()
        break
    elif s == "S" and cpu == "W - Water":
        won()
        break
    elif s == "S" and cpu == "G - Gun":
        lose()
        i= i+1
    elif s == "S" and cpu == "S - Snake":
        draw()
        i = i+1
    elif s == "G" and cpu == "S - Snake":
        won()
        break
    elif s == "G" and cpu == "W - Water":
        lose()
        i= i+1
    elif s == "G" and cpu == "G - Gun":
        draw()
        i = i+1
    else:
        print("Please..Enter Right Word.\nIn Case Your Word Is Not Capital Otherwise You Are Not Selected Right Word.\n")
        continue


print("Game Over")









