## Filename: second_factor.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Second Factor Auth
 # of authelia-squid-helper tool.
 # 
 # ###########################
 # # DISCLAIMER - IMPORTANT! #
 # ###########################
 # 
 # Stuff found here was built as a
 # Proof-Of-Concept or Study material
 # and should not be considered
 # production ready!
 # 
 # USE WITH CARE!
##
import json
from urllib import request
from helpers import config_authelia

def authenticate(this_request):

     # Read Authelia Configuration
    authelia_config = config_authelia.getConfig()

    # Build endpoint URL
    endpoint = authelia_config["proto"] + "://" + authelia_config["host"] + ":" + authelia_config["port"] + authelia_config["second"]

    # Empty cookie
    my_cookie = ""

    # Build TOTP Request based on the param received
    my_request = {
        "token": this_request["token"],
        "targetURL": this_request["targetURL"]
    }

    # Perform a POST request to our endpoint using application/json mime and our cookie
    req = request.Request(endpoint, method="POST")
    req.add_header('Content-Type', 'application/json')
    req.add_header('Cookie', this_request["cookie"])
    my_request = json.dumps(my_request)
    my_request = my_request.encode()

    try:
        # Send the request to our target
        r = request.urlopen(req, data=my_request)

        # Authentication Success
        if (r.status == 200):
            full_cookie = r.getheader('Set-Cookie')
            split_cookie = full_cookie.split(";")
            my_cookie = split_cookie[0]
            status = 200
            message = "OK"
        # Authentication failed
        else:
            status = 401
            message = "ERR Wrong password"
    # Authentication failed
    except Exception as e:
        status = 401
        message = "ERR Wrong password"

    # Build our response payload
    auth_response = {
        "status": status,
        "message": message,
        "cookie": my_cookie
    }

    # Return the payload
    return auth_response