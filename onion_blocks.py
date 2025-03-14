import requests
from colorama import Fore, Style

proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}


def check_onion_blocks(file_path):
    with open(file_path, "r") as input_file:
        for line in input_file:
            line = line.rstrip("\n")
            parts = line.split(",")
            url = parts[0]
            url_name = parts[1] if len(parts) > 1 else "Unknown"
            onion_url = url.split("/api")[0]
            try:
                data = requests.get(url, proxies=proxies)
                status = "Active"
                status_code = data.status_code
                data_json = data.json()
                block_number = data_json.get("height", "NA")
            except requests.RequestException:
                status = "Inactive"
                status_code = "NA"
                block_number = "NA"

            print(
                f"{Fore.GREEN if status == 'Active' else Fore.RED}{status}{Style.RESET_ALL} | Block: {Fore.MAGENTA} {block_number}{Style.RESET_ALL} | {url_name}"
            )
            # f"{url_name} | {Fore.GREEN if status == 'Active' else Fore.RED}{status}{Style.RESET_ALL} | {status_code} | Block: {block_number}")
