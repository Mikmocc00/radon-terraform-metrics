import hcl2


class ResourceTypeDiversity:

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

        types = set()

        for r in resources:
            for t in r.keys():
                types.add(t)

        return len(types)