import hcl2


class NumDataSources:

    def __init__(self, script):
        self.script = script

    def _parse(self):

        try:
            return hcl2.loads(self.script)
        except Exception:
            return {}

    def count(self):

        parsed = self._parse()

        data_sources = parsed.get("data", [])

        return len(data_sources)