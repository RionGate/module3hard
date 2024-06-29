def unbox_ins(*args):
    unbox = []
    if isinstance(*args, list) or isinstance(*args, tuple) or isinstance(*args, set) or isinstance(*args, dict):
        return sum(map(unbox_ins, *args), unbox)
    else:
        return [*args]

def unbox_exs(*args):
    unbox = []
    if isinstance(*args, list) or isinstance(*args, tuple) or isinstance(*args, set):
        return sum(map(unbox_exs, *args), unbox)
    else:
        return [*args]

def summar(x):
    num = 0
    strings = 0
    for i in range(len(x)):
        if type(x[i]) == type(1):
            num = num + x[i]
        else:
            strings = strings + len(x[i])
    return num + strings

def dict_unbox(my_dict1):
    dict_1 = []
    for i in range(len(my_dict1)):
        if isinstance(my_dict1[i], dict):
            dict_1.append(my_dict1[i])
    dict_2 = []
    for i in range(len(dict_1)):
        dict_2.append(sum(dict_1[i].values()))
    a = sum(dict_2)
    return a

def all_sum(data_sructure):
    result1 = unbox_ins(data_structure)
    result2 = (summar(result1))
    result3 = unbox_exs(data_structure)
    result = dict_unbox(result3)
    print(result2 + result)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

all_sum(data_structure)