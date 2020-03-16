# def sosu(n):
#     if n != 1:
#         for i in range(2, n):
#             if n%i == 0:
#                 return False
#     else:
#         return False
#     return True
#
#
# n= int(input())
# if sosu(n):
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")

def sosu(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True

n = int(input())
if sosu(n):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

