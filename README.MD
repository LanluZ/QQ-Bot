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

## 插件

1. 关键词屏蔽

## 注意事项

1. 请选择私域机器人而非公域机器人,他们允许监听的事件是不一样的,该机器人是基于私域机器人开发的