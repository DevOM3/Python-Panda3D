from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file, PointLight
from math import sin, cos

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -15, 0)
        self.set_background_color(0, 0, 0, 1)

        self.cam_model = self.loader.loadModel("models/camera")
        self.cam_model.setHpr(240, 0, 0)
        self.cam_model.setColor(1, 0, 0, 1)
        self.cam_model.reparentTo(self.render)

        self.sun = self.loader.loadModel("models/misc/sphere")
        self.sun.setScale(0.3)
        self.sun.setColor(1, 1, 1, 1)
        self.sun.reparentTo(self.render)

        # specifying light variables
        self.lightX = 0
        self.lightSpeed = 2

        # making the reference of point light
        point_light = PointLight("point_light")
        # setting point light color
        point_light.setColor((1, 1, 1, 1))
        # crating point light node path
        self.point_light_node_path = self.render.attachNewNode(point_light)
        # setting node path position
        self.point_light_node_path.setPos(2, 0, 0)
        # rendering a light
        self.cam_model.setLight(self.point_light_node_path)

        self.taskMgr.add(self.move_light, "move_light")

    def move_light(self, task):
        dt = globalClock.getDt()

        self.point_light_node_path.setPos(cos(self.lightX) * 4, sin(self.lightX) * 4, 0)
        self.sun.setPos(self.point_light_node_path.getPos())
        self.lightX += self.lightSpeed * dt
        # self.lightSpeed

        return task.cont


game = Game()
game.run()
