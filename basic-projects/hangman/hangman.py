import random as rd

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 7

word_list = ["apple","chair","house","book","bicycle","kitchen","garden","astronaut","hypothesis","elephant","pyramid","compass","rainbow"]

random_word = rd.sample(word_list, 1)
word = ''.join(random_word)
print(word)

blanks = ["_"] * len(word)
print(''.join(blanks))


game_over = False

while not game_over:
    letter_guess  =  input("Guess a letter : ").lower()
    if letter_guess in word:
        for i in range(0,len(word)):
            if letter_guess == word[i]:
                blanks[i] = word[i]
                
    else:
        lives -= 1
        print(f"\nIncorrect word\nLives left : {lives}\n\t")
        print(HANGMANPICS[7 - lives - 1])
    
    print(f"Current word: {''.join(blanks)}")
        
    if "_" not in blanks:
        game_over = True
        print("You win!")
    if lives == 0:
        print("You lose")
        print(f"The actual word is {word} ")
        game_over = True