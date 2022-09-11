def solve(s):
       return ' '.join(i.capitalize()   for i in s.split(' '))

if __name__ == '__main__':
    user_input = input("Type the Name here:")
    print(solve(user_input))