import matplotlib.pyplot as plt
  
# This function returns true if  woman 'w' prefers man 'm1' over man 'm'
def wPrefersM1OverM(prefer, w, m, m1):
    N=int(len(prefer)/2)
    # Check if w prefers m over her current engagment m1
    for i in range(N):
        if (prefer[w][i] == m1):
            return True
  
        if (prefer[w][i] == m):
            return False
  

def stableMarriage(prefer):
      
    N=int(len(prefer)/2)
    wPartner = [-1 for i in range(N)]
    mFree = [False for i in range(N)]
    freeCount = N
  
    # While there are free men
    while (freeCount > 0):
          
        # Pick the first free man (we could pick any)
        m = 0
        while (m < N):
            if (mFree[m] == False):
                break
            m += 1
  
        # One by one go to all women according to  m's preferences. Here m is the picked free man
        i = 0
        while i < N and mFree[m] == False:
            w = prefer[m][i]
  
            if (wPartner[w - N] == -1):
                wPartner[w - N] = m
                mFree[m] = True
                freeCount -= 1
  
            else: 
                m1 = wPartner[w - N]
                if (wPrefersM1OverM(prefer, w, m, m1) == False):
                    wPartner[w - N] = m
                    mFree[m] = True
                    mFree[m1] = False
            i += 1
  
    print("Woman ", " Man")
    for i in range(N):
        print("a"+str(i), "\t", wPartner[i])

    rankSum = 0
    postRankingFreq = [0] * N
    for i in range(N):
        aplicant=i
        postRank = prefer[i].index(wPartner[i])
        rankSum += (N - postRank)
        postRankingFreq[postRank] +=1

    print(postRankingFreq)
    print(rankSum/N)
    plt.hist(postRankingFreq)
    plt.show()

  

with open('input.txt', 'r') as f:
        preference = [[int(num) for num in line.split(' ')] for line in f]

N=len(preference)

a=[]
for i in range(N):
    a.append(i)
for i in range(N):
    preference.append(a)

stableMarriage(preference)
  
