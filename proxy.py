def load_proxies(file='proxies.txt'): try: with open(file, 'r') as f: return [line.strip() for line in f if line.strip()] except FileNotFoundError: print("[!] File proxies.txt tidak ditemukan.") return []