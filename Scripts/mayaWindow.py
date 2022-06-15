from maya import cmds
from abc import ABC, abstractmethod


class Window(ABC):
    """ Base class of the window UI in Maya.

    This is a base window class to be inherited in Maya.
    build_ui() method should be overridden in the child class to create content in the window.
    """

    def __init__(self, window_name="Default Window", window_size=(500, 500), background_color=[0.2, 0.2, 0.2]):
        """ A window will be created in Maya when the window object is created.

        :param window_name: The title to be shown on the window.
        :param window_size: The size of the window. Format: (width, height)
        :param background_color: The background color of the window.
        """

        self.__background_color = background_color  # Reference of the window, so we can close it.
        self.__window_reference = self.__create(window_name, window_size)  # Background color of the window.
        print("Window Generated.")

    def __create(self, window_name, window_size):
        """ Private method to create a new window with given parameters.

        :param window_name: The title to be shown on the window.
        :param window_size: The size of the window. Format: (width, height)
        :return: It returns a window reference.
        """

        # Window creation.
        window = cmds.window(title=window_name, widthHeight=window_size,
                             backgroundColor=self.__background_color)

        # Add UI in the window.
        self.build_ui()

        # Show the window.
        cmds.showWindow()

        # Return the window reference.
        return window

    @abstractmethod
    def build_ui(self):
        """ Build the UI elements. It is called when the window is first created.

        Must be implemented in child inheritance.
        """

    def get(self):
        """ Get the window reference.

        :return: The window reference, so we can edit the content.
        """
        return self.__window_reference

    def close(self):
        """ Close the window and the object.

        Close the object and window in scripts.
        """
        if self.__window_reference is not None:
            cmds.deleteUI(self.__window_reference, window=True)

        del self


class TabWindow(Window):
    """ Tab window is a class that inherits basic window abstract class.

    Tab window can separate contents into tab pages. Making the tool organized and tidy.
    """

    def __init__(self, tab_builders, window_name="Default Window", window_size=(500, 500)):
        """ When tab window is initialized with the constructor, a window with all the tabs will be created.

        :param tab_builders: Tab builders is a list of tuples that gives tab window orders to initialize.
        The format should be: [("TabName01", InitFunc), ("TabName02", InitFunc), ...]
        """
        self.all_tabs = None                # The reference of the tab layout.
        self.tab_builders = tab_builders    # The reference of the tab builders.
        super().__init__(window_name, window_size)

    def build_ui(self):
        """ The implementation of the build_ui() abstract method.

        It creates tabs and content with the given params.
        """
        # Create all tabs.
        self.all_tabs = cmds.tabLayout()

        # Create each tab page with the given params.
        for i in range(len(self.tab_builders)):
            self.__create(self.tab_builders[i])

    def __create(self, tab_builder):
        """ Create and add one tab page to the tab layout.

        :param tab_builder: A tuple that holds the tab initializer and name. Format: ("TabName01", InitFunc)
        """
        # Declare the tab page. And lead the cursor to the scroll layout.
        tab = cmds.scrollLayout()

        # Add the tab page to the tab layout. Add the name.
        cmds.tabLayout(self.all_tabs, edit=True, tabLabel=[tab, tab_builder[0]])

        # Build the tab page.
        tab_builder[1]()

        # Go back to the tab layout.
        cmds.setParent("..")

