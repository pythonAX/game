# 比较两个版本号 version1 和 version2。
# 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
# 你可以假设版本字符串非空，并且只包含数字和 . 字符。
#  . 字符不代表小数点，而是用于分隔数字序列。
# 例如，2.5 不是“两个半”，而是第二版中的第五个小版本。
# 你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
v1 = input("请按照格式输入x.x.x:")
v2 = input("请按照格式输入x.x.x:")
v1 = v1.split(".")
v2 = v2.split(".")
longer = None
if len(v1) > len(v2):
    longer = v1
    max_len = len(v2)
elif len(v1) < len(v2):
    max_len = len(v1)
    longer = v2
else:
    max_len = len(v1)
def check(index,v1,v2,longer=None):
    for i in range(index):
        if int(v1[i]) > int(v2[i]):
            print(1)
            return
        elif int(v1[i]) < int(v2[i]):
            print(-1)
            return       ##v1 1.3.5
                         ##v2 1.3.5.0.1
        else:
            if i == max_len-1: ### 在相同长度的版本号判断结束后
                if longer:   # 如果存在更长的 进行处理
                    lst = []
                    for i in range(max_len,len(longer)):
                        lst.append(int(longer[i]))
                    sum = 0
                    for i in lst:
                        sum += i
                    if sum > 0:
                        if longer is v1:
                            print(1)
                            return
                        else:
                            print(-1)
                            return
                    else:
                        print(0)
                        return
                else:
                    print(0)
check(max_len,v1,v2,longer)



