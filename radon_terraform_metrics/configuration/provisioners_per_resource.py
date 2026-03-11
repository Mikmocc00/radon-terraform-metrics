import hcl2


class ProvisionersPerResource:

    def __init__(self, script):
        self.script = script

    def count(self):

        try:
            parsed = hcl2.loads(self.script)
        except Exception:
            return 0

        resources = parsed.get("resource", [])

        nr = len(resources)

        provisioners = 0

        for r in resources:
            for t in r.values():
                for body in t.values():

                    prov = body.get("provisioner")

                    if prov:
                        provisioners += len(prov)

        if nr == 0:
            return 0

        return provisioners / nr