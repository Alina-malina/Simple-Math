# -*- coding: utf-8 -*-
import random
import sys
import time
def main():
    max=50
    operator=['div','mul']
    member1=[1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,28,30]
    member2=[1,2,3,4,5,6,7,8,9,10]
    i=1
    right=0
    wrong=0
    while i<=15:
        try:
            mem1=random.choice(member1)
            mem2=random.choice(member2)
            res=random.choice(operator)
            if res=='mul' and mem1*mem2<=50 and mem1<11:            
                answer=raw_input( str(mem1) +'x'+ str(mem2)+'=')
                if int(answer)==mem1*mem2:
                    print 'Correct :)'
                    right=right+1
                else:
                    print 'Incorrect :('
                    wrong=wrong+1
                print '----------------------'
                i=i+1
            elif res=='div' and mem1>mem2 and mem1//mem2!=0 and mem1%mem2==0:        
                answer=raw_input(str(mem1) + ':' + str(mem2)+'=')
                if int(answer)==mem1/mem2:
                    print 'Correct :)'
                    right=right+1
                else:
                    print 'Incorrect :('
                    wrong=wrong+1            
                print '----------------------'
                i=i+1
        except Exception as e:
            print e    
    print 'Correct answers: ' +str(right)
    print 'Incorrect answers:' + str(wrong)
    time.sleep(20)
    sys.exit()
if __name__ == "__main__":
    main()
