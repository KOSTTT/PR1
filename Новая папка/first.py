try:
    true: bool = True
    while true:
            print('Введите: ID, last_name, first_name, middle_name, age:')
            ID, last_name, first_name, middle_name, age = map(str, input().split())
            if ID.isdigit() != true:
                if first_name.isdigit() != true:
                    if last_name.isdigit() != true:
                        if (middle_name.isdigit() != true) or (middle_name == '-'):
                            if (age.isdigit() != true):
                                with open('test.txt', 'a') as file:
                                   file.write(f'\n{ID}'f'  {last_name}'f'   {first_name}'f'   {middle_name}'f'   {age}')
                                print('Данные записаны')
                            else:
                                 print("Неверный ввод года рождения")
                        else:
                             print("Неверный ввод")
except ValueError:
    print("Неверный ввод данных")
except Exception:
    print("Ошибка")
