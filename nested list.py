if __name__ == '__main__':
    alist=[]
    for _ in range(int(input('Enter number of'))):
        name = input('Enter name: ')
        score = float(input('Enter score: '))
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))
