import botpy

__plugin_name__ = "模板插件"
__plugin_command__ = "测试"
__plugin_author__ = "LanluZ"
__plugin_version__ = 1.0


def __init__(command):
    if command == __plugin_command__:
        print(2)
