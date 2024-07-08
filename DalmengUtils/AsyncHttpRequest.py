
#& Imports
import aiohttp
import json as j

#& HTTP Async Request Processor
class Response:
    def __init__(self, status_code, msg="succeed", data=None, content=None):
        self.status_code = status_code
        self.msg = msg
        self.data = data
        self.content = content

    def json(self):
        try:
            return j.loads(self.data)
        except:
            return j.loads(self.content)

class Request:
    session = None

    @staticmethod
    async def post(url, headers: dict = {}, data: dict = {}, timeout=60):
        if not Request.session:
            timeout = aiohttp.ClientTimeout(total=timeout)
            Request.session = aiohttp.ClientSession(timeout=timeout)

        try:
            res = await Request.session.post(url, headers=headers, json=data)

            data = None
            content = None

            if "Content-Type" not in headers or ("Content-Type" in headers and ('text' in headers["Content-Type"] or 'json' in headers["Content-Type"])):
                data = await res.text()
            else:
                content = await res.read()
            return Response(
                status_code=res.status,
                data=data,
                content=content
            )
        except aiohttp.ClientError as e:
            return Response(
                status_code=400,
                msg=str(e)
            )
        except Exception as e:
            return Response(
                status_code=500,
                msg=str(e)
            )

    @staticmethod
    async def get(url, headers: dict = {}, data: dict = {}):
        if not Request.session:
            Request.session = aiohttp.ClientSession()

        try:
            res = await Request.session.get(url, headers=headers, json=data)
            data = None
            content = None

            if "Content-Type" not in headers or ("Content-Type" in headers and ('text' in headers["Content-Type"] or 'json' in headers["Content-Type"])):
                data = await res.text()
            else:
                content = await res.read()
            return Response(
                status_code=res.status,
                data=data,
                content=content
            )
        except aiohttp.ClientError as e:
            return Response(
                status_code=400,
                msg=str(e)
            )
        except Exception as e:
            return Response(
                status_code=500,
                msg=str(e)
            )

    @staticmethod
    async def stream(url, data: dict = {}, headers: dict = {}):
        if not Request.session:
            Request.session = aiohttp.ClientSession()
        try:
            res = await Request.session.post(url, headers=headers, json=data)
            async for line in res.content:
                if line:
                    yield line
        except aiohttp.ClientError as e:
            yield b'{"status_code": 500, "msg": "{}"}'.format(str(e))
        except Exception as e:
            yield b'{"status_code": 400, "msg": "{}"}'.format(str(e))
