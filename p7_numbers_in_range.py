def numbers_in_range(upper, lower, l):
    l1 = []
    for i in l:
        if i in range(lower, upper + 1):
            l1.append(i)
    return l1

def take_input(n):
    l = []
    for _ in range(n):
        l.append(int(input("")))
    return l

l = take_input(5)
max = int(input("Enter upper range : "))
min = int(input("enter lower range :"))
print(numbers_in_range(max, min, l))