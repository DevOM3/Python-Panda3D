from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file, PointLight, AmbientLight
from math import sin, cos

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -15, 0)
        self.set_background_color(0, 0, 0, 1)

        self.camcorder = self.loader.loadModel("models/camera")
        self.camcorder.setHpr(240, 0, 0)
        self.camcorder.setColor(1, 1, 0, 1)
        self.camcorder.reparentTo(self.render)

        self.sun = self.loader.loadModel("models/misc/sphere")
        self.sun.setPos(3, 0, 2)
        self.sun.setScale(0.4)
        self.sun.reparentTo(self.render)

        point_light = PointLight("point_light")
        point_light.setColor((1, 1, 1, 1))
        self.point_light_node_path = self.sun.attachNewNode(point_light)
        self.camcorder.setLight(self.point_light_node_path)

        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.04, 0.04, 0.04, 1))
        ambient_light_node_path = self.render.attachNewNode(ambient_light)
        self.camcorder.setLight(ambient_light_node_path)

        self.taskMgr.add(self.move_light,"move_light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.sun.setPos(cos(ft) * 4, sin(ft) * 4, 0)

        return task.cont


game = Game()
game.run()
