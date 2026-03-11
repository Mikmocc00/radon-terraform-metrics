import re
import hcl2


class VariableReferenceCount:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        # numero di variabili dichiarate
        if "variable" not in parsed:
            return 0

        variables = []

        for v in parsed["variable"]:
            for name in v.keys():
                variables.append(name)

        nv = len(variables)

        if nv == 0:
            return 0

        # trova riferimenti alle variabili
        pattern = re.compile(r"var\.([a-zA-Z0-9_]+)")
        matches = pattern.findall(self.script)

        # conteggio references per variabile
        ref_count = {v: 0 for v in variables}

        for m in matches:
            if m in ref_count:
                ref_count[m] += 1

        total_refs = sum(ref_count.values())

        return total_refs / nv