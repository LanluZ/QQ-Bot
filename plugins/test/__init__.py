import botpy

__plugin_name__ = "模板插件"  # 插件名称
__plugin_iskeyword__ = True  # 是否需要触发关键词
__plugin_command__ = "模板测试"  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本


def __init__(command):
    if command == __plugin_command__:
        print("模板测试成功")
