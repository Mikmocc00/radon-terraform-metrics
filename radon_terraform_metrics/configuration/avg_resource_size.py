import re


class AvgResourceSize:

    def __init__(self, script):
        self.script = script

    def count(self):

        resources = re.findall(
            r'resource\s+"[^"]+"\s+"[^"]+"\s*{[^}]*}',
            self.script,
            re.DOTALL
        )

        if not resources:
            return 0

        sizes = [len(r.splitlines()) for r in resources]

        return int(sum(sizes) / len(sizes))