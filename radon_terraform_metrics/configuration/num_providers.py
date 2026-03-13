import hcl2


class NumProviders:

    def __init__(self, script):
        self.script = script

    def count(self):

        parsed = parse_hcl(self.script)

        providers = parsed.get("provider", [])

        names = set()

        for block in providers:
            for name in block:
                names.add(name)

        return len(names)