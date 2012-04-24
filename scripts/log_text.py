# Logs text to files in the ETS directory
# A text file is created for each user sending the message and the person receiving the message

import os
import sys
from freeswitch import *

def strip_domain(name):
    loc = name.find('@')
    if loc is -1:
        return name
    return name[0:loc]

def log_msg(target_file, timestamp, to, fromm, content):
    f = open(target_file, "a")
    f.write("[" + timestamp + "] ")
    f.write(to + "->" + fromm + ": ")
    f.write(content)
    f.write('\n')

def log_msgs(ets_log_dir, timestamp, to, fromm, content):
    to = strip_domain(to)
    fromm = strip_domain(fromm)
    to_log = os.path.join(ets_log_dir, to + '.log')
    from_log = os.path.join(ets_log_dir, fromm + '.log')
    log_msg(to_log, timestamp, to, fromm, content)
    log_msg(from_log, timestamp, to, fromm, content)

def chat(msg, args):
    ets_log_dir = getGlobalVariable("ets_log_dir")
    timestamp = msg.getHeader("Event-Date-Local")
    to = msg.getHeader("ets_sms_to")
    fromm = msg.getHeader("ets_sms_from")
    content = msg.getHeader("ets_sms_body")
    
    log_msgs(ets_log_dir, timestamp, to, fromm, content)

