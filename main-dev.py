import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    # Выбор уровня сложности
    print("Выберите уровень сложности:")
    print("1. Легкий (10 попыток)")
    print("2. Средний (7 попыток)")
    print("3. Тяжелый (5 попыток)")

    while True:
        try:
            difficulty = int(input("Введите номер уровня сложности (1, 2 или 3): "))
            if difficulty == 1:
                max_attempts = 10
                break
            elif difficulty == 2:
                max_attempts = 7
                break
            elif difficulty == 3:
                max_attempts = 5
                break
            else:
                print("Пожалуйста, выберите корректный уровень сложности (1, 2 или 3).")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    while not guessed and attempts < max_attempts:
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

    if not guessed:
        print(f"К сожалению, вы не угадали число. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    guess_number()