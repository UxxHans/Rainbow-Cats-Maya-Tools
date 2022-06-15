import importlib
import maya.cmds as cmds


def reload(module_name, show_dialog=False):
    """ Maya does not reload the scripts automatically when we changed the scripts in runtime.
    So we need to reload the scripts manually | explicitly using this method.

    :param module_name: The script name | module name to be reloaded.
    :param show_dialog: Should it show the dialog window to report the status.
    :return:
    """
    try:
        importlib.reload(importlib.import_module(module_name))
        if show_dialog:
            cmds.confirmDialog(title='Reload', message='Reloaded successfully!', button=['Confirm'],
                               defaultButton='Confirm', dismissString='Confirm')
        else:
            print('[Reloader] Reloaded successfully!')

    except Exception as e:
        if show_dialog:
            cmds.confirmDialog(title='Reload', message='[Reload] Failed to attempt reloading scripts: ' + str(e),
                               button=['Confirm'], defaultButton='Confirm', dismissString='Confirm')
        else:
            print('[Reloader] Failed to attempt reloading scripts: ' + str(e))
