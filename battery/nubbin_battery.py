from battery.battery import Battery

class NubbinBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    # overriding abstract method
    def needs_service(self):
        
        # check if service threshold date reached
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False