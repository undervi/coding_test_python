# 재귀 제한 늘리기
import sys
sys.setrecursionlimit(10**9)

# 부모를 찾아야 함!! (2번 노드 부터! 1번 노드는 부모가 없음!)
def recur(node, prv):   # 이동하면서 내(부모)의 정보를 들고 가게 해주기

    # 부모 저장하기!
    par[node] = prv
    
    for nxt in tree[node]:
        if nxt != prv: # 부모로 가면 안돼!
            recur(nxt, node)    

n = int(input())    # 노드의 갯수 (노드 7개 링크 6개)

# 0번째 인덱스 무시 (1~7번 인덱스 사용)
tree = [[] for _ in range(n+1)] 
par = [0 for _ in range(n+1)]

for _ in range(n-1):
    # a랑 b 점이 연결되어 있음!
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

recur(1, 0) # 1번 노드는 부모가 없으므로 0

# 부모 출력
for p in par[2:]:
    print(p)