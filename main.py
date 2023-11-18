def print_matrix(matrix):
    for row in matrix:
        print("|". join(row))
        print("-"* 9)
def check_winner(matrix,player):
    for i in range(3):
        if all(matrix[i][j] == player for j in range(3)) or all(matrix[j][i] == player for j in range(3)):
            return True

    if all(matrix[i][i] == player for i in range(3)) or all(matrix[i][2 - i] == player for j in range(3)):
        return True

    return False
def is_matrix_full(matrix):
    return all(matrix[i][j] != ' ' for i in range(3) for j in range(3))

def play():
    matrix =[[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_matrix(matrix)
        row = int(input("введите номер строки (0, 1, 2): " ))
        col = int(input("введите номер столбца (0, 1, 2): "))

        if matrix[row][col] == ' ': matrix[row][col] = current_player
        if check_winner(matrix, current_player):
                print_matrix(matrix)
                print(f"игрок {current_player}  победил!")
                break

        elif is_matrix_full(matrix):
            print_matrix(matrix)
            print("ничья!")
            break

        current_player = '0' if current_player == 'X' else 'X'
    else:
        print("эта клетка занята, попробуйтееще раз")

if __name__ == "__main__" :
    play()



