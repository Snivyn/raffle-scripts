'''
GetMyLevisJordans Raffle Script
by @snivynGOD

Usage:
Edit the fields under user settings to your preferences and run the script.
Good luck!
'''

import requests
import random

def generate_email(domain):
    pre = "ara" + "nga" + str(random.randint(0, 9999999))
    return pre + '@' + domain

def generate_number(area_code):
    phone = str(area_code) + str(random.randint(1000000, 9999999))
    return phone

if(__name__ == "__main__"):
    # Ignore insecure messages
    requests.packages.urllib3.disable_warnings()

    # User settings
    full_name = "Bill Nye"
    domain = "catchAllDomain.com"
    colour = "black"  # lowercase
    size = "10.5"
    entries = 5
    phone_number = ""  # leave empty to generate random London numbers
    
    # Submit entries
    link = "https://api.getmylevisjordans.co.uk/submit-form"    
    
    for i in range(1, entries + 1):
        try:
            email = 's' + 'h' + generate_email(domain)
            payload = {
                "email": email,
                "fullName": full_name,
                "phoneNumber": generate_number(207),
                "size": "m" + str(size),
                "color": colour,
                "privacyPolicyConsent": True
            }
            
            if(phone_number != ""):
                payload["phoneNumber"] = phone_number
        
            r = requests.post(link, json=payload, verify=False)
    
            if(r.json()["message"] == "Form submitted"):
                print("[SUCCESS] Entry " + str(i) + '/' + str(entries) +
                      " entered successfully with email " + email + ".")
            else:
                print("[ERROR] Entry " + str(i) + '/' + str(entries) +
                      " failed with email " + email + " (" + r.text + ").")
        except:
            print("[ERROR] An unknown error occurred: " + str(e))
                  " failed with email " + email + " (" + r.text + ").")
