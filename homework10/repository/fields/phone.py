from repository.fields.field import Field

class Phone(Field):
    def __str__(self):
        return f'{self.value}'