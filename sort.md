```python
class Sort:

    @classmethod
    def quick_sort(cls, nums):
        if len(nums) <= 1:
            return nums
        left, right = [], []
        value = nums[-1]
        for num in nums[:-1]:
            if num < value:
                left.append(num)
            else:
                right.append(num)
        return cls.quick_sort(left) + [value] + cls.quick_sort(right)

    @staticmethod
    def _merge(left, right):
        a, b, ans = 0, 0, []
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                ans.append(left[a])
                a += 1
            else:
                ans.append(right[b])
                b += 1
        ans += left[a:] or right[b:]
        return ans

    @classmethod
    def merge_sort(cls, nums):
        if len(nums) <= 1:
            return nums
        left = cls.merge_sort(nums[:len(nums) // 2])
        right = cls.merge_sort(nums[len(nums) // 2:])
        return cls._merge(left, right)

    @classmethod
    def bubble_sort(cls, nums):
        if len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    @classmethod
    def insert_sort(cls, nums):
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    break
        return nums

    @classmethod
    def select_sort(cls, nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    @classmethod
    def shell_sort(cls, nums):
        length, gap = len(nums), 1
        while gap < length // 2:
            gap = gap * 2 + 1
        while gap > 0:
            for i in range(gap, length):
                cur, pre = nums[i], i - gap
                while pre >= 0 and cur < nums[pre]:
                    nums[pre + gap] = nums[pre]
                    pre -= gap
                nums[pre + gap] = cur
            gap //= 2
        return nums
```
