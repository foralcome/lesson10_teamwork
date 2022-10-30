import random

from telegram_token import TELEGRAM_TOKEN_PY
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from random import choice

import rational
import complex

app = None
calc_type_number = 'rational'
calc_types_number = ['rational', 'complex']

count_numbers_in_operation = 1
calc_numbers = []

calc_operation = ''

def init():
    global count_numbers_in_operation
    global calc_numbers
    count_numbers_in_operation = 2
    calc_numbers = []


def get_type_number():
    return calc_type_number


def set_type_number(type):
    global calc_type_number
    calc_type_number = type


def get_count_numbers_in_operation():
    return count_numbers_in_operation


def set_count_numbers_in_operation(count):
    global count_numbers_in_operation
    count_numbers_in_operation = count_numbers_in_operation


def get_operation():
    return calc_operation


def set_operation(operation):
    global calc_operation
    global count_numbers_in_operation
    calc_operation = operation
    count_numbers_in_operation = 2
    if operation == 'sqrt':
        count_numbers_in_operation = 1

def get_numbers():
    return calc_numbers


def set_numbers(numbers):
    global calc_numbers
    calc_numbers = calc_numbers

def add_numbers(number):
    global calc_numbers
    calc_numbers.append(number)


def calc(type_numbers, operator):
    if type_numbers == 'rational':
        return rational.calc(operator, calc_numbers)
    if type_numbers == 'complex':
        return complex.calc(operator, calc_numbers)
    else:
        return None