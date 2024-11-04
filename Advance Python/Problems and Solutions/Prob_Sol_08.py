def divisible(n):
    if n % 5 == 0:
        return True
    return False

my_list = [34,43,22,55,10,5]
output = list(filter(divisible, my_list))

print(list(output))