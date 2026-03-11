import hcl2


class AvgDependenciesPerResource:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = parsed.get("resource", [])

        nr = len(resources)

        deps = 0

        for r in resources:
            for t in r.values():
                for body in t.values():

                    d = body.get("depends_on")

                    if d:
                        deps += len(d)

        if nr == 0:
            return 0

        return deps / nr