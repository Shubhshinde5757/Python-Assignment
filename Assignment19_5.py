#Use filter(), map(), and reduce()
#ilter prime numbers
#Multiply each by 2
#Find the maximum number

from functools import reduce

List = [2, 70, 11, 10, 17, 23, 31, 77]

print("Input List =", List)

def Prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

Filter = list(filter(Prime, List))
print("List after filter =", Filter)

Map = list(map(lambda x: x * 2, Filter))
print("List after map =", Map)

Reduce = reduce(lambda x, y: x if x > y else y, Map)
print("Output of reduce =", Reduce)