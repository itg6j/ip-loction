import requests
from colorama import Fore, Style
import pyfiglet
import time
from colorama import init, Fore, Style

init()
text = "Ghost"
formatted_text = pyfiglet.figlet_format(text)
print (Fore.BLUE + formatted_text + Style.RESET_ALL)
words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"Hi","user","welcome","to",Fore.MAGENTA +"@Ghost"+ Style.RESET_ALL,Fore.RED +":)"+Style.RESET_ALL,Fore.MAGENTA +"\n\n<Ghost> : "+ Style.RESET_ALL,"Ghost", "is",Fore.RED +"simple","virus","and","tools"+ Style.RESET_ALL,"for","Beginner","programming","in","python"]
for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.09)  
print()  
words = [Fore.MAGENTA + "<Ghost> : "+ Style.RESET_ALL,"https://t.me/ghostchannel3"]
for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.09)  
print()  

def track_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code != 200:
            print(Fore.RED + f"[-]error api{response.status_code})." + Style.RESET_ALL)
            return
        data = response.json()
        if "bogon" in data:
            print(Fore.RED + "[-] error ip" + Style.RESET_ALL)
            return
        print(Fore.CYAN + f"IP Address  : {data.get('ip', 'N/A')}")
        print(f"Country     : {data.get('country', 'N/A')}")
        print(f"Region      : {data.get('region', 'N/A')}")
        print(f"City        : {data.get('city', 'N/A')}")
        print(f"Location    : {data.get('loc', 'N/A')}")  
        print(f"zip Code    : {data.get('postal', 'N/A')}")
    except Exception as e:
        print(Fore.RED + f"[-]error {e}" + Style.RESET_ALL)
def main():
    ip = input(Fore.YELLOW + "[*] write ip : " + Style.RESET_ALL)
    track_ip(ip)
if __name__ == "__main__":
    main()
