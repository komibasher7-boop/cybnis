import requests

def ping_search_engines(domains):
    print("\n[!] RB-OMEGA 2026: STARTING INSTANT INDEXING PROTOCOL...")
    
    engines = {
        "Google": "https://www.google.com/ping?sitemap=https://{}/sitemap.xml",
        "Bing": "https://www.bing.com/ping?sitemap=https://{}/sitemap.xml"
    }
    
    for domain in domains:
        print(f"\n[*] Targeting Domain: {domain}")
        for name, url in engines.items():
            target = url.format(domain)
            try:
                response = requests.get(target, timeout=10)
                if response.status_code == 200:
                    print(f"  [+] {name}: Indexing Signal Sent [SUCCESS]")
                else:
                    print(f"  [-] {name}: Signal Pending [Status {response.status_code}]")
            except:
                print(f"  [-] {name}: Node Offline")

if __name__ == "__main__":
    my_domains = ["cybnis.com", "oryphonix.com", "lytren.com", "riwep.com"]
    ping_search_engines(my_domains)
