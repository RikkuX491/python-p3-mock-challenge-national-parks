class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        NationalPark.all.append(self)
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if type(new_trip) == Trip:
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if type(new_visitor) == Visitor:
            self._visitors.append(new_visitor)
        return list(set(self._visitors))
    
    def total_visits(self):
        return len([trip for trip in self._trips])
    
    def best_visitor(self):
        max_visitor = None
        max_visits = 0
        for v in self._visitors:
            v_visits = len([t for t in self._trips if t.visitor == v])
            if v_visits > max_visits:
                max_visits = v_visits
                max_visitor = v
            return max_visitor

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not hasattr(self, 'name') and type(name) == str:
            self._name = name
        else:
            raise Exception("Invalid name!")

    name = property(get_name, set_name)