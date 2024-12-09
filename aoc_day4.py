def find_words(matrix, words):
    found_words = 0

    # Check horizontal words
    for row in matrix:
        row_str = "".join(row)
        for word in words:
            if word in row_str:
                found_words += 1

    # Check diagonal words (top-left to bottom-right)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                diagonal_str = ""
                x, y = i, j
                while x < len(matrix) and y < len(matrix[0]):
                    diagonal_str += matrix[x][y]
                    x += 1
                    y += 1
                for word in words:
                    if word in diagonal_str:
                        found_words += 1

    # Check diagonal words (top-right to bottom-left)
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1, -1, -1):
            if i == 0 or j == len(matrix[0]) - 1:
                diagonal_str = ""
                x, y = i, j
                while x < len(matrix) and y >= 0:
                    diagonal_str += matrix[x][y]
                    x += 1
                    y -= 1
                for word in words:
                    if word in diagonal_str:
                        found_words += 1

    return found_words

def read_matrix_from_file(filename):
    """Reads a matrix of letters from a file."""
    with open(filename, "r") as f:
        matrix = [line.strip().split() for line in f]
    return matrix

matrix = read_matrix_from_file("input.txt")
words_to_find = ["XMAS", "SAMX"]
score = find_words(matrix, words_to_find)
print(score)

