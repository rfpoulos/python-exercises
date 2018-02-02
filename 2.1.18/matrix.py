def matrix_mulp(a):
    new_matrix = []
    for i in range(len(a[0])):
            new_matrix.append(a[0][i] + a[1][i])
    return new_matrix

print matrix_mulp([[1, 2, 3], [1, 2, 3]])