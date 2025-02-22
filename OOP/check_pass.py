import re
import string
     
class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(password) < 12:
            raise ValueError("Пароль должен быть длиннее 4 и меньше 12 символов")
        if not self.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not self.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра') 
        if not self.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
     
        self.__password = password
        
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if not isinstance(login, str):
            raise TypeError('Логин должен быть строкой')
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', login):
            raise ValueError('Некорректный логин')
        self.__login = login

    @staticmethod
    def is_include_digit(password):
        return any(char.isdigit() for char in password)

    @staticmethod
    def is_include_all_register(password):
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)

        return has_upper and has_lower

    @staticmethod
    def is_include_only_latin(password):
        return all(char in string.ascii_letters + string.digits for char in password)

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt', 'r') as file:
            for line in file:
                if password == line.strip():
                    return True
        return False
  