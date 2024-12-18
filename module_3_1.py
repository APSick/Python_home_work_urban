calls = 0

def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    halv = len(string)
    verh = string
    count_calls()
    return halv, verh.upper(),  string

def is_contains(string, list_to_search):
    for i in list_to_search:
        name = i.lower()
        string = string.lower()
        if string == name:
            exam = True
            break
        else:
            exam = False
    count_calls()
    return exam


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)