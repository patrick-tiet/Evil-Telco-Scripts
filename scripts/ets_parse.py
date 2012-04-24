# Sets ETS variables given a normal SIP message

import os
import sys
from freeswitch import *

def parse(msg):
    return {"ets_sms_to"   : msg.getHeader("to"),
            "ets_sms_from" : msg.getHeader("from"),
            "ets_sms_body" : msg.getBody()
            }

def chat(msg, args):
    content = parse(msg)
    for key in content.keys():
        msg.chat_execute('set', '%s=%s' % (key, content[key]))
        #sys.stderr.write('set %s=%s' % (key, content[key]))
