class CarFactory:

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine
        engine = CapuletEngine(current_mileage, last_service_mileage)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create car
        car = Car(engine, battery)

        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create car
        car = Car(engine, battery)

        return car

    def create_palindrome(current_date, last_service_date, warning_light_on):
        # create engine
        engine = SternmanEngine(warning_light_on)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create car
        car = Car(engine, battery)

        return car
        
    def create_roschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # create battery
        battery =  NubbinBattery(last_service_date, current_date)

        # create car
        car = Car(engine, battery)

        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # create engine
        engine = CapuletEngine(current_mileage, last_service_mileage)

        # create battery
        battery =  NubbinBattery(last_service_date, current_date)

        # create car
        car = Car(engine, battery)

        return car

    