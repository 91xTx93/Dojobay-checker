from colorama import Fore, Style
from tor_connection import check_tor_connection
from height_mainnet import check_mempool_height
from height_testnet import check_testnetmempool_height
from onion_urls import check_onion_urls
from onion_blocks import check_onion_blocks
import os


def get_data_path(filename):
    """Get absolute path for data files in the data subdirectory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "data", filename)


def check_all_urls():
    """Check all onion URLs"""
    print(f"\n{Fore.YELLOW} CHECKING URLS {Style.RESET_ALL}")
    check_onion_urls(get_data_path("Dojo_mainnet.txt"))
    print("\n" + Fore.YELLOW + " CHECKING TESTNET URLS " + Style.RESET_ALL)
    check_onion_urls(get_data_path("Dojo_testnet.txt"))


def check_all_blocks():
    """Check all mempool and onion blocks"""
    print(f"\n{Fore.YELLOW} CHECKING MEMPOOL BLOCKS {Style.RESET_ALL}")
    check_mempool_height()
    check_onion_blocks(get_data_path("blocks_mainnet.txt"))
    check_testnetmempool_height()
    check_onion_blocks(get_data_path("blocks_testnet.txt"))


if __name__ == "__main__":
    check_tor_connection()
    check_all_urls()
    check_all_blocks()
