import hcl2
from implicit_dependencies import ImplicitDependencies
from explicit_dependencies import ExplicitDependencies


class DependencyGraphDensity:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        # Numero di risorse
        resources = 0

        if "resource" in parsed:
            for r in parsed["resource"]:
                for _, blocks in r.items():
                    resources += len(blocks)

        # Evita divisioni strane
        if resources <= 1:
            return 0

        # Numero di archi del grafo
        implicit_deps = ImplicitDependencies(self.script).count()
        explicit_deps = ExplicitDependencies(self.script).count()

        edges = implicit_deps + explicit_deps

        max_possible_edges = resources * (resources - 1)

        return edges / max_possible_edges