'''
Raffle Script
By @snivynGOD

Site: thenextdoor.fr
Product: Nike Air Max 97 - "Sean Wotherspoon"
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


def enter(fname, lname, size, domain, proxy_list):
    # Setup session
    link = "http://www.thenextdoor.fr/concours/confirm.php"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "116",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.thenextdoor.fr",
        "Origin": "http://www.thenextdoor.fr",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.thenextdoor.fr/concours/airmaxsean.php",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }

    email = generate_email(domain)

    payload = {
        "script": "airmaxsean.php",
        "lang": "en",
        "size": size,
        "f_name": fname,
        "l_name": lname,
        "email": email,
        "cgv": "1"
        }

    proxies = get_proxy(proxy_list)

    try:
        r = requests.post(link, headers=headers, data=payload, proxies=proxies, verify=False)
    except:
        log('e', "Connection failed while attempting to submit entry. Retrying...")
        try:
            r = requests.post(link, headers=headers, cookies=cookies, data=payload, proxies=proxies, verify=False)
        except:
            log('e', "Connection failed while attempting to submit entry.")
            return
    
    log('s', "Entered raffle with email <" + email + ">.")


if(__name__ == "__main__"):
    # Load proxies
    proxy_list = read_from_txt("proxies.txt")
    
    # User settings
    first_name = "Bill"
    last_name = "Nye"
    size = "45,5"  # Use a , instead of . for half sizes. EU sizing.
    domain = "sharanga.pw"  # Enter your catch-all email domain here
    entries = 10

    for count in range(0, entries):
        enter(first_name, last_name, size, domain, proxy_list)
