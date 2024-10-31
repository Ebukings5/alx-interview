#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_of_bytes = 0

    # Masks to check leading bits for continuation bytes (10xxxxxx)
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Ensure only the least significant 8 bits are processed
        byte = byte & 0xFF

        if number_of_bytes == 0:
            # Determine how many bytes in the UTF-8 character
            mask = 1 << 7
            while byte & mask:
                number_of_bytes += 1
                mask >>= 1

            # If it's a single-byte character, no extra bytes to validate
            if number_of_bytes == 0:
                continue

            # UTF-8 can have at most 4-byte sequences
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # Check that the byte follows 10xxxxxx pattern
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the count of bytes to process in the sequence
        number_of_bytes -= 1

    # If we have processed all required continuation bytes, return True
    return number_of_bytes == 0
