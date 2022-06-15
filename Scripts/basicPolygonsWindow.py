from mayaWindow import TabWindow
from basicPolygons import Cube
from maya import cmds


class Window(TabWindow):
    """
    A simple window component that tests all the parameters in cmds.polyCube() in Maya.
    """
    def __init__(self):
        self.cube = Cube()
        super().__init__(tab_builders=[("Cube", self.cube_control_panel)], window_name="Basic Polygon")

    def cube_control_panel(self):
        cmds.floatSliderGrp(label='Axis X', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_axis_x)
        cmds.floatSliderGrp(label='Axis Y', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_axis_y)
        cmds.floatSliderGrp(label='Axis Z', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_axis_z)

        cmds.floatSliderGrp(label='Width', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_width)
        cmds.floatSliderGrp(label='Height', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_height)
        cmds.floatSliderGrp(label='Depth', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_depth)

        cmds.floatSliderGrp(label='Subdivisions X', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_x)
        cmds.floatSliderGrp(label='Subdivisions Y', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_y)
        cmds.floatSliderGrp(label='Subdivisions Z', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_z)

        cmds.floatSliderGrp(label='Subdivisions Width', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_width)
        cmds.floatSliderGrp(label='Subdivisions Height', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_height)
        cmds.floatSliderGrp(label='Subdivisions Depth', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0,
                            fieldMaxValue=100.0, value=0, dragCommand=self.cube.edit_cube_subdivisions_depth)