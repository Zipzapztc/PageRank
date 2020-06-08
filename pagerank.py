
maxIteration=100
d=0.85
error=0.0001

def setDigraph(digraphList,N):
    counter=[0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if digraphList[i][j]!=0:
                counter[i]+=1
    for i in range(N):
        for j in range(N):
            digraphList[i][j]=digraphList[i][j]/counter[i]
    return digraphList

def calculate(pagerankList,digraphList,N):
    result=[0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            result[i]+=pagerankList[j]*digraphList[j][i]
        result[i]=(1-d)/N+d*result[i]
    return result
    
def pageRank(digraphList,N):
    temp=100
    iteration=0
    pagerankList=[1/len(digraphList) for i in range(N)]
    digraphList=setDigraph(digraphList,N)
    while temp>error and iteration<maxIteration:
        new_pagerankList=calculate(pagerankList,digraphList,N)
        temp=0
        for i in range(N):
            temp+=abs(new_pagerankList[i]-pagerankList[i])
        pagerankList=new_pagerankList
        iteration+=1
        print(new_pagerankList,iteration)


if __name__=='__main__':
    digraphList=[[0,1,1],[1,0,1],[1,0,0]]
    N=len(digraphList)
    pageRank(digraphList,N)
                 
    
                       
    




    
