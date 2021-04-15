import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

if __name__ == "__main__":

    fposts=[]
    sposts=[]
    posts=[]
    
    #read data from the file
    with open('input.txt', 'r') as f:
        preference = [[int(num) for num in line.split(' ')] for line in f]

    n=len(preference)
    
    #Finding the f-posts and adding the edges to the reduced graph
    G=nx.Graph()
    i=0
    for el in preference:
        x=el[0]
        G.add_edge(x,'a'+ str(i))
        posts.append(x)
        if(x not in fposts):
            fposts.append(x)
        i+=1
    
    #Finding the s-posts and adding them to the reduced graph
    i=0
    rezerva = n+1
    for el in preference:
        x=1
        while (el[x] in fposts and x<len(el) ):
            x+=1
        if x<len(el):
            G.add_edge(el[x],'a'+ str(i))
            if el[x] not in sposts:
                sposts.append(el[x])
        else:
            G.add_edge(rezerva,'a'+ str(i))
            rezerva+1
        i+=1

    print(fposts)
    print(sposts)

    #Promoting the f-posts to the M graph
    H=G.copy()
    M=nx.Graph()
    deg= G.degree()
    for i in range(0,n):
        if i in fposts:
            l = [n for n in G.neighbors(i)]
            aux=l[0]
            M.add_edge(i,aux)
            G.remove_node(i)
            G.remove_node(aux) 


    maximalMatching = list(nx.algorithms.matching.maximal_matching(G))
    mEdges = list(M.edges)
    final =  maximalMatching + mEdges

    postRankingFreq = [0] * n
    rankSum = 0
    for elem in final:
        if type(elem[0]) is str:
            aplicant = elem[0]
            postPrimit=elem[1]
        else:
            aplicant =elem[1]
            postPrimit = elem[0]
        
        aplicantNumber = int(aplicant[1:])
        if postPrimit in preference[aplicantNumber]:
            postRank = preference[aplicantNumber].index(postPrimit)
            postRankingFreq[postRank] += 1
        else:
            postRank = n
        rankSum += (n-postRank)

    print(rankSum/n)
               

    print(postRankingFreq)
 
    plt.hist(postRankingFreq)
    plt.show()
#    nx.draw(H,with_labels = True)
#    plt.show()

    