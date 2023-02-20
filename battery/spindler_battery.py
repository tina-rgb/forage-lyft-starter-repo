from datetime import date

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    # overriding abstract method
    def needs_service(self):
        
        # update current date
        self.current_date = date.today()

        # check if service threshold date reached
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False