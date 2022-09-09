## Filename: main.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Main component
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
import sys
from helpers import first_factor
from helpers import second_factor
from helpers import globalholders
from helpers import config_authentication

def main():

	# Checking if config file was provided
	if(len(sys.argv) != 2):
		print("No config file provided")
		sys.exit()
	else:
		globalholders.config_file = sys.argv[1]

	# Loading Authentication Config
	authentication = config_authentication.getConfig();

	# Expects stdin forever
	while True:

		# Read stdin
		input_buffer = input("")
		buffer_split = input_buffer.split()

		# Two-Factor Authentication
		if(authentication["two_factor"] == True):
			# Parsing username/password+appended-token
			first_req = {
				"username": buffer_split[0],
				"password": buffer_split[1][0:-6],
				"targetURL": authentication["target_url"],
				"keepMeLoggedIn": authentication["keep_logged_in"]
			}

			# Perform password check
			first_response = first_factor.authenticate(first_req)

			# Password check passed
			if(first_response["status"] == 200):

				# Parsing Appended TOKEN
				second_req = {
					"token": buffer_split[1][-6:],
					"targetURL": authentication["target_url"],
					"cookie": first_response["cookie"]
				}

				# Perform token check
				second_response = second_factor.authenticate(second_req)

				# Return message to stdout
				print(second_response["message"])
			
			# Failed password check
			else:
				# Return message to stdout
				print(first_response["message"])

		# One-Factor Authentication
		else:
			# Parsing username/password
			first_req = {
				"username": buffer_split[0],
				"password": buffer_split[1],
				"targetURL": authentication["target_url"],
				"keepMeLoggedIn": authentication["keep_logged_in"]
			}

			# Performing password check
			first_response = first_factor.authenticate(first_req)

			# Return message to stdout
			print(first_response["message"])
	


if __name__ == '__main__':
    main()