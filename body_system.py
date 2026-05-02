class BodySystem:

    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)
        
    def remove_body(self, body):
        self.bodies.remove(body)