def show_data() -> None:
    """Выводит информацию из справочника"""
    pass

def add_data() -> None:
    """Добавляет информацию в справочник."""
    pass


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))

def search(book: list[str], info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return "Нет совпадений"
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('--------')
        print('\n'.join(result))
        new_info = input('Введите данные для уточнения: ')
        return search(result, new_info)
    return 'Нет совпадений'

def change() -> None:
    """Изменение/удаление данных в справочнике."""
    print('\n'.join(data))
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    mode = input('Удалить или измениит? 1- удалить, 2 - изменить')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_contact()

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data)

def enter_contact() -> str:
    fio = input('Ввдите ФИО: ')
    phone = input('Введите номер телефона: ')
    return f'{fio} | {phone}'