import sys

def show_size(var, total = 0):
    # print(sys.getsizeof(var), type(var))
    total += sys.getsizeof(var)
    if hasattr(var, '__iter__') and not isinstance(var, str):
        if not isinstance(var, dict):
            for i in var:
                total += show_size(i)
        else:
            for i in var:
                total += show_size(var[i])
    return total 

def mem_calc(obj):

    totalmem = 0

    for current_obj in obj:
        if current_obj.startswith('__'):
            continue
        elif hasattr(obj[current_obj], '__call__'):
            continue
        elif hasattr(obj[current_obj], '__loader__'):
            continue
        else:
            totalmem += show_size(obj[current_obj])
            print(current_obj, f'Variable type is {type(obj[current_obj])}, uses {show_size(obj[current_obj])} bytes of memory')

    return totalmem



