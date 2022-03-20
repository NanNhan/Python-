


local = input("请输入用户名:")
keyword = input("请输入密码:")
if keyword == '123456' and local !=' Margaret':
    print("用户名错误")
elif keyword != '123456' and local == 'Margaret':
    print("密码错误")
elif keyword != '123456' and local != 'Margaret':
    print("账号和密码错误")
else:
    print("hello python")
