import hcl2


class ResourcesPerProvider:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = parsed.get("resource", [])
        providers = parsed.get("provider", [])

        nr = len(resources)
        np = len(providers)

        if np == 0:
            return 0

        return nr / np