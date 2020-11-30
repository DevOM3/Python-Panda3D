from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        # loading box.load panda3d file
        box = self.loader.loadModel("models/box")
        # positioning the box using the setPos() method accepting x, y, z as argument
        box.setPos(0, 11, 1)
        # rendering a box using reparentTo()
        box.reparentTo(self.render)

        panda = self.loader.loadModel("models/panda")
        panda.setPos(-2, 12, -1)
        # scaling the panda using setScale() method taking x, y, z, as argument
        panda.setScale(0.2, 0.2, 0.2)
        panda.reparentTo(self.render)


game = Game()
game.run()
