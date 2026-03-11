import hcl2


class VariableDefaultRatio:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        variables = parsed.get("variable", [])

        total = len(variables)

        if total == 0:
            return 0

        with_default = 0

        for v in variables:
            for name, body in v.items():

                if "default" in body:
                    with_default += 1

        return with_default / total