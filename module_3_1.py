calls = 0

def count_calls():
    global calls
    calls += 1

count_calls()

string = 'capybara'
def string_info(string):
    a = len(string), string.upper(), string.lower()
    print(a)

string_info(string)
count_calls()

string = 'armageddon'
list_to_search = [1, 2, 3]
def is_contains(string, list_to_search):
    b = len(string), string.upper(), string.lower()
    print(b)
    count_calls()

    print('armageddon' in string)
    print('armageddon' in list_to_search)

is_contains(string, list_to_search)
count_calls()
print(calls)
