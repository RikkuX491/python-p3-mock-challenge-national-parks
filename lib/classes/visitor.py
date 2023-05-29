class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []
        Visitor.all.append(self)
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if type(new_trip) == Trip:
            self._trips.append(new_trip)
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if type(new_national_park) == NationalPark:
            self._national_parks.append(new_national_park)
        return list(set(self._national_parks))

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not hasattr(self, 'name') and type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Invalid name!")

    name = property(get_name, set_name)