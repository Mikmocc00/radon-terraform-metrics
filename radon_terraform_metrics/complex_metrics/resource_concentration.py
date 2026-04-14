from radon_terraform_metrics.configuration.max_resources_per_file import MaxResourcesPerFile
from radon_terraform_metrics.configuration.avg_resource_size import AvgResourceSize


class ResourceConcentration:
    """
    Misura quanto le risorse sono concentrate confrontando
    il picco massimo per file con la dimensione media dei blocchi.
    Formula: max_resources_per_file / avg_resource_size
    Alto = molte risorse concentrate in un file con blocchi piccoli.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        max_res = MaxResourcesPerFile(self.script).count()
        avg_size = AvgResourceSize(self.script).count()

        if avg_size == 0:
            return 0.0

        return max_res / avg_size
