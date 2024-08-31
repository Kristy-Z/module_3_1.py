calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    a = len(string), string.upper(), string.lower()
    count_calls()
    return a

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('cat', ['apple', 'door', 'glass'])) # No matches
print(is_contains('UrBAn', ['Urban', 'urBAN', 'URBAN', 'uRban'])) # Urban ~ urBAN

print(calls)
