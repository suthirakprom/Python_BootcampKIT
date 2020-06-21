import random

lst = []
def random_tuple(num):
    for i in range(num):
        ran_num = random.randint(0, 100)
        lst.append(ran_num)
        print(f"Random number {i+1}: {ran_num}")
    tp = tuple(lst)
    print()
    print(tp)
    print()
    print(sum(tp))

random_tuple(5)
