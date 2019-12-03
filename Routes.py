from datetime import date, timedelta
from copy import deepcopy

class Route:
    def __init__(self, destination_id = 0, outbound_departure = date(1,1,1), returning_departure = date(1,1,1), employees = [], pilots = [], head_pilot = 0, assistants = [], head_assistant = []):
        self.destination_id = destination_id
        self.outbound_departure = outbound_departure
        self.returning_departure = returning_departure
        self.employees = employees
        self.pilots = pilots
        self.head_pilot = head_pilot
        self.assistants = assistants
        self.head_assistant = head_assistant

    def repeat_after(self, time = timedelta(0)):
        new_route = deepcopy(self)
 
        new_route.outbound_departure += time
        new_route.returning_departure += time

    def is_valid(self):
        return self.pilots.len() >= 2 and self.assistants.len() >= 1 and self.head_pilot != 0 and self.head_assistant != 0 and self.head_pilot in self.pilots and self.head_assistant in self.assistants

class Routes:
    def __init__(self):
        self._routes = []

    def add_route(self, route):
        route.id = self._routes.len()
        self._routes.append(route)

