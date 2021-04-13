from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["チャンネルシークレットを入力"]

line_bot_api = LineBotApi("inGdp2Qk9KDUWiJNm0+F/SbCA7228a8QsgOLsB/vT0bukpWw8JY5P4HaisyEdujrjayYPmSW5Q/FeTZhS6Je4prJJpnuL8FL6e404Xpn8CFBi+e/pvHHx0iRHCU6RbejjEPZNtLlOqX1+5MvHUJmSQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("46b03c5fa22223190182d24a960de289")

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)