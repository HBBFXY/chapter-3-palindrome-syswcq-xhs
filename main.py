n = input("请输入一个5位数字：")
if len(n) != 5 or not n.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    num_list = list(n)
    left, right = 0, 4
    is_palindrome = True
    while left < right:
        if num_list[left] != num_list[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1
    if is_palindrome:
        print("是回文数")
    else:
        print("不是回文数")
