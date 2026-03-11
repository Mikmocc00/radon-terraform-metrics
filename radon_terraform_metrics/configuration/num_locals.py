import hcl2


class NumLocals:

    def __init__(self, script):
        self.script = script

    def _parse(self):

        try:
            return hcl2.loads(self.script)
        except Exception:
            return {}

    def count(self):

        parsed = self._parse()

        locals_blocks = parsed.get("locals", [])

        total = 0

        for block in locals_blocks:
            total += len(block)

        return total