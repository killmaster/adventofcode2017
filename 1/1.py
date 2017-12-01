res = 0
f = open("input.txt","r")
captcha = f.readline().rstrip()

def solver(captcha, offset):
    res = 0
    size = len(captcha)
    for i in range(size):
        if captcha[i] == captcha[(i+offset)%size]:
            res += int(captcha[i])
    return res

print("Part 1: {}".format(solver(captcha,1)))
print("Part 2: {}".format(solver(captcha,int(len(captcha)/2))))

