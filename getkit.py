import os


def get_plugin_list(plugins_path: str):
    plugin_list = []

    for plugin_dirname in os.listdir(plugins_path):
        module_name = plugin_dirname
        module_path = f"plugins.{plugin_dirname}.__init__"
        plugin_list.append([module_name, module_path])

    return plugin_list
