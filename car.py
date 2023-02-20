class Car(Serviceable):
     
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    # overriding abstract method
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False