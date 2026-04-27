import hcl2


class AvgResourceSize:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = parsed.get("resource", [])

        total_sizes = []
        lines = self.script.splitlines()

        for block in resources:
            for rtype in block:
                for name in block[rtype]:

                    size = len(name.keys())
                    total_sizes.append(size)

        if not total_sizes:
            return 0

        return sum(total_sizes) / len(total_sizes)