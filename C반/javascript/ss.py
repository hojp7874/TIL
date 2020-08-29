# ladder2
def ladder(data, s1, s2,direction=0,cnt=0):
    if s1 == 99:
        return cnt
    else:
        if s2 >= 1 and data[s1][s2-1] == 1 and direction !=1:
            return ladder(data, s1, s2-1,2,cnt+1)
        elif s2 < 99 and data[s1][s2+1] == 1 and direction !=2:
            return ladder(data, s1, s2+1,1,cnt+1)
        else:
            return ladder(data, s1+1, s2, 0,cnt+1)


for tc in range(1, 11):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(100)]
    s2 = []
    for i in range(100):
        if adj[0][i] == 1:
            s2.append(i)
    cnt=0
    s1 = 0
    ans=[]
    for j in s2:
        ans_x=j
        ans_count=ladder(adj,s1,j,0,cnt)
        ans.append([ans_x,ans_count])
        ans.sort(key = lambda x: (x[1],-x[0]))
    print(f'#{N} {ans[0][0]}')