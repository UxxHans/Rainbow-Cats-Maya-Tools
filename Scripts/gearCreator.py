from maya import cmds
from mayaWindow import TabWindow


class Gear:
    """ This is a gear creator using cmds.polyPipe() in Maya

    The create() function creates the gear with default params.
    The change() function edit the created gear with given params.
    """
    def __init__(self):
        self.default_teeth_count = 10
        self.default_teeth_length = 0.5
        self.default_teeth_width = 0.5
        self.default_teeth_height = 0.25
        self.default_height = 2
        self.default_thickness = 0.35
        self.default_radius = 1.5

        self.model_name = None
        self.transform_name = None
        self.extrude_faces_name = None
        self.create(self.default_teeth_count,
                    self.default_teeth_length,
                    self.default_teeth_width,
                    self.default_teeth_height,
                    self.default_height,
                    self.default_thickness,
                    self.default_radius)

    def create(self,
               teeth_count=10,
               teeth_length=0.5,
               teeth_width=0.5,
               teeth_height=0.5,
               height=1,
               thickness=0.25,
               radius=1.0):

        sides = teeth_count * 2
        self.transform_name, self.model_name = cmds.polyPipe(subdivisionsAxis=sides,
                                                             height=height,
                                                             thickness=thickness,
                                                             radius=radius)
        cmds.select(clear=True)
        for face_index in range(sides * 2, sides * 3, 2):
            cmds.select('%s.f[%s]' % (self.transform_name, face_index), add=True)
        self.extrude_faces_name = cmds.polyExtrudeFacet(localTranslateZ=teeth_length,
                                                        localScaleX=teeth_width,
                                                        localScaleY=teeth_height)[0]
        cmds.select(clear=True)

    def change(self, teeth_count, teeth_length, teeth_width, teeth_height, height, thickness, radius):
        sides = teeth_count * 2
        cmds.polyPipe(self.model_name, edit=True,
                      subdivisionsAxis=sides,
                      height=height,
                      thickness=thickness,
                      radius=radius)

        renewed_extrude_face_names = []
        for face_index in range(sides * 2, sides * 3, 2):
            face_name = 'f[%s]' % face_index
            renewed_extrude_face_names.append(face_name)

        cmds.setAttr('%s.inputComponents' % self.extrude_faces_name,
                     len(renewed_extrude_face_names),
                     *renewed_extrude_face_names, type="componentList")

        cmds.polyExtrudeFacet(self.extrude_faces_name, edit=True,
                              localTranslateZ=teeth_length,
                              localScaleX=teeth_width,
                              localScaleY=teeth_height)


class Window(TabWindow):
    """ This is a user interface to modify the gear using the gear object.

    The window inherits the tab window and creates tab pages.
    It mainly uses the cmds.floatSliderGrp() which is a convenient way to create slider interfaces.
    """
    def __init__(self):
        self.gear = Gear()

        self.height_slider = None
        self.thickness_slider = None
        self.radius_slider = None

        self.teeth_count_slider = None
        self.teeth_length_slider = None
        self.teeth_width_slider = None
        self.teeth_height_slider = None

        super().__init__(window_name="Gear Creator",
                         window_size=(475, 125),
                         tab_builders=[("Basic", self.gear_basic_control_panel),
                                       ("Advanced", self.gear_detail_control_panel)])

    def gear_basic_control_panel(self):
        self.height_slider = cmds.floatSliderGrp(label='Height',
                                                 field=True,
                                                 minValue=0.01,
                                                 maxValue=10.0,
                                                 fieldMinValue=0.01,
                                                 fieldMaxValue=10.0,
                                                 value=self.gear.default_height,
                                                 step=0.01,
                                                 dragCommand=self.change)

        self.thickness_slider = cmds.floatSliderGrp(label='Thickness',
                                                    field=True,
                                                    minValue=0.05,
                                                    maxValue=10.0,
                                                    fieldMinValue=0.01,
                                                    fieldMaxValue=10.0,
                                                    value=self.gear.default_thickness,
                                                    step=0.01,
                                                    dragCommand=self.change)

        self.radius_slider = cmds.floatSliderGrp(label='Radius',
                                                 field=True,
                                                 minValue=0.05,
                                                 maxValue=10.0,
                                                 fieldMinValue=0.01,
                                                 fieldMaxValue=1.0,
                                                 value=self.gear.default_radius,
                                                 step=0.01,
                                                 dragCommand=self.change)

    def gear_detail_control_panel(self):
        self.teeth_count_slider = cmds.intSliderGrp(label='Teeth Count',
                                                    field=True,
                                                    minValue=2,
                                                    maxValue=100,
                                                    fieldMinValue=2,
                                                    fieldMaxValue=100,
                                                    value=self.gear.default_teeth_count,
                                                    dragCommand=self.change)

        self.teeth_length_slider = cmds.floatSliderGrp(label='Teeth Length',
                                                       field=True,
                                                       minValue=0.01,
                                                       maxValue=10.0,
                                                       fieldMinValue=0,
                                                       fieldMaxValue=10.0,
                                                       value=self.gear.default_teeth_length,
                                                       step=0.01,
                                                       dragCommand=self.change)

        self.teeth_width_slider = cmds.floatSliderGrp(label='Teeth Width',
                                                      field=True,
                                                      minValue=0,
                                                      maxValue=2.0,
                                                      fieldMinValue=0,
                                                      fieldMaxValue=2.0,
                                                      value=self.gear.default_teeth_width,
                                                      step=0.01,
                                                      dragCommand=self.change)

        self.teeth_height_slider = cmds.floatSliderGrp(label='Teeth Height',
                                                       field=True,
                                                       minValue=0,
                                                       maxValue=2.0,
                                                       fieldMinValue=0,
                                                       fieldMaxValue=2.0,
                                                       value=self.gear.default_teeth_height,
                                                       step=0.01,
                                                       dragCommand=self.change)

    def change(self, value):
        height = cmds.floatSliderGrp(self.height_slider, query=True, value=True)
        thickness = cmds.floatSliderGrp(self.thickness_slider, query=True, value=True)
        radius = cmds.floatSliderGrp(self.radius_slider, query=True, value=True)

        teeth_count = cmds.intSliderGrp(self.teeth_count_slider, query=True, value=True)
        teeth_length = cmds.floatSliderGrp(self.teeth_length_slider, query=True, value=True)
        teeth_width = cmds.floatSliderGrp(self.teeth_width_slider, query=True, value=True)
        teeth_height = cmds.floatSliderGrp(self.teeth_height_slider, query=True, value=True)

        self.gear.change(height=height,
                         thickness=thickness,
                         radius=radius,
                         teeth_count=teeth_count,
                         teeth_length=teeth_length,
                         teeth_width=teeth_width,
                         teeth_height=teeth_height)
