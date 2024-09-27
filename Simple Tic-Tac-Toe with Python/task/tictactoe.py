# write your code here
x = []
char = ['X','O']
x_or_o = set()
start_game = True
start_grid_game = True
winner = []
def input_checker(user_input):
    if len(user_input) != 9:
        return True
    return False
def grid_slicer(slicer):
    container = []
    for i in range(0,len(slicer),3):
        container.append(list(map(lambda k: k, slicer[i:i+3])))
    return container
def grid_to_str(grid):
    k = [''.join(p) for p in x]
    return ''.join(k)
# write your code here
def store_x_o(c):
    set_container = set(c)
    if len(set_container) == 1:
        x_or_o.add(str(set_container))
        return True
    return False
def left_diagonal():
    left_diagonal_row = [x[0][2],x[1][1],x[2][0]]
    if left_diagonal_row.count(x[0][2]) == 3 and (x[0][2] in char):
        winner.append(x[0][2])
        return True
    return False
def right_diagonal():
    right_diagonal_row = [x[0][0],x[1][1],x[2][2]]
    if right_diagonal_row.count(x[0][0]) == 3 and (x[0][0] in char):
        winner.append(x[0][0])
        return True
    return False
def upper_row():
    up_row = [x[0][0],x[0][1],x[0][2]]
    if up_row.count(x[0][0]) == 3 and (x[0][0] in char):
        winner.append(x[0][0])
        return True
    return False
def lower_row():
    low_row = [x[2][0],x[2][1],x[2][2]]
    if low_row.count(x[2][0]) == 3 and (x[2][0] in char):
        winner.append(x[2][0])
        return True
    return False
def middle_row():
    mid_row = [x[1][0],x[1][1],x[1][2]]
    if mid_row.count(x[1][0]) == 3 and (x[1][0] in char):
        winner.append(x[1][0])
        return True
    return False
def left_col():
    left_col_row = [x[0][0],x[1][0],x[2][0]]
    if left_col_row.count(x[0][0]) == 3 and (x[0][0] in char):
        winner.append(x[0][0])
        return True
    return False
def right_col():
    right_col_row = [x[0][2],x[1][2],x[2][2]]
    if right_col_row.count(x[0][2]) == 3 and (x[0][2] in char):
        winner.append(x[0][2])
        return True
    return False
def first_col():
    f_col = [x[0][0],x[1][0],x[2][0]]
    if f_col.count(x[0][0]) == 3 and (x[0][0] in char):
        winner.append(x[0][0])
        return True
    return False
def second_col():
    s_col = [x[0][1],x[1][1],x[2][1]]
    if s_col.count(x[0][1]) == 3 and (x[0][1] in char):
        winner.append(x[0][1])
        return True
    return False
def third_col():
    th_col = [x[0][2],x[1][2],x[2][2]]
    if th_col.count(x[0][2]) == 3 and (x[0][2] in char):
        winner.append(x[0][2])
        return True
    return False
def game_state():
    r_diagonal = right_diagonal()
    l_diagonal = left_diagonal()
    up_row = upper_row()
    l_row = lower_row()
    m_row = middle_row()
    l_col = left_col()
    r_col = right_col()
    f_col = first_col()
    s_col = second_col()
    th_col = third_col()
    if r_diagonal or l_diagonal or up_row or l_row or m_row or l_col or r_col or f_col or s_col or th_col:
        return True
    return False
def game_checker(user_input):
    global start_game, start_grid_game
    count_X = user_input.count('X')
    count_O = user_input.count('O')
    difference_x_o = abs(count_X - count_O)
    if game_state():
        start_game = False
        start_grid_game = False
        print(f'{winner[0]} wins')
    elif '_' not in user_input:
        start_game = False
        start_grid_game = False
        print('Draw')
def grid(grid_input):
    global x
    x = grid_slicer(grid_input)
    print('---------')
    for i in x:
        print('| ', end='')
        print(' '.join(i), end='')
        print(' |', end='')
        print()
    print('---------')
def coordinates_checker(c):
    num = c.split()
    if (len(num) > 2 or len(num) < 2):
        print('You should enter numbers!')
        return True
    elif not num[0].isdigit() and not num[1].isdigit():
        print('You should enter numbers!')
        return True
    elif (int(num[0]) > 3 or int(num[0]) < 1) or (int(num[1]) > 3 or int(num[1]) < 1):
        print('Coordinates should be from 1 to 3!')
        return True
    elif x[int(num[0])-1][int(num[1])-1] != '_':
        print('This cell is occupied! Choose another one!')
        return True
def play_move(c, char):
    global x
    num1,num2 = c.split()
    x[int(num1)-1][int(num2)-1] = char
def play_X_O():
    global start_game, start_grid_game
    while start_game:
        
        grid('_________')
        index = 0
        while start_grid_game:
            coordinates = input()

            if coordinates_checker(coordinates):
                continue
            else:
                play_move(coordinates,char[index])
                grid(grid_to_str(x)) # print grid
                game_checker(grid_to_str(x))
                if index == 0:
                    index = 1
                else:
                    index = 0
        #game_checker(user_input)
play_X_O()