import re
import hcl2
from ..utils import all_values


class ImplicitDependencies:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        values = all_values(parsed)

        pattern = re.compile(r"[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+")

        deps = 0

        for v in values:

            if isinstance(v, str):

                matches = pattern.findall(v)

                deps += len(matches)

        return deps