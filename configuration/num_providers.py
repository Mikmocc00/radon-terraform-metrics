import hcl2


class NumProviders:

    def __init__(self, script):
        self.script = script

    def _parse(self):

        try:
            return hcl2.loads(self.script)
        except Exception:
            return {}

    def count(self):

        parsed = self._parse()

        providers = parsed.get("provider", [])

        names = set()

        for provider in providers:
            for name in provider.keys():
                names.add(name)

        return len(names)