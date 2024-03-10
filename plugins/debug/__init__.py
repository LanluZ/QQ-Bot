import bot

from botpy.message import Message

__plugin_name__ = "调试"  # 插件名称
__plugin_iskeyword__ = True  # 是否需要触发关键词
__plugin_command__ = ["调试"]  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本
__plugin_dir__ = "debug"  # 插件所在目录名称


async def __init__(command, client: bot.BotClient, message: Message):
    if not __plugin_iskeyword__ or command in __plugin_command__:
        print(message.author)  # 消息来源
        print(message.content)  # 消息内容
        print(message.guild_id)  # 频道ID
        print(message.channel_id)  # 子频道ID
