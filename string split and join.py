

def split_and_join(line):
    # write your code here
    words=line.split()
    return "-".join(words)

if __name__ == '__main__':
    line = input('Enter a string: ')
    result = split_and_join(line)
    print(result)
