import random
import logging
from datetime import datetime

logging.basicConfig(filename='games.log', level=logging.DEBUG)

def generate_number(n):
    # Генерирует случайное число от 1 до N
    number = random.randint(1, n)
    logging.info(f"Generated number: {number}")
    return number

def get_user_guess():
    # Получает от пользователя предполагаемое число
    while True:
        try:
            guess = int(input("Enter the expected number: "))
            logging.info(f"The expected number has been entered: {guess}")
            return guess
        except ValueError:
            print("Please enter a number.")

def check_guess(number, guess):
    # Проверяет предполагаемое число пользователя
    if guess < number:
        print("The hidden number is bigger.")
        logging.info("The user entered a number less than the desired one")
        return False
    elif guess > number:
        print("The hidden number is less")
        logging.info("The user entered a number greater than the desired one")
        return False
    else:
        print("You guessed it!")
        logging.info("The user guessed the number")
        return True

def game(n, k):
    """Основная функция игры"""
    logging.info(f"The numbers N = {n}, k = {k} are given")
    
    number = generate_number(n)
    guesses_left = k

    while guesses_left > 0:
        print(f"You have {guesses_left} attempts left.")
        guess = get_user_guess()

        if check_guess(number, guess):
            return
        
        guesses_left -= 1

    print("The attempts ended.")
    logging.info("The attempts ended.")

if __name__ == "__main__":
    print("The game 'Guess the number'")
    n = int(input("Enter the number N: "))
    k = int(input("Enter the number k: "))

    logging.info(f"Start of the game with numbers N = {n}, k = {k} in {datetime.now()}")

    game(n, k)

    logging.info(f"The game is completed in {datetime.now()}")
