class NationalPark:
    all=[]
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self,"name") and (len(name) >= 3):
            self._name = name

    def trips(self):
        '''Returns a list of all trips at a particular national park. Trips must be of type Trip'''
        return [t for t in Trip.all if t.national_park is self]
    
    def visitors(self):
        '''Returns a unique list of all visitors a particular national park has welcomed. Visitors must be of type Visitor'''
        return list({t.visitor for t in Trip.all if t.national_park is self})
    
    def total_visits(self):
        '''Returns the total number of times a park has been visited'''
        if self.trips() == []:
            return 0
        else:
            return len(self.trips())
    
    def best_visitor(self):
        '''Returns the Visitor instance that has visited that park the most. Returns None if the park has no visitors''' 
        visitors = [t.visitor for t in self.trips()]
        return max(set(visitors), key=visitors.count)

    @classmethod
    def most_visited(cls):
        '''Returns the NationalPark instance with the most visits.Returns None if there are no visits.'''
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,start_date):
        if isinstance(start_date,str) and (len(start_date)>=7):
            self._start_date = start_date 

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self,end_date):
        if isinstance(end_date,str) and (len(end_date)>=7):
            self._end_date = end_date 

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor,Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,national_park):
        if isinstance(national_park,NationalPark):
            self._national_park = national_park


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception
        
    def trips(self):
        '''Returns a list of all trips for that visitor. Trips must be of type Trip'''
        return [t for t in Trip.all if t.visitor is self]
    
    def national_parks(self):
        '''Returns a unique list of all parks that visitor has visited. Parks must be of type NationalPark'''
        return list({t.national_park for t in Trip.all if t.visitor is self})
    
    def total_visits_at_park(self, park):
        ''' Receives a NationalPark object as argument. 
            Returns the total number of times a visitor visited the park passed in as argument
            Returns 0 if the visitor has never visited the park
        '''
        # x = [i for i in self.all if i.national_park is park]
        # if x == []:
        #     return 0
        # else:
        #     return len(x)
        if not park.visitors():
            return 0
        return len([t for t in self.trips() if trip.national_park == park])