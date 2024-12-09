#!/usr/bin/python3
"""0. Prime Game - Maria and Ben playing a game"""

def isWinner(x, nums):
    """Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the maximum number in each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben"), or None if it's a tie.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize the scores
    ben = 0
    maria = 0

    # Get the maximum number in nums to generate primes up to that point
    max_n = max(nums)
    primes = generate_primes(max_n)

    # Determine the winner for each round
    for n in nums:
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def generate_primes(n):
    """Generates a list where each index represents if it's a prime (1) or not (0).

    Args:
        n (int): The maximum number to check for primes.

    Returns:
        list: A list where primes[i] = 1 if i is a prime, otherwise 0.
    """
    primes = [1 for _ in range(n + 1)]
    primes[0], primes[1] = 0, 0  # 0 and 1 are not prime

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0

    return primes