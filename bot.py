import asyncio
import os
import botpy
import importlib

from src import getkit

from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message, DirectMessage

# 读取配置文件
config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()

cwd_path = os.getcwd()
plugins_path = os.path.join(cwd_path, "plugins")


class BotClient(botpy.Client):
    plugins = dict()
    plugins_path = plugins_path
    admin_id = config["admin_id"]

    # ==========初始化事件==========
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

        _log.info("==========完成载入插件==========")

    # ==========公域消息事件==========
    # at机器人消息事件
    async def on_at_message_create(self, message: Message):
        pass

    # 频道消息被删除事件
    async def on_public_message_delete(self, message: Message):
        pass

    # ==========消息事件==========

    # 普通消息事件监听 仅私域机器人可用
    async def on_message_create(self, message: Message):
        # 日志-消息记录
        _log.info(f"{message.author.username} {message.content}")

        # 命令匹配
        message_command = getkit.get_message_command(message)  # 提取会话消息中命令
        for plugin_name in self.plugins:
            await self.plugins[plugin_name].__init__(message_command, self, message)

    # 撤回消息事件
    async def on_message_delete(self, message: Message):
        pass

    # ==========私信事件==========

    # 私信消息事件
    async def on_direct_message_create(self, message: DirectMessage):
        pass

    # 撤回消息事件
    async def on_direct_message_delete(self, message: DirectMessage):
        pass


# ==========消息互动事件==========

# ==========频道事件==========

# ==========频道成员事件==========

# ==========互动事件==========

# ==========消息审核事件==========

# ==========论坛事件==========

# ==========音频事件==========


if __name__ == "__main__":
    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True, guild_messages=False)
    client = BotClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
