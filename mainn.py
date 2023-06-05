import functions as func

while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. изменить')
    mode = int(input())
    if mode == 1:
        func.show_data()
    elif mode == 2:
        func.add_data()
    elif mode == 3:
        func.find_data()
    elif mode == 4:
        func.change()
    else:
        break
