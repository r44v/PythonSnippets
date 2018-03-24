import ssl
import socket
import datetime
import time
import urllib
import requests


PERSONAL_API_URL = "<telegram_bot_api_url>"

def send_api_call(msg):
    """
    Sends msg to usoro delivery bot
    """
    # The message to send
    msg = """
## SSL EXPIRE MONITOR ##
""" + msg

    # Create api url
    msg = urllib.quote(msg, safe='')
    url = PERSONAL_API_URL+msg

    # preform api call
    try:
        jsonresp = requests.get(url)
        response = jsonresp.json()
        if response['status'] != "success":
            print "Something went wrong with api call (request was a succes)"
    except:
        print "Something went wrong with api call"


def ssl_expiry_datetime(hostname):
    """
    Retrieves expire date of hostname's ssl certificate

    source:
        https://serverlesscode.com/post/ssl-expiration-alerts-with-lambda/
    """
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # parse the string from the certificate into a Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

EXPIRE = ssl_expiry_datetime("<url_to_check>")
if not isinstance(EXPIRE, datetime.datetime):
    send_api_call("Getting expire time had an error")
elif (time.mktime(EXPIRE.timetuple()) - time.time()) < 432000:
    # 5 days == 432000 seconds
    send_api_call("expires in less than 5 days - " + str(EXPIRE))
else:
    print "There is still time left - " + str(EXPIRE)

