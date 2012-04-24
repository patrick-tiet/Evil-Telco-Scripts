# Handles messages sent to the operator

import sys
import sqlite3
from freeswitch import *

#'args' is passed from the chatplan
#'msg' is some kind of event object
def chat(msg, args):
    sys.stderr.write("Received a message to operator\n\n")
	#string user_db_path = getGlobalVariable("ets_user_db")
	#if (from not in users && msg.body() == "yes" or "y"):
	#	users.add(from)
	#else:
	#	emit on-connect message from operator to from
	
	#sys.stderr.write("Received a message to operator\n\n")

