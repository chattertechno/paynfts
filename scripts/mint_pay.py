from brownie import ChatterNft, accounts, config

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    chatter_nft = ChatterNft[len(ChatterNft) - 1]
    transaction = chatter_nft.mint( 
    {"from": dev})