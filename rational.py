import model_sum as rational_sum
import model_sub as rational_sub
import model_mult as rational_mult
import model_div as rational_div
import model_pow as rational_pow
import model_sqrt as rational_sqrt


def calc(operator, args):
    if operator == 'adding':
        return rational_sum.sum(args[0], args[1])
    elif operator == 'subtraction':
        return rational_sub.sub(args[0], args[1])
    elif operator == 'multiplication':
        return rational_mult.mult(args[0], args[1])
    elif operator == 'simple division':
        return rational_div.div(args[0], args[1])
    elif operator == 'integer division':
        return rational_div.div(args[0], args[1])
    elif operator == 'remainder of the division':
        return rational_div.rem_div(args[0], args[1])
    elif operator == 'degree':
        return rational_pow.pow(args[0], args[1])
    elif operator == 'sqrt':
        return rational_sqrt.sqrt(args[0])
    else:
        return None