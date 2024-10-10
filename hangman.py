import random
words = [
    "python",
    "hangman",
    "computer",
    "programming",
    "challenge",
    "difficult",
    "easy",
    "puzzle",
    "random",
    "solution",
    "guessing",
    "keyboard",
    "monitor",
    "internet",
    "software",
    "hardware",
    "network",
    "function",
    "variable",
    "integer"
]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

chosenWord = random.choice(words)
blank = "_" * len(chosenWord)
print(blank)
guessed = False
tries = 6
guessedLetters = []
guessedWords = []
wrongGuesses = 0
def display_hangman(wrongGuesses):
  print(HANGMANPICS[wrongGuesses])


while tries > 0 and not guessed:
  guess = input('Guess a letter or word!  ')
  if len(guess) == 1:
    if guess in guessedLetters:
        print("You already guessed the letter", guess)
    elif guess not in chosenWord:
        print(guess, "is not in the word.")
        guessedLetters.append(guess)
        wrongGuesses += 1
    else: 
        print("Good job,", guess, "is in the word!")
        guessedLetters.append(guess)
        wordsAsList = list(blank)
        indices = [i for i, letter in enumerate(chosenWord) if letter == guess]
        for index in indices:
          wordsAsList[index] = guess
        blank = "".join(wordsAsList)
        if "_" not in blank:
            guessed = True
  elif len(guess) == len(blank):
      if guess in guessedWords:
        print("You already guessed the word", guess)
      elif guess != chosenWord:
        print(guess, "is not the word.")
        wrongGuesses += 1  
        print(wrongGuesses)
        guessedWords.append(guess)  
      else:
        guessed = True  
        blank =chosenWord 
  else: 
    print("Not a valid guess.")
  if wrongGuesses == 7:
      break

  display_hangman(wrongGuesses) 
  print(blank) 
   
if not guessed or wrongGuesses == 6:
  print("Sorry, you ran out of tries. The word was " + chosenWord + ". Maybe next time!")
else:
  print("Congrats, you guessed the word! You win!")
      