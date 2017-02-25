    for i in range(len(myarray)):
        for j in range(len(myarray[i])):
            if myarray[i][j] == target:
                print (myarray[i+][j+1])
            print (myarray[n-i-1][j], end="\t")
        print()
