import asyncio
import json

import openai
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .tasks import get_progress_data  # ✅ Function to fetch progress updates


class ProgressConsumer(AsyncWebsocketConsumer):
    """WebSocket Consumer for Real-Time Progress Updates"""

    async def connect(self):
        """Accept WebSocket connection and send initial progress"""
        await self.accept()
        progress_data = get_progress_data()
        await self.send(json.dumps(progress_data))

    async def send_progress_updates(self):
        """Continuously send real-time progress updates"""
        while True:
            progress_data = await sync_to_async(get_progress_data)()  # ✅ Fetch progress from Celery
            await self.send(json.dumps(progress_data))

            if progress_data["progress"] >= 100:
                break  # ✅ Stop sending updates when processing is complete

            await asyncio.sleep(3)  # ✅ Prevent excessive requests

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        print(f"Progress WebSocket closed with code {close_code}")

class ChatConsumer(AsyncWebsocketConsumer):
    """WebSocket Consumer for Real-Time AI Chat"""

    async def connect(self):
        """Accept WebSocket connection"""
        await self.accept()
        await self.send(json.dumps({"message": "Connected to AI Chat."}))

    async def receive(self, text_data):
        """Process user question & respond using OpenAI API"""
        data = json.loads(text_data)
        question = data.get("question")
        api_key = data.get("api_key")

        if not api_key:
            await self.send(json.dumps({"error": "No API key provided."}))
            return

        # ✅ Call OpenAI API asynchronously
        ai_response = await self.get_openai_response(api_key, question)

        await self.send(json.dumps({"response": ai_response}))

    async def get_openai_response(self, api_key, question):
        """Asynchronous OpenAI API Call"""
        try:
            openai.api_key = api_key  # ✅ Set API Key

            response = await sync_to_async(openai.ChatCompletion.create)(
                model="gpt-4",
                messages=[{"role": "user", "content": question}]
            )

            return response["choices"][0]["message"]["content"]

        except openai.error.OpenAIError as e:
            return f"OpenAI API Error: {str(e)}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        print(f"Chat WebSocket closed with code {close_code}")
