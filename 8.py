def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt("example.txt")
    while choice != 7:
        if choice == 1:
            print(phone_book)
        elif choice == 2:
            lastname = input("Введите Фамилию ")
            print(find_by_lastname(phone_book, lastname))
        elif choice == 3:
            lastname = input("Введите Фамилию ")
            new_number = input("Введите новый номер ")
            print(change_number(phone_book, lastname, new_number))
        elif choice == 4:
            lastname = input("Введите Фамилию ")
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input("Введите номер ")
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input(
                "Введите Фамилию, имя, телефон и профессию через запятую "
            )
            add_user(phone_book, user_data)
            write_txt("example.txt", phone_book)
        choice = show_menu()


def show_menu():
    print(
        "\nВыберите дейтвие:\n"
        "1. Посмотреть справочник\n"
        "2. Поиск по фамилии\n"
        "3. Изменить телефон\n"
        "4. Удалить по фамилии\n"
        "5. Поиск по номеру\n"
        "6. Добавить"
    )
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Профессия"]
    with open(filename) as phb:
        for line in phb:
            record = dict(zip(fields, line.split(", ")))
            record["Профессия"] = record["Профессия"].rstrip()
            phone_book.append(record)
        return phone_book


def find_by_lastname(phone_book, lastname):
    for item in phone_book:
        if lastname == item["Фамилия"]:
            return item


def change_number(phone_book, lastname, new_number):
    for item in phone_book:
        if lastname == item["Фамилия"]:
            item["Телефон"] = new_number
            return item


def delete_by_lastname(phone_book, lastname):
    for item in phone_book:
        if lastname == item["Фамилия"]:
            del item
            return phone_book


def find_by_number(phone_book, number):
    for item in phone_book:
        if number == item["Телефон"]:
            return item


def add_user(phone_book, user_data):
    fields = ["Фамилия", "Имя", "Телефон", "Профессия"]
    record = dict(zip(fields, user_data.split(",")))
    phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s = s + v + ", "
            phout.write(f"{s[:-1]}\n")


work_with_phonebook()
