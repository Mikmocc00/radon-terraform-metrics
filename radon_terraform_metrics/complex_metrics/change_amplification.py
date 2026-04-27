from ..configuration.avg_dependencies_per_resource import AvgDependenciesPerResource
from ..configuration.variable_reference_count import VariableReferenceCount


class ChangeAmplification:
    """
    Amplificazione cambiamenti:
    avg_dependencies_per_resource * variable_reference_count
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        avg_deps = AvgDependenciesPerResource(self.script).count()
        var_refs = VariableReferenceCount(self.script).count()

        return avg_deps * var_refs