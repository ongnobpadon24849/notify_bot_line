import sys
from linebot import LineBotApi
from linebot.models import TextMessage

# รับ Token และ User ID จาก "Secrets" ของ GitHub
YOUR_CHANNEL_ACCESS_TOKEN = sys.argv[1]
YOUR_USER_ID = sys.argv[2]
# รับ "ประเภท" ของการแจ้งเตือน (clock_in หรือ clock_out)
MESSAGE_TYPE = sys.argv[3] 

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

if MESSAGE_TYPE == "clock_in":
    message_text = "⏰ ได้เวลาเข้างาน! (08:55 น.)\nอย่าลืม Clock-In นะครับ"
    print("Sending Clock-In message...")
else:
    message_text = "🌙 ได้เวลาเลิกงาน! (18:00 น.)\nอย่าลืม Clock-Out ครับ"
    print("Sending Clock-Out message...")

line_bot_api.push_message(YOUR_USER_ID, TextMessage(text=message_text))
print("Message sent successfully!")