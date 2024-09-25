num = [1,2,3,4,5,6]

even = [x for x in num if x%2==0]

print(even)

#===========================

n1 = [1,2,3]
n2 = [4,5,6]

result = map(lambda x,y:x+y,n1,n2)

print(list(result))
#===========================
def sq(n):
    return n*n

lst = [5,6,4,7,8,9,5,2,4]
res = map(sq , lst)
print( list(res))