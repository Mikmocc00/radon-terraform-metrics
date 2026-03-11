import hcl2


class NumOutputs:

    def __init__(self, script):
        self.script = script

    def _parse(self):

        try:
            return hcl2.loads(self.script)
        except Exception:
            return {}

    def count(self):

        parsed = self._parse()

        outputs = parsed.get("output", [])

        return len(outputs)