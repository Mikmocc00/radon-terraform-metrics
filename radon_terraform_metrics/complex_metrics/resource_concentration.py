import re

class ResourceConcentration:
    """
    Concentrazione risorse:
    max risorse per file / dimensione media blocchi
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        resources = re.findall(r'^\s*resource\s+"', self.script, re.MULTILINE)
        total_resources = len(resources)

        blocks = re.split(r'^\s*resource\s+"', self.script, flags=re.MULTILINE)[1:]
        block_sizes = [len(b.splitlines()) for b in blocks]

        if not block_sizes:
            return 0.0

        avg_size = sum(block_sizes) / len(block_sizes)
        max_res = total_resources

        if avg_size == 0:
            return 0.0

        return max_res / avg_size