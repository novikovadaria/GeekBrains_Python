print("Добро пожаловать!")
while True:
    print("Выберите действие:\n"
          "Сложение: +\n"
          "Вычетание: -\n"
          "Умножение: *\n"
          "Деление: /\n"
          "Для выхода нажмите: q\n")
    action = input("")
    if action == "q":
        print("Выход из программы")
        break
    if action in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if action == '+':
            print('%.2f + %.2f = %.2f' % (x, y, x+y))
        elif action == '-':
            print('%.2f - %.2f = %.2f' % (x, y, x-y))
        elif action == '*':
            print('%.2f * %.2f = %.2f' % (x, y, x*y))
        elif action == '/':
            if y != 0:
                print('%.2f / %.2f = %.2f' % (x, y, x/y))
            else:
                print("Ошибка!")
