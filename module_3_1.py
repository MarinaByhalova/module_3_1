calls = 0
def count_calls():
    global calls
    calls += 1
#count_calls('Capybara')
def string_info (string):
    count_calls()
    return (len(string),string.upper(),string.lower())
    #print (string)
#print(string_info('Capybara'))
def is_contains (string,list_to_search):
    count_calls()
    list_to_search = [x.upper() for x in list_to_search]
    string = string.upper()
    if string in list_to_search:
        return False
    else:
        return True
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
