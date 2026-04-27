from ..configuration.variable_reference_count import VariableReferenceCount
from ..configuration.implicit_dependencies import ImplicitDependencies
from ..configuration.module_fan_in import ModuleFanIn
from ..configuration.num_resources import NumResources


class CouplingPressure:
    """
    Pressione di accoppiamento:
    (variable refs + implicit deps + module fan-in) / risorse
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        var_refs = VariableReferenceCount(self.script).count()
        implicit = ImplicitDependencies(self.script).count()
        fan_in = ModuleFanIn(self.script).count()
        resources = NumResources(self.script).count()

        if resources == 0:
            return 0.0

        return (var_refs + implicit + fan_in) / resources