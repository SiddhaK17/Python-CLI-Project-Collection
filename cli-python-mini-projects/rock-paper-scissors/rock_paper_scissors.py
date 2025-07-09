import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

input_from_user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if input_from_user == '0':
    print(rock)
elif input_from_user == '1':
    print(paper)
elif input_from_user == '2':
    print(scissors)
else:
    print("You entered the number which is out of the option. Please choose between the given numbers")

print("Computer chose :\n")

list = ["Rock", "Paper", "Scissors"]
index_numbers = random.randint(0, 2)
print(list[index_numbers])

if index_numbers == 0:
    print(rock)
    if input_from_user == '0':
        print("It's a Draw!")
    elif input_from_user == '1':
        print("You Win!")
    elif input_from_user == '2':
        print("You Lose")
elif index_numbers == 1:
    print(paper)
    if input_from_user == '0':
        print("You Lose")
    elif input_from_user == '1':
        print("It's a Draw!")
    elif input_from_user == '2':
        print("You Win!")
elif index_numbers == 2:
    print(scissors)
    if input_from_user == '0':
        print("You Win!")
    elif input_from_user == '1':
        print("You Lose")
    elif input_from_user == '2':
        print("It's a Draw!")
else:
    print("The program has been terminated because of choosing a number out of option.")