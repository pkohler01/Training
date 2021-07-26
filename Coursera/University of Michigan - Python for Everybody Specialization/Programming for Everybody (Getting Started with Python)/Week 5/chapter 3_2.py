score = input("Enter Score: ")
sc = float(score)

if sc >= 0.9:
    grade = 'A'
elif sc >= 0.8:
    grade = 'B'
elif sc >= 0.7:
    grade = 'C'
elif sc >= 0.6:
    grade = 'D'
elif sc < 0.6:
    grade = 'F'
else:
    grade = 'Out of bounds'
print(grade)
