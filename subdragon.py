#!/usr/bin/env python3
import requests
import os
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

BANNER = Fore.RED + r"""
 _____       _   ______                        
/  ___|     | |  |  _  \                       
\ `--. _   _| |__ | | | |_ __ __ _  __ _  ___  _ __ 
 `--. \ | | | '_ \| | | | '__/ _` |/ _` |/ _ \| '_ \
/\__/ / |_| | |_) | |/ /| | | (_| | (_| | (_) | | | |
\____/ \__,_|_.__/|___/ |_|  \__,_|\__, |\___/|_| |_|
                                    __/ |            
                                   |___/             
""" + Fore.WHITE + " >> Subdomain Fuzzer | Created by 0xCr7ck3r\n"

def check_subdomain(subdomain, domain):
    url = f"https://{subdomain}.{domain}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Found: {Style.BRIGHT}{url}")
            return url
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Subdragon - Subdomain Fuzzing Tool")
    parser.add_argument("-d", "--domain", help="Target Domain", required=True)
    parser.add_argument("-w", "--wordlist", help="Path to wordlist", required=True)
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Threads (default: 50)")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    os.system("clear")
    print(BANNER)

    if not os.path.exists(args.wordlist):
        print(f"{Fore.RED}[!] Error: {args.wordlist} not found.")
        sys.exit(1)

    with open(args.wordlist, "r") as f:
        subs = [line.strip() for line in f if line.strip()]

    found_subs = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(check_subdomain, s, args.domain) for s in subs]
        try:
            for future in as_completed(futures):
                res = future.result()
                if res: found_subs.append(res)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Stopping...")
            sys.exit()

    print(f"\n{Fore.CYAN}--- Scan Complete. Found: {len(found_subs)} ---")

if __name__ == "__main__":
    main()