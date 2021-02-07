entityList = []

class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def update():
    for entity in entityList:
        entity.update()

def getEntityList():
    return entityList