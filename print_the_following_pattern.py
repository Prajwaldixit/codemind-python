rows = int(input())
for i in range(rows, 0,-1):
    for j in range(rows, 0,-1):
        if j == i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()