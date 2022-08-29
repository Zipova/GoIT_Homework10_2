from repository.address_book import AddressBook
from decorators.error_handlers import input_error

def main():
    phone_book = AddressBook()
    print("Hello! I am Your Phone Book! You can add Your friends' contacts and birthday or load your Phone Book from file. Let's start!")
    while True:
        user_command = input('>>>')
        if user_command.lower() == 'hello':
            print(greeting())
        elif user_command.lower() in (".", "good bye", "close", "exit"):
            print(good_buy())
            break
        elif user_command.lower() == 'show all':
            print(show_all(phone_book))
        else:
            command = user_command.split(' ')
            if command[0].lower() == 'add':
                print(add(command, phone_book))
            elif command[0].lower() == 'change':
                print(change(command, phone_book))
            elif command[0].lower() == 'phone':
                print(phone(command, phone_book))
            elif command[0].lower() == 'delate':
                print(delate(command, phone_book))
            else:
                print('Unknown command.')


def greeting():
    return 'How can I help you?'

def good_buy():
    return 'Good buy!'

def show_all(phone_book):
    return phone_book
    
@input_error
def add(command, phone_book): 
    if len(command) != 3:
        raise IndexError()
    phone_book.add_record(command)
    return 'Done!'

@input_error
def change(command, phone_book):
    if len(command) != 4:
        raise IndexError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    phone_book[command[1]].edit_phone(command[2], command[3])
    return 'Done!'

@input_error
def delate(command, phone_book):
    if len(command) != 3:
        raise IndexError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    return phone_book[command[1]].del_phone(command[2])
    

@input_error
def phone(command, phone_book):
    if len(command) != 2:
        raise KeyError()
    if command[1] not in phone_book.keys():
        raise KeyError()
    all_phones = ''
    for p in phone_book[command[1]].phones:
            all_phones += str(p.value) + ', ' 
    return (all_phones[:-2])


if __name__ == "__main__":
    main()