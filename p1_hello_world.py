# print("Hello World...")
import sys
num = int(input(""))
l = [int(i) for i in input().split()[:num]]
min = sys.maxsize
for i in l:
    if i < min:
        min = i
print(min)