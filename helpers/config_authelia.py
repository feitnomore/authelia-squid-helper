## Filename: config_authelia.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Authelia Config
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
from helpers import globalholders

def getConfig():
    config = configparser.ConfigParser()
    config.read(globalholders.config_file)

    # Authelia Config
    authelia_host = config['authelia']['host']
    authelia_port = config['authelia']['port']
    authelia_proto = config['authelia']['proto']
    authelia_first = config['authelia']['firstfactor']
    authelia_second = config['authelia']['secondfactor'] 

    config_authelia = {
	    "host": authelia_host,
        "port": authelia_port,
	    "proto": authelia_proto,
	    "first": authelia_first,
        "second": authelia_second
    }

    return config_authelia
