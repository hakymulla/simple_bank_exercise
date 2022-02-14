import imp
from brownie import SimpleBank
from scripts.helpful_scripts import get_account


def deploy_simple_bank():
    account = get_account()
    simple_bank = SimpleBank.deploy({"from": account})
    print(f"Simple Bank deployed to {simple_bank.address}")
    return simple_bank


def main():
    deploy_simple_bank()
