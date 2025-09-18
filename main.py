n = input("请输入一个5位数字：")
if len(n) != 5 or not n.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    if n == n[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
break
