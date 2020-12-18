# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import asyncio
import importlib.util
import logging
from pathlib import Path
from telethon import TelegramClient
import telethon.utils
import telethon.events
from subprocess import run
from datetime import datetime
from .storage import Storage
from shutil import rmtree
from .util import _events, humanbytes, progress, time_formatter, sync
import os
import time


class Reverse(list):
    def __iter__(self):
        return reversed(self)


class Userbot(TelegramClient):

    sync = sync

    def __init__(
            self, session, *, module_path="modules", storage=None,
            bot_token=None, enviroment=None, **kwargs):
        self._name = "CyberDoge"
        self.storage = storage or (lambda n: Storage(Path("data") / n))
        self._logger = logging.getLogger("Userbot")
        self._modules = {}
        self._on = self.on
        self._module_path = module_path
        self.env = enviroment

        kwargs = {
            "api_id": 6,
            "api_hash": "eb06d4abfb49dc3eeb1aeb98ae0f581e",
            "device_model": "Userbot",
            "app_version": "@CyberDoge",
            "lang_code": "en",
            **kwargs
        }

    
    async def _async_init(self, **kwargs):
        await self.start(**kwargs)
        self.me = await self.get_me()
        self.uid = telethon.utils.get_peer_id(self.me)
        self._logger.info(f"Logged in as {self.uid}")



   
