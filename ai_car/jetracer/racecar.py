import traitlets


class Racecar(traitlets.HasTraits):
    steering = traitlets.Float()
    throttle = traitlets.Float()
    
    @traitlets.validate('steering')
    def _clip_steering(self, proposal):
        if proposal['value'] > 3:
            return 3.0
        elif proposal['value'] < -3.0:
            return -3.0
        else:
            return proposal['value']
        
    @traitlets.validate('throttle')
    def _clip_throttle(self, proposal):
        if proposal['value'] > 1.5:
            return 1.5
        elif proposal['value'] < -1.5:
            return -1.5
        else:
            return proposal['value']
