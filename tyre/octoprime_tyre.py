from tyre.tyre import Tyre

class OctoprimeTyre:

    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear

    # override abstract method
    def needs_service(self):
        for tyre in self.tyre_wear:
            if tyre >= 3:
                return True
        return False