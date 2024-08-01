def get_matrix(n, m,value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for i in range(m):
                list_.append(value)

    print(matrix)

get_matrix(5,4,10)
get_matrix(6,5,7)
get_matrix(1,3,4)