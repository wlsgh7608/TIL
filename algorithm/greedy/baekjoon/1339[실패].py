"""
https://www.acmicpc.net/problem/1339

"""
def comp_digits(alps,n):

    pass




n = int(input())
max_len = 0
words = []

alp_set = set()
for _ in range(n):
    word = input()
    words.append(word)
sizes = [len(p) for p in words]
freq_dic = [{} for _ in range(max(sizes))]

for word in words:
    size = len(word)
    for idx,a in enumerate(word):
        alp_set.add(a)
        digit = size - idx - 1 
        if a in freq_dic[digit]:
            freq_dic[digit][a] +=1
        else:
            freq_dic[digit][a] = 1

print(alp_set)
print(freq_dic)

# ans = {}

# for digit in range(max(sizes),-1,-1): # 최대자리수 부터 체크
#     freq = {}
#     for idx,word in enumerate(words):
#         if sizes[idx]>=digit:
#             j = sizes[idx] - digit
#             alpha = word[j]
#             if alpha in freq:
#                 freq[alpha] +=1
#             else:
#                 freq[alpha] = 1 
    



