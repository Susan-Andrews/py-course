def fizzbuzz(r):
 for i in range(1,r):
    if(i%3==0 and i%5==0):
        print(i,"FIZZ")
    elif(i%3==0):
        print(i,"BUZZ")
    elif(i%5==0 ):
        print(i,"FIZZBUZZ")
    else:
        print(i) 


fizzbuzz(51)