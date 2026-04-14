import re

class ComplexityScore:
    """
    Complessità strutturale:
    (dynamic + conditionals + provisioners) / resources
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        dynamic = len(re.findall(r'\bdynamic\s+"', self.script))
        conditionals = len(re.findall(r'\?.*:', self.script))
        provisioners = len(re.findall(r'\bprovisioner\s+"', self.script))

        resources = len(re.findall(r'^\s*resource\s+"', self.script, re.MULTILINE))

        if resources == 0:
            return 0.0

        return (dynamic + conditionals + provisioners) / resources