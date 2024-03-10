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

    # 初始化机器人事件
    async def on_ready(self):  # 准备就绪事件
        _log.info(f"「{self.robot.name}」初始化")
        _log.info("==========开始载入插件==========")

        # 载入插件
        plugin_list = getkit.get_plugin_list(plugins_path)
        for plugin in plugin_list:
            self.plugins[plugin[0]] = importlib.import_module(plugin[1])

            # 输出载入插件相关信息
            plugin_name = self.plugins[plugin[0]].__plugin_name__
            plugin_author = self.plugins[plugin[0]].__plugin_author__
            plugin_version = self.plugins[plugin[0]].__plugin_version__

            _log.info(f"「{plugin_name}」{plugin_author} {plugin_version}")

    # at消息事件监听
    async def on_at_message_create(self, message: Message):
        if "sleep" in message.content:
            await asyncio.sleep(10)
        _log.info(message.author.username)

    # 普通消息事件监听 仅私域机器人可用
    async def on_message_create(self, message: Message):
        if "sleep" in message.content:
            await asyncio.sleep(10)
        _log.info(f"{message.author.username} {message.content}")

        # 命令匹配
        message_command = getkit.get_message_command(message)  # 提取会话消息中命令
        for plugin_name in self.plugins:
            await self.plugins[plugin_name].__init__(message_command, self, message)


if __name__ == "__main__":
    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True, guild_messages=True)
    client = BotClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
