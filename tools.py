from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))
        print(word1)
        i = i + k

if __name__ == '__main__':
    string, k = input('enter a string:'), int(input('enter number of'))
    merge_the_tools(string, k)