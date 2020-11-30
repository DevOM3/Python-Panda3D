from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file

load_prc_file("config/no1.prc")


# dictionary for keyboard inputs
KeyMap = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "rotate": False
}


def update_key_map(key, state):
    KeyMap[key] = state


class Game(ShowBase):
    cnt = 0

    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -15, 0)

        self.jack = self.loader.loadModel("models/jack")
        self.jack.setHpr(180, 0, 0)
        self.jack.reparentTo(self.render)

        self.speed = 4
        self.angle = 0

        # accepting keyboard inputs
        self.accept("arrow_left", update_key_map, ["left", True])
        self.accept("arrow_left-up", update_key_map, ["left", False])

        self.accept("arrow_right", update_key_map, ["right", True])
        self.accept("arrow_right-up", update_key_map, ["right", False])

        self.accept("arrow_up", update_key_map, ["up", True])
        self.accept("arrow_up-up", update_key_map, ["up", False])

        self.accept("arrow_down", update_key_map, ["down", True])
        self.accept("arrow_down-up", update_key_map, ["down", False])

        self.accept("space", update_key_map, ["rotate", True])
        self.accept("space-up", update_key_map, ["rotate", False])

        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()

        pos = self.jack.getPos()

        if KeyMap["left"]:
            pos.x -= self.speed * dt
        if KeyMap["right"]:
            pos.x += self.speed * dt
        if KeyMap["up"]:
            pos.z += self.speed * dt
        if KeyMap["down"]:
            pos.z -= self.speed * dt
        if KeyMap["rotate"]:
            self.angle += 1
            self.jack.setH(self.angle)

        self.jack.setPos(pos)

        return task.cont


game = Game()
game.run()
