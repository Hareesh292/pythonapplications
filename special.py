num=5
for val in range(num):
    for vv in range(num):
        if vv==0 or val==0 or vv==num-1 or val==num-1:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('----------hellow triangle pattern------------')
num=5
for val in range(num):
    for vv in range(val+1):
        if vv==0 or val==vv or val==num-1:
            print('* ',end='')
        else:
            print('  ',end='')
    print()
print('---------------right traingle pattern-------------------')


