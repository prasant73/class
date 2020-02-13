def list_input(num):
    inputs = []
    for i in range(num):
        inputs.append(int(input("enter value {} : ".format(i+1))))
    return inputs

def string_input(n):
    return input("")[:n]

    
if __name__ == "__main__":
    print("from inputs file, name is : ", __name__) 

# __main__ -> executing inputs
# execute it from a different file -> __name__ -> inputs