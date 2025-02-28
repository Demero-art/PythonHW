import math
def square (side_square):
    return math.ceil(side_square * side_square)
sum_square = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(sum_square)}")