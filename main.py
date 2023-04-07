"""
Since python does not allow relative imports we have a main function 
that invokes the client or or server code based on command line 
arguments
"""

import sys

from packages.communication.server import server
from packages.communication.driver import driver

arguments = sys.argv

# check if arguments are correct
if len(arguments) == 1: # if no arguments passed
    print("Don't know what to run!")
    print("Pass \"server\" or \"driver\" as an argument")
elif arguments[1] not in ["server", "driver"]:
    print("Incorrect first argument")
    print("Pass \"server\" or \"driver\" as the first argument")
elif arguments[1] == "driver" and len(arguments) < 3:
    print("Pass address of the server as \
            the second argument after driver")


if arguments[1] == "server":
    server.run_server
elif arguments[2] == "driver":
    driver.run_driver
