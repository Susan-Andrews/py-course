

def magic_square(n):


    magicsquare=[]
    for i in range(n):
        l=[]   #new list to add everything
        for j in range(n):
            l.append(0)     # l=[0,0,0]
        magicsquare.append(l)

    i=n//2
    j=n-1
    num=n*n
    count=1    
    while(count<num):  #10<9 breaks
        if(i==-1 and j==n):  # c4
            j=n-2
            i=0
        else:
            if(j==n): # col num is exceeding
                j=0
            if(i<0): # row is becoming -1
                i=n-1
        if(magicsquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicsquare[i][j]=count
            count=count+1
        i=i-1
        j=j+1  # c1                   
    
    for i in range(n):
        for j in range(n): 
            print(magicsquare[i][j],end=" ") # in a single line
        print()     # splits into row
    print("sum of each r/c/diagonal is:"+str(n*(n**2+1)/2))
magic_square(3)             # to print 3x3. change number in order to give different size of magic squares.
