def print_full_name(first, last):
    # Write your code here
    full_name=first+" "+last
    print("Hello", full_name+ "! You just delved into python.")

if __name__ == '__main__':
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name:')
    print_full_name(first_name, last_name)