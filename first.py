try:
    true: bool = True
    while true:
        print('Введите "+" для добавления данных и "-" для завершения')
        check: str = input()
        if check == '-':
            print("Ну и вали!")
            raise SystemExit
        elif check == '+':
            print('Введите фамилию, имя, отчество и год рождения:')
            surname, name, patronymic, year = map(str, input().split())
            if name.isdigit() != true:
                if surname.isdigit() != true:
                    if (patronymic.isdigit() != true) or (patronymic == '-'):
                        if (year.isdigit() == true) and (len(year) == 4):
                            with open('test.txt', 'a') as file:
                                file.write(f'\n{surname}'f'   {name}'f'   {patronymic}'f'   {year}')
                            print('Данные записаны')
                        else:
                            print("Неверный ввод года рождения")
                    else:
                        print("Неверный ввод")
except ValueError:
    print("Неверный ввод данных")
except PermissionError:
    print("Не хватает прав доступа")
except Exception:
    print("Ошибка")
except KeyboardInterrupt:
    print("Ошибка")
