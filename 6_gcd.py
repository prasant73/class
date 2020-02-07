# Euclid's algorithm

# 20 8

# 8)20(2
#   16
#   __
#    4)8(2
#      8
#      __
#      0

def return_gcd(a, b):
    # gcd = 0
    if a == b:
        return a
    elif a > b:
        pass
    else:
        a, b = b, a

    while b != 0:
        temp = b 
        if a % b == 0:
            return b
        else:
            b = a % b
            a = temp

num1, num2 = [int(i) for i in input("Enter 2 numbers separated by space : ").split()]

print(return_gcd(num1, num2))

# for i in range(len(input("Enter 2 numbers separated by space : ").split())):
#     l[i] = int(i)


'''
'5 4'
['5', '4']
num1, num2= [5, 4]
'''