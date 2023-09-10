from .base import BotCheckin


class ZhihuCheckin(BotCheckin):
    name = "知乎机器人"
    bot_username = "zhihu_bot"
    bot_checkin_cmd = "/sign"
