'''
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
'''
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

'''
Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:
'''

squares = list(map(lambda x: x**2, range(10)))

'''
OR
'''

squares = [x**2 for x in range(10)]

