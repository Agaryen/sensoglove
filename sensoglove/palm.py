from rotation import Rotation

class Speed:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

class Palm:
    def __init__(self, data):
        palm = data['data']['palm']
        self.rotation = Rotation(palm['quat'][1], palm['quat'][2], palm['quat'][3])
        self.speed = Speed(palm['spd'][0], palm['spd'][1], palm['spd'][2])
        self.acceleration = Speed(palm['acc'][0], palm['acc'][1], palm['acc'][2])
        self.accuration = palm['accuracy']
