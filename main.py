if __name__ == '__main__':
    valid1 = False
    while not valid1:
        print('Enter the value of a')
        num1 = input()
        if num1.isdigit() == False:
            print('Invalid Input for the value of a')
            valid1 = False
        else:
            valid1 = True
    else:
        valid1 = True

    valid2 = False
    while not valid2:
        print('Enter the value of b')
        num2 = input()
        if num2.isdigit() == False:
            print('Invalid Input for the value of b')
            valid2 = False
        else:
            valid2 = True
    else:
        valid2 = True

temp = num1
num1 = num2
num2 = temp

print('The value of a after swapping is {}'.format(num1))
print('The value of b after swapping is {}'.format(num2))
