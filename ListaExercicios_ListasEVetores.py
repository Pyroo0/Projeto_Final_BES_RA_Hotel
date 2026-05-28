code = int(input("choose your exercise (1-20)\n"))

if code == 1:
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

elif code == 2:
    colors = ['red', 'blue', 'green', 'yellow']
    print(colors[1])

elif code == 3:
    numbers = [1, 2, 3]
    numbers.append(10)
    print(numbers)

elif code == 4:
    fruits = ["apple", "banana", "orange"]
    fruits.remove("banana")
    print(fruits)

elif code == 5:
    items = [10, 20, 30, 40, 50]
    print(len(items))

elif code == 6:
    values = [1, 3, 5, 7, 9]
    print(7 in values)

elif code == 7:
    list1 = [1, 2]
    list2 = [3, 4]
    list3 = list1 + list2
    print(list3)

elif code == 8:
    letters = ['a', 'b', 'c', 'd']
    letters.reverse()
    print(letters)

elif code == 9:
    numbers = [1, 2, 2, 3, 2, 4]
    print(numbers.count(2))

elif code == 10:
    prices = [10.5, 20.0, 15.5]
    print(sum(prices))

elif code == 11:
    nums = [1, 2, 2, 3, 4, 4, 5]
    seen = []
    for n in nums:
        if n not in seen:
            seen.append(n)
    print(seen)

elif code == 12:
    nums = [5, 2, 9, 1, 7]
    max_val = nums[0]
    min_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    print("Max:", max_val, "Min:", min_val)

elif code == 13:
    squares = [x**2 for x in range(1, 11)]
    print(squares)

elif code == 14:
    mixed = [1, 2, 3, 4, 5, 6, 7]
    odds = [x for x in mixed if x % 2 != 0]
    print(odds)

elif code == 15:
    lst = [1, 2, 3, 4, 5]
    n = 2
    rotated = lst[-n:] + lst[:-n]
    print(rotated)

elif code == 16:
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    intersection = [x for x in list1 if x in list2]
    print(intersection)

elif code == 17:
    matrix = [[1, 2], [3, 4]]
    flat = [item for sublist in matrix for item in sublist]
    print(flat)

elif code == 18:
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    arr = [5, 2, 9, 1, 7]
    print(merge_sort(arr))

elif code == 19:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = nums[0]
    current_sum = nums[0]
    for n in nums[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    print(max_sum)

elif code == 20:
    def permutations(lst):
        if len(lst) == 0:
            return [[]]
        result = []
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in permutations(rest):
                result.append([lst[i]] + p)
        return result

    nums = [1, 2, 3]
    print(permutations(nums))

else:
    print("Type a valid exercise")
