from pyrogram.types import Message

from .base import BotCheckin


class ToolsCheckin(BotCheckin):
    name = "测试1"
    bot_username = "T00lsBot"
    bot_checkin_cmd = "/start"


    async def message_handler(self, client, message: Message):
        if message.caption and "Welcome" in message.caption and message.reply_markup:
            keys = [k.text for r in message.reply_markup.inline_keyboard for k in r]
            for k in keys:
                if "签到" in k:
                    await message.click(k)
                    return
        await super().message_handler(client, message)
