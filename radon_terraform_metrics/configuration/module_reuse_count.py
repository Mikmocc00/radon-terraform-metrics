import hcl2
from collections import Counter


class ModuleReuseCount:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        modules = parsed.get("module", [])

        sources = []

        for m in modules:
            for name, body in m.items():

                src = body.get("source")

                if src:
                    sources.append(src)

        if not sources:
            return 0

        c = Counter(sources)

        reuse = 0

        for s in c:
            if c[s] > 1:
                reuse += c[s]

        return reuse