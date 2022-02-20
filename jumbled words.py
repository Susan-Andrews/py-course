import random
print("Its a food related jumbled words game!\n")
def choose():
    words=['Coffee','Water','Pasta','Biriyani','Noodles','Sphagetti','Barbeque','Tea','Choclate','Brownies']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,",your score is:",p1) 
    print(p2n,",your score is:",p2)  
    print("Thanks for playing")  
   

def play():
    p1name=input("Player 1,please enter your name")
    p2name=input("Player 2,please enter your name")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if turn%2==0:
            print(p1name,",your turn.")
            ans=input("what is on my mind:")
            if ans==picked_word:
                pp1=pp1+1
                print("Your score is:",pp1)
            else:
                print("Better luck next time.i thought,",picked_word)
            c=int(input("Press 1 to continue and 0 to exit"))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2
        else:
            print(p2name,",your turn.")
            ans=input("What is on my mind")
            if ans==picked_word:
                pp2=pp2+1
                print("Your score is:",pp2)
            else:
                print("\nBetter luck next time.i thought,",picked_word)
            c=int(input("Press 1 to continue and 0 to exit")) 
            if c==0:   
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()
