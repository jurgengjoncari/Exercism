def is_valid(isbn):
    ls1 = [i if type(i) == int else 10 for i in isbn if i != "-"]
    for (x, n) in zip([int(i) for i in isbn if i != "-" and ], range(10, 0, -1)):
        print(x, n)
        if sum(x * n) % 11 == 0:
            return True
        else:
            return False
