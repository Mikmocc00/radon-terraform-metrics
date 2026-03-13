import hcl2


class ExplicitDependencies:

    def __init__(self, script):
        self.script = script

    def count(self):

        parsed = parse_hcl(self.script)

        resources = parsed.get("resource", [])

        deps = 0

        for block in resources:

            for rtype, instances in block.items():

                for name, body in instances.items():

                    if not isinstance(body, dict):
                        continue

                    if "depends_on" in body:

                        depends = body["depends_on"]

                        if isinstance(depends, list):
                            deps += len(depends)
                        else:
                            deps += 1

        return deps