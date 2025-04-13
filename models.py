from typing import Union, Optional

from pydantic import BaseModel, field_validator, Field, EmailStr
import re



class BookModel(BaseModel):
    id: int = Field(..., description="ID книги")
    title: str  = Field(..., description="Назва книги")
    author: str = Field(..., description="Автор книги")
    year: int = Field(..., description="Рік видання")
    available_copies: int = Field(..., description="Доступна кількість")



    @field_validator("id")
    def check_id(cls, id):
        if 0 < id < 100:
            return id
        raise ValueError("ID повинен бути у діапазоні від 0 до 100 ☹️")

    @field_validator("title")
    def check_title(cls, title):
        if len(title) > 3:
            return title.upper()
        raise ValueError("Назва книги повинна бути довшим за 3 символи ☹️")
    
    @field_validator("author")
    def check_author(cls, author):
        if len(author) > 3:
            return author.title()
        raise ValueError("Автор книги повинен бути довшим за 3 символи ☹️")
    
    @field_validator("year")
    def check_year(cls, year):
        if 1900 < year < 2026:
            return year
        raise ValueError("Рік видання повинен бути у діапазоні від 1900 до 2025 ☹️")
    
    @field_validator("available_copies")
    def check_available_copies(cls, available_copies):
        if -1 < available_copies < 6:
            return available_copies
        raise ValueError("Кількість доступних копій повинна бути у діапазоні від 0 до 6 ☹️")
    
class BookModelResponse(BaseModel):
    id: int = Field(..., description="ID книги")
    title: str  = Field(..., description="Назва книги")
    author: str = Field(..., description="Автор книги")
    year: int = Field(..., description="Рік видання")
    available_copies: int = Field(..., description="Доступна кількість")


class UserModel(BaseModel):
    user_id: int = Field(..., description="ID користувача")
    first_name: str = Field(..., description="Ім'я користувача")
    last_name: str = Field(..., description="Прізвище користувача")
    email: EmailStr = Field(..., description="Електронна пошта користувача")
    password: str = Field(..., description="Пароль користувача")
    phone_number: str = Field(..., description="Номер телефону користувача")


    @field_validator("user_id")
    def check_user_id(cls, user_id):
        if 0 < user_id < 100:
            return user_id
        raise ValueError("ID повинен бути у діапазоні від 0 до 100 ☹️")

    @field_validator("first_name")
    def validate_first_name(cls, first_name):
        if first_name.isalpha() and len(first_name) >= 2:
            return first_name.title()
        raise ValueError("Ім'я повинно містити мінімум 2 символи і складатися лише з літер ☹️")

    @field_validator("last_name")
    def validate_last_name(cls, last_name):
        if last_name.isalpha() and len(last_name) >= 2:
            return last_name.title()
        raise ValueError("Прізвище повинно містити мінімум 2 символи і складатися лише з літер ☹️")

    @field_validator("password")
    def validate_password(cls, password):
        if (len(password) >= 8 and 
            re.search(r'[A-Z]', password) and 
            re.search(r'[a-z]', password) and 
            re.search(r'\d', password) and 
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            return password
        raise ValueError("Пароль повинен містити мінімум 8 символів, одну велику літеру, одну маленьку літеру, одну цифру та один спеціальний символ ☹️")

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number):
        if re.fullmatch(r'\+?[\d\s\-()]{10,15}', phone_number):
            return phone_number
        raise ValueError("Номер телефону повинен відповідати патерну мобільного телефону ☹️")
    


class UserModelResponse(BaseModel):
    user_id: int = Field(..., description="ID користувача")
    first_name: str = Field(..., description="Ім'я користувача")
    last_name: str = Field(..., description="Прізвище користувача")
    email: EmailStr = Field(..., description="Електронна пошта користувача")
    password: str = Field(..., description="Пароль користувача")
    phone_number: str = Field(..., description="Номер телефону користувача")
