from ..configuration.num_dynamic_blocks import NumDynamicBlocks
from ..configuration.num_conditionals import NumConditionals
from ..configuration.num_loops import NumLoops
from ..configuration.avg_resource_size import AvgResourceSize


class DynamicComplexity:
    """
    Complessità dinamica:
    (dynamic + conditionals + loops) * dimensione media risorse
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        dynamic = NumDynamicBlocks(self.script).count()
        cond = NumConditionals(self.script).count()
        loops = NumLoops(self.script).count()
        avg_size = AvgResourceSize(self.script).count()

        return (dynamic + cond + loops) * avg_size