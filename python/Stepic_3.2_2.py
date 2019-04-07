st = [i.lower() for i in input().split()]
for i in set(st):
    print("{} {}".format(i, st.count(i)))
   
    
