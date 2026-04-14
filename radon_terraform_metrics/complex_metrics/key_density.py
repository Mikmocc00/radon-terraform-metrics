import hcl2
import re


def parse_hcl(script):
    try:
        return hcl2.loads(script)
    except Exception:
        return {}


class KeyDensity:
    """
    Densità di configurazione:
    numero di chiavi per risorsa Terraform.
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        parsed = parse_hcl(self.script)

        resources = parsed.get("resource", [])

        total_resources = 0
        for block in resources:
            for rtype in block:
                total_resources += len(block[rtype])

        pattern = r'^\s*[a-zA-Z0-9_\-]+\s*='
        total_keys = len(re.findall(pattern, self.script, re.MULTILINE))

        if total_resources == 0:
            return 0

        return total_keys / total_resources