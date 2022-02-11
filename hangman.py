
import random

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

word_list = ["aardvark", "baboon", "camel", "potato", "stove", "traverse", "cookie", "sample", "bedrock", "elephant", "lungs", "movie", "friend", "melon", "staircase", "grape", "country", "these", "pants", "applesauce", "simulator", "trash", "label", "snow", "giraffe", "restaurant", "spoon", "pebble", "dominate", "couch"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
player_lives = 6

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}!")
  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
    player_lives -= 1
    if player_lives == 0:
      end_of_game = True
      print("You lose!")

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")

  print(stages[player_lives])
