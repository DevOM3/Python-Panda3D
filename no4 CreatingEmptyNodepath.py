from panda3d.core import load_prc_file, NodePath
from direct.showbase.ShowBase import ShowBase

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        empty = NodePath("empty")
        model = self.loader.loadModel("models/box")
        model.reparentTo(empty)
        empty.reparentTo(self.render)


game = Game()
game.run()
