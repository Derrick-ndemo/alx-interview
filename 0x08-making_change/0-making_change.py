#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Return fewest number of coins ndded to meet the toatal
    """
    if total <= 0:
        return 0

    # initialize  list to store the min no. of coins needed for each value
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate over all coin values
    for coin in coins:
        # update dp array for each possible total vlue
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is stiill foat('inf') it means that the total cannot be reached
    return dp[total] if dp[total] != float('inf') else -1