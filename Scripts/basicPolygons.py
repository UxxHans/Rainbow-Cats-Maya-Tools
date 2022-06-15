from maya import cmds


class Cube(object):
    """
    A simple cube object that tests all the parameters in cmds.polyCube() in Maya.
    """
    def __init__(self, height=1, width=1):
        self.construct = None
        self.create(height, width)

    def create(self, height=1, width=1):
        self.construct = cmds.polyCube(height=height, width=width)

    def edit_cube_axis_x(self, x):
        axis = cmds.polyCube(q=True, axis=True)
        cmds.polyCube(self.construct, e=True, axis=[x, axis[1], axis[2]])

    def edit_cube_axis_y(self, y):
        axis = cmds.polyCube(q=True, axis=True)
        cmds.polyCube(self.construct, e=True, axis=[axis[0], y, axis[2]])

    def edit_cube_axis_z(self, z):
        axis = cmds.polyCube(q=True, axis=True)
        cmds.polyCube(self.construct, e=True, axis=[axis[0], axis[1], z])

    def edit_cube_depth(self, v):
        cmds.polyCube(self.construct, e=True, depth=v)

    def edit_cube_height(self, v):
        cmds.polyCube(self.construct, e=True, height=v)

    def edit_cube_width(self, v):
        cmds.polyCube(self.construct, e=True, width=v)

    def edit_cube_subdivisions_depth(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsDepth=v)

    def edit_cube_subdivisions_height(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsHeight=v)

    def edit_cube_subdivisions_width(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsWidth=v)

    def edit_cube_subdivisions_x(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsX=v)

    def edit_cube_subdivisions_y(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsY=v)

    def edit_cube_subdivisions_z(self, v):
        cmds.polyCube(self.construct, e=True, subdivisionsZ=v)
