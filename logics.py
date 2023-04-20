import random
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
initial_capital = int(config['settings']['MY_MONEY'])


def play_slot_machine(capital):
    print(f"Your current capital: {capital}")
    bet = int(input("Choose a slot number (1-30): "))
    bet_amount = int(input("Enter your bet amount: "))

    if bet_amount > capital:
        print("You have not money for this bet")
        return 0


    winning_number = random.randint(1, 30)

    if bet == winning_number:
        print("You win!")
        return bet * 2
    else:
        print("You lost!")
        return -bet_amount


capital = initial_capital
while True:

    win_or_loss = play_slot_machine(capital)
    capital += win_or_loss

    if capital <= 0:
        print("You lost! Game over")
        break

    answer = input("Do you want to continue? (y/n)")
    if answer.lower() == 'n':
        print(f"Game over. Your capital: {capital}")
        break