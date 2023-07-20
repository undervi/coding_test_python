def recur(node):
    if node == 46:
        # .을 아스키 코드로 바꾸면 46이 되기 때문
        return
    
    pre.append(chr(node))    # 전위 순회 노드 추가 (문자로 바꾸기)
    recur(tree[node][0])    # 왼쪽
    inorder.append(chr(node))    # 중위 순회 노드 추가 (문자로 바꾸기)
    recur(tree[node][1])    # 오른쪽
    pos.append(chr(node))    # 후위 순회 노드 추가 (문자로 바꾸기)

n = int(input())    # 노드의 갯수

tree = [[] for _ in range(128)]
# 예) A의 경우 아스키 코드가 65임 => 65번쨰 배열에 A의 자식들(왼쪽, 오른쪽)을 넣어준다.
# A의 오른쪽 자식을 보여줘! => print(tree[65][1]) 이렇게 볼 수 있음

for _ in range(n):
    # 아스키 코드로 변환해서 담기 (숫자로 변환은 ord, 문자로 변환은 chr)
    node, left, right = map(ord, input().split())

    tree[node].append(left)
    tree[node].append(right)


pre = [] # 전위 순회
pos = [] # 후위 순회
inorder = [] # 중위 순회

recur(ord('A'))

print(''.join(pre))
print(''.join(inorder))
print(''.join(pos))