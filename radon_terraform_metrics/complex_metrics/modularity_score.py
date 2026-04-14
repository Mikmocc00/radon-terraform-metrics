import re

class ModularityScore:
    """
    Modularità:
    (locals + moduli riusati) / risorse
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        locals_ = len(re.findall(r'\blocals\s*{', self.script))
        modules = len(re.findall(r'\bmodule\s+"', self.script))

        resources = len(re.findall(r'^\s*resource\s+"', self.script, re.MULTILINE))

        if resources == 0:
            return 0.0

        return (locals_ + modules) / resources