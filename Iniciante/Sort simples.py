nums = list(map(int, input().split()))

original = nums[:]
ordenado = sorted(nums)

for n in ordenado:
    print(n)

print()

for n in original:
    print(n)