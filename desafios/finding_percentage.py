from functools import reduce
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    acc = reduce((lambda value,acc:value+acc), student_marks[query_name])
    percentage = acc/len(student_marks[query_name])
    print("{:.2f}".format(percentage))
    
