# Censors text messages. Changes message content

import os
import sys
from freeswitch import *

def strip_domain(name):
    loc = name.find('@')
    if loc is -1:
        return name
    return name[0:loc]
    
def censor(censorSet, text):
    newText = ""
    for word in text.split():
        if word in censorSet:
            newText += "[CENSORED]" + ' '
        else:
            newText += word + ' '
    
    newText = newText[0:len(newText)-1] #remove the trailing ' '
    return newText

def parseFile(path):
    parsed = set([])
    f = open(path, 'r')
    for line in f:
        word = line[0:len(line)-1] #cut off new line
        parsed.add(word)
        
    return parsed

def chat(msg, args):
    ets_censor_words = getGlobalVariable("ets_censor_words")
    to = msg.getHeader("ets_sms_to")
    fromm = msg.getHeader("ets_sms_from")
    content = msg.getHeader("ets_sms_body")
    
    content = censor(parseFile(ets_censor_words), content)
    msg.chat_execute('set', 'ets_sms_body=%s' % (content))

