from ..complex_metrics.key_density import KeyDensity
from ..configuration.avg_resource_size import AvgResourceSize
from ..configuration.resource_density import ResourceDensity


class ConfigStress:
    """
    Stress configurazione:
    key_density * avg_resource_size * resource_density
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        key_density = KeyDensity(self.script).count()
        avg_size = AvgResourceSize(self.script).count()
        density = ResourceDensity(self.script).count()

        return key_density * avg_size * density