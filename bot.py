import asyncio
import os
import botpy
import importlib

import getkit

from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()

cwd_path = os.getcwd()
plugins_path = os.path.join(cwd_path, "plugins")


class BotClient(botpy.Client):
    plugins = dict()

    # @初始化机器人事件
    async def on_ready(self):  # 准备就绪事件
        _log.info(f"「{self.robot.name}」初始化")  # 日志
        _log.info("==========开始载入插件==========")  # 日志

        # 载入插件
        plugin_list = getkit.get_plugin_list(plugins_path)
        for plugin in plugin_list:
            self.plugins[plugin[0]] = importlib.import_module(plugin[1])

            plugin_name = self.plugins[plugin[0]].__plugin_name__
            plugin_author = self.plugins[plugin[0]].__plugin_author__
            plugin_version = self.plugins[plugin[0]].__plugin_version__

            _log.info(f"「{plugin_name}」{plugin_author} {plugin_version}")  # 日志

    # @消息事件监听
    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)  # 日志-头像
        if "sleep" in message.content:
            await asyncio.sleep(10)
        _log.info(message.author.username)  # 日志-用户名

        # 消息内容提取
        message_content = message.content[message.content.find(" "):]
        message_command = ""
        if message_content[0] == "/":  # 是否属于命令调用
            message_content = message_content.replace("/", "")
            message_command = message_content.split(" ")  # 提取命令

        # 命令匹配
        for plugin_name in self.plugins:
            self.plugins[plugin_name].__init__(message_command)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True)
    client = BotClient(intents=intents, )
    client.run(appid=config["appid"], secret=config["secret"])
