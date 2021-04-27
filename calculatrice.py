def ask_user(sentence = "Saisir un chiffre"): # do_something, refactor name def
    choice = input(f"""{sentence}\n>""") #transform string on int
    return choice

def addition(number): # do_something, refactor name def
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à additionner ou clicker sur '=' ")
        result = sum(list_numbers) # do_something ajout de la fonction sum
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            print('Toto')
            list_numbers.append((int(number)) # do_something ajouter la methode int
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == '0': # do_something
            result = list_number
        else:
            result = result / list_number # do_something
    return result
multiplication('3')

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(number) # do_something
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        else:
            result = result + list_number # do_something
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit: # do_something
        if number.isdigit():
            list_numbers.append(number) # do_something
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result

def display_interface():
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = choice # do_something
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = multiplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = division(choice)
        return print(f"Le resultat est ==> {result}")


