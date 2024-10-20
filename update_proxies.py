import requests
import time

def download_and_modify_proxies():
    url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        proxies = response.text.splitlines()
        
        modified_proxies = [f"{proxy}::" for proxy in proxies]
        
        with open("proxies.txt", "w") as f:
            f.write("\n".join(modified_proxies))
        
        print("Proxies updated successfully.")
    except Exception as e:
        print(f"Error updating proxies: {e}")

if __name__ == "__main__":
    download_and_modify_proxies()
