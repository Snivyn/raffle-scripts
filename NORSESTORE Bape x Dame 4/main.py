import requests
import time
from log import log as log
import random

class OutOfProxies(Exception):
    ''' Raised when the program runs out of proxies to use. '''

def enter_draw(email):
    '''
    Given an email <email>, an account is created on www.norsestore.com and
    the raffle for the adidas Dame 4 x BAPE is entered.
    '''

    # Sign up the account
    log('i', "Signing up with email <" + email + ">.")
    s = requests.session()

    link = "https://www.norsestore.com/account"

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "112",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Host": "www.norsestore.com",
        "Origin": "https://www.norsestore.com",
        "Referer": "https://www.norsestore.com/account?-return-url=https%3A%2F%2Fwww.norsestore.com%2Fdraw%2Fadidas-dame-4-x-a-bathing-apea",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

    payload = {
        "formid": "register",
        "first_name": first_name,
        "surname": last_name,
        "email": email,
        "password": password,
        "password_repeat": password
    }

    try:
        random_proxy = random.choice(proxy_list)
    except:
        log('e', "Ran out of proxies!")
        raise OutOfProxies

    proxy= {
        "http": random_proxy,
        "https": random_proxy
        }

    try:
        r = s.post(link, data=payload, headers=headers, proxies=proxy, timeout=15, verify=False)
    except:
        proxy_list.remove(random_proxy)
        log('e', "Connection failed.")
        return

    # Enter the raffle
    log('i', "Entering raffle with email <" + email + ">.")
    link = "https://www.norsestore.com/draw/adidas-dame-4-x-a-bathing-apea"

    payload = {
        "formid": "draw",
        "item_pid": "228571",
        "option:7": "on"
        }

    try:
        r = s.post(link, data=payload, headers=headers, proxies=proxy, timeout=15, verify=False)
    except:
        proxy_list.remove(random_proxy)
        log('e', "Connection failed.")
        return

    # Check to see if the entry was successful
    flag = "You are participating in this draw." in r.text

    # Return whether or not the entry was successful
    return flag
    
    
if(__name__ == "__main__"):
    # Ignore insecure messages
    requests.packages.urllib3.disable_warnings()

    # User settings
    first_name = "Bill"
    last_name = "Nye"
    password = "skrtskrt"
    domain = "@catchalldomain.com"

    proxy_list = [
        "149.56.133.2:3128",
        "199.195.253.124:3128",
        "200.60.130.162:3128"      
        ]

    entries = 100000

    for count in range(0, entries):
        email = "mjolnir" + str(count) + domain
        success = enter_draw(email)
        
        if(success):
            log('s', "Entry under email <" + email + "> succeeded.")
        else:
            log('e', "Entry under email <" + email + "> failed.")
        
        time.sleep(6)