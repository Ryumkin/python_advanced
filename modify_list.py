def modify_list(a):
    new_list = [i for i in a if i % 2 != 0]
    for i in new_list:
        a.remove(i)
    for i in range(len(a)):
        a[i] /= 2
