class Character():
    def __init__(self, health=20, armour=10):
        self._health = health
        self._armour = armour
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferDamage = self._health + self._armour - damage

        if sufferDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def getHealth(self):
        return self._health

    def isAlive(self):
        return self._isAlive

def handleEvents(events):
    eventHandlers = {
        'damage': applyDamage,
        'heal': applyHeal
    }
    list(map(handleEvent, events))

def handleEvent(event):
    eventHandlers[event['type']](event)

def applyHeal(event):
    event['character'].heal(event['size'])

def applyDamage(event):
    event['character'].sufferDamage(event['size'])
