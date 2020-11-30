from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file
from math import sin, cos

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -15, 0)

        # loading the jack model
        self.jack = self.loader.loadModel("models/jack")
        # Rotation of the object on the H-z_axis, P-x_axis, R-y_axis
        self.jack.setHpr(0, 180, 180)
        self.jack.reparentTo(self.render)

        # loading a panda
        self.panda = self.loader.loadModel("models/panda")
        # single value in setScale() method distributes it for each side equally i.e. setScale(0.2, 0.2, 0.2)
        self.panda.setScale(0.2)
        self.panda.setPos(2, 0, 0)
        self.panda.reparentTo(self.render)

        # loading a teapot model
        self.teapot = self.loader.loadModel("models/teapot")
        # single value in setScale() method distributes it for each side equally i.e. setScale(0.3, 0.3, 0.3)
        self.teapot.setScale(0.3, 0.3, 0.3)
        self.teapot.setPos(-3, 0, 0)
        self.teapot.setColor(1, 0, 0, 1)
        self.teapot.reparentTo(self.render)

        # loading a sphere on the screen
        self.sphere = self.loader.loadModel("models/misc/sphere")
        self.sphere.setScale(0.2)
        self.sphere.setColor(0, 1, 0, 1)
        self.sphere.reparentTo(self.render)

        self.x = 0
        self.speed = 2
        self.angle = 0

        # calling update method to update the window
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()

        # rotating panda on the z-axis
        self.panda.setH(self.angle)

        # rotating the teapot
        self.teapot.setHpr(self.angle, 0, self.angle)

        # rotating the sphere around each other object
        self.sphere.setPos(cos(self.x) * 4, sin(self.x) * 4, cos(self.x) * 2)

        # let jack look at the green sphere
        self.jack.lookAt(self.sphere)

        self.angle += 1
        self.x += self.speed * dt

        return task.cont


game = Game()
game.run()
