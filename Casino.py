from logics import main
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
initial_capital = int(config['settings']['MY_MONEY'])


if __name__ == '__main__':
    main()
