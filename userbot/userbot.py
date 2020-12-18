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
