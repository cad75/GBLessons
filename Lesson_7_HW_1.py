class Matrix:
    def __init__(self, all_titels):
        self.all_titels = all_titels

    def __str__(self):
        result = ''
        for i in self.all_titels:
            for el in i:
                result += str(el) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        result = []
        for i in range(len(self.all_titels)):
            result.append([])
            for j in range(len(self.all_titels[i])):
                result[i].append(self.all_titels[i][j] + other.all_titels[i][j])
        return Matrix(result)


first_matrix = Matrix([[1, 2, 7, 3], [5, 6, 9, 1]])
second_matrix = Matrix([[4, 2, 8, 4], [1, 5, 6, 2]])

print(first_matrix)
print(second_matrix)
print(f'Результат сложения')
print(first_matrix + second_matrix)

