l1=[1,2,"r1",3,4,"r2"]
res=[i+10 if isinstance(i,(int,float)) else i for i  in l1]
print(res)
for i in res:
    print(i)
print ("*"*50)
l1=[1,2,"r1",3,4,"r2"]
res = (i+10 if isinstance(i,(int,float)) else i for i  in l1)
print (res)
for i in res:
    print (i)