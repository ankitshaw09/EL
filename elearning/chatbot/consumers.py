import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .ai_model import get_response

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data["message"]
        bot_response = get_response(user_message)

        await self.send(text_data=json.dumps({"message": bot_response}))
