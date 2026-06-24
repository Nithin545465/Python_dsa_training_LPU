from collections import Counter
nums = [1,2,2,3,3,3]
k=2
print(Counter(nums))
print(Counter(nums).most_common(k))

print([num for num,freq in Counter(nums).most_common(k)])