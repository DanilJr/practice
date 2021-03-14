def check_win(map):
    new_map = [['#', '#', '#'],
               ['#', '#', '#'],
               ['#', '#', '#']]
    for i in range(3):
        for j in range(3):
            new_map[i][j] = map[i][j].but['text']
    patterns = (['X', 'X', 'X'], ['O', 'O', 'O'])
    rows = [[], [], []]
    columns = [[], [], []]
    diagonals = [[], []]
    for row in range(3):
        rows[row] += new_map[row]
        diagonals[0] += new_map[row][row]
        diagonals[1] += new_map[row][2-row]
        columns[row] += [new_map[i][row] for i in range(3)]
    #print(rows, columns, diagonals, sep='\n')
    for pattern in patterns:
        if pattern in rows or pattern in columns or pattern in diagonals:
            return True
