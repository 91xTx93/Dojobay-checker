import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}


def check_onion_urls(file_path):
    with open(file_path, "r") as input_file:
        for line in input_file:
            line = line.rstrip("\n")
            parts = line.split(",")
            url = parts[0]
            url_name = parts[1] if len(parts) > 1 else "Unknown"
            try:
                data = requests.get(url, proxies=proxies)
                status = "Active"
                status_code = data.status_code
                soup = BeautifulSoup(data.text, "html.parser")
                page_title = soup.title.string if soup.title else "NA"
            except requests.RequestException:
                status = "Inactive"
                status_code = "NA"
                page_title = "NA"

            print(
                f" {Fore.GREEN if status == 'Active' else Fore.RED}{status}{Style.RESET_ALL} | {url_name}"
            )
            # f"{url_name} | {Fore.GREEN if status == 'Active' else Fore.RED}{status}{Style.RESET_ALL} | {status_code} | {page_title}")
