import random


wordlist=["Python","Cprogram","Ruby","banana"]
lives=6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

ran_wordlist=random.choice(wordlist)

print(ran_wordlist)

display=[]
for letter in range(len(ran_wordlist)):
  display+="_"

print(display)
end_of_game=False

while not end_of_game:

    guess_letter=input("Enter a guess letter\n")

    for position in range(len(ran_wordlist)):

        letter =ran_wordlist[position]

        if letter==guess_letter:
            display[position]= letter

    if guess_letter not in ran_wordlist:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")

    if "_" not in display:
        end_of_game=True
        print("YOU WIN")

    print(f"{' '.join(display)}")

    print(stages[lives])
        
