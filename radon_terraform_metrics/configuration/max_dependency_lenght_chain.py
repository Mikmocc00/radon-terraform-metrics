import re
import hcl2
from radon_terraform_metrics.utils import all_values


class MaxDependencyChainLength:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        # pattern per trovare riferimenti terraform
        pattern = re.compile(r"([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\.[a-zA-Z0-9_]+")

        graph = {}

        # costruzione nodi
        if "resource" in parsed:
            for r in parsed["resource"]:
                for rtype, blocks in r.items():
                    for name, attrs in blocks.items():
                        node = f"{rtype}.{name}"
                        graph[node] = []

        # estrazione dipendenze implicite
        values = all_values(parsed)

        for v in values:

            if isinstance(v, str):

                matches = pattern.findall(v)

                for m in matches:

                    if m not in graph:
                        graph[m] = []

        # aggiunta archi impliciti
        for r in parsed.get("resource", []):

            for rtype, blocks in r.items():

                for name, attrs in blocks.items():

                    node = f"{rtype}.{name}"

                    values = all_values(attrs)

                    for v in values:

                        if isinstance(v, str):

                            matches = pattern.findall(v)

                            for dep in matches:

                                graph[node].append(dep)

        # aggiunta archi espliciti
        for r in parsed.get("resource", []):

            for rtype, blocks in r.items():

                for name, attrs in blocks.items():

                    node = f"{rtype}.{name}"

                    if "depends_on" in attrs:

                        for dep in attrs["depends_on"]:

                            if isinstance(dep, str):

                                graph[node].append(dep)

        # DFS per longest path
        memo = {}

        def dfs(node):

            if node in memo:
                return memo[node]

            if node not in graph or len(graph[node]) == 0:
                memo[node] = 1
                return 1

            max_depth = 1

            for neigh in graph[node]:

                depth = 1 + dfs(neigh)

                if depth > max_depth:
                    max_depth = depth

            memo[node] = max_depth
            return max_depth

        max_chain = 0

        for node in graph:

            depth = dfs(node)

            if depth > max_chain:
                max_chain = depth

        return max_chain