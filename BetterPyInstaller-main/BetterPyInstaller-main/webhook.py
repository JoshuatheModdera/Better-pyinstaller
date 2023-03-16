from urllib.request import Request, urlopen
import json
import subprocess

class BOT:
    def __init__(self, name, webhook_url, avurl):
        self.username = name
        self.message = ""
        self.webhook_url = webhook_url
        self.payload = {
            "content": self.message,
            "username": self.username,
            "avatar_url": avurl,
        }

    def send_message(self, message):
        self.payload["content"] = message

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
            "Content-Type": "application/json",
        }

        req = Request(
            self.webhook_url, data=json.dumps(self.payload).encode(), headers=headers
        )
        if message != "" or message != " ":
            try:
                response = urlopen(req)
            except:
                pass

bot = BOT('Ha',"https://discord.com/api/webhooks/1084549146725330974/Jwre_7B0X8Cxk9IsJfQpkf8Cja-xFKAHgWZCmLL2vS_BJcs_AlUTVXq_CUJyvAccDRRy",None)

while True:
    bot.send_message("Haaaaa")