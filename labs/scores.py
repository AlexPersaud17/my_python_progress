def main():
    grades = [90, 100, 70, 45, 76, 84, 93, 21, 36, 99, 100]
    grade_a = 0
    grade_b = 0
    grade_c = 0
    grade_d = 0
    grade_f = 0
    
    for g in grades:
        if g in range(90, 101):
            grade_a += 1
        elif g in range(80, 90):
            grade_b += 1
        elif g in range(70, 80):
            grade_c += 1
        elif g in range(55, 70):
            grade_d += 1
        else:
            grade_f += 1

    print("Number of A's:", grade_a)
    print("Number of B's:", grade_b)
    print("Number of C's:", grade_c)
    print("Number of D's:", grade_d)
    print("Number of F's:", grade_f)

    if grade_a + grade_b > grade_c + grade_d + grade_f:
        print("This is a good class.")
    else:
        print("This class needs work.")

    

main()
