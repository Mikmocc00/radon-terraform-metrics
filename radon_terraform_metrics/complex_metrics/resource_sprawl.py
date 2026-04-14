import re

class ResourceSprawl:
    """
    Sprawl risorse:
    num_resources / diversità tipi
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        resource_types = re.findall(r'resource\s+"([^"]+)"', self.script)
        resources = len(resource_types)
        diversity = len(set(resource_types))

        if diversity == 0:
            return 0.0

        return resources / diversity