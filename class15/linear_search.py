import random

def linear_search(list, target):
    match = False
    for i in list:
        if i == target:
            match = True
            break
    return match

if __name__ == "__main__":
    list_size = int(input("List size:"))
    target = int(input("Target:"))
    list = [random.randint(0, 100) for i in range(list_size)]
    found = linear_search(list, target)
    print(list)
    print(f'Target {target}" "{"is" if found else "is not"} in the list')