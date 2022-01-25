from brownie import Token, config, network
from scripts.helpful_scripts import get_account


def deploy_token():
    account = get_account()
    token = Token.deploy({'from': account}, publish_source=True)


def main():
    deploy_token()
