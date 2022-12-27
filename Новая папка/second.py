try:
    with open('test.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())
except Exception:
    print("Ошибка")
