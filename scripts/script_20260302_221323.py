# Auto-generated script
# Created: 2026-03-02T22:13:23.095897
# Account: Account 3

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Script executed successfully!")
