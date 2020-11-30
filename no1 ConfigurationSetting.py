from panda3d.core import load_prc_file
from direct.showbase.ShowBase import ShowBase

load_prc_file("config/no1.prc")


class First(ShowBase):
    def __init__(self):
        super().__init__()


f = First()
f.run()
