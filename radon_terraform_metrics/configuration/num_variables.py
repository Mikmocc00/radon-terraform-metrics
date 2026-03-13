import hcl2


class NumVariables:

    def count(self):

        parsed = self._parse()

        variables = parsed.get("variable", [])

        total = 0

        for v in variables:
            total += len(v)

        return total