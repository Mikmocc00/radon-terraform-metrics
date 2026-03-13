import hcl2


class VariablesPerResource:

    def __init__(self, script):
        self.script = script

    def count(self):

        parsed = parse_hcl(self.script)

        variables = parsed.get("variable", [])
        resources = parsed.get("resource", [])

        nv = 0
        for v in variables:
            nv += len(v)

        nr = 0
        for block in resources:
            for rtype in block:
                nr += len(block[rtype])

        if nr == 0:
            return 0

        return nv / nr