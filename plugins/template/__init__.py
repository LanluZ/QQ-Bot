import bot

from botpy.message import Message

__plugin_name__ = "模板插件"  # 插件名称
__plugin_iskeyword__ = True  # 是否需要触发关键词
__plugin_command__ = ["模板插件"]  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本
__plugin_event__ = []  # 插件触发事件
__plugin_dir__ = "template"  # 插件所在目录名称


async def __init__(command, client: bot.BotClient, message: Message):
    if not __plugin_iskeyword__ or command in __plugin_command__:
        # 再此键入代码
        print("模板插件")
