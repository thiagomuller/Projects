import random

def jogar():

    def even_or_odd(n):
        even = n%2 == 0
        odd = n%2 == 1
        if(even):
            print("The secret number is an even!!!\n")
        elif(odd):
            print("The secret number is an odd!!!\n")

    def prime_numbers(n):
        if(n%1 == 0 and n%n == 0):
            print("The secret number is a prime number!!!\n")

    def below_or_above_fifty(n):
        if(n > 50):
            print("The secret number is above fifty!!!\n")
        if(n < 50):
            print("The secret number is below fifty!!!\n")

    def greater_or_lower(guess , score,  n):


        greater = guess > secret_number
        lower = guess < secret_number

        if greater:

            print("Your number was greater than secret number\n")
            score = score - (guess - secret_number)
            print("Your score is: {}\n".format(score))

        elif lower:
            print("Your number was lower than secret number\n")
            score = score - (secret_number - guess)
            print("Your score is: {}\n".format(score))

        return score


    def random_tip(n):  #generates a random tip in case user requires it
        ran_n = random.randrange(0, 3)

        if(ran_n == 0):
            even_or_odd(secret_number)
        elif(ran_n == 1):
            prime_numbers(secret_number)
        elif(ran_n == 2):
            below_or_above_fifty(secret_number)


    def beginning_messages():
        print("Welcome to guessing game")
        print("Your task here is to guess one number between 1 and 100")
        print("Could you please choose between below difficulties:")


    def possible_answers_tip():
        list_tip = ["tip", "wanna tip", "want tip", "i want a tip"]
        return(list_tip)

    def possible_answers_guess():
        list_guess = ["guess", "wanna guess", "i want to guess", "want guess"]
        return(list_guess)

    def choosing_difficulties():
        diff = int(input("(1) Easy ,  (2) Medium , (3)Hard\n"))

        if (diff == 1):
            tries = 50
            tips = 3
        elif (diff == 2):
            tries = 20
            tips = 2
        elif (diff == 3):
            tries = 5
            tips = 1
        tries_tips = [tries, tips]
        return tries_tips

    def game_loop(secret_number):

        tries_tips = choosing_difficulties()
        expected_guess = possible_answers_guess()
        expected_tip = possible_answers_tip()
        score = 1000
        print("Type q to quit anytime you want\n")
        print(secret_number)
        guess_or_tip = input("Would you like to guess or take a tip?\n").strip().lower()
        for rodada in range(1 , tries_tips[0] + 1):
            if(guess_or_tip == "q"):
                print("You quited, thanks for playing!")
                break
            while(guess_or_tip in expected_tip and tries_tips[1] > 0):
                    random_tip(secret_number)
                    tries_tips[1] -= 1
                    guess_or_tip = input("Would you like to guess or take a tip?\n").strip().lower()
                    if(tries_tips[1] == 0):
                        print("Seems like you ran out of tips!\n")
                        guess_or_tip = "guess"
            while(guess_or_tip in expected_guess and tries_tips[0] > 0):
                    guess = int(input("Please type your guess\n"))
                    if(guess == secret_number):
                        print("Congratulations, you won!\n")
                        print("Your final score was: {}".format(score))
                        exit()
                    elif(guess != secret_number):
                        print("Wrong number!\n")
                        tries_tips[0] -= 1
                        score = greater_or_lower(guess, score, secret_number)
                        print("You got {} chances\n".format(tries_tips[0]))
                        if(tries_tips[0] > 0 and tries_tips[1] > 0):
                            guess_or_tip = input("Would you like to guess or take a tip?\n")
                        elif(tries_tips[0] == 0 and tries_tips[1] == 0):
                            print("Game over!\n")
                            print("Thanks for playing!\n")
                            break
        print("Your final score was: {}".format(score))




    secret_number = random.randrange(1 , 101)   #creating a random number to be used in the game

    beginning_messages()

    game_loop(secret_number)



if(__name__ == "__main__"):
    jogar()