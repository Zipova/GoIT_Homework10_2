from repository.fields.phone import Phone
from decorators.error_handlers import input_error

class Record:
    def __init__(self, name, phone = None) -> None:
        self.name = name
        self.phones = []
        self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)
        return 'Done!'

    def del_phone(self, phone):
        phone_number = Phone(phone)
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p) 
                return 'Done!'
        return "This phone doesn't exist in this contact."

    @input_error
    def edit_phone (self, phone, phone_2):
        for p in self.phones:
            if p.value == phone:
                p.value = phone_2
                print(p.value)
                return 'Done!'
        return "This phone doesn't exist in this contact."
