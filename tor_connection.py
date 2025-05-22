import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}


def check_tor_connection():
    print("Tor Connection Check")
    try:
        # Get IP using Tor proxy
        system_ip = requests.get("https://ident.me", proxies=proxies, timeout=10).text.strip()
        # Get Tor exit node list
        tor_exit_data = requests.get("https://check.torproject.org/exit-addresses", timeout=10).text
        # Check if IP is in Tor exit node list
        if system_ip in tor_exit_data:
            #print("Tor_IP:", system_ip)
            print("Tor Connection Success")
        else:
            print("Tor Connection Failed")
            #print("Your IP:", system_ip)
    except requests.RequestException as e:
        print("Error: Could not connect through Tor.")
        print("Details:", e)
        print("Make sure Tor is running on 127.0.0.1:9050")
        exit(1)
