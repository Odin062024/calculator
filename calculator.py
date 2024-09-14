import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y
    print(x+y)
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
    
#Komentarz

if __name__ == "__main__":
    operation = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:')
    if operation == '1':
        num1 = input('Podaj składnik 1.')
        num2 = input('Podaj składnik 2.')
        num1 = float(num1)
        num2 = float(num2)
        logging.info(f'Dodaję {num1} i {num2}')
        result1 = add(num1, num2)
        logging.info(f'Wynik to {result1}')
    if operation == '2':
        num1 = input('Podaj składnik 1.')
        num2 = input('Podaj składnik 2.')
        num1 = float(num1)
        num2 = float(num2)
        logging.info(f'Odejmuję {num1} i {num2}')
        result1 = subtract(num1, num2)
        logging.info(f'Wynik to {result1}')
    if operation == '3':
        num1 = input('Podaj składnik 1.')
        num2 = input('Podaj składnik 2.')
        num1 = float(num1)
        num2 = float(num2)
        logging.info(f'Mnożę {num1} i {num2}')
        result1 = multiply(num1, num2)
        logging.info(f'Wynik to {result1}')
    if operation == '4':
        num1 = input('Podaj składnik 1.')
        num2 = input('Podaj składnik 2.')
        num1 = float(num1)
        num2 = float(num2)
        logging.info(f'Dzielę {num1} i {num2}')
        result1 = divide(num1, num2)
        logging.info(f'Wynik to {result1}')
        





    