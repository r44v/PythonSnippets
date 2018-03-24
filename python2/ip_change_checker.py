# system imports
import urllib
import requests
import sys
import re
import pickle
import os

# Set some variables
personalApiUrl = "<telegram_msg_bot_api_url>"
last_knowm_ip_pickle = "lastKnowIp.pickle"


# Get external url
def getRemoteIp():
    # Try url with cool name
    remoteUrl = getUrlContent("http://canihazip.com/s")
    if match_ip(remoteUrl):
        return remoteUrl
    else:
        # Try backup url checker
        remoteUrl = getUrlContent("http://ipecho.net/plain")
        if match_ip(remoteUrl):
            return remoteUrl
        else:
            return ""


def getUrlContent(url):
    responseText = ""
    try:
        resp = requests.get(url)
        responseText = resp.text
    except:
        pass

    return responseText


def match_ip(string):
    match = re.search('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', string)
    if match:
        return True
    else:
        return False


def load_last_known_ip():
    if os.path.isfile(last_knowm_ip_pickle):
        return pickle.load(open(last_knowm_ip_pickle, 'rb'))
    else:
        return ""


def save_last_known_ip(ip):
    pickle.dump(ip, open(last_knowm_ip_pickle, 'wb'))

# ###################>>>>>>         <<<<<<################### #
# ###################### Program Start ###################### #
# ###################>>>>>>         <<<<<<################### #


last_knowm_ip = load_last_known_ip()
print "Last know ip: " + last_knowm_ip
current_ip = getRemoteIp()
print "Current ip  : " + current_ip
save_last_known_ip(current_ip)

print ""

if current_ip == last_knowm_ip:
    print "No ip change detected"
    sys.exit(0)
else:
    print "Change detected, sending to message to delivery bot"

# The message to send
msg = """
Ip Change Detected:
Last know ip : """ + last_knowm_ip + """
Current ip   : """ + current_ip + """
"""

# Create api url
msg = urllib.quote(msg, safe='')
url = personalApiUrl+msg

# preform api call
try:
    jsonResp = requests.get(url)
    response = jsonResp.json()
    if response['status'] != "success":
        print "Something went wrong with api call (request was a succes)"
except:
    print "Something went wrong with api call"
