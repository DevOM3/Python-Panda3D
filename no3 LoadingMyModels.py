from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        my_model = self.loader.loadModel("myeggs/first")
        my_model.setPos(-2, 10, 0)
        my_model.reparentTo(self.render)


game = Game()
game.run()
