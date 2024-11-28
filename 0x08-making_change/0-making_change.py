#!/usr/bin/python3

"""Contains makeChange function with different values"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)

    change = 0  # Counter for the number of coins used
    for coin in coins:
        if total <= 0:
            break
        # Use as many of the current coin as possible
        count = total // coin
        change += count
        total -= coin * count

    # If there's any amount left, it means it can't be met with the given coins
    if total != 0:
        return -1

    return change