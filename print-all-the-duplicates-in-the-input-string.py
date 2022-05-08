#bruteforce approch
s = "geeksforgeeks"
x=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
       
        if(s[i]==s[j]):
            if(s[i] not in x):
              x.append(s[i])
for i in x:
    print(i,s.count(i))
