class Subject:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, obs):
        self.observers.append(obs)
    
    def notify(self, entity, event):
        for obs in self.observers:
            obs.on_notify(entity, event)
