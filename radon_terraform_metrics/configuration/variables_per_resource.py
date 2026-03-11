import hcl2


class VariablesPerResource:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        nv = len(parsed.get("variable", []))
        nr = len(parsed.get("resource", []))

        if nr == 0:
            return 0

        return nv / nr