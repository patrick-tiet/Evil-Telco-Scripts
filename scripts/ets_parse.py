# Sets ETS variables given a normal SIP message

import os
import sys
import sqlite3
from freeswitch import *

def convert_to_callerid(caller):
    try:
        conn = sqlite3.connect(getGlobalVariable("openbts_db_loc"))
        cur = conn.cursor()

    except:
        err("Bad DB\n")

    cur.execute('SELECT callerid from sip_buddies where name=?', (caller,))
    res = cur.fetchone()

    if(res):
        #Strip parens
        return str(res[0])
    
    return caller

def parse(msg):
    return {"ets_sms_to"   : convert_to_callerid(msg.getHeader("openbts_tp_dest_address")),
            "ets_sms_from" : convert_to_callerid(msg.getHeader("from_user")),
            "ets_sms_body" : msg.getHeader("openbts_text"),
            }

def chat(msg, args):
    content = parse(msg)
    for key in content.keys():
        msg.chat_execute('set', '%s=%s' % (key, content[key]))
        #sys.stderr.write('set %s=%s' % (key, content[key]))
    consoleLog("info", "Parsed: " + content["ets_sms_body"] + " from: " + content["ets_sms_from"] + " to: " + content["ets_sms_to"])
