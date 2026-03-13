import hcl2


class NumOutputs:

    def count(self):

        parsed = self._parse()

        outputs = parsed.get("output", [])

        total = 0

        for o in outputs:
            total += len(o)

        return total