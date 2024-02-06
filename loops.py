a=[1,2,3,4,5,6,7,8]
# for i in range(7):
#     a[i]=a[i]+1
# print(a)
# new=[]
# for i in a:
#     i=i+1
#     new.append(i)
# print(new)
# b=['ab','cd','ef','gh','ij','kl']
# for i in range(len(b)):
#     print(b[i])
# else:
#     print('No such element')
# n=0
# while n<=10:
#     print(n+1)
# while n<5:
#     print('hi')
#     n+=1
# else:
#     print('goodbye')
# for i in range(3):
#     print("*",i)
#     continue
#     print("*",i+1)
# for i , element in enumerate(a):
#     if i==3:
#         continue
#         element=element+1
#         a[i]=element
# print(a)
max=15
total=0
for i,element in enumerate(a):
    total=total+element
    if total>max:
        break
    print(i)
