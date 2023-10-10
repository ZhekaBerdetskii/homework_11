from collections import UserDict
from datetime import datetime, date
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Phone(Field):
    __phones = []

    @property
    def phone(self):
        return self.__phones

    @phone.setter
    def phone(self, phone):
        if len(phone.value) == 10:
            self.__phones.append(phone)
        else:
            raise ValueError('Please enter correct phone')

    def add_phone(self, phone_number):
        if phone_number not in self.__phones:
            self.__phones.append(phone_number)

    def remove_phone(self, phone_number):
        self.__phones.remove(phone_number)

    def edit_phone(self, old_phone, new_phone):
        index = self.__phones.index(old_phone)
        self.__phones[index] = new_phone


class Name(Field):
    pass


class Birthday:
    def __init__(self, birthday):
        self.__birthday = None

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        y, m, d = tuple(birthday.split('-'))
        if 1900 < int(y) <= datetime.now().date().year and 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
            self.__birthday = birthday
        else:
            raise ValueError('Please enter correct birthday')


class Record:
    def __init__(self, name: Name, phone: Phone, birthday='1970-01-01'):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f'name: {self.name}, phone: {self.phone}, birthday: {self.birthday}'

    def days_to_birthday(self):
        y, m, d = tuple(self.birthday.split('-'))
        now = datetime.now().date()
        if self.birthday == '1970-01-01':
            return 'Please enter birthday'
        elif int(m) < now.month or int(m) == now.month and int(d) < now.day:
            y = datetime.now().year + 1
        else:
            y = datetime.now().year
        return (date(year=int(y), month=int(m), day=int(d)) - now).days


class AddressBook(UserDict):
    MAX_VALUE = 2

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __next__(self):
        self.current_value = 0
        if self.current_value <= self.MAX_VALUE:
            self.current_value += 1
            return self.data.values()
        raise StopIteration

    def __iter__(self):
        return self












