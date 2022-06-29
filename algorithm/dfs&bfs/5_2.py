from collections import deque


Q = deque()

Q.append(5)
Q.append(2)
Q.append(3)
Q.append(7)
Q.popleft()
Q.append(1)
Q.append(4)
Q.popleft()
print(Q)
Q.reverse()
print(Q)