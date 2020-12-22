class Matrix:

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_chars = [row_string.split() for row_string in self.matrix_string.splitlines()]
        self.matrix_int = [[int(char) for char in self.matrix_chars[row]] for row in range(len(self.matrix_chars))]

    def row(self, index):
        return self.matrix_int[index - 1]

    def column(self, index):
        return [self.matrix_int[row][index - 1] for row in range(len(self.matrix_int))]
