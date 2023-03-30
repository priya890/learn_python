

def identify_even_odd(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


def factorial(number):
    facto = 1
    while number > 0:
        facto = facto * number
        number = number - 1
    print(f"Factorial is  : {facto}")


def find_vowels(sample_string):
    for character in sample_string:
        if character in ['a', 'e', 'i', 'o', 'u']:
            print(character)


def find_item(list_items, search_item):
    for i in range(len(list_items)):
        if list_items[i] == search_item:
            print(f"Found the item {search_item}")


identify_even_odd(20)
factorial(5)
find_vowels("presto")
find_item(['apple', 'mango', 'kiwi', 'grapes'], 'kiwi')
