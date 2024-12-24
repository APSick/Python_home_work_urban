def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (11, "stroka", False)
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = (111, "stroka2")

print_params()
print_params(3)
print_params("qwerty", 1 )
print_params(3, 3, 3)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)