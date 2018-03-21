'''
Raffle Script
By @snivynGOD

Site: soleheaven.com
Product: Nike Air Max 97 - "Sean Wotherspoon"
Powered by ViralSweep

Note:
ViralSweep uses IP detection to prevent bots from spamming raffle entries.
Increase number of proxies being used for best results.
'''

import requests
import random
from log import log as log

class FileNotFound(Exception):
    ''' Raised when a file required for the program to operate is missing. '''


class NoDataLoaded(Exception):
    ''' Raised when the file is empty. '''


''' ------------------------------ FUNCTIONS ------------------------------ '''


def read_from_txt(path):
    '''
    (None) -> list of str
    Loads up all sites from the sitelist.txt file in the root directory.
    Returns the sites as a list
    '''
    # Initialize variables
    raw_lines = []
    lines = []

    # Load data from the txt file
    try:
        f = open(path, "r")
        raw_lines = f.readlines()
        f.close()

    # Raise an error if the file couldn't be found
    except:
        log('e', "Couldn't locate <" + path + ">.")
        raise FileNotFound()

    if(len(raw_lines) == 0):
        raise NoDataLoaded()

    # Parse the data
    for line in raw_lines:
        lines.append(line.strip("\n"))

    # Return the data
    return lines


def get_proxy(proxy_list):
    '''
    (list) -> dict
    Given a proxy list <proxy_list>, a proxy is selected and returned.
    '''
    # Choose a random proxy
    proxy = random.choice(proxy_list)

    # Set up the proxy to be used
    proxies = {
        "http": str(proxy),
        "https": str(proxy)
    }

    # Return the proxy
    return proxies


def generate_email(domain):
    email = "drizzy" + str(random.randint(1, 999999999)) + "@" + domain

    return email

def enter(size, domain, proxy_list):
    s = requests.session()
    try:
        r = s.get("https://www.soleheaven.com/pages/wotherspoon-raffle")
    except:
        log('e', "Connection to the raffle page failed. Retrying...")
        try:
            r = s.get("https://www.soleheaven.com/pages/wotherspoon-raffle")
        except:
            log('e', "Connection to the raffle page failed.")
            return

    # Setup session
    link = "https://app.viralsweep.com/promo/enter"
    headers = {
        "authority": "app.viralsweep.com",
        "method": "POST",
        "path": "/promo/enter",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "178",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "__cfduid=d1914024a174826a33ff1a44b12181b121521584104; PHPSESSID=bfpjt9vsk6og3ndt1k5h7hjpj4; viewed_33312=1521584104; _ga=GA1.2.999917462.1521584113; _gid=GA1.2.1525774921.1521584113; _gat=1",
        "dnt": "1",
        "origin": "https://app.viralsweep.com",
        "referer": "https://app.viralsweep.com/vrlswp/full/40e2ef-33312?framed=1&ref=&hash=",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
        }

    cookies = r.cookies

    email = generate_email(domain)

    payload = {
        "id": "40e2ef-33312",
        "type": "full",
        "refer_source": "",
        "entry_source": "https://soleheaven.com/pages/wotherspoon-raffle",
        "email": email,
        "email_again": "",
        "23202_1521393710": "UK" + str(size)
        }

    proxies = get_proxy(proxy_list)

    try:
        r = s.post(link, headers=headers, cookies=cookies, data=payload, proxies=proxies)
    except:
        log('e', "Connection failed while attempting to submit entry. Retrying...")
        try:
            r = s.post(link, headers=headers, cookies=cookies, data=payload, proxies=proxies)
        except:
            log('e', "Connection failed while attempting to submit entry.")
            return
    
    log('s', "Entered raffle with email <" + email + ">.")

if(__name__ == "__main__"):
    # Load proxies
    proxy_list = read_from_txt("proxies.txt")
    # Enter raffle approximately 10 times per IP
    max_attempts = 10 * len(proxy_list)
    
    # User settings
    size = 10.5  # This is UK sizing
    domain = "sharanga.pw"  # Enter your catch-all email domain here
    entries = 10

    for count in range(0, entries):
        enter(size, domain, proxy_list)
