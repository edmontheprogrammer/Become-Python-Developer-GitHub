""" Validate external input """

""" Overloading a Circuit Breaker """

class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps # max capacity in amps
        self.load = 0

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('connect will exceed capacity')
        elif self.load + amps < 0:
            raise Exception('connect will cause negative load')
        else:
            self.load += amps


# Create a 20A circuit breaker
cb = CircuitBreaker(20)
