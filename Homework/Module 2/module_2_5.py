def get_matrix(n, m, value):
    matrix = []
    for i in list(range(n)):
        matrix.append([])
        for j in list(range(m)):
            matrix[i].append(value)
    return matrix
