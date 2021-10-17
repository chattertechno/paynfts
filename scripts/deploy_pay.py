from brownie import ChatterNft, config, network, accounts


def main():
    dev = accounts.add(config['wallets']['from_key'])
    print(network.show_active())
    publish_source = True
    chatterNft = ChatterNft.deploy(
        config['networks'][network.show_active()]['name_'],
        config['networks'][network.show_active()]['symbol_'],
        config['networks'][network.show_active()]['baseURI_'],
        {"from": dev},
        publish_source=publish_source
    )
    return chatterNft