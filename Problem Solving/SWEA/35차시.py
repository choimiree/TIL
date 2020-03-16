ls = ["가위", "바위", "보"]
def check(n,m):
    if (n == ls[0] and m == ls[2]) or (n == ls[2] and m == ls[0]):
        return "가위가 이겼습니다!"
    elif (n == ls[1] and m == ls[0]) or (n==ls[0] and m==ls[1]):
        return "바위가 이겼습니다!"
    elif (n==ls[2] and n==ls[1]) or (n==ls[1] and m==ls[2]):
        return "보가 이겼습니다!"
    else:
        return False
a = input()
b = input()
n = input()
m = input()
print(check(n,m))