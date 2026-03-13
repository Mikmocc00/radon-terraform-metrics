import hcl2


class NumModules:

    def count(self):

        parsed = self._parse()

        modules = parsed.get("module", [])

        total = 0

        for m in modules:
            total += len(m)

        return total