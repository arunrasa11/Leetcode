# import numpy
#
#
# def solution(matrix):
#     sum = 0
#     a = numpy.array(matrix)
#     x, y = numpy.shape(a)
#
#     for i in range(y):
#         for j in range(x):
#             if matrix[j][i] == 0:
#                 break
#             sum = sum + matrix[j][i]
#
#     return sum


def solution(matrix):
    sum = 0
    x = len(matrix)
    y = len(matrix[0])

    for i in range(y):
        for j in range(x):
            if matrix[j][i] == 0:
                break
            sum = sum + matrix[j][i]

    return sum

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
print(solution(matrix))