import sys
input = sys.stdin.readline

# class Node:
    
#     def parent(self,a):
#         self.next.append(a)
#     def __init__(self,name):
#         self.next = []
#         self.name = name
    
# a = Node('')

# n = int(input())
# for _ in range(n):
#     k,*nodes = input().split()
#     current = a
#     for i, node in enumerate(nodes):
#         if node not in current.next:
#             # next에 없는 경우
#             new_node = Node(node)
#             current.next.append(new_node)
#         else:
#             # next에 있는 경우 
#             for next in node.next:
#                 if next.name == node



# print(a.next)
ants = []
n = int(input())
for _ in range(n):
    _,*routes = input().split()
    ants.append(routes)

print(ants)