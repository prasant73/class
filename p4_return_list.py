def fill_list(size):
    # return a list with user input
    l = []
    for i in range(size):
        l.append(input(f"Enter number {i+1} : "))
        print(l)
    return l

n = int(input("Enter the size of the list : "))

print(fill_list(n))