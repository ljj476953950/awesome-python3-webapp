#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-12
# @Author  : Lijiajie (476953950@qq.com)
# @Link    : http://ljj.cloud
# @Version : 1.0

import logging; logging.basicConfig(level=logging.INFO)
import os
import asyncio

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Ljj</h1>')

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000')
	return srv

async def hello():
	print("hello world!")
	r = await asyncio.sleep(1)
	print("hello again")

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
