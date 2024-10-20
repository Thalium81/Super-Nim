from random import randint

#генерация поля:

grid = []

for y in range(8):
    row = []
    for x in range(8):
        if randint(0,1) == 0:
            row.append("O")
        else:
            row.append("-")
    grid.append(row)


#правила игры:

print("ПРАВИЛА ИГРЫ:")
print("На шахматной доске в некоторых клетках случайно разбросаны фишки или пуговицы. Игроки ходят по очереди.")
print("За один ход можно снять все фишки с какой-либо горизонтали или вертикали, на которой они есть.")
print("Выигрывает тот, кто заберет последние фишки.")

print("\nЧтобы высбрать строку или столбец, игрок должен сначала написать ось (x или y), а потом номер. Пример: \"x2\"")

print("\n \"-\" - клетка без фишки")
print("\"O\" - фишка")



#игра:

won = 0 #Сюда запишется номер победившего игрока.
player = 2 #Номер игрока, совершающего текуй ход.
while won == 0:

    #смена ходов:
    print("\n\n\n-------------------------------\n\n\n")
    if player == 2:
        player = 1
    else:
        player = 2
    print("  Сейчас ходит игрок",player)
        
    #Вывод поля:
    print("\n     1 2 3 4 5 6 7 8  x >")
    print()
    for i in range(8):
        print(i+1,"  ",*grid[i])
    print()
    print("y\nv")

    #Ввод и проверка вводимых данных на соответствие шаблону
    while True:
        select = input("\n\nВыберите строку или столбец: ")
        if select[0].lower() == "x" or select[0].lower() == "y":
            if select[1] in "12345678":
                if len(select) == 2:
                    break
        print("Неправильная форма ввода! Прочитайте правила!")

    #Убирание фишек:
        
    if select[0].lower() == "y":
        for i in range(8):
            grid[int(select[1])-1][i] = grid[int(select[1])-1][i].replace("O","-")
            
    if select[0].lower() == "x":
        for i in range(8):
            grid[i][int(select[1])-1] = grid[i][int(select[1])-1].replace("O","-")

    #Проверка на конец игры:
    won = player
            
    for i in grid:
        if "O" in i:
            won = 0


print("\n\n\n\nПОБЕДИЛ ИГРОК",won)
            

    

    


    
    
        
        
        
            
    
