def deposit(accounts: dict, name: str, amount: int):
    money = accounts.get(name, 0)
    accounts[name] = money + amount


def withdraw(accounts: dict, name: str, amount: int):
    money = accounts.get(name, 0)
    accounts[name] = money - amount


def balance(accounts: dict, name: str):
    money = accounts.get(name, "ERROR")
    print(money)


def transfer(accounts: dict, name1: str, name2: str, amount: int):
    withdraw(accounts, name1, amount)
    deposit(accounts, name2, amount)


def income(accounts: dict, percent: int):
    for name, amount in accounts.items():
        if amount <= 0:
            continue
        accounts[name] = int((amount*percent/100 + amount))


bank_accounts = dict()
while True:
    try:
        string = input()
        if string == "":
            break
        words = string.split()
        if words[0] == "DEPOSIT":
            deposit(bank_accounts, words[1], int(words[2]))
        if words[0] == "WITHDRAW":
            withdraw(bank_accounts, words[1], int(words[2]))
        if words[0] == "BALANCE":
            balance(bank_accounts, words[1])
        if words[0] == "TRANSFER":
            transfer(bank_accounts, words[1], words[2], int(words[3]))
        if words[0] == "INCOME":
            income(bank_accounts, int(words[1]))
    except EOFError:
        break
