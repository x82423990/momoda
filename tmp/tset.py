class Account(object):
        num_accounts = 0
 
        def __init__(self, name, balance):
            self.name = name 
            self.balance = balance 
            Account.num_accounts += 1
 
        def del_account(self):
            Account.num_accounts -= 1

        def deposit(self, amt):
            self.balance = self.balance + amt 
 
        def withdraw(self, amt):
            self.balance = self.balance - amt 
 
        def inquiry(self):
            return self.balance


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():
    L = [1]
    while True:
            yield L
            L.append(0)
            L = [L[i-1]+L[i] for i in range(len(L))]

def yide_test():
    for i in range():
        print i

for i in range(10):
    yide_test()





























