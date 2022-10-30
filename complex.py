import model_sum as complex_sum
import model_sub as complex_sub
import model_mult as complex_mult
import model_div as complex_div
import model_pow as complex_pow
import model_sqrt as complex_sqrt


def calc(operator, args):
    if operator == 'adding':
        return complex_sum.sum(args[0], args[1])
    elif operator == 'subtraction':
        return complex_sub.sub(args[0], args[1])
    elif operator == 'multiplication':
        return complex_mult.mult(args[0], args[1])
    elif operator == 'simple division':
        return complex_div.div(args[0], args[1])
    elif operator == 'degree':
        return complex_pow.pow(args[0], args[1])
    else:
        return None