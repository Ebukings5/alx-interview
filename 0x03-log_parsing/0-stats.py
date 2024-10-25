#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C) and prints final stats."""
    print_stats()
    sys.exit(0)

# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            # Split the line by spaces and extract the necessary fields
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip line if it doesn't have enough parts

            # Last element is the file size
            file_size = int(parts[-1])
            # Second last element is the status code
            status_code = int(parts[-2])

            # Update the total file size
            total_file_size += file_size

            # Update the status code count if it's a valid status code
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Ignore lines that don't have the correct format or any conversion issues
            continue

        # Every 10 lines, print the accumulated stats
        if line_count % 10 == 0:
            print_stats()

# Handle any unexpected interrupts or errors gracefully
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)