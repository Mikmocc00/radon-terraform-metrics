import hcl2


class NumLoops:

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

        loops = 0

        for r in resources:
            for resource_type in r.values():
                for resource_body in resource_type.values():

                    if "count" in resource_body:
                        loops += 1

                    if "for_each" in resource_body:
                        loops += 1

        return loops