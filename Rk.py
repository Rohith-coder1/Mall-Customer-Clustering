def search(list,n):
    for i in range(4):
        if n == list[i]:
            print(list[i],"is in", i)

        else:
            print("not found")
            i=i+1



n=5
list=[2,3,5,7]
search(list,n)

