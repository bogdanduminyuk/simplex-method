# coding: utf-8


def get_col(matrix, index):
    return [matrix[i][index] for i in range(len(matrix))]


def get_bj(matrix):
    return [max(get_col(matrix, i)) for i in range(len(matrix[0]))]


def get_ai(matrix):
    return [min(matrix[i]) for i in range(len(matrix))]


if __name__ == "__main__":
    matrix = [
        [46, 22, 39, 27],
        [10, 34, 39, 27],
        [55, 31, 48, 24],
        [19, 43, 12, 36],
    ]

    Ai = get_ai(matrix)
    Bj = get_bj(matrix)
    alpha = max(Ai)
    betha = min(Bj)
    
    print("Your matrix is:")

    for i in range(len(matrix)):
        print(matrix[i])
    
    print()
    print("Ai:", Ai)
    print("Bj:", Bj)
    print()
    print("Alpha:", alpha)
    print("Betha:", betha)
    print()
    print("Clear strategies") if alpha == betha else print("Mixed strategies")
