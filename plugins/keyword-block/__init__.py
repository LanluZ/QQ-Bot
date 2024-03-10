import bot
import yaml

import os.path
import botpy.errors

from botpy.message import Message

__plugin_name__ = "关键词屏蔽"  # 插件名称
__plugin_iskeyword__ = False  # 是否需要触发关键词
__plugin_command__ = ["关键词屏蔽"]  # 触发关键词
__plugin_author__ = "LanluZ"  # 插件作者
__plugin_version__ = 1.0  # 插件版本
__plugin_dir__ = "./plugins/keyword-block"  # 插件所在目录

ban_filename = "ban.txt"


async def __init__(command, client: bot.BotClient, message: Message):
    # 由关键词触发
    if command in __plugin_command__:
        # 字符串切割
        message_list = message.content.split(" ")
        # 子命令判断
        if message_list[1] == "添加":
            await add_ban_word(message_list[2], client, message)
        elif message_list[1] == "删除":
            await del_ban_word(message_list[2], client, message)
        elif message_list[1] == "查看":
            await show_ban_word(client, message)
        elif message_list[1] == "帮助":
            await info_ban_word(client, message)
    # 默认触发
    elif not __plugin_iskeyword__:
        await ban_word(client, message)


# 添加屏蔽词
async def add_ban_word(word: str, client: bot.BotClient, message: Message):
    # 权限判断
    if message.author.id == client.admin_id:
        # 加载屏蔽词
        with open(os.path.join(__plugin_dir__, ban_filename), "r", encoding="utf-8") as f:
            ban = f.read()
            ban_list = ban.split(",")
            # 添加屏蔽词
            for i in ban_list:
                if i == "":
                    ban_list.remove("")
            ban_list.append(word)
        # 保存屏蔽词
        with open(os.path.join(__plugin_dir__, ban_filename), "w", encoding="utf-8") as f:
            for ban_word in ban_list:
                f.write(ban_word)
                f.write(",")
        await message.reply(content=f"{word} 添加成功")
    else:
        await message.reply(content="权限不足!")


# 删除屏蔽词
async def del_ban_word(word: str, client: bot.BotClient, message: Message):
    # 权限判断
    if message.author.id == client.admin_id:
        # 加载屏蔽词
        with open(os.path.join(__plugin_dir__, ban_filename), "r", encoding="utf-8") as f:
            ban = f.read()
            ban_list = ban.split(",")
            # 删除屏蔽词
            try:
                ban_list.remove(word)
            except ValueError:
                await message.reply(content="无此关键词")
                return
        # 保存屏蔽词
        with open(os.path.join(__plugin_dir__, ban_filename), "w", encoding="utf-8") as f:
            for ban_word in ban_list:
                f.write(ban_word)
                f.write(",")
            await message.reply(content=f"{word} 删除成功")
    else:
        await message.reply(content="权限不足!")


# 查看屏蔽词
async def show_ban_word(client: bot.BotClient, message: Message):
    # 权限判断
    if message.author.id == client.admin_id:
        # 加载屏蔽词
        with open(os.path.join(__plugin_dir__, ban_filename), "r", encoding="utf-8") as f:
            ban = f.read()
            ban_list = ban.split(",")
            await message.reply(content=str(ban_list))
    else:
        await message.reply(content="权限不足!")


# 帮助
async def info_ban_word(client: bot.BotClient, message: Message):
    await message.reply(content="还没写好")


# 屏蔽
async def ban_word(client: bot.BotClient, message: Message):
    # 加载屏蔽词
    with open(os.path.join(__plugin_dir__, ban_filename), "r", encoding="utf-8") as f:
        ban = f.read()
        ban_list = ban.split(",")
        for word in ban_list:
            if message.content.find(word) != -1:
                try:  # 管理员判断
                    await client.api.recall_message(channel_id=message.channel_id, message_id=message.id, hidetip=False)
                    await message.reply(content="内容违规")
                except botpy.errors.ServerError:
                    return
