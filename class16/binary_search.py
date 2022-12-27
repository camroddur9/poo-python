import random

def binary_search(list, start, end, target):
    if start > end:
        return False

    mid = (start + end) // 2

    if list[mid] == target:
        return True
    elif list[mid] > target:
        return binary_search(list, start, mid - 1, target)
    else:
        return binary_search(list, mid + 1, end, target)

if __name__ == "__main__":
    list_size = int(input("List size:"))
    target = int(input("Target:"))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list, 0, len(list), target)
    print(list)
    print(f'Target {target}" "{"is" if found else "is not"} in the list')