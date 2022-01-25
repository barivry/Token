
from brownie import network, config, accounts

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "maimmet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(id=None, index=None):
    # account, in the plase of the index, from local chain
    if index:
        return accounts[index]
    # account from account list
    if id:
        return accounts.load(id)
    # account from local chain
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
