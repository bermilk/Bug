import numpy as np
nbug = 3
dbug = np.array(['+','+','+'])
ebug = np.array(['-','-','-'])
time = np.array([2,1,2])
limitP = np.array([['0','0','0'],['0','0','-'],['0','-','-']])
reP = np.array([['0','-','-'],['-','-','+'],['-','+','+']])

def bug() :
    t = 0
    end = 0
    while(np.array_equal(dbug,ebug) == False):   
        b = np.array([0,0,0])
        for i in range (0,nbug):
            for j in range (0,nbug):
                if dbug[j] == limitP[i][j] and limitP[i][j] == '+' :
                    b[i] += 1
                elif dbug[j] == limitP[i][j] and limitP[i][j] == '-' :
                    b[i] += 2
                print b
        print "P",(np.argmax(b)+1),"  ",time[np.argmax(b)],"  ",
        t += time[np.argmax(b)]
        i = np.argmax(b)
        ###change bug
        for j in range (0,nbug):
            if(reP[i][j] != '0'):
                dbug[j] = reP[i][j]
        print dbug
        print ' '
    print "time = %d"%t," ",dbug
