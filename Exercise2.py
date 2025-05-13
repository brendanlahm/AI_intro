#######################################
print("1")

def print_pattern(n):
    if n > 9:
        return
    for i in range(1, n + 1):
        print(str(i) * i)

n = input("give a number: \n")
n = int(n)
print_pattern(n)