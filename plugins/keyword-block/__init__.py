import botpy

__plugin_name__ = "关键词屏蔽"  # 插件名称
__plugin_iskeyword__ = False  # 是否需要触发关键词
__plugin_command__ = ""  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本


def __init__(command, message):
    if not __plugin_iskeyword__ or command == __plugin_command__:
        print(2)
