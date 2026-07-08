#Use filter(), map(), and reduce()
#Filter numbers between 70 and 90 (inclusive)
#Double each number
#Find the product of all numbers


from functools import reduce

List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

print("Input List =", List)

Filter = list(filter(lambda x: x >= 70 and x <= 90, List))
print("List after filter =", Filter)

Map = list(map(lambda x: x * 2, Filter))
print("List after map =", Map)

Reduce = reduce(lambda x, y: x * y, Map)
print("Output of reduce =", Reduce)