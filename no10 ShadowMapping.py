from math import sin, cos
from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file, NodePath, PointLight, AmbientLight

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        self.cam.setPos(0, -10, 0)
        self.set_background_color(0, 0, 0, 1)

        self.trees = NodePath("trees")

        self.tree1 = self.loader.loadModel("myeggs/tree")
        self.tree1.setPos(0, 0, -2.5)
        self.tree1.reparentTo(self.trees)

        self.camera1 = self.loader.loadModel("models/camera")
        self.camera1.setPos(4, 5, -1.5)
        self.camera1.setColor(1, 0, 1, 1)
        self.camera1.reparentTo(self.trees)

        self.cube = self.loader.loadModel("models/box")
        self.cube.setPos(-4, 7, -2.5)
        self.cube.reparentTo(self.trees)

        self.panda = self.loader.loadModel("models/panda")
        self.panda.setPos(2, 9, -2.5)
        self.panda.setScale(0.2)
        self.panda.reparentTo(self.trees)

        self.trees.reparentTo(self.render)

        self.floor = self.loader.loadModel("myeggs/floor")
        self.floor.setPos(0, 0, -2.5)
        self.floor.reparentTo(self.render)

        self.sun = self.loader.loadModel("models/misc/sphere")
        self.sun.setScale(0.2)
        self.sun.reparentTo(self.render)

        point_light = PointLight("point_light")
        point_light.setShadowCaster(True, 512, 512)
        self.render.setShaderAuto()
        point_light_node_path = self.sun.attachNewNode(point_light)
        self.trees.setLight(point_light_node_path)

        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.04, 0.04, 0.04, 1))
        ambient_light_node_path = self.render.attachNewNode(ambient_light)
        self.trees.setLight(ambient_light_node_path)

        self.floor.setLight(point_light_node_path)
        self.floor.setLight(ambient_light_node_path)

        self.taskMgr.add(self.move_light, "move_light")

    def move_light(self, task):
        ft = globalClock.getFrameTime()

        self.sun.setPos(cos(ft) * 4, sin(ft) * 4, 0)

        return task.cont


game = Game()
game.run()
