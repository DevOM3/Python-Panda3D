from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file

load_prc_file("config/no1.prc")


class Game(ShowBase):
    def __init__(self):
        super(Game, self).__init__()

        self.disableMouse()

        # accepting mouse inputs
        self.accept("mouse1", self.mouse_click)
        self.accept("mouse1-up", self.mouse_click)

        self.accept("mouse2", self.mouse_click)
        self.accept("mouse2-up", self.mouse_click)

        self.accept("mouse3", self.mouse_click)
        self.accept("mouse3-up", self.mouse_click)

        self.taskMgr.add(self.update, "update")

    def mouse_click(self):
        # getting mouse co-ordinates
        md1 = self.win.getPointer(0)
        # printing mouse click points and release points
        print(md1.getX(), md1.getY())

        # get the relative axis position of mouse click
        md2 = self.mouseWatcherNode.getMouse()
        print(md2.getX(), md2.getY())

    def update(self, task):
        # getting the mouse position from 1280 to 720px
        mouse_pos = self.win.getPointer(0)
        print(mouse_pos.getX(), mouse_pos.getY())

        # getting the mouse position on the axis
        # below condition is necessary or the window will crash of cursor is out of it
        if self.mouseWatcherNode.hasMouse():
            x = self.mouseWatcherNode.getMouseX()
            y = self.mouseWatcherNode.getMouseY()
            print(x, y)

        return task.cont


game = Game()
game.run()
