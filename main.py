from telegram_token import TELEGRAM_TOKEN_PY

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

import user_interface as ui

import calc as mod_calc
import file_calc as mod_file
import log_calc as mod_log

START_MENU = 0
CHOICE_START_MENU = 1
CHOICE_TYPE_NUMBERS = 2
CHOICE_CALC_OPERATION = 3
CHOICE_CALC_OPERATION_DIVISION = 4
INPUT_RATIONAL_NUMBER = 5
INPUT_COMPLEX_NUMBER = 6
INPUT_NUMBERS = 7
RUN_CALC_OPERATION = 8
RATIONAL_MENU = 9
COMPLEX_MENU = 10
CLOSE = 11


async def restart_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == 'Да':
        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS
    if update.message.text == 'Нет':
        reply_keyboard = [ui.main_menu]
        await update.message.reply_text(
            "Выберите действие:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_START_MENU


async def start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [ui.main_menu]
    await update.message.reply_text(
        "Выберите действие:",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
        ),
    )
    return CHOICE_START_MENU


async def choice_start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    if update.message.text == 'run calc':
        mod_log.add_log_calc(user.id, 'run calc')
        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS

    else:
        mod_log.add_log_calc(user.id, 'close calc')
        await update.message.reply_text(f"Bye, {user.name}!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END


async def choice_type_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    mod_calc.init()
    reply_keyboard = []
    if update.message.text == 'rational':
        mod_calc.calc_type_number = update.message.text
        mod_log.add_log_calc(user.id, 'work with rational numbers')
        reply_keyboard = [[v] for v in ui.menu_operation_rational]
    if update.message.text == 'complex':
        mod_calc.calc_type_number = update.message.text
        mod_log.add_log_calc(user.id, 'work with complex numbers')
        reply_keyboard = [[v] for v in ui.menu_operation_complex]
    if update.message.text == 'back':
        reply_keyboard = [ui.main_menu]
        await update.message.reply_text(
            "Выберите действие:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_START_MENU

    await update.message.reply_text(
        "Выберите операцию: ",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
        ),
    )
    return CHOICE_CALC_OPERATION


async def choice_calc_operation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    type_numbers = mod_calc.get_type_number()
    operation = update.message.text
    mod_calc.set_operation(operation)
    count_numbers = mod_calc.get_count_numbers_in_operation()

    if update.message.text == 'adding':
        mod_log.add_log_calc(user.id, 'select operation adding')
    if update.message.text == 'subtraction':
        mod_log.add_log_calc(user.id, 'select operation subtraction')
    if update.message.text == 'multiplication':
        mod_log.add_log_calc(user.id, 'select operation multiplication')
    if update.message.text == 'division':
        mod_log.add_log_calc(user.id, 'select operation division')
        reply_keyboard = [[v] for v in ui.menu_operation_division]
        await update.message.reply_text(
            "Выберите операцию деления: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_CALC_OPERATION_DIVISION
    if update.message.text == 'back':
        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS

    if type_numbers == 'rational':
        if count_numbers > 1:
            await update.message.reply_text("Введите 1 число: ")
            return INPUT_RATIONAL_NUMBER
        else:
            await update.message.reply_text("Введите число: ")
            return INPUT_RATIONAL_NUMBER
    else:
        await update.message.reply_text("Введите 1 комплексное число вида (N<пробел>M): ")
        return INPUT_COMPLEX_NUMBER


async def choice_calc_operation_division(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    type_numbers = mod_calc.get_type_number()
    operation = update.message.text
    mod_calc.set_operation(operation)
    count_numbers = mod_calc.get_count_numbers_in_operation()

    if update.message.text == 'simple division':
        mod_log.add_log_calc(user.id, 'select operation simple division')
    if update.message.text == 'remainder of the division':
        mod_log.add_log_calc(user.id, 'select operation remainder of the division')
    if update.message.text == 'integer division':
        mod_log.add_log_calc(user.id, 'select operation integer division')
    if update.message.text == 'back':
        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS

    if type_numbers == 'rational':
        if count_numbers > 1:
            await update.message.reply_text("Введите 1 число: ")
            return INPUT_RATIONAL_NUMBER
        else:
            await update.message.reply_text("Введите число: ")
            return INPUT_RATIONAL_NUMBER
    else:
        await update.message.reply_text("Введите 1 комплексное число вида (N<пробел>M): ")
        return INPUT_COMPLEX_NUMBER


async def input_rational_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    type_number = mod_calc.get_type_number()
    numbers = mod_calc.get_numbers()

    count_input_numbers = len(numbers)

    operation = mod_calc.get_operation()

    number_str = update.message.text
    number = None
    if number_str.replace('-', '').isdigit():
        number = int(number_str)
    elif number_str.replace('-', '').replace('.', '').isdigit():
        number = float(number_str)
    else:
        mod_log.add_log_calc(user.id, f'input error value of number {count_input_numbers + 1}')
        await update.message.reply_text(f"input error value of number {count_input_numbers + 1}")
        return INPUT_RATIONAL_NUMBER

    mod_log.add_log_calc(user.id, f'set number {count_input_numbers + 1} value {number_str}')
    mod_calc.add_numbers(number)
    count_input_numbers += 1
    if count_input_numbers == mod_calc.count_numbers_in_operation:
        mod_log.add_log_calc(user.id, f'run operation {operation}')
        result = mod_calc.calc(type_number, operation)
        if result != None:
            mod_log.add_log_calc(user.id, f'result operation: {result}')
            await update.message.reply_text(f'Результат: {result}')
        else:
            await update.message.reply_text(f'Ошибка выполнения!')

        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS
    else:
        await update.message.reply_text(f"Введите {count_input_numbers + 1} число: ")
        return INPUT_RATIONAL_NUMBER


async def input_complex_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    type_number = mod_calc.get_type_number()
    numbers = mod_calc.get_numbers()

    count_input_numbers = len(numbers)

    operation = mod_calc.get_operation()

    number_arr = update.message.text.split(' ', 2)
    number_complex = None
    if len(number_arr)==2 and number_arr[0].replace('-', '').replace('.', '').isdigit() and number_arr[1].replace('-', '').replace('.', '').isdigit():
        number = complex(float(number_arr[0]), float(number_arr[1]))
    else:
        mod_log.add_log_calc(user.id, f'input error value of complex number {count_input_numbers + 1}')
        await update.message.reply_text(f"input error value of complex number {count_input_numbers + 1}")
        return INPUT_COMPLEX_NUMBER

    mod_log.add_log_calc(user.id, f'set complex number {count_input_numbers + 1} value {number}')
    mod_calc.add_numbers(number)
    count_input_numbers += 1
    if count_input_numbers == mod_calc.count_numbers_in_operation:
        mod_log.add_log_calc(user.id, f'run operation {operation}')
        result = mod_calc.calc(type_number, operation)
        if result != None:
            mod_log.add_log_calc(user.id, f'result operation: {result}')
            await update.message.reply_text(f'Результат: {result}')
        else:
            await update.message.reply_text(f'Ошибка выполнения!')

        reply_keyboard = [ui.menu_type_numbers]
        await update.message.reply_text(
            "Выберите тип чисел: ",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, input_field_placeholder="Ваш выбор?"
            ),
        )
        return CHOICE_TYPE_NUMBERS
    else:
        await update.message.reply_text(f"Введите {count_input_numbers + 1} комплексное число вида (N<пробел>M): ")
        return INPUT_COMPLEX_NUMBER


async def run_calc_operation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    type_number = mod_calc.get_type_number()

    operation = mod_calc.get_operation()
    mod_log.add_log_calc(user.id, f'run operation {operation}')
    result = mod_calc.calc(type_number, operation)
    if not isinstance(result, None):
        mod_log.add_log_calc(user.id, f'result operation: {result}')

    return CHOICE_CALC_OPERATION


async def close(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    await update.message.reply_text(
        f"Bye, {user.name}!", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


application = Application.builder().token(TELEGRAM_TOKEN_PY).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_menu)],
    states={
        START_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, start_menu)],
        CHOICE_START_MENU: [MessageHandler(filters.Regex(f"^({'|'.join(ui.main_menu)})$"), choice_start_menu)],
        CHOICE_TYPE_NUMBERS: [
            MessageHandler(filters.Regex(f"^({'|'.join(ui.menu_type_numbers)})$"), choice_type_numbers)],
        CHOICE_CALC_OPERATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, choice_calc_operation)],
        CHOICE_CALC_OPERATION_DIVISION: [MessageHandler(filters.TEXT & ~filters.COMMAND, choice_calc_operation_division)],
        INPUT_RATIONAL_NUMBER: [MessageHandler(filters.TEXT, input_rational_number)],
        INPUT_COMPLEX_NUMBER: [MessageHandler(filters.TEXT, input_complex_number)],
        RUN_CALC_OPERATION: [MessageHandler(~filters.COMMAND, run_calc_operation)],
        CLOSE: [MessageHandler(filters.COMMAND, close)],
    },
    fallbacks=[CommandHandler("close", close)],
)

application.add_handler(conv_handler)

application.run_polling()
