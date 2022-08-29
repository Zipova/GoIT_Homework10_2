from collections import UserDict
from repository.fields.name import Name
from repository.fields.phone import Phone
from decorators.error_handlers import input_error
from repository.record import Record

class AddressBook(UserDict):
    @input_error
    def add_record(self, command):
        name = Name(command[1])
        phone_number = Phone(command[2])
        if name.value in self.data.keys():
            rec = self.data[name.value]
            rec.add_phone(phone_number)
            return 'Done!'
        rec = Record(name, phone_number)
        self.data[rec.name.value] = rec

    def __repr__(self):
        title = '|{:^15}|{:^20}'.format('Name', 'Phone')
        result = title + '\n'
        for k, v in self.data.items():
            phones = ''
            for phone in v.phones:
                phones += str(phone) + ', '
            s = '|{:<15}|{:^20}'.format(k, phones[:-2])
            result += s + '\n' 
        return result
        