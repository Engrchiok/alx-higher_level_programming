#!/usr/bin/python3
if __name__ == "__main__":
    """Prints numbers from arguments."""
    import sys
    if len(sys.argv) >= 2:
        print(f"{len(sys.argv) - 1} {'argument' if len(sys.argv) == 2 else 'arguments'}:")
        for a in range(1, len(sys.argv)):
            print(f"{a}: {sys.argv[a]}")
    elif len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
