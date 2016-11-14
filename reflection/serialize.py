import re

################################################
###   Serialization to JSON

TAB = '\t'


def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    
    print "{}{}".format(get_tabs(level), '{')
    level += 1
    
    obj_dict = obj.__dict__
    for index, (k, v) in enumerate(obj_dict.items()):
        if '__dict__' in dir(v):
            print "{}\"{}\": ".format(get_tabs(level), k)
            to_json(v, level)
        else:
            comma = '' if index == len(obj_dict) - 1 else ','

            if type(v) is bool or v is None:
                if v:
                    data = 'true'
                elif v is None:
                    data = 'null'
                else:
                    data = 'false'
                
                print "{}\"{}\": {}{}".format(get_tabs(level), k, data, comma)
            elif type(v) is str:
                escape_string(v)
                print "{}\"{}\": \"{}\"{}".format(get_tabs(level), k, v, comma)
            else:
                print "{}\"{}\": {}{}".format(get_tabs(level), k, v, comma)
    
    print "{}{}{}".format(get_tabs(level - 1), '}', ',')

def get_tabs(level):
    tabs = ''
    for tab in range(level):
        tabs += TAB
    return tabs

def escape_string(string):
    return re.sub(r"([\"\\])", r'\\\1', string)