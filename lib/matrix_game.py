# coding: utf-8


def get_bj(matrix):
    def get_max_col(matrix, index):
        col = []

        for i in range(len(matrix)):
            col.append(matrix[i][index])

        return max(col)
    
    bj = []

    for i in range(len(matrix[0])):
        bj.append(get_max_col(matrix, i))

    return bj

def get_ai(matrix):
    ai = []

    for i in range(len(matrix)):
        ai.append(min(matrix[i]))

    return ai

def get_alpha(ai):
    return max(ai)

def get_betha(bj):
    return min(bj);


if __name__ == "__main__":
    matrix = [
        [46, 22, 39, 27],
        [10, 34, 39, 27],
        [55, 31, 48, 24],
        [19, 43, 12, 36],
    ]

    Ai = get_ai(matrix)
    Bj = get_bj(matrix)
    alpha = get_alpha(Ai)
    betha = get_betha(Bj)
    
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
