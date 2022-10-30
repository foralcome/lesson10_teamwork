main_menu = ["run calc", "close"]

menu_type_numbers = ["rational", "complex", "back"]

menu_operation_rational = ['adding', 'subtraction', 'multiplication', 'division', 'degree',
                           'sqrt', "back"]

menu_operation_complex = ['adding', 'subtraction', 'multiplication', 'division', "back"]

menu_operation_division = ['simple division', 'remainder of the division', 'integer division']


def get_message_table(size, data):
    mes = ''
    for row in range(size):
        # mes += '| '
        for col in range(size):
            mes += f'{data[row * size + col]}  '
            if col == size - 1:
                mes += '\n'
    return mes
