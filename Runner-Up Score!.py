if __name__ == '__main__':
    n = int(input('Enter a number: '))
    arr = map(int, input('enter a score: ').split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])
