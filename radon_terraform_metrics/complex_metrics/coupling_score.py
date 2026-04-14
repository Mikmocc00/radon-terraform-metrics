from radon_terraform_metrics.configuration.implicit_dependencies import ImplicitDependencies
from radon_terraform_metrics.configuration.module_fan_in import ModuleFanIn
from radon_terraform_metrics.general.lines_code import LinesCode



class CouplingScore:
    """
    Misura quanto il file è accoppiato ad altri moduli/risorse esterne.
    Formula: (implicit_dependencies + module_fan_in) / lines_code
    Alto = forte dipendenza da entità esterne al file.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        implicit = ImplicitDependencies(self.script).count()
        fan_in = ModuleFanIn(self.script).count()
        loc = LinesCode(self.script).count()

        if loc == 0:
            return 0.0

        return (implicit + fan_in) / loc