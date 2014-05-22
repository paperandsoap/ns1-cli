#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#

import json


class CommandException(Exception):

    def __init__(self, cmd, msg):
        self.cmd = cmd
        self.message = msg


class BaseCommand:

    SHORT_HELP = ""

    """:type : nsone.NSONE"""
    nsone = None

    def __init__(self):
        pass

    def jsonOut(self, d):
        print(json.dumps(d))

    def out(self, msg):
        print(msg)

    def isTextFormat(self):
        return self.nsone.config.get('cli', {}).get('output_format',
                                                    'text') == 'text'

    def ppText(self, d):
        import collections
        od = collections.OrderedDict(sorted(d.items()))
        for (k, v) in od.items():
            if type(v) is str:
                self.out('%s: %s' % (k, v))
            elif type(v) is list or type(v) is tuple:
                self.out('%s: %s' % (k, ', '.join(v)))
            else:
                self.out('%s: %s' % (k, str(v)))