#Use filter(), map(), and reduce()
#Filter even numbers
#Find square of each
#Add all squared numbers


from functools import reduce

List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

print("Input List =", List)

Filter = list(filter(lambda x: x % 2 == 0, List))
print("List after filter =", Filter)

Map = list(map(lambda x: x ** 2, Filter))
print("List after map =", Map)

Reduce = reduce(lambda x, y: x + y, Map)
print("Output of reduce =", Reduce)