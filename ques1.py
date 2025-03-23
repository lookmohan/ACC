
n = int(input())
prices = [int(input()) for _ in range(n)]

def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    left = 0  
    right = 1  
    max_profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit
print(max_profit(prices))

# output :
Input:
5  
7  
1  
5  
3  
6  

Output:
5
