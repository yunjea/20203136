data = int(input("Enter a number:"))

for i in range(1, data+1) :
    for j in range(0,i):
        print("*", end='')
    print()
