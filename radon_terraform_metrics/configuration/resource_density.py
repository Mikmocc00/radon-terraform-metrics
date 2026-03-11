import hcl2
from radon_terraform_metrics.general.lines_code import LinesCode


class ResourceDensity:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = parsed.get("resource", [])

        nr = len(resources)
        loc = LinesCode(self.script).count()

        if loc == 0:
            return 0

        return nr / loc