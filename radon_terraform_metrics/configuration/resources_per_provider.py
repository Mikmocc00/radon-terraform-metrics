import hcl2


class ResourcesPerProvider:

    def __init__(self, script):
        self.script = script

    def count(self):

        parsed = parse_hcl(self.script)

        resources = parsed.get("resource", [])
        providers = parsed.get("provider", [])

        nr = 0

        for block in resources:
            for rtype in block:
                nr += len(block[rtype])

        np = len(providers)

        if np == 0:
            return 0

        return nr / np