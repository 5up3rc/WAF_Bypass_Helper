# -*- coding: utf-8 -*
from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.LOW




def tamper(payload, **kwargs):
    """
    >>> tamper("<SCRIPT>alert("XSS");//</SCRIPT>")
<<SCRIPT>alert("XSS");//<</SCRIPT>
    """

    
    return payload.replace("<",'<<') if payload else payload


