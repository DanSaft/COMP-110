""" One Shot World """

secret_word: str = "python"
secret_word_len: str = len(secret_word)
guess_word: str = input(f"What is your {secret_word_len}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
indx: int = 0
guess_evaluation: str = ""

while len(str(guess_word)) != len(str(secret_word)):
    #Check length of word
    guess_word: str = input(f"That was not {secret_word_len}-letters! Try again: ") 
    
    

if len(str(guess_word)) == len(str(secret_word)):
    while indx < len(secret_word):
     if guess_word[indx] == secret_word[indx]:
        guess_evaluation = guess_evaluation + GREEN_BOX

     if guess_word[indx] != secret_word[indx]:
        within_word: bool = False
        secret_checker: int = 0
        while secret_checker < len(secret_word) and within_word == False:
        #False means that the indx of the guess word is not found anywhere in the secret word
         if secret_word[secret_checker] == guess_word[indx]:
            within_word = True
            guess_evaluation = guess_evaluation + YELLOW_BOX
         else: secret_checker = secret_checker + 1
        if within_word == False:
            guess_evaluation = guess_evaluation + WHITE_BOX
     indx = indx + 1
    if str(guess_word) == str(secret_word):
        print(guess_evaluation)
        print("Woo! You got it!")
    else:
        print(guess_evaluation)
        print("Not quite. Play again soon!")

        





    

    







