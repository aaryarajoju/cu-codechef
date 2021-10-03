for _ in range (int(input())):
    (n, k) = map(int, input().split(' '))
    
    maxCoins = 0
    for i in range(1, k+1):
        coins = n - (i * (n//i))
        maxCoins = max(maxCoins, coins)
    
    print(maxCoins)
