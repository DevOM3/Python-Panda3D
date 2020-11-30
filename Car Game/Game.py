from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file
import time

exec_time = time.time()

load_prc_file("config.prc")

move = {
    "forward": False,
    "backward": False,
    "left": False,
    "right": False
}


def move_car(key, val):
    move[key] = val


class Game(ShowBase):
    var = 2

    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -30, 11)
        self.cam.setHpr(0, -21, 0)
        self.disableMouse()

        self.car = self.loader.loadModel("mymodels/Car")
        self.car.setScale(0.4)
        self.car.setPos(0, )
        self.car.reparentTo(self.render)

        self.speed = 2

        self.accept("arrow_up", move_car, ["forward", True])
        self.accept("arrow_up-up", move_car, ["forward", False])

        self.accept("arrow_down", move_car, ["backward", True])
        self.accept("arrow_down-up", move_car, ["backward", False])

        self.accept("arrow_left", move_car, ["left", True])
        self.accept("arrow_left-up", move_car, ["left", False])

        self.accept("arrow_right", move_car, ["right", True])
        self.accept("arrow_right-up", move_car, ["right", False])

        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()

        pos = self.car.getPos()
        cam = self.cam.getPos()
        pos.y += self.speed * self.var * dt
        if exec_time % 50 == 0:
            self.var += 1
        # if pos.y > 7:
        #     cam.y += self.speed * self.var * dt
        self.cam.setPos(cam)
        self.car.setPos(pos)
        if move["backward"]:
            pos = self.car.getPos()
            cam = self.cam.getPos()
            pos.y -= self.speed * dt
            self.cam.setPos(cam)
            self.car.setPos(pos)
        if move["left"]:
            pos = self.car.getPos()
            cam = self.cam.getPos()
            cam.x += self.speed * dt
            pos.x -= self.speed * 11 * dt
            self.cam.setPos(cam)
            self.car.setPos(pos)
        if move["right"]:
            pos = self.car.getPos()
            cam = self.cam.getPos()
            cam.x -= self.speed * dt
            pos.x += self.speed * 11 * dt
            self.cam.setPos(cam)
            self.car.setPos(pos)
        return task.cont















game = Game()
game.run()
