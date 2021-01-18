source = input()
matrix = []
while source != 'end':
    matrix.append([int(i) for i in source.split()])
    source = input()
for i in range(len(matrix)): # кол-во строк
    for j in range(len(matrix[i])): # len(matrix[i]) - кол-во символов в строке (столбцов)
        print((matrix[i - 1][j]) +
              matrix[i - len(matrix) + 1][j] +
              matrix[i][j - 1] +
              matrix[i][j - len(matrix[i]) + 1], end=' ')
    print()