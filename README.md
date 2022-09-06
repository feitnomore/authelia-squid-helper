<!--- Filename: README.md
  --- Author: Marcelo Feitoza Parisi
  --- 
  --- Description: Readme file for
  --- authelia-squid-helper tool.
  ---  
  --- ###########################
  --- # DISCLAIMER - IMPORTANT! #
  --- ###########################
  --- 
  --- Stuff found here was built as a
  --- Proof-Of-Concept or Study material
  --- and should not be considered
  --- production ready!
  --- 
  --- USE WITH CARE!
--->

# authelia-squid-helper

## Summary
This application is a helper application in Python3, to be used as an authentication middleware between Squid Proxy and Authelia.
It supports both, Single Factor authentication and Two Factor authentication with TOTP. To use Two Factor authentication with TOTP, 
the token must be appended to the password in the Proxy Authentication screen.

## Installation
These steps illustrates how to install this application into `/opt`.

* First lets `cd` to the directory and clone the repo
```
cd /opt
sudo git clone https://github.com/feitnomore/authelia-squid-helper.git
sudo chown proxy authelia-squid-helper/* -R
```

* Install the required Python packages:
```
sudo pip3 install json
sudo pip3 install urrlib
sudo pip3 install configparser
```

* Adjust the config file `authelia.cfg` with the desired parameters
```
[authelia]
host = XXX.XXX.XXX.XXX
port = 9091
proto = http
firstfactor = /api/firstfactor
secondfactor = /api/secondfactor/totp

[authentication]
two_factor = True
keep_logged_in = False
target_url = https://my-proxy-url.com/
```

* Add the entry for you proxy on your Authelia config, for example
```
    - domain: my-proxy-url.com
      policy: two_factor
      subject:
      - ["group:admins", "group:others"]
```

* Adjust your Squid configuration for authentication
```
auth_param basic program /opt/authelia-squid-helper/authelia-squid-helper
acl ncsa_users proxy_auth REQUIRED
http_access allow ncsa_users
```

## Usage Info
If the tool is set to perform `two_factor` authentication, the TOTP token **must** be appended to the password in the proxy authentication screen. For example, if the user password is `foobar` and the TOTP is `246135`, the user **must** use `foobar246135` as password in the proxy authentication screen.

## Development info
This is how the tool is organized:
* authelia-squid-helper - Shellscript wrapper to main.py.  
* main.py - This is the main authentication loop.  
* authelia.cfg - Sample configuration file
* README.md - This file
* helpers/config_authelia.py - Reads authelia config parameters
* helpers/config_authentication.py - Reads authentication config parameters
* helpers/first_factor.py - Performs the username/password check
* helpers/second_factor.py - Performos TOTP verification


## Requirements
* json  
  `sudo pip3 install --upgrade json`
* urllib  
  `sudo pip3 install --upgrade urrlib`
* configparser  
  `sudo pip3 install --upgrade configparser`
