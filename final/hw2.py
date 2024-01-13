#第一方法
def power_of_2_mul(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

#第二方法
def power_of_2_exp(n):
    return 2 ** n

#第三方法
def power_of_2_bitwise(n):
    return 1 << n

#第四方法
def power_of_2_recursive(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_2_recursive(n - 1)

#The results of these implementations are the same, with n subparties of calculating 2.
#You can choose different methods according to your specific needs.