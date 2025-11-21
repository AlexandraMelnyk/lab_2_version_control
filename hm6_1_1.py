from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit string.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if any(str(p) == phone for p in self.phones):
            raise ValueError("This phone number already exists.")
        self.phones.append(new_phone)

    def delete_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                validated_phone = Phone(new_phone)  # валідація нового номера
                p.value = validated_phone.value
                return
        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        raise ValueError("Phone number not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found.")

    def find_record(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise KeyError("Contact not found.")


if __name__ == "__main__":
    book = AddressBook()

    # Створення запису John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Створення запису Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх контактів
    for name, record in book.data.items():
        print(record)

    # Редагування телефону John
    john = book.find_record("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    # Пошук телефону
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Видалення запису Jane
    book.delete_record("Jane")