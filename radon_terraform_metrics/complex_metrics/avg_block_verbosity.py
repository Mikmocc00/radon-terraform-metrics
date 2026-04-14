import re

class AvgBlockVerbosity:
    """
    Verbosità media per risorsa:
    numero di token / numero di risorse.
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        tokens = len(re.findall(r'\S+', self.script))

        resources = len(re.findall(r'^\s*resource\s+"', self.script, re.MULTILINE))

        if resources == 0:
            return 0.0

        return tokens / resources