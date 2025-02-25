import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    while not guessed:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < number_to_guess:
                print("Загаданное число больше.")
            elif guess > number_to_guess:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} с {attempts} попытки(ок).")
                guessed = True
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_number()