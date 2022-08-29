def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This name do not exist in your phone book!'
        except ValueError:
            return 'Please enter a phone number.'
        except IndexError:
            return 'Give me name and phone please.'
    return inner