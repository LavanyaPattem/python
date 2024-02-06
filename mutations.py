def mutate_string(string, position, character):
    # return string[:position] + character + string[position+1]
    string_list = list(string)
    string_list[position] = character
    modified_string = ''.join(string_list)

    return modified_string


if __name__ == '__main__':
    s = input('Enter a string: ')
    i, c = input('position index').split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)