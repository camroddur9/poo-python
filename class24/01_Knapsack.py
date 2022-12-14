

def knapsack(size, weights, values, n):
    if n == 0 or size == 0:
        return 0
    
    if weights[n-1] > size:
        return knapsack(size, weights, values, n-1)

    return max(values[n - 1] + knapsack(size - weights[n - 1], weights, values, n - 1), knapsack(size, weights, values, n - 1))

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    size = 50
    n = len(values)

    res = knapsack(size, weights, values, n)
    print(res)