if __name__ == '__main__':
    n = int(input('Enter a number: '))
    student_marks = {}
    for _ in range(n):
        name, *line = input('enter a name').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('enter your value')
    l1 = list(student_marks[query_name])
    addition = sum(l1)
    result = addition/len(l1)
    print('%.2f'% result)
