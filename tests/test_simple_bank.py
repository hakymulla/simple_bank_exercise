from click import exceptions
from brownie import accounts, exceptions
from scripts.deploy import deploy_simple_bank
from scripts.helpful_scripts import get_account
import pytest


amount = 100
withdraw_amount = 30
high_fund = 200


def test_deposit():
    account = get_account()
    simple_bank = deploy_simple_bank()
    tx = simple_bank.enroll({"from": account})
    tx.wait(1)
    assert simple_bank.enrolled(account) == True
    tx = simple_bank.deposit({"from": account, "value": amount})
    tx.wait(1)
    assert simple_bank.getBalance() == amount


def test_withdraw():
    account = get_account()
    simple_bank = deploy_simple_bank()
    tx = simple_bank.enroll({"from": account})
    tx.wait(1)
    tx = simple_bank.deposit({"from": account, "value": amount})
    tx.wait(1)
    tx = simple_bank.withdraw(withdraw_amount, {"from": account})
    tx.wait(1)
    assert simple_bank.getBalance() == amount - withdraw_amount


def test_enough_fund_withdraw():
    account = get_account()
    simple_bank = deploy_simple_bank()
    tx = simple_bank.enroll({"from": account})
    tx.wait(1)
    tx = simple_bank.deposit({"from": account, "value": amount})
    tx.wait(1)
    with pytest.raises(exceptions.VirtualMachineError):
        simple_bank.withdraw(high_fund, {"from": account})


def test_only_enrolled_can_witdraw():
    account = accounts.add()
    simple_bank = deploy_simple_bank()
    with pytest.raises(exceptions.VirtualMachineError):
        simple_bank.withdraw(withdraw_amount, {"from": account})
