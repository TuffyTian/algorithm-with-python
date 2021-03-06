# n代表这个树种有多少个元素
# i 表示从哪里开始做heapify() 操作
def heapify(nums, n, i):
    # 算出两个子节点
    left = 2 * i + 1
    right = 2 * i + 2
    # 先设置最大值为i这个节点
    largest = i

    if left < n and nums[i] < nums[left]:
        largest = left

    if right < n and nums[largest] < nums[right]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def build_heap(nums):
    n = len(nums)
    for i in range((n - 1) // 2, -1, -1):
        heapify(nums, n, i)


def heap_sort(nums):
    build_heap(nums)
    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)


if __name__ == '__main__':
    array = [33, 69, 77, 21, 10, 11, 33, 36, 39, 66, 44, 22]
    heap_sort(array)
    print(array)
