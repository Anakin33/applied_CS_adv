"""
# Algorithms Homework

## FYI: common gotchas with complexity
* Complexity is a function of how the space or performance grows *as the input scales*. For example, with time complexity, if the same expensive operation executes every single timregardless of a small input vs huge input—then it has constant complexity.
* Drop constants and trailing terms. Some examples:
    * O(n^2 + n) -> O(n^2)
    * O(n/2) -> O(n/2)

## Free response

1. Recursion can always be implemented via for loops instead. So, why still use recursion?

From my understanding loops are superior to recursion due to potential stack overflow and speed of processing the data.

But recursion can be nice due to the call stack. We can hold off on a calulation until you get to the base value and then work backwards. We can do this with the power or factorial examples.


2. When looking at complexity, we drop the constants and trailing terms (see the gotchas section). Why is this? Does this actually mean O(n/2) isn't better than O(n)?
No this would be much slower. O(n) is linear because its  n + n so the more input the longer the function takes at a linear scale.

for O(n/2)  we are saying that for each new input we are growing expontially which can quickly get out of control. For instance figuring out the next fibonacci number with recurusion, you could use all of the worlds processing power very quickly.

O(n/2) is actually O(2 ^n + n)

3. For each code snippet, give the time and space complexity.
    a)
        def complexity(xs: List[int]) -> None:
            for x in xs:
                print(x)
                O(n) Linear Search since input list can grow in size


    b)
        def complexity() -> None:
            for x in [1, 2, 3]:
                print(x)
                O(1) instant, since list can not grow


    c)
        def complexity(xs: List[int]) -> None:
            for x in [1, 2, 3]:
                result = x+ xs[0]
                print(result)
                O(1) since the input sizes are fixed



    d)
        def complexity(xs: List[int]) -> None:
            for x in xs:
                for y in xs:
                    result = x + y
                    print(result)
        O(n^2) since the dataset size growth leads to both loops needed to be called. This would be expontial.



    e)
        def complexity(xs: List[int]) -> Set[int]:
            return set(xs)
  O(n) Linear Search since input list can grow in size and each element must be converted


    f)
        def complexity(xs: List[int]) -> List[int]:
            s = set(xs)
            return xs
         I think it would be 0(n) since the computer would go through the hassle of changing everyhting to a set for no reason and then return the orginal list


    f)
        def complexity(xs: List[int]) -> Set[int]:
            first_half_xs = xs[:len(xs)//2]
            return set(first_half_xs)
            O(1) since it the same simple divison no matter the length of the list



    g)
        def complexity(xs: List[int]) -> List[int]:
            return reversed(xs)
     O(n) Linear Search since input list can grow linerally in size


4) At a high level, how does merge sort work? What technique does it use?

Merge sort starts with a middle value and then checks to see if that target is  >, < , = . Depending on the result, it will then exclude the other half of the data saving the computer a massive amount of resorouces. It will continue to do this until we quickly find the target.

Divde and conquer
"""