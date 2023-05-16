from ..explorers import blockchain
from .base import BaseCoin


class Bitcoin(BaseCoin):
    coin_symbol = "BTC"
    display_name = "Bitcoin"
    segwit_supported = True
    magicbyte = 0
    script_magicbyte = 5
    minimum_fee = 450
    segwit_hrp = "bc"
    wif_prefix: int = 0x80
    client_kwargs = {
        'server_file': 'bitcoin.json',
    }

    testnet_overrides = {
        'display_name': "Bitcoin Testnet",
        'coin_symbol': "BTCTEST",
        'magicbyte': 111,
        'script_magicbyte': 196,
        'segwit_hrp': 'tb',
        'hd_path': 1,
        'wif_prefix': 0xef,
        'minimum_fee': 1000,
        'client_kwargs': {
            'server_file': 'bitcoin_testnet.json',
            'use_ssl': False
        },
        'electrum_pkey_format': 'wif',
        'xprv_headers': {
            'p2pkh': 0x04358394,
            'p2wpkh-p2sh': 0x044a4e28,
            'p2wsh-p2sh': 0x295b005,
            'p2wpkh': 0x04358394,
            'p2wsh': 0x2aa7a99
        },
        'xpub_headers': {
            'p2pkh': 0x043587cf,
            'p2wpkh-p2sh': 0x044a5262,
            'p2wsh-p2sh': 0x295b43f,
            'p2wpkh': 0x043587cf,
            'p2wsh': 0x2aa7ed3
        },
    }
