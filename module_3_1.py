calls = 0

def count_calls():
    global calls
    calls += 1

count_calls()

string = 'capybara'
def string_info(string):
    global calls
    calls += 1
    print(len(string), string.upper(), string.lower())

string_info(string)

string = 'armageddon'
list_to_search = [1, 2, 3]
def is_contains():
    global calls
    calls += 1
    print(len(string), string.upper(), string.lower())
    calls += 1
    print('armageddon' in string)
    print('armageddon' in list_to_search)
    print(calls)

is_contains()