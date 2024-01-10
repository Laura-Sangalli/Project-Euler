# a² + b² =c²
# a + b + c = 1000
# a < b < c. a, b and c are Natural Numbers. Find a*b*c
def calculo():
    for c in range(1000, 0, -1):
        for b in range((1000-c), 0, -1):
            a = 1000 - b - c
            if(a != 0 and a**2 + b**2 == c**2):
                return[a, b, c]

nums = calculo()
print(nums)
print(nums[0]*nums[1]*nums[2])