# 还没想好叫什么的机器人

和还没写好的README

---

## 准备

1. 在 [QQ开放平台](https://q.qq.com) 注册开发者账号并创建QQ机器人
2. 在 [QQ开放平台](https://q.qq.com) 机器人管理中找到 **AppId** 和 **AppSecret** 并填入 ```/config.yaml```

## 部署

1. 下载仓库文件
2. 安装依赖```pip install -r requirements.txt```
3. 填写```/config.yaml```
4. 运行```python bot.py```

## 开发

- 官方文档 参考 [QQ机器人文档](https://bot.q.qq.com/wiki)
- 插件格式 参考 ```/plugins/template/__init__.py```

**插件监听事件**

| __ plugin_event __ | 数值  | 事件                            |
|--------------------|-----|-------------------------------|
| at机器人消息事件          | 0   | on_at_message_create          |
| 频道消息被删除事件          | 1   | on_public_message_delete      |
| 普通消息事件监听           | 10  | on_at_message_create          |
| 撤回消息事件             | 11  | on_public_message_delete      |
| 私信消息事件             | 20  | on_message_create             |
| 撤回消息事件             | 21  | on_message_delete             |
|                    | 30  | on_direct_message_create      |
|                    | 31  | on_direct_message_delete      |
|                    | 40  | on_message_reaction_add       |
|                    | 41  | on_message_reaction_remove    |
|                    | 50  | on_guild_create               |
|                    | 51  | on_guild_update               |
|                    | 52  | on_guild_delete               |
|                    | 53  | on_channel_create             |
|                    | 54  | on_channel_update             |
|                    | 55  | on_channel_delete             |
|                    | 60  | on_guild_member_add           |
|                    | 61  | on_guild_member_update        |
|                    | 62  | on_guild_member_remove        |
|                    | 70  | on_interaction_create         |
|                    | 80  | on_message_audit_pass         |
|                    | 81  | on_message_audit_reject       |
|                    | 90  | on_forum_thread_create        |
|                    | 91  | on_forum_thread_update        |
|                    | 92  | on_forum_thread_delete        |
|                    | 93  | on_forum_post_create          |
|                    | 94  | on_forum_post_delete          |
|                    | 95  | on_forum_reply_create         |
|                    | 96  | on_forum_reply_delete         |
|                    | 97  | on_forum_publish_audit_result |
|                    | 100 | on_audio_start                |
|                    | 101 | on_audio_finish               |
|                    | 102 | on_audio_on_mic               |
|                    | 103 | on_audio_off_mic              |

## 插件

1. 关键词屏蔽 (开发中)

## 注意事项

1. 请选择私域机器人而非公域机器人,他们允许监听的事件是不一样的,该机器人是基于私域机器人开发的