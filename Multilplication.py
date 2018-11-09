a = [1, 2, 3]
b = [4, 5, 6, 7]
c = []
for i in range(len(a)):
    # print(i)
    for j in range(len(b)):
        # print(j)
        c.append(a[i] * b[j])
print(c)

# x = str(783)
# endmsg = ""
# for i in range(0, len(x)):
#     # reverse string
#     endmsg = x[i] + endmsg
#     # same string
#     # endmsg = endmsg + x[i]
# print(endmsg)
