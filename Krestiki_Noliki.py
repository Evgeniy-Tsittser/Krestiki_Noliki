
def chek_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area [0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[1][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[2][0] == '0' and area[1][1] == '0' and area[0][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    return '*'



def new_area():
    for i in area:
        print(*i)
    print()


area = [['*', '*', '*'], ['*', '*', '*'],['*', '*', '*']]
print('Добро пожаловать в крестики-нолики!')
print('-----------------------------------')
new_area()

for j in range(1, 10):
    print(f'Ход, {j}')
    if j % 2 == 0:
        j_char = '0'
        print('Ходят нолики ')
    else:
        j_char = 'X'
        print('Ходят крестики ')
    row = int(input('Введи номер строки (1,2,3): ')) - 1
    column = int(input('Введи номер столбца (1,2,3): ')) - 1
    if area[row][column] == '*':
        area[row][column] = j_char
    else:
        print('Ячейка уже занята, ты пропускаешь ход')
        new_area()
        continue
    new_area()

    if chek_winner() == 'X':
        print('Победили крестики!')
        break
    if chek_winner() == '0':
        print('Победили нолики!')
        break
    if chek_winner() == '*' and j == 9:
        print('Ничья!')
        break