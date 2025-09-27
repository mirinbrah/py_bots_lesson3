def dog_speaks():
    """Собака просто лает."""
    print("Гав!")

def cat_speaks():
    """Кошка просто мяукает."""
    print("Мяу!")

# Вызываем их
# print("Обычные звуки:")
# dog_speaks()
# cat_speaks()

# def dog_speaks_with_logging():
#     print("Начинается запись...")
#     print("Гав!")
#     print("Запись окончена.")
#
# def cat_speaks_with_logging():
#     print("Начинается запись...")
#     print("Мяу!")
#     print("Запись окончена.")

def add_logging(animal_function):
    def wrapper():
        print("Начинается запись...")
        animal_function()
        print("Запись окончена.")
    return wrapper

variable_for_cat_speaks = add_logging(cat_speaks)

variable_for_cat_speaks()

# add_logging(cat_speaks)()

logged_dog_speaks = add_logging(dog_speaks)

logged_dog_speaks()

# add_logging(dog_speaks)()

@add_logging
def cat_speaks():
    print("Мяу!")

def add_logging(animal_function):
    def wrapper():
        print("Начинается запись...")
        animal_function()
        print("Запись окончена.")
    return wrapper

@add_logging
def dog_speaks():
    print("Гав!")

@add_logging
def cat_speaks():
    print("Мяу!")

dog_speaks()

# add_logging (Декоратор-Обёртка)

# @router.message (Декоратор-Регистратор)