# def average(class_points, your_points):
#     answer = (sum(class_points))
#     answer2 = (answer/len(class_points))
#     if your_points < answer2:
#         print("Ты лох!")
#     elif your_points > answer2:
#         print("Заэбумба!")
#
# print(average([43, 56, 45, 66, 11], 32))

def arenda(dayz):
    return (40*7) if dayz >= 7 else (40*3), dayz < 7 or dayz > 3

print(arenda(7))