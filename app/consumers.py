import json
import os

import requests_async as requests
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep

from app.models import Obj1Cmn, Obj2Cmn, Obj1Ai, Obj2Ai


class GraphConsumerCmn(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            choice_query_set_1 = await sync_to_async(list)(Obj1Cmn.objects.values())
            choice_query_set_2 = await sync_to_async(list)(Obj2Cmn.objects.values())
            await self.send(json.dumps({'value_1': choice_query_set_1,'value_2': choice_query_set_2}))
            await sleep(1)


class GraphConsumerAi(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            choice_query_set_1 = await sync_to_async(list)(Obj1Ai.objects.values())
            choice_query_set_2 = await sync_to_async(list)(Obj2Ai.objects.values())
            await self.send(json.dumps({'value_1': choice_query_set_1, 'value_2': choice_query_set_2}))
            await sleep(1)


class DetailsConsumerCmn(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            for i in range(1, 11):
                response_1 = await requests.get(f"http://{os.environ.get('HOST')}:8011/api/tables-1/?idai={i}")
                response_2 = await requests.get(f"http://{os.environ.get('HOST')}:8011/api/tables-2/?idai={i}")
                await self.send(json.dumps({'value_1': response_1.text, 'value_2': response_2.text, "sensor_number": i}))
            await sleep(1)
