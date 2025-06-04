import sys
import time

def countdown(n):
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    countdown(n)
