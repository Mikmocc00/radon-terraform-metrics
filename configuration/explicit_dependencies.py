import hcl2
from utils import all_values


class ExplicitDependencies:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        values = all_values(parsed)

        deps = 0

        for v in values:

            if isinstance(v, dict) and "depends_on" in v:

                depends = v["depends_on"]

                if isinstance(depends, list):
                    deps += len(depends)

                else:
                    deps += 1

        return deps