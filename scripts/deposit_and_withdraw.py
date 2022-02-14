from webbrowser import get
from brownie import SimpleBank
from scripts.deploy import deploy_simple_bank
from scripts.helpful_scripts import get_account

amount = 100


def deposit():
    simple_bank = SimpleBank[-1]
    account = get_account()
    print(f"Getting Balance before Depositing, balacne is {simple_bank.getBalance()}")
    print(f"Check if Account is enrolled or Enrolling Account")
    tx = simple_bank.enroll({"from": account})
    tx.wait(1)
    print("Depositing Eth")
    tx = simple_bank.deposit({"from": account, "value": amount})
    tx.wait(1)
    print(f"New Balance is {simple_bank.getBalance()}")


def withdraw():
    simple_bank = SimpleBank[-1]
    account = get_account()
    tx = simple_bank.withdraw(50, {"from": account})
    tx.wait(1)


def getbalace():
    simple_bank = SimpleBank[-1]
    account = get_account()
    balance = simple_bank.getBalance()
    print(f"Balance of {account} is {balance}")


def main():
    deposit()
    # withdraw()
    # getbalace()
