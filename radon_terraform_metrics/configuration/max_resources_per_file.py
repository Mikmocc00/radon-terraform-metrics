import hcl2


class MaxResourcesPerFile:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = 0

        if "resource" in parsed:
            for r in parsed["resource"]:
                for _, blocks in r.items():
                    resources += len(blocks)

        return resources