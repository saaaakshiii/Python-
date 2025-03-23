# l1=[1,2,3,4,5]
# ans=0
# for i in l1:
#     ans+=i
# print(ans)
# print(max(l1), min(l1))

#que 21
l1=[1,1,2,3,4,4,5]
unique_nums=[]
seen=set()

for i in l1:
    if i not in seen:
        unique_nums.append(i)
        seen.add(i)
print(unique_nums)