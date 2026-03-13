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

        total = 0

        for r in resources:
            for resource_type in r.values():
                total += len(resource_type)

        return total