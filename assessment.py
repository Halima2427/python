# w1,w2=map(str,input().split())
# if len(w1)!=len(w2):
#     print("no")
# elif [len(set(w1)),len(set(w2))]==2*[len(set(zip(w1,w2)))]:
#     print("yes")


# a=input()
# b=[]
# b.append(a)
# b.append(".")
# print("".join(b))

n=(input())
res=list(map(int,''.join(str(n).split())))
print(res)
m=len(res)
count=0
for i in range(0,m):
    for j in range(i+1,m):
        if(res[i]==res[j]):
            count+=1
print(count)
