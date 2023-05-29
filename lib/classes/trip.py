from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        visitor.trips(self)
        visitor.national_parks(national_park)
        national_park.trips(self)
        national_park.visitors(visitor)
        Trip.all.append(self)

    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor
        else:
            raise Exception("Invalid visitor")
        
    def get_national_park(self):
        return self._national_park
    
    def set_national_park(self, national_park):
        if type(national_park) == NationalPark:
            self._national_park = national_park
        else:
            raise Exception("Invalid national park!")

    visitor = property(get_visitor, set_visitor)
    national_park = property(get_national_park, set_national_park)