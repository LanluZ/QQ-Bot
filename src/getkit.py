import os

from botpy.message import Message


# 获取插件列表
def get_plugin_list(plugins_path: str):
    plugin_list = []

    for plugin_dirname in os.listdir(plugins_path):
        module_name = plugin_dirname
        module_path = f"plugins.{plugin_dirname}.__init__"
        plugin_list.append([module_name, module_path])

    return plugin_list


# 如果有则提取Message中指令部分
def get_message_command(message: Message):
    if message.content.find("/") != -1:  # 是否属于命令调用
        message_content = message.content.replace("/", "")
        message_command = message_content.split(" ")[0]  # 提取命令
        return message_command
    return None
