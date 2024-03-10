import bot

from botpy.message import Message

__plugin_name__ = "模板插件"  # 插件名称
__plugin_iskeyword__ = True  # 是否需要触发关键词
__plugin_command__ = "模板插件"  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本


async def __init__(command, client: bot.BotClient, message: Message):
    if not __plugin_iskeyword__ or command == __plugin_command__:
        print("模板插件")
