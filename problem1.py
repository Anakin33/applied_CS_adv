## Project 1 - bisect
import random
import timeit
from math import floor


'''
Your goal is to time the difference between binary search and linear search of a list.

You'll generate a list of 10_000 random numbers between 1 and 20,000, grab one of its members by randomly selecting an index ' \'in the sample range' \
   ', reshuffle the list, then search for the list either using binary search or linear search. ' \
   'The search will be timed. Then you'll repeat this 10 times for each method, and find its average time.

You'll use several functions from the random module (https://docs.python.org/3/library/random.html), ' \
   'the bisect library (https://docs.python.org/3/library/bisect.html#searching-sorted-lists), and the timeit function ' \
   '(https://docs.python.org/3/library/timeit.html). I recommend first getting the functionality down, and then add timing ' \
   'and the average.

To get you started, here's the snippet to generate the random list:

```python
original_list = random.sample(range(1, 20_000), 10_000)
```

Note that the setup should not be timed. The only thing you should time is the search.

Once you finish, why are you seeing the results you get, that one technique is faster than the other? Is this what you expected? How does it change if you consistently preprocess the data (e.g. sort) regardless of technique used?
'''
original_list = random.sample(range(1, 20_000), 10_000)
guess_number = random.sample(range(1, 20_000), 1)
sorted_list = sorted(original_list)
guess = guess_number[0]

def linear_search (listy,inty):
   return [x for x in listy if x == inty]

def binary_search(Array, Search_Term):
   n = len(Array)
   L = 0
   R = n - 1

   while L <= R:
      mid = floor((L + R) / 2)
      if Array[mid] < Search_Term:
         L = mid + 1
      elif Array[mid] > Search_Term:
         R = mid - 1
      else:
         return mid
   return -1

print(linear_search(original_list,guess))
print(binary_search(sorted_list,guess))

