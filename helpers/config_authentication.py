## Filename: config_authentication.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Authentication Config
 # component.
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
import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('authelia.cfg')

    # Authentication Config
    two_factor = config['authentication']['two_factor']
    auth_target_url = config['authentication']['target_url']
    keep_logged_in = config['authentication']['keep_logged_in']

    if(two_factor.lower() == "true" or two_factor.lower() == "yes"):
        auth_two_factor = True
    else:
        auth_two_factor = False

    if(keep_logged_in.lower() == "true" or keep_logged_in.lower() == "yes"):
        auth_keep_logged_in = True
    else:
        auth_keep_logged_in = False

    config_authentication = {
	    "two_factor": auth_two_factor,
        "target_url": auth_target_url,
	    "keep_logged_in": auth_keep_logged_in
    }

    return config_authentication
