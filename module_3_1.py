calls = 0

def count_calls():
    global calls
    calls += 1

count_calls()

string = 'capybara'
def string_info(string):
    a = len(string), string.upper(), string.lower()
    return a

count_calls()
print(string_info(string))

name = 'Armageddon'
list_to_search = [1, 2, 3]
def is_contains(name, list_to_search):
    b = len(name), name.upper(), name.lower()
    return b

count_calls()
print(is_contains(name, list_to_search))

print(isinstance(name, str))
print(isinstance(list_to_search, str))
count_calls()
print(calls)
