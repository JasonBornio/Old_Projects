#physics

class Physics(object):
    def __init__(self, objects):
        super().__init__()
        self.num_steps = 8
        self.objects = objects
        self.gravity = (0, 9.81)
        
    def update(self, dt):
        for i in range(self.num_steps):
            self.apply_gravity()
            self.update_positions(dt)
        return

    def update_positions(self, dt):
        for obj in self.objects:
            obj.updatePosition(dt)
            #print(obj.position_current)
        return 
    
    def apply_gravity(self):
        for obj in self.objects:
            obj.accelerate(self.gravity)
        return
        