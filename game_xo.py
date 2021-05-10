def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show():
    # Функция, которая выводит на экран игровое поле.
    print("---------------- ")
    print(f" 2 | {field[2][0]} | {field[2][1]} | {field[2][2]} |")
    print("---------------- ")
    print(f" 1 | {field[1][0]} | {field[1][1]} | {field[1][2]} |")
    print("---------------- ")
    print(f" 0 | {field[0][0]} | {field[0][1]} | {field[0][2]} |")
    print("---------------- ")
    print("   | 0 | 1 | 2 | ")
    print()

def ask():
    # Функция запрашивает координаты и проверяет правильность ввода.
    while True:
        cords = input("         Ваш ход: ").split() # разделяем строку ввода на 2 значения
        
        if len(cords) != 2:   # проверяем, чтобы было 2 координаты
            print(" Введите 2 координаты через пробел! ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()): # проверяем, чтобы координаты были числами
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 : # проверяем, чтобы координаты были 0, 1 или 2
            print(" Координаты вне диапазона! ")
            continue
        
        if field[x][y] != " ":     # проверяем, чтобы клетка была свободной
            print(" Клетка занята! ")
            continue
        
        return x, y
            
def check_win():
    # Функция проверяет выйгрышные комбинации.
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл 0!!!")
            return True
        
    return False

greet()
field = [[" "] * 3 for i in range(3) ] # Создаём поле, как список списков из 3 -х элементов
count = 0   # Объявляем счётчик, чтобы определять чей ход и какое значение присваивать полю
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    x, y = ask()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Ничья!")
        break