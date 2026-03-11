import hcl2


class NumResources:

    def __init__(self, script):
        self.script = script

    def _parse(self):

        try:
            return hcl2.loads(self.script)
        except Exception:
            return {}

    def count(self):

        parsed = self._parse()

        resources = parsed.get("resource", [])

        return len(resources)(resources)