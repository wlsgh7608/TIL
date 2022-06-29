# 성적이 낮은 순서로 학생 출력

N = int(input())

grades = []
for _ in range(N):
    name, grade = input().split()
    grade = int(grade)
    grades.append((grade,name))

grades.sort()
for _ , n in grades:
    print(n,end = " ")