import re

class CouplingScore:
    """
    Accoppiamento:
    (riferimenti impliciti + moduli) / linee di codice
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        implicit = len(re.findall(r'\b[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+', self.script))
        modules = len(re.findall(r'\bmodule\s+"', self.script))

        loc = len(self.script.splitlines())

        if loc == 0:
            return 0.0

        return (implicit + modules) / loc